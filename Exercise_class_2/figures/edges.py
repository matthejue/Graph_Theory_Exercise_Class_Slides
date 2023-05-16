#!/usr/bin/env python

from math import floor

acc = []
for i in range(16):
    acc += [(floor(i / 2), i % 4)]

print(acc)
