from time import sleep
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabetCaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeric = '0123456789'
print ("Welcome")
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
			newMessage += character
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
	choice = input('Type "julius" to encrypt, "brutus" to decrypt, or "exit" to exit...')
	if choice == "julius":
		julius()
	elif choice == "brutus":
		brutus()
#/*DEV SHORTHANDS#
	elif choice == "j":
		julius()
	elif choice == "b":
		brutus()
#DEV SHORTHANDS*/#
	elif choice == "exit":
		sleep(1)
		exit()
	else:
		print ("Invalid input, retrying...")
		senate()
senate()

input('Press enter to continue...')