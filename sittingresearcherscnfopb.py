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
        literals.append("+1 x"+str(var(i,j,m)))
    literals.append(">= 1;")
    print(' '.join(map(str,literals)))

def at_most_one(j,m):
    for i in range(1,m+1):
        for k in range(i+1,m+1):
            print("+1 ~x%d +1 ~x%d >= 1;" % (var(i,j,m),var(k,j,m)))

if (len(sys.argv)!=2):
    m = 4
else:
    m = int(sys.argv[1])

print ("* #variable= %d #constraint= %d" % (m*m-m,m+(m-1)*m*(m-1)/2))
print ("* beginMapping")
for i in range(1,m+1):
    for j in range(1,m):
        print ("* %d=R%dS%d" %(var(i,j,m),i,j))
print ("* endMapping")
for i in range(1,m+1):
    at_least_one(i,m)

for j in range(1,m):
    at_most_one(j,m)
