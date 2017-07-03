## Main mumbler script that generates the next word based on the
## frequencies found in the 2gram google dataset.

import random
import os
import json
import subprocess
import sys

gpfs1_filename = '/gpfs/gpfsfpo/ngrams_gpfs1.json'
gpfs2_filename = '/gpfs/gpfsfpo/ngrams_gpfs2.json'
gpfs3_filename = '/gpfs/gpfsfpo/ngrams_gpfs3.json'

def read_ngrams_from_json(file_name): ##read json file created from subprocess
    with open(file_name, 'r') as f:
        ngrams = json.load(f)
    return ngrams

def pick_random_ngram(ngrams): #pass ngrams dict
    ngrams_list = []
    max_count = int(ngrams[max(ngrams, key=ngrams.get)]/100) ##anything less than 1% of highest count will be discarded
    ngrams_pruned = {}
    for key, value in ngrams.iteritems():
        if value > max_count:
            ngrams_pruned[key] = value
        else:
            next
    min_count = ngrams_pruned[min(ngrams_pruned, key=ngrams_pruned.get)]
    for key, value in ngrams_pruned.iteritems():
        ngrams_list.extend([key.split(' ')[1]] * int(value/min_count))
    return random.choice(ngrams_list)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        starting_word = sys.argv[1]
        max_iter = int(sys.argv[2])
        print "Starting with \"%s\"" %starting_word
        for a in range(max_iter):
            ps = []
            p = subprocess.Popen(['python', 'ngrams_gpfs1.py', starting_word])
            ps.append(p)
            p = subprocess.Popen(['ssh', 'gpfs2', 'python', 'ngrams_gpfs2.py', starting_word])
            ps.append(p)
            p = subprocess.Popen(['ssh', 'gpfs3', 'python', 'ngrams_gpfs3.py', starting_word])
            ps.append(p)
            for p in ps:
                p.wait()
            ngrams_gpfs1 = read_ngrams_from_json(gpfs1_filename)
            ngrams_gpfs2 = read_ngrams_from_json(gpfs2_filename)
            ngrams_gpfs3 = read_ngrams_from_json(gpfs3_filename)
            dicts = {}
            dicts[0], dicts[1], dicts[2] = ngrams_gpfs1, ngrams_gpfs2, ngrams_gpfs3
            super_dict = {}
            for a in range(3):
                for k, v in dicts[a].iteritems():
                    if not k in super_dict:
                        super_dict[k] = v
                    else:
                        super_dict[k] = super_dict.get(k) + v

            if bool(super_dict):
                starting_word = pick_random_ngram(super_dict)
                print "Next word: \"%s\"" %starting_word
            else:
                print "Ending mumbler \"%s\" not found" %starting_word
                break
    else:
        print "Please pass starting word and max number."