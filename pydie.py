import sys, os, random						#PyDie - A Python Dice Box

def dice(a, b,):						#Rolls The Dice
	total = 0
	while b >= 1:
		roll = random.randint(1, a)
		b = b - 1
		total = total + roll
	return total

def clear_screen():						#Clear Screen function - OS Specific
	if sys.platform == 'linux2' or sys.platform == 'linux':
		os.system('clear')
	elif sys.platform == 'darwin':
		os.system('clear')
	elif sys.platform == 'win32':
		os.system('cls')
	else:
		print("\n") * 5

def fail():							#Fail Checker
	print("You fucked up Shitlord.")
	input("Press Return to continue.")

def int_check(a):						#Check user input is an integer
	check = a.isdigit()
	if check == True:
		return int(a)
	else:
		fail()
		engine()

def erase():							#Wipe the log file
	log.seek(0)
	log.truncate()
	user_response = True
	return user_response

def view():							#Access the log file
	log.seek(0)
	print(log.read())
	print("1:) Roll some more Dice.")
	print("2:) Erase the log and roll some more Dice.")
	print("3:) Exit PyDie.")
	choice = str(input("What would you like to do? > "))
	if choice == "1":
		user_response = True
	elif choice == "2":
		user_response = erase()
	elif choice == "3":
		user_response = False
	else:
		user_response = True
		fail()
	return user_response

def engine():							#Main program loop
	user_response = True
	while user_response == True:
		clear_screen()
		print(" ---------- PyDie ---------- ")
		sides = str(input("How many sides on your dice? > "))
		sides = int_check(sides)
		minimum = str(input("How many dice are you rolling? > "))
		minimum = int_check(minimum)
		modifier = str(input("Is there any bonus to the roll? > "))
		modifier = int_check(modifier)
		maximum = minimum * sides
		roll = dice(sides, minimum)
		total = roll + modifier
		output = "\nYour result was: %d\n%d (+%d) on %dd%d\n" % (
			total, roll, modifier, minimum, sides)
		print(output)
		log.write(output)
		print("1:) Roll some more dice.")
		print("2:) View the log.")
		print("3:) Wipe the log.")
		print("4:) Exit PyDie.")
		response = str(input("What would you like to do? > "))
		if response == "1":
			user_response = True
		elif response == "2":
			user_response = view()
		elif response == "3":
			user_response = erase()
		elif response == "4":
			user_response = False
		else:
			fail()

create_log = open('log.txt', 'a')
create_log.close()
log = open('log.txt', 'r+')
erase()
engine()
clear_screen()
print("Thank you for using PyDie!")
log.close()
