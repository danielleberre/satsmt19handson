#!/usr/bin/python3

import sys

def var(i,j,k):
    """
    parameters:
    i: row
    j: column
    m: value
    """
    return i*100+j*10+k

def exactly_one_cell(i,j):
    literals=[]
    for k in range(1,n2+1):
        literals.append(var(i,j,k))
    print("%s = 1;" % ' '.join(map(lambda i : "+1 x"+str(i),literals)))


def exactly_one_row(i):
    for k in range(1,n2+1):
        literals=[]
        for j in range(1,n2+1):
            literals.append(var(i,j,k))
        print("%s = 1;" % ' '.join(map(lambda i : "+1 x"+str(i),literals)))

def exactly_one_column(j):
    for k in range(1,n2+1):
        literals=[]
        for i in range(1,n2+1):
            literals.append(var(i,j,k))
        print("%s = 1;" % ' '.join(map(lambda i : "+1 x"+str(i),literals)))

def exactly_one_block(r,c):
    for k in range(1,n2+1):
        literals=[]
        for i in range(r,r+n):
            for j in range(c,c+n):
                literals.append(var(i,j,k))
        print("%s = 1;" % ' '.join(map(lambda i : "+1 x"+str(i),literals)))

if (len(sys.argv)!=2):
    n = 3
else:
    n = int(sys.argv[1])

n2 = n*n
max = n2*100+n2*10+n2

print ("* #variable= %d #constraint= %d" % (max,n2*n2*4))

for i in range(1,n2+1):
    for j in range(1,n2+1):
        exactly_one_cell(i,j)

for i in range(1,n2+1):
    exactly_one_row(i)

for j in range(1,n2+1):
    exactly_one_column(j)

blocks = list(filter(lambda i: i%n==1,range(1,n2+1)))
for i in blocks:
    for j in blocks:
        exactly_one_block(i,j)