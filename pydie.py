import sys, os, random					#PyDie - A Python Dice Box with log file

def header():							#Graphical Header
	print(" ---------- PyDie ----------\n ")

def cont():								#Function to continue
	input("Press Return to continue...")

def fail():								#Fail Checker
	print("You fucked up Shitlord.")
	cont()

def dice(a, b,):						#Rolls The Dice
	total = 0
	while b >= 1:
		roll = random.randint(1, a)
		b = b - 1
		total = total + roll
	return total

def int_check(a):						#Check user input is an integer
	check = a.isdigit()
	if check == True:
		return int(a)
	else:
		fail()
		menu()

def clear_screen():						#Clear Screen function - OS Specific
	if sys.platform == 'linux2' or sys.platform == 'linux':
		os.system('clear')
	elif sys.platform == 'darwin':
		os.system('clear')
	elif sys.platform == 'win32':
		os.system('cls')
	else:
		print("\n") * 5

def view(a):							#Access the log file
	clear_screen()
	header()
	if a == True:
		log.seek(0)
		print(log.read())
	else:
		for i in log:
			print(i)
	cont()
	clear_screen()
	menu()

def erase(a):							#Wipe the log file
	clear_screen()
	header()
	user_response = str(input(
		"Are you sure you want to wipe the log file? (y/n) >"))
	if user_response == "Y" or user_response == "y":
		print("Wiping the log.")
		if a == True:
			log.seek(0)
			log.truncate()
		else:
			del log[:]
		cont()
		menu()
	elif user_response == "N" or user_response == "n":
		print("The log has not been wiped.")
		cont()
		menu()
	else:
		fail()
		menu()

def menu():								#Menu System
	clear_screen()
	header()
	print("1:) Roll some dice.")
	print("2:) View the log.")
	print("3:) Wipe the log.")
	print("4:) Exit PyDie.")
	response = str(input("\nWhat would you like to do? > "))
	if response == "1":
		engine(user_log)
	elif response == "2":
		view(user_log)
	elif response == "3":
		erase(user_log)
	elif response == "4":
		close(user_log)
	else:
		fail()
		menu()

def engine(a):							#Main program loop
	clear_screen()
	header()
	sides = str(input("How many sides on your dice? > "))
	sides = int_check(sides)
	minimum = str(input("How many dice are you rolling? > "))
	minimum = int_check(minimum)
	modifier = str(input("Is there any bonus to the roll? > "))
	modifier = int_check(modifier)
	maximum = minimum * sides
	roll = dice(sides, minimum)
	total = roll + modifier
	output = "Your result was: %d\n%d (+%d) on %dd%d\n" % (
		total, roll, modifier, minimum, sides)
	print("\n" + output)
	if a == True:
		log.write(output)
		log.write("\n")
	else:
		log.append(output)
	cont()
	menu()

def close(a):							#Close PyDie
	clear_screen()
	header()
	print("Thank you for using PyDie!")
	cont()
	clear_screen()
	if a == True:
		log.close()
	else:
		a == False

clear_screen()
header()
user_log = str(input("Would ou like to use a persistent log file? (y/n) >"))
if user_log == "Y" or user_log == "y":
	user_log = True
	print("Creating the log file.")
	create_log = open('log.txt', 'a')
	create_log.close()
	log = open('log.txt', 'r+')
	cont()
	menu()
elif user_log == "N" or user_log == "n":
	user_log = False
	print("The log will not be persistent.")
	log = []
	cont()
	menu()
else:
	fail()
	close(user_log)
