#!/usr/bin/python3

import sys

def var(i,j,n):
    """
    parameters:
    i: researcher id between 1 and m
    j: seat id between 1 and m-1
    m: total number of researchers
    """
    return (i-1)*n+j

def at_least_one(i,m,n):
    literals=[]
    for j in range(1,n+1):
        literals.append(var(i,j,n))
    print("[1] %s >= 1;" % ' '.join(map(lambda i : "+1 x"+str(i),literals)))

def at_most_one(j,m,n):
    literals=[]
    for i in range(1,m+1):
        literals.append(var(i,j,n))
    print("%s >= -1;" % ' '.join(map(lambda i : "-1 x"+str(i),literals)))

if (len(sys.argv)!=3):
    m = 4
    n = 3
else:
    m = int(sys.argv[1])
    n = int(sys.argv[2])

print ("* #variable= %d #constraint= %d #soft= %d mincost= %d maxcost= %d sumcost= %d" % (m*n,m+n,m,1,1,m))
print ("* beginMapping")
for i in range(1,m+1):
    for j in range(1,n+1):
        print ("* %d=R%dS%d" %(var(i,j,n),i,j))
print ("* endMapping")
print ("soft: %d ;" % m)

for i in range(1,m+1):
    at_least_one(i,m,n)

for j in range(1,n+1):
    at_most_one(j,m,n)
