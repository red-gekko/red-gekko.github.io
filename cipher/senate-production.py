from time import sleep
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabetCaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeric = '0123456789'
sleep(1)
print("PROGRAM ACTIVATING")
sleep(1)
print("RUNNING SYSTEM CHECK...")
sleep(1)
print("COMPLETE")
sleep(0.5)
print("RUNNING DIAGNOSTICS...")
sleep(1)
print("COMPLETE")
sleep(0.5)
print("CHECKING HARDWARE...")
sleep(1)
print("COMPLETE")
sleep(1)
print("ALL CHECKS COMPLETE")
sleep(1)
print("Welcome")
sleep(2)
def inputNumber(message):
	while True:
		try:
			userInput = int(input(message))
		except ValueError:
			print("Not an integer! Try again.")
			continue
		else:
			return userInput
			break
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
def julius():
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
			newMessage += newCharacter
	print('Your new message is: ', newMessage)
	senate()

def brutus():
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
	senate()
def senate():
	choice = input('Type "julius" to encrypt, "brutus" to decrypt, "help" for info, or "exit" to quit...')
	if choice == "julius":
		julius()
	elif choice == "brutus":
		brutus()
	elif choice == "exit":
		sleep(1)
		exit()
	elif choice == "help":
		senate_help()
	else:
		print ("Invalid input, retrying...")
		senate()
senate()