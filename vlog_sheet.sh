#!/bin/bash

if [ "$#" -lt  "1" ]
then
    echo "missing argument: site_directory"
    exit 1
fi

if [ -f "vlog.txt" ]; then
  rm "vlog.txt"
fi

wget https://michaelleidel.net/$1/vlog.txt

python3 ip2loc_vlog_csv.py output/$1.csv

libreoffice --calc --infilter="CSV:44,39,0,1,1/4/1/1/1/1/1/1" output/$1.csv
