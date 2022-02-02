#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 14:38:47 2022

@author: janeth
"""
import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists

def frequency_calc(textFname, outputFname):
    d = {}
    with open(textFname, 'r') as inputFile:
        for line in inputFile:
            # get rid of newline characters
            line = line.strip()
            # split line on whitespace and punctuation
            words = re.split("\s+|[,.-;'\"-]|''", line)
            for word in words:
                word = word.lower()
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1
    
    del d['']
    sorted_d = dict(sorted(d.items()))
                    
    with open(outputFname, "w") as outputFile:
        # Writing data to a file
        for key, value in sorted_d.items():
            content = key + " " + str(value) + "\n"
            outputFile.write(content)


def main():
    print("Begin calculating...")
    if len(sys.argv) != 3:
        print("Correct usage: wordCountTest.py <input text file> <output file> <solution key file>")
        sys.exit()

    textFname = sys.argv[1]
    outputFname = sys.argv[2]
    
    #make sure text file exists
    if not os.path.exists(textFname):
        print ("text file input %s doesn't exist! Exiting" % textFname)
        sys.exit()
    
    frequency_calc(textFname, outputFname)   
    print("Finished!")
    
if __name__ == "__main__":
    main()
    
    
    
    