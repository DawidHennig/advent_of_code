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

hsr = [[0, 0]]
hs = [0, 0]
hr = [0, 0]

for s, d in enumerate(f):
    if s % 2 == 0:
        if d == "^":
            hs[1] += 1
            m = hs[:]
            if m not in hsr:
                hsr.append(m)

        elif d == "v":
            hs[1] += -1
            m = hs[:]
            if m not in hsr:
                hsr.append(m)

        elif d == ">":
            hs[0] += 1
            m = hs[:]
            if m not in hsr:
                hsr.append(m)

        elif d == "<":
            hs[0] += -1
            m = hs[:]
            if m not in hsr:
                hsr.append(m)
    else:
        if d == "^":
            hr[1] += 1
            m = hr[:]
            if m not in hsr:
                hsr.append(m)

        elif d == "v":
            hr[1] += -1
            m = hr[:]
            if m not in hsr:
                hsr.append(m)

        elif d == ">":
            hr[0] += 1
            m = hr[:]
            if m not in hsr:
                hsr.append(m)

        elif d == "<":
            hr[0] += -1
            m = hr[:]
            if m not in hsr:
                hsr.append(m)

print("Santa:", hs)
print("Robot:", hr)
print("Santa&Robot:", hsr)
print(len(hsr))
