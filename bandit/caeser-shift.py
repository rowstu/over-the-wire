
message = "Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh"

key = 13

mode = 'decrypt'

UPPER='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER='abcdefghijklmnopqrstuvwxyz'

translated = ''

for symbol in message:
	if symbol in UPPER:
		num = UPPER.find(symbol) #get the number of the symbol
		if mode == 'encrypt':
			num = num + key
		elif mode == 'decrypt':
			num = num - key

		# handle the wrap around if num is larger then the length of
		# UPPER or less than 0
		if num >= 26:
			num = num - 26
		elif num < 0:
			num = num + 26

		translated = translated + UPPER[num]
	elif symbol in LOWER:
		num = LOWER.find(symbol) #get the number of the symbol
		if mode == 'encrypt':
			num = num + key
		elif mode == 'decrypt':
			num = num - key

		# handle the wrap around if num is larger then the length of
		# LOWER or less than 0
		if num >= 26:
			num = num - 26
		elif num < 0:
			num = num + 26

		translated = translated + LOWER[num]
		

	else:
		# just add the symbol without encrypting/decrypting
		translated = translated + symbol

print(translated)
