#!/usr/bin/python3

import sys

def var(i,j,m):
    """
    parameters:
    i: researcher id between 1 and m
    j: seat id between 1 and m-1
    m: total number of researchers
    """
    return (i-1)*(m-1)+j

def at_least_one(i,m):
    literals=[]
    for j in range(1,m):
        literals.append(var(i,j,m))
    print("%s >= 1;" % ' '.join(map(lambda i : "+1 x"+str(i),literals)))

def at_most_one(j,m):
    literals=[]
    for i in range(1,m+1):
        literals.append(var(i,j,m))
    print("%s >= -1;" % ' '.join(map(lambda i : "-1 x"+str(i),literals)))

if (len(sys.argv)!=2):
    m = 4
else:
    m = int(sys.argv[1])

print ("* #variable= %d #constraint= %d" % (m*(m-1),m+(m-1)))
print ("* beginMapping")
for i in range(1,m+1):
    for j in range(1,m):
        print ("* %d=R%dS%d" %(var(i,j,m),i,j))
print ("* endMapping")
for i in range(1,m+1):
    at_least_one(i,m)

for j in range(1,m):
    at_most_one(j,m)
