## This is the  script that takes the raw google 2gram dataset and pre-processes
## it and places a resulting json file into each of the gpfs nodes.

import zipfile
import os
import string
import json

def pre_process(word):
    word = word.lower()
    if word.isdigit():
        word = '<digit>'
    return word

ngrams_full = {}
os.chdir("/gpfs/gpfsfpo")

for a in range(34): #gpfs1
    file_name = 'googlebooks-eng-all-2gram-20090715-' + str(a) + '.csv.zip'
    zip_ref = zipfile.ZipFile(file_name, 'r')
    zip_ref.extractall("/gpfs/gpfsfpo")
    zip_ref.close()
    file_name = 'googlebooks-eng-all-2gram-20090715-' + str(a) + '.csv'
    with open(file_name) as csv_file:
        for line in csv_file:
            ngram = ' '.join([pre_process(s) for s in line.split('\t')[0].split(' ')])
            count = int(0 if line.split('\t')[2] is None else line.split('\t')[2])
            if set(ngram).issubset(string.printable):
                if not ngram in ngrams_full: 
                    ngrams_full[ngram] = count
                else:
                    ngrams_full[ngram] = ngrams_full.get(ngram) + count
            else:
                next
    os.remove(file_name)

with open("/root/gpfs/gpfsfpo/ngrams_full_gpfs1.json", "w") as f:
    json.dump(ngrams_full, f)