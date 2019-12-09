#!/usr/bin/python3

import fileinput


for line in fileinput.input():
    if line.startswith("v "):
        values = filter(lambda i: i[0]=='x',line.split()[1:])
        current=[]
        nbRow=0
        for v in values:
            current.append(v[3])
            if len(current)==11:
                print(''.join(current))
                current=[]
                nbRow+=1
                if nbRow==3 or nbRow==6:
                    print()
            elif len(current)==3 or len(current)==7:
                current.append(' ')
