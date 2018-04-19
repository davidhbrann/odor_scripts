import pickle
from pypulse import PulseInterface
from daqface import DAQ


def load_pkl(filename):
    with open(filename, 'rb') as fn:
        data = pickle.load(fn)
    return data


# file names
trial_file = 'PulseBoy/TrialBanks/PWMTest.trialbank'
config_file = 'PulseBoy/params.config'

config = load_pkl(config_file)
hardware_params = config['hardware_params']
global_params = config['global_params']

arraydata = load_pkl(trial_file)
trial_params = arraydata[0][1]

pulses, t = PulseInterface.make_pulse(hardware_params['samp_rate'],
                                      global_params['global_onset'],
                                      global_params['global_offset'],
                                      trial_params)

trial_daq = DAQ.DigitalOut(hardware_params['digital_dev'],
                           hardware_params['samp_rate'],
                           len(t) / hardware_params['samp_rate'], pulses,
                           hardware_params['sync_clock'])

trial_daq.DoTask()
