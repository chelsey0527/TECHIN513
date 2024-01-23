import simpleaudio as sa

wav_obj = sa.WaveObject.from_wave_file('train32.wav')
fs = wav_obj.sample_rate
channels = wav_obj.num_channels
print('Sampling rate = ', fs)
print('Number of channels = ', channels)
play_obj = wav_obj.play()
play_obj.wait_done()