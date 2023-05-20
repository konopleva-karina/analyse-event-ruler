#!/bin/bash

for (( i=1; i < 1000; i+=5 ))
do
    gzip "rule_$i.json"
    cp "rule_$i.json.gz" /Users/karina/seminars/pythonProject2/gz
done