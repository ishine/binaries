# mix-16-all-pad-pcm/ mix-16-all-pad-wav/ mix-48-all-pad-pcm/ mix-48-all-pad-wav/ org-16k-pcm/        org-16k-wav/        org-48k-pcm/        org-48k-wav/ 

#mkdir -p rnnoise_mix_org
#mkdir -p rnnoise_mix_t1
#for i in asr_cli_sounds/mix-48-all-pad-pcm/*.pcm
#do
#file=`basename $i`
#filename=`echo "$file" | cut -d'.' -f-1`
#echo $file
#./rnnoise_demo_org $i rnnoise_mix_org/rnnoise_48k_$filename.s16
#./rnnoise_demo_t1 $i rnnoise_mix_t1/rnnoise_48k_$filename.s16
#sox -r 48000 -c 1 rnnoise_mix_org/rnnoise_48k_$filename.s16 -r 16000 -c 1 rnnoise_mix_org/rnnoise_16k_$filename.wav
#sox -r 48000 -c 1 rnnoise_mix_org/rnnoise_48k_$filename.s16 -r 48000 -c 1 rnnoise_mix_org/rnnoise_48k_$filename.wav
#sox -r 48000 -c 1 rnnoise_mix_t1/rnnoise_48k_$filename.s16 -r 16000 -c 1 rnnoise_mix_t1/rnnoise_16k_$filename.wav
#sox -r 48000 -c 1 rnnoise_mix_t1/rnnoise_48k_$filename.s16 -r 48000 -c 1 rnnoise_mix_t1/rnnoise_48k_$filename.wav
#done

#exit 

echo "==========People============="
for i in rnnoise_people*.wav
do
file=`basename $i`
filename=`echo "$file" | cut -d'.' -f-1`
original=`echo $file | awk -Frnnoise_people_ '{print $2}'`
#echo $original
score=`./bin/pesq +16000 +wb ../asr_cli_sounds/org-16k-wav/$original $file |grep MOS`
echo $score
done

echo "==========Street============="
for i in rnnoise_street*.wav
do
file=`basename $i`
#filename=`echo "$file" | cut -d'.' -f-1`
original=`echo $file | awk -Frnnoise_street_ '{print $2}'`
score=`./bin/pesq +16000 +wb ../asr_cli_sounds/org-16k-wav/$original $file | grep MOS`
echo $score
done


echo "==========Car============="
for i in rnnoise_car*.wav
do
file=`basename $i`
filename=`echo "$file" | cut -d'.' -f-1`
#echo $filename
original=`echo $file | awk -Frnnoise_car_ '{print $2}'`
score=`./bin/pesq +16000 +wb ../asr_cli_sounds/org-16k-wav/$original $file | grep MOS`
#./rnnoise_demo $i rnnoise_$file
echo $score
done
