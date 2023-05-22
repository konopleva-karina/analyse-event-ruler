#!/bin/bash

rm events_*
rm rule_*
rm -f gz/*
python3 main.py

for (( i=1; i < 1000; i+=5 ))
do
    gzip "rule_$i.json"
    gzip "events_$i.json"
    cp "rule_$i.json.gz" /Users/karina/seminars/pythonProject2/gz
    cp "events_$i.json.gz" /Users/karina/seminars/pythonProject2/gz
done