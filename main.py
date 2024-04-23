import random
import sys
from termcolor import colored

def print_menu():
    print("Welcome to Wordle!")
    print("Type a 5 letter word to start.")

def rand_word():
    with open("words.txt") as f:
        wordsArray = f.read().splitlines()
        return random.choice(wordsArray)

print_menu()
# word = rand_word()
word = "MONEY"

# 7 is exclusive
for attempt in range(1, 7):
    guess = input().upper()

    # Do not allow hints for more than 5 letters
    for i in range( min(len(guess), 5) ):
        if guess[i] == word[i]:
            # Print correct letter but do not print endline
            print(colored(guess[i], "green"), end = "")
        elif guess[i] in word:
            print(colored(guess[i], 'yellow'), end = "")
        else:
            print(guess[i], end = "")
    
    # Print an endline at the end of the word
    print("")
        
    # If the entire guess is correct, we win
    if guess == word:
        print(f"Correct! You guessed the word in {attempt} tries.") # f string
        break