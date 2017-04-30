#!/usr/bin/env python
"""
soisearch.py: search for strings of interest against a given file
"""
import subprocess, sys
import os
import argparse

def soi_search(target, search_strs):
    """
    Search for strings of interest (soi!).
    usage: soi_search(target=<target-file>, search_strs=<strings to search for>)
    """
    
    print "[FILE: \t%s]" % (target)
    try:
        for func in search_strs.keys():
            process = subprocess.Popen(["strings", target], 
                                        stdout=subprocess.PIPE, 
                                        universal_newlines=True)
            for line in process.stdout:
                if str(line).find(func) == -1: pass 
                else: search_strs[func] += 1

            print "[+] %s: \t%d" % (func, search_strs[func])
            process.terminate
    except subprocess.CalledProcessError as err:
        print("[!!!] An ERROR occured: %s") % (err)

if __name__ == "__main__":
    # Argument handling
    parser = argparse.ArgumentParser(description=\
        'Search a file against a list of strings for strings of interest.')
    
    parser.add_argument('target', metavar='TARGET', type=str, 
                            help='target file to search against \
                            (if a directory, search all regular files in top level)')
    
    parser.add_argument('--input', dest='input_file', action='store', 
                            help='input file of search strings')
    
    parser.add_argument('--output', dest='output_file', action='store',
                            help='output file to save results to')
    
    args = parser.parse_args()

    # handle input files containing search strings
    if args.input_file:
        with open(args.input_file, 'r') as input_fd:
            search_strs = [x.rstrip('\n') for x in input_fd]   
        SOI = dict.fromkeys(search_strs, 0)
    else:
        SOI = {
            "strcpy": 0,
            "strcmp": 0,
            "memcpy": 0,
            "memcmp": 0,
            "gets": 0,
            "strcat": 0,
            "malloc": 0
            }
                
    # handle outputting to a file
    if args.output_file:
        sys.stdout = open(args.output_file, 'a')

    if os.path.isdir(args.target):
        for fd in os.listdir(args.target):
            fd_path = os.path.join(args.target, fd)
            soi_search(fd_path, SOI)
    
    else:
        soi_search(args.target, SOI)