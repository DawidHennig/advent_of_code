#!/bin/env python3
from re import findall

f = open("input.txt", "r").read().split()

p = 0
r = 0

for _ in f:
    dim = [int(x) for x in findall('(\d+)', _)]
    dim.sort()
    p += 2*dim[0]*dim[1] + 2*dim[1]*dim[2] + 2*dim[2]*dim[0] + dim[0]*dim[1]

print(p)

for _ in f:
    dim = [int(x) for x in findall('(\d+)', _)]
    dim.sort()
    r += 2*dim[0] + 2*dim[1] + dim[0]*dim[1]*dim[2]

print(r)
