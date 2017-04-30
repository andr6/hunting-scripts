#!/usr/bin/env python
"""
soisearch.py: search for strings of interest against a given file
"""
import subprocess
import argparse

def soi_search(target, search_strs):
    """
    Search for strings of interest (soi!).
    usage: soi_search(target=<target-file>, search_strs=<strings to search for>)
    """
    try:
        for func in search_strs.keys():
            # run strings against the target file, saving the output
            process = subprocess.Popen(["strings", target], stdout=subprocess.PIPE, universal_newlines=True)
            for line in process.stdout:
                # if the name of the function is -1 there was no match, else add one to the counter
                # for the given function
                if str(line).find(func) == -1: pass
                else: search_strs[func] += 1
            
            # show count after all iterations are complete
            print "[+] %s: \t%d" % (func, search_strs[func])
            process.terminate
    except subprocess.CalledProcessError as err:
        print("[!!!] An ERROR occured: %s") % (err)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Search a file against a list of strings for strings of interest.'
        )
    parser.add_argument('target', metavar='TARGET', type=str, help='target file to search against')
    parser.add_argument('--input', dest='input_file', action='store', help='input file of search strings')
    args = parser.parse_args()

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
    
    soi_search(args.target, SOI)
