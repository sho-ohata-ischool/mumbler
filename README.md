# mumbler

Implementation of the mumbler program from the Scaling Up! Really Big Data class under the UC Berkeley Master of Information in Data Science program. 

Execute the program by passing the starting word and the iteration amount, e.g. `python mumbler.py 'hello' 3`. The first argument is the starting word and the second argument is the max number of words to print out. 

Details of setting up the GPFS environment with three virtual servers can be seen [here](https://github.com/MIDS-scaling-up/coursework/tree/master/week4/hw/gpfs_setup).

`ngrams.py` should be placed in each of the gpfs nodes as the main python script will be calling each of the script placed in each of the gpfs nodes.

`ngrams_summary.py` is the script that takes the raw 2grams google dataset and outputs a smaller summary file that the mumbler script will be reading data off of to generate the next word.
