alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabetCaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeric = '0123456789'
key = 3
newMessage = ''

message = input('Please enter a message: ')

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
input('Press enter to continue...')
