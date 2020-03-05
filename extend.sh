#asr_cli_sounds/mix-16-all-pad-wav/car_call_2483487124_analogue_near.wav rnnoise_mix_org/rnnoise_16k_car_call_2483487124_analogue_near.wav
for i in asr_cli_sounds/mix-16-all-pad-wav/*.wav
do
filename=$(basename "$i")
echo $filename

org_sample=$(soxi $i | grep samples | awk -F '=' '{print $2}' | awk '{print $1;}')
echo $org_sample
pico_sample=$(soxi rnnoise_mix_org/rnnoise_16k_$filename | grep samples | awk -F '=' '{print $2}' | awk '{print $1;}')
echo $pico_sample
extend_scale=$(echo "scale=14; $org_sample/$pico_sample-1" | bc)
echo $extend_scale
f2=final_mix_16k
f1=org-16k-wav-pad
mkdir -p $folder
sox rnnoise_mix_org/rnnoise_16k_$filename rnnoise_mix_org_pad/rnnoise_16k_$filename pad 0 $extend_scale
sox rnnoise_mix_org/rnnoise_16k_$filename rnnoise_mix_org_pad/rnnoise_16k_$filename pad 0 $extend_scale
sox rnnoise_mix_org/rnnoise_16k_$filename rnnoise_mix_org_pad/rnnoise_16k_$filename pad 0 $extend_scale
done
