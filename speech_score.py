import glob
import os
import soundfile as sf
import sys
from pystoi.stoi import stoi
from scipy.io import wavfile
from pypesq import pypesq


org_folder='asr_cli_sounds/org-16k-wav-pad'
noise_folder='asr_cli_sounds/final-mix-16k-wav'
rnnoise_folder='final-t1-new-rnnoise-16k-wav'


for filepath in glob.iglob(org_folder +'/*.wav'):
    #print(filepath)
    filename=os.path.basename(filepath)

    #original
    rate, ref = wavfile.read(filepath)
    clean, fs = sf.read(filepath)    

    
    #mix with noise degraded    
    rate, deg = wavfile.read(noise_folder+'/car_'+filename)
    denoised, fs = sf.read(noise_folder+'/car_'+filename)
    estoi_deg = "%.3f"%stoi(clean, denoised, fs, extended=True)
    pesq_deg="%.3f"%pypesq(rate, ref, deg, 'wb')
    

    #rnnoise processed
    rate, deg = wavfile.read(rnnoise_folder+'/rnnoise_16k_car_'+filename)
    denoised, fs = sf.read(rnnoise_folder+'/rnnoise_16k_car_'+filename)
    estoi_rnn = "%.3f"%stoi(clean, denoised, fs, extended=True)
    pesq_rnn="%.3f"%pypesq(rate, ref, deg, 'wb')

    #print("=========================Car Noise==================================")
    print("car," + filename + ',' + str(pesq_deg) + ',' + str(pesq_rnn) + ',' + str(estoi_deg) + ',' + str(estoi_rnn)) 
    #print(str(pesq_rnn))
    
#print("pseq score",pypesq(rate, ref, deg, 'wb'))
#print("stoi score",d)
#print("estoi score",ed)


     #mix with noise degraded    
    rate, deg = wavfile.read(noise_folder+'/people_'+filename)
    denoised, fs = sf.read(noise_folder+'/people_'+filename)
    estoi_deg = "%.3f"%stoi(clean, denoised, fs, extended=True)
    pesq_deg="%.3f"%pypesq(rate, ref, deg, 'wb')


    #rnnoise processed
    rate, deg = wavfile.read(rnnoise_folder+'/rnnoise_16k_people_'+filename)
    denoised, fs = sf.read(rnnoise_folder+'/rnnoise_16k_people_'+filename)
    estoi_rnn = "%.3f"%stoi(clean, denoised, fs, extended=True)
    pesq_rnn="%.3f"%pypesq(rate, ref, deg, 'wb')

    #print("=========================people Noise==================================")
    #print(filename + ',' + str(pesq_deg) + ',' + str(pesq_rnn) + ',' + str(100-pesq_rnn-pesq_deg/pesq_rnn*100))
    print("people,"+filename + ',' + str(pesq_deg) + ',' + str(pesq_rnn) + ',' + str(estoi_deg) + ',' + str(estoi_rnn)) 
    #print(str(pesq_rnn)) 


    rate, deg = wavfile.read(noise_folder+'/street_'+filename)
    denoised, fs = sf.read(noise_folder+'/street_'+filename)
    estoi_deg = "%.3f"%stoi(clean, denoised, fs, extended=True)
    pesq_deg="%.3f"%pypesq(rate, ref, deg, 'wb')


    #rnnoise processed
    rate, deg = wavfile.read(rnnoise_folder+'/rnnoise_16k_street_'+filename)
    denoised, fs = sf.read(rnnoise_folder+'/rnnoise_16k_street_'+filename)
    try:
        estoi_rnn = "%.3f"%stoi(clean, denoised, fs, extended=True)
    except:
        print(filename)
        pass
    pesq_rnn="%.3f"%pypesq(rate, ref, deg, 'wb')

    #print("=========================Street Noise==================================")
    #print(filename + ',' + str(pesq_deg) + ',' + str(pesq_rnn) + ',' + str(100-pesq_rnn-pesq_deg/pesq_rnn*100))
    print("street,"+ filename + ',' + str(pesq_deg) + ',' + str(pesq_rnn) + ',' + str(estoi_deg) + ',' + str(estoi_rnn)) 
    #print(str(pesq_rnn)) 

    
