symbols = ["<",">","+","-","[","]",",","."]
cleanedChars = []

def clean(i):
	for char in i:
		if char in symbols:
			cleanedChars.append(char);

	return "".join(cleanedChars)
