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
  |\\  |
  |   |
      |
      |
    ===
'''
,
'''
  +---+
  O   |
 /|\\  |
  |   |
      |
      |
    ===
'''
,
'''
  +---+
  O   |
 /|\\  |
  |   |
 /    |
      |
    ===
'''
,
'''
  +---+
  O   |
 /|\\  |
  |   |
 / \\  |
      |
    ===
'''
]

secretWord = ["halloween","candy","costume","scare","monster"]
mystery = random.choice(secretWord)
mystery = list(mystery)
guessList = list("____________")
misses = 0

while misses > 7:
  print(hangList)
  print("Welcome to hangman")
  print(guessList)
  guess = ("Guess a letter: ")
  index = 0




