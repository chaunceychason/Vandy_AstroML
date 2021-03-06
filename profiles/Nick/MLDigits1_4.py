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
1_4 computes primary average pixel values. 
-----------------------------------------------------

"""

def plot_image_basic( xlist, ylist, title, xlab, ylab, legend_val, psize, xlog, ylog, yflip , pcounter, cmap_var=''):
	print("Entered Basic Plot Function")
	
	if legend_val != 0:
		pass
	plot_title=" Blank Title "   
	x_axis="Blank X"
	y_axis="Blank Y"
	pointsize = 5
	#sets new plot features from call. 	
	"""
	if True:
		plot_title = title
		x_axis = xlab
		y_axis = ylab
 		pointsize = psize
 	"""
	
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
=====================
 PRINT INITIAL INFO
=====================
"""
max_pixel_value = 16
test_reduce_fraction = 4.   #1/(fraction)  Reduces the test set. [set 2 for half.]
pcount = 0
#Set the Colormap
color_map_used = plt.get_cmap('autumn')

#Print the Data Keys
print 'Data Dict Keys: ', digits.keys()

#Loading in data
#Including the pixel values for each sample.
digits_data = digits['data']
total_number_of_images = len(digits_data)
#Get a single random image index for print and plot.
max_image_idx = total_number_of_images
rand_image_idx = int(random.random() * max_image_idx)

digits_targetnames = digits['target_names']
digits_target = digits['target']

"""
#PRINT HEADER INFORMAtION
"""
print '\nSample Data Matrix: Element #', rand_image_idx
print '------------------------'
#Prints digits_data[rand_image_idx]. 
#The pixel row length is currently set to 8. 
length_row = 8  
for idx, value in enumerate(digits_data[rand_image_idx]):
	print ("%d " % int(value)),
	#print " ",
	if ((idx+1)%length_row == 0):
		print '\n',

print 'Possible Target names: ', digits_targetnames
print 'Truth Targets: ', digits_target 
print 'Total Images: ', len(digits_data)


"""
===========================
 BUILD TRAINING / TEST SET
===========================
"""
test_fraction = 0.2
training_fraction = 1. - test_fraction
#Get Random Indexes. 
test_number_of_images = math.floor(total_number_of_images * test_fraction)
test_idxs = random.sample(range(0, total_number_of_images), int(test_number_of_images))
training_number_of_images = math.floor(total_number_of_images * training_fraction)
training_idxs = random.sample(range(0, total_number_of_images), int(training_number_of_images))
print 'Length test    : ', len(test_idxs)
print 'Length training: ', len(training_idxs)
test_training_ratio = test_number_of_images/training_number_of_images
test_total_ratio = test_number_of_images/total_number_of_images
print 'The Test/Training ratio is: ', test_training_ratio
print 'The Test/Total ratio is: ', test_total_ratio


"""
BUILD A SORTED LIST OF LISTS OF training DATA!
"""
#2 - Dimensional. 0-->9 ; [0 -- > matching indexes]
Training_Index_Master_Array = []
#Loop over all possilbe Number Values. {0 --> 9}
for num in range(0, 10):
	num_idxs = []
	for i, idx in enumerate(training_idxs):
		if digits_target[idx] == num:
			num_idxs.append(idx)
	num_idxs.sort()
	Training_Index_Master_Array.append(num_idxs)



"""
BUILD A SORTED LIST OF LISTS OF test DATA!
NOTE: CAUTION! DO NOT ACCESS THESE UNTIL THE END!!!!!!!
"""
#2 - Dimensional. 0-->9 ; [0 -- > matching indexes]
Test_Index_Master_Array = []
#Loop over all possilbe Number Values. {0 --> 9}
for num in range(0, 10):
	num_idxs = []
	for i, idx in enumerate(test_idxs):
		if digits_target[idx] == num:
			num_idxs.append(idx)
	num_idxs.sort()
	Test_Index_Master_Array.append(num_idxs)


#To Access the indexes of the training set matching Truth = index_TIMA
#index_TIMA = 2
#print Training_Index_Master_Array[index_TIMA]

#Do something 
"""
==========================================================
                Begin Machine Magic
==========================================================
"""
print("Building the Average Set of Numbers from Training Set...")
"""
          -------------------------------
              Build Average Number
          -------------------------------
""" 
#Declare Variables for loops
#Initialize Array for storing a single Average pixel array for a number. 

#Training_Pixels_Master_Array = [[0 for i in range(10)] for y in range(64)]
#pix_vals     = [[1 for x in range(length_row)] for y in range(length_row)]

pix_vals = [1 for x in range(length_row*length_row)]
#print pix_vals
temp_sum    = 0
idx_counter = 0 
pix_val = 0

#  For each number, for each training example matching that number,
#  for each pixel, FIND THE AVERAGE VALUE. 
#Sums over each number
for num in range(0, 10):
	#Sums over each pixel. 
	for pix_idx in range(0, (length_row*length_row)):
		#tracks the sum of the pixel value for each matching image
		#Sums over each matching image
		for i, index in enumerate(Training_Index_Master_Array[num]):
			pix_val = digits_data[index][pix_idx]
			temp_sum += pix_val 
			idx_counter += 1
		#Store Average Value and Clear temporary values.
		avg_pix_val = temp_sum / idx_counter
		idx_counter = 0
		temp_sum    = 0

		pix_vals[pix_idx] = avg_pix_val

	#Was done as a debegging measure. too lazy to remove. 
	if num == 0:
		Training_Pixel_0 = pix_vals[:]
	if num == 1:
		Training_Pixel_1 = pix_vals[:]
	if num == 2:
		Training_Pixel_2 = pix_vals[:]
	if num == 3:
		Training_Pixel_3 = pix_vals[:]
	if num == 4:
		Training_Pixel_4 = pix_vals[:]
	if num == 5:
		Training_Pixel_5 = pix_vals[:]
	if num == 6:
		Training_Pixel_6 = pix_vals[:]
	if num == 7:
		Training_Pixel_7 = pix_vals[:]
	if num == 8:
		Training_Pixel_8 = pix_vals[:]
	if num == 9:
		Training_Pixel_9 = pix_vals[:]
	if num == 10:
		print("ERROR NUMBER SHOULDNT EQUAL 10...")

#SETS THE TRAINING ARRAY. 
Training_Pixels_Master_Array= [ Training_Pixel_0, \
		Training_Pixel_1,  Training_Pixel_2,  Training_Pixel_3, \
		Training_Pixel_4,  Training_Pixel_5,  Training_Pixel_6, \
		Training_Pixel_7,  Training_Pixel_8,  Training_Pixel_9, ]


"""
#========================================
#TO PRING OUT TRAINING Matrix
#========================================
"""

rand_number_value = int(digits_target[rand_image_idx])
print("Training_Pixels_Master_Array for Random Value: %d" % int(rand_number_value))
print("==================================================")

for idx, value in enumerate(Training_Pixels_Master_Array[rand_number_value]):
	print ("%.2f " % value),
	#print " ",
	if ((idx+1)%length_row == 0):
		print '\n',


"""
          -------------------------------
             END: Build Average Number
          -------------------------------
""" 
print("Finished Building Average Numbers from Training Data!... Computing average residual.")

#Compute the average residuals. 


print("Building the Average Residual Set of Numbers from Training Set...")
"""
          -------------------------------
           Build Average Residual Number
          -------------------------------
""" 
#Declare Variables for loops
#Initialize Array for storing a single Average pixel array for a number. 
Training_res_Index_Master_Array = []

"""
BUILD A SORTED LIST OF LISTS OF residual training DATA!
"""
#COMMENTED OUT SHOULD WORK: 
"""
#2 - Dimensional. 0-->9 ; [0 -- > matching indexes]
Training_res_Index_Master_Array = []
#Loop over all possilbe Number Values. {0 --> 9}
for num in range(0, 10):
	num_idxs = []
	for i, idx in enumerate(training_idxs):
		if digits_target[idx] == num:
			num_idxs.append(idx)
	num_idxs.sort()
	Training_Index_Master_Array.append(num_idxs)
"""

#Training_Pixels_Master_Array = [[0 for i in range(10)] for y in range(64)]
#pix_vals     = [[1 for x in range(length_row)] for y in range(length_row)]

res_pix_vals = [1 for x in range(length_row*length_row)]
#print pix_vals
res_temp_sum    = 0
res_idx_counter = 0 
res_pix_val = 0

#  For each number, for each training example matching that number,
#  for each pixel, FIND THE AVERAGE VALUE. 
#Sums over each number
for num in range(0, 10):
	#Sums over each pixel. 
	for res_pix_idx in range(0, (length_row*length_row)):
		#tracks the sum of the pixel value for each matching image
		#Sums over each matching image: uses T_I_M_A[num] for enumerate. 
		for i, index in enumerate(Training_Index_Master_Array[num]):
			# - digits_data[index][res_pix_idx] gives specific value
			# - T_P_M_A[index_value][pixel_index] gives average values
			res_pix_val = abs(float(digits_data[index][res_pix_idx] - \
         				Training_Pixels_Master_Array[num][res_pix_idx] ))
			#OLD STATEMENT: res_pix_val = digits_data[index][res_pix_idx]
			res_temp_sum += res_pix_val 
			res_idx_counter += 1
		#Store Average Value and Clear temporary values.
		avg_res_pix_val = res_temp_sum / res_idx_counter
		res_idx_counter = 0
		res_temp_sum    = 0

		res_pix_vals[res_pix_idx] = avg_res_pix_val

	#Was done as a debegging measure. too lazy to remove. 
	if num == 0:
		Training_res_Pixel_0 = res_pix_vals[:]
	if num == 1:
		Training_res_Pixel_1 = res_pix_vals[:]
	if num == 2:
		Training_res_Pixel_2 = res_pix_vals[:]
	if num == 3:
		Training_res_Pixel_3 = res_pix_vals[:]
	if num == 4:
		Training_res_Pixel_4 = res_pix_vals[:]
	if num == 5:
		Training_res_Pixel_5 = res_pix_vals[:]
	if num == 6:
		Training_res_Pixel_6 = res_pix_vals[:]
	if num == 7:
		Training_res_Pixel_7 = res_pix_vals[:]
	if num == 8:
		Training_res_Pixel_8 = res_pix_vals[:]
	if num == 9:
		Training_res_Pixel_9 = res_pix_vals[:]
	if num == 10:
		print("ERROR NUMBER SHOULDNT EQUAL 10...in residual average.")

#SETS THE TRAINING ARRAY. 
Training_res_Pixels_Master_Array = [ Training_res_Pixel_0, \
		Training_res_Pixel_1,  Training_res_Pixel_2,  Training_res_Pixel_3, \
		Training_res_Pixel_4,  Training_res_Pixel_5,  Training_res_Pixel_6, \
		Training_res_Pixel_7,  Training_res_Pixel_8,  Training_res_Pixel_9, ]


"""
#========================================
#TO PRING OUT TRAINING Matrix
#========================================
"""

rand_number_value = int(digits_target[rand_image_idx])
print("Training_Res_Pixels_Master_Array for Random Value: %d" % int(rand_number_value))
print("==================================================")

for idx, value in enumerate(Training_res_Pixels_Master_Array[rand_number_value]):
	print ("%.2f " % value),
	#print " ",
	if ((idx+1)%length_row == 0):
		print '\n',


"""
          -------------------------------
         END: Build Residual Average Number
          -------------------------------
""" 
print("Finished Building Average Residual Numbers from Training Data!...")


#Find secondary class 

"""
=============================================
*********************************************
   TESTING PORTION OF THE CODE. ENTER HERE. 
*********************************************
=============================================
"""
predicted_value     = 0    #What does the code predict
success_truths      = 0    #How many correctly predicted
secondary_predicted_value   = 0  #What is the codes second choice
secondary_success_truths    = 0  #How many correctly predicted out of top two guesses
false_predictions           = 0  #How many primary predictions are false
false_secondary_predictions = 0  #How many primary or secondary predictions are false

#Initialize relevant things
iterations = 0   #Total number of items looped over.
predictions = []
truths      = []
successes   = []


res_predicted_value = 0
res_success_truths  = 0
res_secondary_predicted_value = 0
res_secondary_success_truths = 0



res_false_predictions = 0
res_false_secondary_predictions = 0

res_predictions = []
res_successes   = []


#LOOP FOR GOING OVER TEST SET!
print("MAX ITERATIONS SET TO 1/%d of test set." % test_reduce_fraction)
max_test_iterations = len(test_idxs)/test_reduce_fraction

#OPEN FILE
fail_output_file = open('fail_truth_output_file.dat', 'a')
fail_guess_output_file = open('fail_guess_output_file.dat', 'a')

#print Test_Index_Master_Array[1]
for poop_index, poop_value in enumerate(test_idxs):
	pass 

	if iterations >= max_test_iterations:
		print("Breaking due to max_test_iterations being reached! ... Break")
		break

	"""
	=====================================
	TESTING SINGLE RANDOM DRAW from test
	=====================================
	"""
	#Uncomment to choose a single Choice to evaluate. 
	random_test_idx = poop_value
	#random_test_idx = random.choice(training_idxs)

	print("\nSelected index: %s, as random choice." % random_test_idx)

	#Compute the cost of random image from averages store in costs and residuals. 
	#INITIALIZE COSTS. 
	costs_SI = []
	costs = 0

	res_costs_SI= []
	res_costs = 0 
	res_cost_val = 0
	#Loop over all possilble training images. 
	for i_counter in range(len(Training_Pixels_Master_Array)):
		#print Training_Pixels_Master_Array[i_counter]
		for pix_idx in range(length_row*length_row):
			cost_val = abs(float(Training_Pixels_Master_Array[i_counter][pix_idx]) - \
						float(digits_data[random_test_idx][pix_idx]))
			costs += cost_val

			#Should work over the same indexes of T_P_M_A since they use same counter
			res_cost_val = abs(float(Training_res_Pixels_Master_Array[i_counter][pix_idx]) - \
						float(digits_data[random_test_idx][pix_idx]))
			res_costs += res_cost_val

		costs_SI.append(costs)
		costs = 0

		res_costs_SI.append(res_costs)
		res_costs = 0

	#PRINT THE COSTS TO THE SCREEN.
	print("======================================================")
	print("               COSTS CALCULATED! ..."             )
	print("======================================================")
	print("Predicted # |  Pixel Cost_per_image ")
	#PRint out the Costs for each possible class. 
	for i in range(10):
		stringv = float(costs_SI[i])
		res_stringv = float(res_costs_SI[i])
		print "   {0} ..........  {1:.1f}   {2:.1f}".format(i, stringv, res_stringv)


	"""
	------------------------
	FIND MIMIMUM COST
	------------------------
	"""
	#Sets the predicted_value by finding the minum index cost. 
	predicted_value = costs_SI.index(min(costs_SI))
	predicted_value_cost = costs_SI[predicted_value]

	res_predicted_value = res_costs_SI.index(min(res_costs_SI))
	res_secondary_predicted_value = -1

	#Find Secondary Value by looping through costs ignoring predicted cost. 
	current_cost = 9999999
	res_current_cost = 9999999 

	for i, cost in enumerate(costs_SI):
		if i == predicted_value or cost >= current_cost:
			pass
		else:
			current_cost = cost
			secondary_predicted_value = i 

	"""
	---------------------------------
	CHECK PRIMARY VS SECONDARY GUESS
	---------------------------------
	"""
	#if predicted_value_cost > (current_cost - (.25*predicted_value_cost)):
	if ((current_cost - predicted_value_cost) < (0.25*predicted_value_cost)):
		print("THE COSTS ARE QUITE CLOSE!")

		"""
		---------------------------------
	         	CHECK RESIDUALS! 
		---------------------------------
		"""	
		for res_i, res_cost in enumerate(res_costs_SI):
				if res_i == res_predicted_value or res_cost >= res_current_cost:
					pass
				else:
					res_current_cost = res_cost
					res_secondary_predicted_value = res_i 

	truth = digits_target[random_test_idx]
	print("WE FIRST PREDICT A VALUE OF: %d" % predicted_value)
	print("It may also be the value : %d" % secondary_predicted_value)
	print("THE ACTUAL VALUE WAS   : %d" % truth)

	print("\nThe residual predicted cost value is         :  %d" % res_predicted_value)	
	print("The Secondary residual predicted cost value is:  %d" % res_secondary_predicted_value)	

	#LISTS to store predictions and truths for analysis. 
	predictions.append(predicted_value)
	truths.append(truth)
	
	res_predictions.append(res_predicted_value)

	"""
	--------------------------------------
	TEST THE PRIMARY PREDICTIONS AND STATS
	--------------------------------------
	"""
	if predicted_value == truth:
		successes.append(1)  #Successes == 1 means TRUTH
		success_truths += 1
	else:
		successes.append(0)  #Successes == 0 means FAILURE
		fail_output_file.write('%d\n' % truth)
		fail_guess_output_file.write('%d\n' % predicted_value)

		"""
		============================
		#PLOT AND SAVE THE FAILURES.
		============================ 
		"""

		print("FAILURE EXAMPLE PRINTING....")
		title_label = "A single number. " 
		x_label = "x coordinate"
		y_label = "y coordinate"
		x_data  = digits['images'][poop_value]
		y_data  = []
		legend_val = 0
		pointsize = 3
		yflip = False
		ylog = 0
		xlog = 0
		pcount = plot_image_basic(x_data, y_data, title_label, x_label, y_label, \
		         legend_val, pointsize, xlog, ylog,  yflip, pcount, color_map_used)

		false_predictions += 1

	if (secondary_predicted_value == truth) or (predicted_value == truth):
		secondary_success_truths += 1
	else:
		false_secondary_predictions += 1


	"""
	--------------------------------------
	TEST THE RESIDUAL PREDICTIONS AND STATS
	--------------------------------------
	"""
	if res_predicted_value == truth:
		res_successes.append(1)  #Successes == 1 means TRUTH
		res_success_truths += 1
	else:
		res_successes.append(0)  #Successes == 0 means FAILURE
		"""
		============================
		#PLOT AND SAVE THE FAILURES.
		============================ 
		
		print("FAILURE EXAMPLE PRINTING....")
		title_label = "A single number. " 
		x_label = "x coordinate"
		y_label = "y coordinate"
		x_data  = digits['images'][poop_value]
		y_data  = []
		legend_val = 0
		pointsize = 3
		yflip = False
		ylog = 0
		xlog = 0
		pcount = plot_image_basic(x_data, y_data, title_label, x_label, y_label, \
		         legend_val, pointsize, xlog, ylog,  yflip, pcount, color_map_used)
		"""

		res_false_predictions += 1

	if (res_secondary_predicted_value == truth) or (res_predicted_value == truth):
		res_secondary_success_truths += 1
	else:
		res_false_secondary_predictions += 1

	iterations += 1

print("\n")
print("*************************************************************")
print(" ****************      FINISHED TESTING     **************** ")
print("*************************************************************\n")
print("================================")
print("SUCCESS/ failure TABLE: ")
print("================================")
print("Correct Primary Predictions: %d " % success_truths)
print("Correct Pri|Sec Predictions: %d " % secondary_success_truths)
print("Total Predictions Made:  %d " % iterations)
print("Ratio of Correct (Primary) to Total:  %.3f" % (1.0*success_truths/iterations))
print("Ratio of Correct (Pri|Sec) to Total:  %.3f" % (1.0*secondary_success_truths/iterations))
print("================================")

print("\nCorrect RES Primary Predictions: %d " % res_success_truths)
print("Correct RES Pri|Sec Predictions: %d " % res_secondary_success_truths)
print("Total RES Predictions Made:  %d " % iterations)
print("Ratio of Correct (RES Primary) to Total:  %.3f" % (1.0*res_success_truths/iterations))
print("Ratio of Correct (RES Pri|Sec) to Total:  %.3f" % (1.0* res_secondary_success_truths/iterations))
print("================================")



suc_count  = 0
fail_count = 0
tot_count  = 0
fail_num_by_num      = []
success_ratio_by_num = []
fail_ratio_by_num    = []

for num in range(10):
	for i, elem in enumerate(truths):
		if elem == num:
			if successes[i] == 1:
				#FAILURE
				suc_count += 1
			else: 
				fail_count += 1
			tot_count += 1
	try:
		suc_ratio = 1.0*suc_count/tot_count
		fail_ratio = 1.0*fail_count/tot_count
	except:
		print("Encountered a value with no data points! num = %d " % num)
		suc_ratio = 0
		fail_ratio = 0 

	success_ratio_by_num.append(suc_ratio)
	fail_num_by_num.append(fail_count)
	fail_ratio_by_num.append(fail_ratio)
	suc_count  = 0
	fail_count = 0
	tot_count  = 0

print("Success Ratio By Number\n ------------------------------")
print("Truth_val | Success | Failure | #Fail Pri. ")
for imtired, reallytired in enumerate(success_ratio_by_num):
	print("    %d:       %.3f       %.3f        %d" % \
		  (imtired, reallytired, fail_ratio_by_num[imtired],  \
		  	fail_num_by_num[imtired]))


"""
====================
 PRINT SAMPLE IMAGE
====================
"""
#initial plots generated to 0. 
#pcount = 0
#Set the Colormap
#color_map_used = plt.get_cmap('autumn')

#Plot 1. A single number. 
#------------------------------------------------------------------
#Generate a random number for the image from 0 ==> max_image_idx
#max_image_idx = total_number_of_images
#rand_image_idx = int(random.random() * max_image_idx)
"""
title_label = "A single number. " 
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

"""

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
fail_output_file.close()
fail_guess_output_file.close()

print("Time: ")
print (datetime.now() - startTime)
print("END. ")




#Doop. 
