#! usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description='Hexdump of a file')
parser.add_argument('-i', '--infile', type=str, required=True, metavar='', help='input file')
parser.add_argument('-o', '--outfile', type=str, metavar='', help='input file')
args = parser.parse_args()

with open(i, "r") as infile:
    while True:
        chunk = infile.read(16)
        if not chunk:break

        print(chunk)
