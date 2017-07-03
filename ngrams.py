## This script should be placed in each of the gpfs.
## The subprocess from the main mumbler script will call
## this script in each of the gpfs nodes.
## This script is written for the gpfs2 node.

import os
import json
import sys

gpfs2_filename_full = '/gpfs/gpfsfpo/ngrams_full_gpfs2.json'

def construct_ngrams_from_full_json(starting_word, file_name): 
    ngrams = {}
    with open(file_name, 'r') as f:
    	for line in f:
	        if line[3:].split('":')[0].split(' ')[0] == starting_word:
	            ngrams[line[3:].split('":')[0]] = int(line[3:].split('":')[1].split(',')[0])
	        else:
	        	next
    return ngrams

if __name__ == '__main__':
    if len(sys.argv) == 2:
        starting_word = sys.argv[1]
        ngrams = construct_ngrams_from_full_json(starting_word, gpfs2_filename_full)
        with open("/gpfs/gpfsfpo/ngrams_gpfs2.json", "w") as f:
    		json.dump(ngrams, f)
