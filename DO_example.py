import pickle
from pypulse import PulseInterface
from daqface import DAQ


hardware_params = config['hardware_params']
global_params = config['global_params']

# load data
file_conf = 'PulseBoy/TrialBanks/PWMTest.trialbank'
with open(file_conf, 'rb') as fn:
    arraydata = pickle.load(fn)

trial_params = arraydata[0][1]


pulses, t = PulseInterface.make_pulse(hardware_params['samp_rate'],
                                      global_params['global_onset'],
                                      global_params['global_offset'],
                                      trial_params)

trial_daq = DAQ.DoAiMultiTask(hardware_params['analog_dev'], hardware_params['analog_channels'],
                                       hardware_params['digital_dev'], hardware_params['samp_rate'],
                                       len(t) / hardware_params['samp_rate'], pulses,
                                       hardware_params['sync_clock'])

trial_daq = daq.DigitalOut(hardware_params['digital_dev'], hardware_params['samp_rate'],
                                       len(t) / hardware_params['samp_rate'], pulses,
                                       hardware_params['sync_clock'])

trial_daq.DoTask()