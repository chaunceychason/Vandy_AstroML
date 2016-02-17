import sys
import os
import numpy as np
import math
import random
from scipy import stats  
import matplotlib
matplotlib.use( 'Agg' )
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
#import sklearn 

from datetime import datetime
startTime = datetime.now()

print("WELCOME TO A QUICK PYTHON PROGRAM.")
print("It will do machine learning stuff with Numbers.. yep. ")


"""
-----------------------------------------------------
NICHOLAS CHASON 
Machine Learning Code 1. - Native Nays. 
-----------------------------------------------------

"""

def plot_image_basic( xlist, ylist, title, xlab, ylab, legend_val, psize, xlog, ylog, yflip , pcounter, cmap_var=''):
	print("Entered Basic Plot Function")
	
	
	if len(xlist) != len(ylist):
		print("ERROR! X and Y DATA LENGTHS ARE DIFFERENT!")
		print("Length: x_data: %g" % len(xlist))
		print("Length: y_data: %g" % len(ylist))
	if len(xlist)==0 or len(ylist)==0:
		print("ERROR: list length is ZERO!")
		print("Length: x_data: %g" % len(xlist))
		print("Length: y_data: %g" % len(ylist))
	else:
		print("Length: x_data: %g" % len(xlist))
		print("Length: y_data: %g" % len(ylist))

	if legend_val != 0:
		pass
	plot_title=" Blank Title "   
	x_axis="Blank X"
	y_axis="Blank Y"
	pointsize = 5
	#figure_name=os.path.expanduser('~/Feb9LSSHW2_plot1_A' +'.png')
	#figure_name=os.path.expanduser('~/Feb9LSSHW2_plot1_A' +'.png')
	#Choose which type of plot you would like: Commented out.
	#sets new plot features from call. 	
	"""
	if True:
		plot_title = title
		x_axis = xlab
		y_axis = ylab
 		pointsize = psize
 	"""
	#plt.scatter(xlist, ylist, s=pointsize, lw=0)

	#plt.title(plot_title)
	#plt.xlabel(x_axis)
	#plt.ylabel(y_axis)
	#plt.yscale("log")
	"""
	if yflip == True:
		try:
			plt.ylim(max(ylist), min(ylist))
		except:
			print("uh.oh.... try except statement. check ylim.")
	if ylog != 0:
		plt.yscale("log", nonposy='clip')
	if xlog != 0:
		plt.xscale("log", nonposy='clip')
	"""
	plt.imshow(xlist, cmap=cmap_var)
	#plt.xlim(min(xlist), max(xlist) )
	figure_name=os.path.expanduser('~/Feb17astroML_plot%s.png' % pcount)
	plt.savefig(figure_name)
	print("Saving plot: %s" % figure_name)
	plt.clf()

	dummy = pcounter + 1
	return dummy

"""
===================
   LOAD DIGITS
===================
"""
digits = load_digits()

"""
#----------------------------------------
#To print the Descritption of load_digits 
#----------------------------------------
#To print the full description of data...
print digits['DESCR']
"""


"""
===================
 PRINT INIT INFO
===================
"""
print 'Data Dict Keys: ', digits.keys()

#Loading in data
#Including the pixel values for each sample.
digits_data = digits['data']
sample_element = 1
print '\nSample Data Matrix: Element #', sample_element
print '------------------------\n', digits_data[sample_element-1]

#Targets
#This prints the possible targets
digits_targetnames = digits['target_names']
print 'Possible Target names: ', digits_targetnames

digits_target = digits['target']
print 'Truth Targets: ', digits_target 



"""
====================
 PRINT SAMPLE IMAGE
====================
"""
color_map_used = plt.get_cmap('autumn')

#Plot 1. A single number. 
#------------------------------------------------------------------
pcount = 0
#Generate a random number for the image from 0 ==> max_image_idx
max_image_idx = 10.
rand_image_idx = int(random.random() * max_image_idx)
title_label = "A single number" 
x_label = "x coordinate"
y_label = "y coordinate"
x_data  = digits['images'][rand_image_idx]
y_data  = []
legend_val = 0
pointsize = 3
yflip = False
ylog = 0
xlog = 0

pcount = plot_image_basic(x_data, y_data, title_label, x_label, y_label, \
         legend_val, pointsize, xlog, ylog,  yflip, pcount, color_map_used)





#Guess something
#initial_guess = 1


#Initialize relevant things
iterations = 0


#Initialize Derivative

"""
print("Now Plotting....")

#
===================
PLOTTING GUESSES 
===================
#
pcount = 0
title_label = "" 
x_label = ""
y_label = ""
x_data  = np.linspace(0, len(errorsLIST), num=len(errorsLIST))
y_data  = errorsLIST
legend_val = 0
pointsize = 3
yflip = False
ylog = 0
xlog = 0

pcount = plot_basic(x_data, y_data, title_label, x_label, y_label, \
         legend_val, pointsize, xlog, ylog,  yflip, pcount)

"""


print("Time: ")
print (datetime.now() - startTime)

print("END. ")




#Doop. 