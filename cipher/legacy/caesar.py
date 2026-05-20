alphabet = 'abcdefghijklmnopqrstuvwxyz'
#alphabetCaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#numberbet = '0123456789'
key = 3
newMessage = ''

#character = input('Please enter a character: ')
message = input('Please enter a message: ')

for character in message:
	if character in alphabet:
		position = alphabet.find(character)
#		print(position)
		newPosition = (position + key) % 26
#		print(newPosition)
		newCharacter = alphabet[newPosition]
#		print(newCharacter)
		newMessage += newCharacter
		print('Your new message is: ', newMessage)
#	if character in alphabetCaps:
#		position = alphabetCaps.find(character)
#		print(position)
#		newPosition = (position + key) % 26
#		print(newPosition)
#		newCharacterCaps = alphabetCaps[newPosition]
#		print(newCharacter)
#		print('Your new message is: ', newMessage)
#		newMessage += newCharacter + newCharacterCaps
	else:
		newMessage += newCharacter