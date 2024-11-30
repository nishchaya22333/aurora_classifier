#!/bin/bash

mkdir ../images/cropped_scaled_rotated
linecount=0
headerlength=19
while IFS="," read class2 class6 picNum label angle
do
  if [ "${linecount}" -lt "${headerlength}" ]
  then
    ((linecount++))
    continue
  fi
  infile="../images/cropped_scaled/${picNum}.png"
  outfile="../images/cropped_scaled_rotated/${picNum}_${angle}.png"
  convert ${infile} -background black -distort SRT ${angle} +repage ${outfile}
  ((linecount++))
done < "../classifications/classifications.csv"

exit 1
