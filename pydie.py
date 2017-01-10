import sys, os, random					#PyDie - A Python Dice Box with log file

def header():
	print(" ---------- PyDie ----------\n ")

def dice(a, b,):						#Rolls The Dice
	total = 0
	while b >= 1:
		roll = random.randint(1, a)
		b = b - 1
		total = total + roll
	return total

def cont():								#Function to continue
	input("Press Return to continue...")

def clear_screen():						#Clear Screen function - OS Specific
	if sys.platform == 'linux2' or sys.platform == 'linux':
		os.system('clear')
	elif sys.platform == 'darwin':
		os.system('clear')
	elif sys.platform == 'win32':
		os.system('cls')
	else:
		print("\n") * 5

def fail():								#Fail Checker
	print("You fucked up Shitlord.")
	cont()
	menu()

def int_check(a):						#Check user input is an integer
	check = a.isdigit()
	if check == True:
		return int(a)
	else:
		fail()
		menu()

def erase():
	clear_screen()						#Wipe the log file
	header()
	user_response = str(input(
		"Are you sure you want to wipe the log file? (y/n) >"))
	if user_response == "Y" or user_response == "y":
		print("Wiping the log.")
		log.seek(0)
		log.truncate()
		cont()
		menu()
	elif user_response == "N" or user_response == "n":
		print("The log has not been wiped.")
		cont()
		menu()
	else:
		fail()

def view():								#Access the log file
	clear_screen()
	header()
	log.seek(0)
	print(log.read())
	cont()
	clear_screen()
	menu()

def engine():							#Main program loop
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
	log.write(output)
	log.write("\n")
	cont()
	menu()

def menu():								#Main Menu
	clear_screen()
	header()
	print("1:) Roll some dice.")
	print("2:) View the log.")
	print("3:) Wipe the log.")
	print("4:) Exit PyDie.")
	response = str(input("\nWhat would you like to do? > "))
	if response == "1":
		engine()
	elif response == "2":
		view()
	elif response == "3":
		erase()
	elif response == "4":
		close()
	else:
		fail()

def close():							#Close PyDie
	clear_screen()
	header()
	print("Thank you for using PyDie!")
	cont()
	clear_screen()
	log.close()

create_log = open('log.txt', 'a')
create_log.close()
log = open('log.txt', 'r+')
menu()
