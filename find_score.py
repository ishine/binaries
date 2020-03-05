#packages to install
#pip3 install https://github.com/ludlows/python-pesq/archive/master.zip
#pip3 install pystoi

import soundfile as sf
import sys
from pystoi.stoi import stoi
from scipy.io import wavfile
from pypesq import pypesq

rate, ref = wavfile.read(sys.argv[1])
rate, deg = wavfile.read(sys.argv[2])


clean, fs = sf.read(sys.argv[1])
denoised, fs = sf.read(sys.argv[2])

# Clean and den should have the same length, and be 1D
d = stoi(clean, denoised, fs, extended=False)
ed = stoi(clean, denoised, fs, extended=True)

print(pypesq(rate, ref, deg, 'wb'))
#print("pseq score",pypesq(rate, ref, deg, 'wb'))
#print("stoi score",d)
#print("estoi score",ed)
