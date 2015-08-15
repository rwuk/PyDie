import sys							#PyDie
import os							#A Dice box by Syn
import random

def dice(a, b):							#RNG function - emulates the dice roll
	roll = random.randint(a, b)			#a = lowest integer, b = highest integer
	return roll

def clear_screen():						#Clear Screen function - OS Specific
	if sys.platform == 'linux2' or sys.platform == 'darwin':
		os.system('clear')				
	elif sys.platform == 'win32':
		os.system('cls')
	else:
		print "\n" * 5

user_response = "y"						#Variable to control the while loop

while user_response == "y" or user_response == "Y":		#Check if variable is true
	clear_screen()
	print " ---------- PyDie ---------- "
	sides = int(raw_input("How many sides on your dice? > "))		#user input to
	minimum = int(raw_input("How many dice are you rolling? > "))	#configure variables
	modifier = int(raw_input("Is there any bonus to the roll? > "))	#for the dice roll
	maximum = minimum * sides				#Obtain the maximum integer
	roll = dice(minimum , maximum)			#RNG call from lowest to highest numbers
	total = roll + modifier					#Add any bonus'
	print """
	\nYour result was: %d\n\n%d (%d <-> %d) + %d\n
	""" % (total ,roll, minimum, maximum, modifier)		#Display output
	user_response = raw_input("Do you want to roll some more dice? y/n > ")	#Break the while loop?

clear_screen()
print "Thank you for using PyDie!"
