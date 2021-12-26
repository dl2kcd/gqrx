#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Script to generate test data for GQRX.
# The test data allow to verify S-meter calibration and accuracy of
# displayed spectrum frequencies.
#----------------------------------------------------------------------------
import numpy as np
#----------------------------------------------------------------------------
# parameters
duration = 60         # duration in seconds
span     = 500e3      # sample rate and I/Q bandwidth
fcenter  = 100e6      # center frequency in Hz (used for filename)
foffset  = 123e3      # offset of test signal from center, in Hz

sig_dBFS = -30        # signal amplitude in dBFS
noise_dBFS_1kHz = -50 # noise amplitude per 1 kHz bandwidth in dBFS
#----------------------------------------------------------------------------
# calculate data
sigamp   = pow(10, sig_dBFS / 20)
noiseamp = pow(10, noise_dBFS_1kHz / 20) * np.sqrt(span / 1e3)

t = np.arange(0, duration, 1/span, dtype = 'float64')
n = t.shape[0]

signal = np.exp(2j * np.pi * foffset * t)
noise  = (np.random.normal(0,1,n) + 1j * np.random.normal(0,1,n)) / np.sqrt(2)

u = sigamp * signal + noiseamp * noise
#----------------------------------------------------------------------------
# save data
fname = 'gqrx_test_%d_%d_fc.raw' % (int(fcenter), int(span))
u.astype('complex64').tofile(fname)
print("output: %s" % fname)


