import sys						#PyDie
import os						#Please make sure you have a file called
import random						#log.txt in the same folder as this script

def dice(a, b):						#RNG function - emulates the dice roll
	roll = random.randint(a, b)			#a = lowest integer, b = highest integer
	return roll

def clear_screen():					#Clear Screen function - OS Specific
	if sys.platform == 'linux2' or sys.platform == 'darwin':
		os.system('clear')				
	elif sys.platform == 'win32':
		os.system('cls')
	else:
		print "\n" * 5
		
def erase():						#Wipe the log file
	log.seek(0)
	log.truncate()
	user_response = True
	return user_response

def view():						#Access the log file
	log.seek(0)
	print log.read()
	print "\n1:) Roll some more Dice."
	print "2:) Erase the log and roll some more Dice."
	print "3:) Exit PyDie."
	choice = raw_input("What would you like to do? > ")
	
	if choice == "1":
		user_response = True
	elif choice == "2":
		user_response = erase()
	elif choice == "3":
		user_response = False
	else:
		user_response = True
		print "You fucked up Shitlord."
		raw_input("Press Return to continue.")
		
	return user_response

def engine():
	user_response = True				#Variable to control the while loop
	while user_response == True:			#Check if variable is true
		clear_screen()
		print " ---------- PyDie ---------- "
		sides = int(raw_input("How many sides on your dice? > "))	#user input to
		minimum = int(raw_input("How many dice are you rolling? > "))	#configure variables
		modifier = int(raw_input("Is there any bonus to the roll? > "))	#for the dice roll
		maximum = minimum * sides		#Obtain the maximum integer
		roll = dice(minimum , maximum)		#RNG call from lowest to highest numbers
		total = roll + modifier			#Add any bonus'
		output = "\nYour result was: %d\n%d (%d <-> %d) + %d\n" % (total ,roll, minimum, maximum, modifier)
		print output
		log.write(output)
		print "1:) Roll some more dice."
		print "2:) View the log."
		print "3:) Wipe the log."
		print "4:) Exit PyDie."
		response = raw_input("What would you like to do? > ")	#What ya wanna do?
		
		if response == "1":
			user_response = True
		elif response == "2":
			user_response = view()
		elif response == "3":
			user_response = erase()
		elif response == "4":
			user_response = False
		else:
			print "You fucked up Shitlord."
			raw_input("Press Return to continue.")
			

log = open('log.txt', 'r+')
erase()
engine()
clear_screen()
print "Thank you for using PyDie!"
log.close()
