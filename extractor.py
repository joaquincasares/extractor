#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
    print "Usage: ./extractor.py filename <delimiter>"

delimiter = '#'
if len(sys.argv) == 3:
    delimiter = sys.argv[2]

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

for line in lines:
    if line.lstrip()[0:1] == delimiter:
        print line
