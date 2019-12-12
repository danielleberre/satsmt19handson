#!/usr/bin/python3

import fileinput
import sys

mapping = {}

if (len(sys.argv)==2):
    for line in open(sys.argv[1],"r").readlines():
        if line.__contains__('='):
            splitted = line[1:].split('=')
            mapping[int(splitted[0].strip())]=splitted[1].strip()

for line in sys.stdin.readlines():
    if line.startswith("v "):
        values = filter(lambda i: i>0,map(int,line.split()[1:]))
        print(' '.join(map(lambda i: mapping[i],values)))
