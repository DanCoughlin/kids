cipher_key = {
	'a' : 'b',
	'b' : 'c',
	'c' : 'd',
	'd' : 'e',
	'e' : 'f',
	'f' : 'm',
	'g' : 'n',
	'h' : 'l',
	'i' : 'z',
	'j' : 'q',
	'k' : 'o',
	'l' : 'x',
	'm' : 'v',
	'n' : 'w',
	'o' : 'p',
	'p' : 'r',
	'q' : 'a',
	'r' : 'y',
	's' : 'g',
	't' : 'h',
	'u' : 'i',
        'v' : 'u',
	'w' : 'j',
	'x' : 'k',
	'y' : 's',
	'z' : 't',
	' ' : ' '
}

def encrypt(plain):
	encrypted = [] 
	plain = plain.lower()
	for letter in plain:
		encrypted.append(cipher_key[letter])
	print(''.join(encrypted))

def decrypt(scramble):
	scramble = scramble.lower()
	decrypted = []
	for letter in scramble:
		for k, v in cipher_key.items():
			if v == letter:
				decrypted.append(k)
	print(''.join(decrypted))

if __name__ == "__main__":
	print("Hello Friend. What would you like to encrypt?")
	plain = raw_input()	
	encrypt(plain)
	print("Ok, would you like me to decrypt something?")
	scramble = raw_input()
	decrypt(scramble)

