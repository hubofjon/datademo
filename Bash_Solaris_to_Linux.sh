#author: JonQLi
#!/usr/bin/bash

#Example of update feed of "SAMPL20180511.csv" with new date "20180514"
#1. copy SAMPL20180511.csv and .mrk file from PROD to TEST /tmp directory
#2. in DEV1/tmp, run "chmod 666 SAMPL20180511*"
#3. login as op run "./itp_kit.sh SAMPL20180511.csv 20180514"

if [ "$#" -ne 2 ]; then
         echo "Sample usage:" $0 "SAMPL20180511.csv" "20180514"
         exit 1
elif [ "${#1}" -ne 20 ] || [ "${#2}" -ne 8 ]; then
        echo "please check arguments length"
        exit 1
fi

script_dir=""
source_dir="/tmp"
source_file=$1
target_dir=""
target_file=$(echo $1 |sed "s/[0-9]//g" |sed "s/\./$2\./")

convert_date() {
mm=${1:12:2}
yy=${1:8:4}
dd=${1:14:2}
converted_date=$mm/$dd/$yy
echo "$converted_date"
}

source_date=$(convert_date "$source_file")
target_date=$(convert_date "$target_file")

if [ -e $source_dir/$source_file ]; then
        sed "s~$source_date~$target_date~g" $source_dir/$source_file\
         > $source_dir/$target_file
fi

## make marker
sha256sum $source_dir/$source_file > $source_dir/$target_file.tmpmrk
source_date=$(convert_date "$source_file")
target_date=$(convert_date "$target_file")

if [ -e $source_dir/$source_file ]; then
        sed "s~$source_date~$target_date~g" $source_dir/$source_file\
         > $source_dir/$target_file
fi

## make marker
sha256sum $source_dir/$source_file > $source_dir/$target_file.tmpmrk
if [ -s $source_dir/$target_file.tmpmrk ]; then
        awk '{print $1}' $source_dir/$target_file.tmpmrk >\
                 $source_dir/$target_file.mrk
        rm $source_dir/$target_file.tmpmrk
else
        echo "mrk file is empty"
fi

cp $source_dir/$target_file $target_dir/$target_file
cp $source_dir/$target_file.mrk $target_dir/$target_file.mrk

if [ "$?" -eq 0 ]; then
        echo "2 files copied: " $target_file  $target_file.mrk
fi
