import sys
import os
import numpy as np
import math
import matplotlib
matplotlib.use( 'Agg' )
import matplotlib.pyplot as plt
#import sklearn 
from datetime import datetime
startTime = datetime.now()

print("WELCOME TO A QUICK PYTHON PROGRAM.")
print("It will do machine learning stuff with Numbers.. yep. ")


"""
-----------------------------------------------------
NICHOLAS CHASON 
Plot False Truth values in histogram to see if theres a pattern.
-----------------------------------------------------

"""

#f = open("fail_truth_output_file.dat", 'r')

with open("fail_truth_output_file.dat", 'r') as f:
    lines = f.read().splitlines()

hist_LIST = []
for i, val in enumerate(lines):
	hist_LIST.append(int(val))

#print lines
print("Length of list: %d" % len(hist_LIST))

bin_list = np.linspace(-0.5, 9.5, 11)
print bin_list
plt.hist(hist_LIST, bins=bin_list)


plt.title("Fail Condition Truth Values")
plt.xlabel("Truth Value")
plt.ylabel("Incorrect Count")
plt.savefig("fail_truth_histogram.png")

print("SAVING FIGURE. fail_truth_histogram.png")
