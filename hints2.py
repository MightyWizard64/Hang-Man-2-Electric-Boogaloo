# Eric Nunez
# 10/23/19
# hints for hangman project

# How to keep track of misses
secret = "christmas"
misses = 0
secret = list(secret)

hangList = ['''pic1''','''pic2''','''pic3''','''pic4''','''pic5''','''pic6''','''pic7''']

while misses > 7:
	print(hangList[misses])
	guess = input("Guess a letter: ")
	if guess in secret:
		# loop through secret and find all matching letters
		print("That letter is in the secret word")
	else:
		misses += 1