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
    literals.append(m-i+1)  # weighted soft clause
    for j in range(1,n+1):
        literals.append(var(i,j,n))
    literals.append(0)
    print(' '.join(map(str,literals)))

def at_most_one(j,m,n):
    for i in range(1,m+1):
        for k in range(i+1,m+1):
            print("10 -%d -%d 0" % (var(i,j,n),var(k,j,n))) # hard clause

if (len(sys.argv)!=3):
    m = 4
    n = 3
else:
    m = int(sys.argv[1])
    n = int(sys.argv[2])

print ("c beginMapping")
for i in range(1,m+1):
    for j in range(1,n+1):
        print ("c %d=R%dS%d" %(var(i,j,n),i,j))
print ("c endMapping")
print ("p wcnf %d %d" % (m*n,m+n*m*(m-1)/2))
for i in range(1,m+1):
    at_least_one(i,m,n)

for j in range(1,n+1):
    at_most_one(j,m,n)
