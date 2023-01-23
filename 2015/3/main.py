#!/bin/env python3

f = open("input.txt", "r").read()

print(f)

h = [[0, 0]]
h1 = [0, 0]


for d in f:
    if d == "^":
        h1[1] += 1
        m = h1[:]
        if m not in h:
            h.append(m)

    elif d == "v":
        h1[1] += -1
        m = h1[:]
        if m not in h:
            h.append(m)

    elif d == ">":
        h1[0] += 1
        m = h1[:]
        if m not in h:
            h.append(m)

    elif d == "<":
        h1[0] += -1
        m = h1[:]
        if m not in h:
            h.append(m)

print(len(h))
