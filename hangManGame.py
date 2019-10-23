# Eric Nunez
# 10/21/19
# Period 6

import os
import time
import random 

hangList = [
'''
  +---+
      |
      |
      |
      |
    ===
'''
,
'''
  +---+
  O   |
      |
      |
      |
      |
    ===
'''
,
'''
  +---+
  O   |
  |   |
  |   |
      |
      |
    ===
'''
,
'''
  +---+
  O   |
  |\\ |
  |   |
      |
      |
    ===
'''
,
'''
  +---+
  O   |
 /|\\ |
  |   |
      |
      |
    ===
'''
,
'''
  +---+
  O   |
 /|\\ |
  |   |
 /    |
      |
    ===
'''
,
'''
  +---+
  O   |
 /|\\ |
  |   |
 / \\ |
      |
    ===
'''
]
secretWord = ["halloween","candy","costume","scare","monster"]
randomWord = random.choice(secretWord)
letterList = list(randomWord)
print(letterList)
secret = []
misses = 0

while misses < 7:
	print(hangList[misses])
	guess = input("Choose a letter: ")
	if guess in letterList:

		print("You guessed the word")
	else:
		misses += 1


if misses == 7:
	print("Game Over")





