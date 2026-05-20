######################
# SENATE is an application
# built for basic encryption
# of strings.
# It allows users to create basic
# encrypted communications based
# on the historical "Caesar Cipher".
# This is the developer build.
######################
from time import sleep
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabetCaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeric = '0123456789'
sleep(1)											# IMPORTANT NOTE:
print("PROGRAM ACTIVATING")							# These "system checks" are
sleep(1)											# not really checking anything.
print("RUNNING SYSTEM CHECK...")					# All they're doing is contributing to a
sleep(1)											# "security theatre".
print("COMPLETE")									# If users *feel* that the program is
sleep(0.5)											# more advanced than it truly is,
print("RUNNING DIAGNOSTICS...")						# they may be more immersed within its use,
sleep(1)											# thus providing a more complete experience.
print("COMPLETE")									# In reality, the program has no need to
sleep(0.5)											# check for these things.
print("CHECKING HARDWARE...")
sleep(1)
print("COMPLETE")
sleep(1)
print("ALL CHECKS COMPLETE")
sleep(1)
print("Welcome")
sleep(2)
def inputNumber(message):							# COMMENTS:
	while True:										# This function allows us to
		try:										# verify that the Cipher Key
			userInput = int(input(message))			# (seen later)
		except ValueError:							# is a valid integer.
			print("Not an integer! Try again.")
			continue
		else:
			return userInput
			break
def devPass():										# COMMENTS:
	print("Accessing developer mode...")			# This function helps restrict
	devPassKey = input("ENTER DEV KEY: ")			# developer mode by providing
	if devPassKey == "KHOOR ZRUOG":					# a puzzle beforehand.
		dev()										# It's extremely basic and not secure at all.
	elif devPassKey == "hint":						# But it doesn't really need to be.
		print("HELLO WORLD")
		print("JULIUS 3")
		print("DEVNOTE- TOO OBVIOUS, GOTTA FIX THIS SOON")
		devPass()
	else:
		print("INCORRECT")
		senate()
def dev():											# Developer mode allows for
	print("Developer mode active!")					# faster debugging by providing
	devchoice = input("Please enter a dev shorthand. To view shorthands, enter 'help'. To exit dev mode, enter 'senate'... ")
	if devchoice == "help":							# shorthands for the Senate.
		dev_help()									# It's sealed off (barely)
	elif devchoice == "h":							# by the devPass function
		dev_help()									# above.
	elif devchoice == "he":
		dev_help()
	elif devchoice == "hel":
		dev_help()
	elif devchoice == "HELP":
		dev_help()
	elif devchoice == "H":
		dev_help()
	elif devchoice == "HE":
		dev_help()
	elif devchoice == "HEL":
		dev_help()
	elif devchoice == "julius":
		dev_julius()
	elif devchoice == "j":
		dev_julius()
	elif devchoice == "ju":
		dev_julius()
	elif devchoice == "jul":
		dev_julius()
	elif devchoice == "juli":
		dev_julius()
	elif devchoice == "juliu":
		dev_julius()
	elif devchoice == "JULIUS":
		dev_julius()
	elif devchoice == "J":
		dev_julius()
	elif devchoice == "JU":
		dev_julius()
	elif devchoice == "JUL":
		dev_julius()
	elif devchoice == "JULI":
		dev_julius()
	elif devchoice == "JULIU":
		dev_julius()
	elif devchoice == "BRUTUS":
		dev_brutus()
	elif devchoice == "B":
		dev_brutus()
	elif devchoice == "BR":
		dev_brutus()
	elif devchoice == "BRU":
		dev_brutus()
	elif devchoice == "BRUT":
		dev_brutus()
	elif devchoice == "BRUTU":
		dev_brutus()
	elif devchoice == "exit":
		sleep(1)
		exit()
	elif devchoice == "e":
		sleep(1)
		exit()
	elif devchoice == "ex":
		sleep(1)
		exit()
	elif devchoice == "exi":
		sleep(1)
		exit()
	elif devchoice == "EXIT":
		sleep(1)
		exit()
	elif devchoice == "E":
		sleep(1)
		exit()
	elif devchoice == "EX":
		sleep(1)
		exit()
	elif devchoice == "EXI":
		sleep(1)
		exit()
	elif devchoice == "dev":
		print("You are already in Developer Mode!")
		dev()
	elif devchoice == "DEV":
		print("You are already in Developer Mode!")
		dev()
	elif devchoice == "senate":
		senate()
	elif devchoice == "SENATE":
		senate()
	else:
		print("Invalid input, retrying...")
		dev()
def dev_help():
	print("")
	print("DEV is a tool used by the developers of senate.py, it allows for faster debugging by introducing shorthands. Includes a cipher-locked pass key.")
	print("")
	print("BRUTUS is a tool used for decrypting the Caesar Cipher, or more accurately, back-rolls the Cipher Discus. It takes input (typically ciphertext) and subtracts the Cipher Key.")
	print("BRUTUS shorthands: b, br, bru, brut, brutus.")
	print("")
	print("JULIUS is a tool used for encrypting the Caesar Cipher, or more accurately, forward-rolls the Cipher Discus. It takes input (typically plaintext) and adds the Cipher Key.")
	print("JULIUS shorthands: j, ju, jul, juli, juliu, julius.")
	print("")
	print("EXIT allows users to exit the program. I'm not sure how to explain it any futher than that.")
	print("EXIT shorthands: e, ex, exi, exit.")
	print("")
	print("HELP views this page. Chances are you don't need me to tell you that.")
	print("HELP shorthands: h, he, hel, help.")
	dev()

def senate_help():
	print("")
	print("BRUTUS is a tool used for decrypting the Caesar Cipher, or more accurately, back-rolls the Cipher Discus. It takes input (typically ciphertext) and subtracts the Cipher Key.")
	print("")
	print("JULIUS is a tool used for encrypting the Caesar Cipher, or more accurately, forward-rolls the Cipher Discus. It takes input (typically plaintext) and adds the Cipher Key.")
	print("")
	print("EXIT allows users to exit the program. I'm not sure how to explain it any futher than that.")
	print("")
	print("HELP views this page. Chances are you don't need me to tell you that.")
	senate()

def julius():												# Clocks the Discus forward
	key = inputNumber('Please enter an encryption key: ') 	# Provides the Key value for clocking the Discus forward.
	message = input('Please enter a message: ')			  	# Provides the plaintext.
	newMessage = ''										 	# Blanks out the message for use.
	for character in message:							 	# Begins the loop.
		if character in alphabet:							# Checks if the character in the string is in the alphabet (lower case).
			position = alphabet.find(character)				# Finds the character's position in the alphabet out of 26.
			newPosition = (position + key) % 26				# Clocks the Key into the Discus to discover the new position.
			newCharacter = alphabet[newPosition]			# Records the Discus to produce the new ciphertext character.
			newMessage += newCharacter						# Adds the ciphertext character to the message.
		elif character in alphabetCaps:						# Checks if the character in the string is in the alphabet (upper case).
			position = alphabetCaps.find(character)			# ^^
			newPosition = (position + key) % 26				# ^^
			newCharacter = alphabetCaps[newPosition]		# ^^
			newMessage += newCharacter						# ^^
		elif character in numeric:							# Checks if the character in the string is in the numerical system.
			position = numeric.find(character)				# ^^
			newPosition = (position + key) % 10				# ^^
			newCharacter = numeric[newPosition]				# ^^
			newMessage += newCharacter						# ^^
		else:												# ^^
			newMessage += character							# Adds punctuation
	print('Your new message is: ', newMessage)				# Prints the message
	senate()												# Backtracks to Senate console

def dev_julius():											# Developer mode for Julius, same as above except:
	key = inputNumber('Please enter an encryption key: ')
	message = input('Please enter a message: ')
	newMessage = ''
	for character in message:
		if character in alphabet:
			position = alphabet.find(character)
			newPosition = (position + key) % 26
			newCharacter = alphabet[newPosition]
			newMessage += newCharacter
		elif character in alphabetCaps:
			position = alphabetCaps.find(character)
			newPosition = (position + key) % 26
			newCharacter = alphabetCaps[newPosition]
			newMessage += newCharacter
		elif character in numeric:
			position = numeric.find(character)
			newPosition = (position + key) % 10
			newCharacter = numeric[newPosition]
			newMessage += newCharacter
		else:
			newMessage += character
	print('Your new message is: ', newMessage)
	dev()													# Backtracks to Dev console instead!

def brutus():												# Named because it "undoes" Julius. It clocks back the Cipher Discus.
	key = inputNumber('Please enter an encryption key: ')	# All of this is the same as Julius. The only difference...
	message = input('Please enter a message: ')
	newMessage = ''
	for character in message:
		if character in alphabet:
			position = alphabet.find(character)
			newPosition = (position - key) % 26				# The key is subtracted from the message instead!
			newCharacter = alphabet[newPosition]
			newMessage += newCharacter
		elif character in alphabetCaps:
			position = alphabetCaps.find(character)
			newPosition = (position - key) % 26
			newCharacter = alphabetCaps[newPosition]
			newMessage += newCharacter
		elif character in numeric:
			position = numeric.find(character)
			newPosition = (position - key) % 10
			newCharacter = numeric[newPosition]
			newMessage += newCharacter
		else:
			newMessage += character
	print('Your new message is: ', newMessage)
	senate()
def dev_brutus():											# Developer version of Brutus.
	key = inputNumber('Please enter an encryption key: ')
	message = input('Please enter a message: ')
	newMessage = ''
	for character in message:
		if character in alphabet:
			position = alphabet.find(character)
			newPosition = (position - key) % 26
			newCharacter = alphabet[newPosition]
			newMessage += newCharacter
		elif character in alphabetCaps:
			position = alphabetCaps.find(character)
			newPosition = (position - key) % 26
			newCharacter = alphabetCaps[newPosition]
			newMessage += newCharacter
		elif character in numeric:
			position = numeric.find(character)
			newPosition = (position - key) % 10
			newCharacter = numeric[newPosition]
			newMessage += newCharacter
		else:
			newMessage += character
	print('Your new message is: ', newMessage)
	dev()													# Sends you back to dev
def senate():												# Senate is the overall console. The central hub.
	choice = input('Type "julius" to encrypt, "brutus" to decrypt, "help" for info, or "exit" to quit...')
	if choice == "julius":									# The "choice" module allows users to select their funtion:
		julius()											# Julius, Brutus, Exit, Dev, and Help.
	elif choice == "brutus":
		brutus()
#/*DEV SHORTHANDS#
	elif choice == "dev":									# Accesses the Developer console.
		devPass()
#DEV SHORTHANDS*/#
	elif choice == "exit":									# Exits the program.
		sleep(1)
		exit()
	elif choice == "help":									# Reads the Help dialogue.
		senate_help()
	else:
		print ("Invalid input, retrying...")				# Catches invalid commands and backtracks user.
		senate()
senate()													# Initialises Senate to begin usage of program.

input('Press enter to continue...')							# Mostly obsolete, used in debugging to show a module hasn't been backtracked
															# properly.