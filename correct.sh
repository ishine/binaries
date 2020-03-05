folder=final-final-t2-rnnoise-16k-wav
fin=final-t2-rnnoise-16k-wav
mkdir -p $folder

for i in org-16k-wav-pad/*.wav
do 
 
file=$(basename "$i")
sox $fin/rnnoise_16k_car_$file $folder/rnnoise_16k_car_$file trim 0 `soxi -D org-16k-wav-pad/$file`
 sox $fin/rnnoise_16k_street_$file $folder/rnnoise_16k_street_$file trim 0 `soxi -D org-16k-wav-pad/$file`
 sox $fin/rnnoise_16k_people_$file $folder/rnnoise_16k_people_$file trim 0 `soxi -D org-16k-wav-pad/$file`
done
