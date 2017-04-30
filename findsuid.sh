#!/bin/sh
tempfile="~/suids.txt"
find $1 \( -type f -a -user root -a -perm -4001 \) -print > $tempfile
