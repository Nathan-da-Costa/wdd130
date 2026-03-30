# Program: Word Guessing Game
# Author: Nathan da 
# Random and the list are my criativity lines
# added .lower() to the input so that if someone types with a capital letter it still works
import random

# Simple list of words to choose from
word_list = ["temple", "heart", "python", "brazil", "school"]
secret_word = random.choice(word_list)
temple_lenght = len(secret_word)

# 1. I'll create the initial hint (The __ line)
hint = ""
for i in range(0, temple_lenght, 1):
    hint = hint + "_ "

print("Welcome to the word guessing game!")
print(f"Your hint is: {hint}")

# 2. I'll Setup the game variables
guess = ""
guess_count = 0

# 3. The main game loop
while guess != secret_word:
    print() # Just adds a space
    guess = input("What is your guess? ").lower()
    guess_count = guess_count + 1

    # to Check if they got it exactly right
    if guess == secret_word:
        print("Congratulations! You guessed it!")
    
    # to check if the guess has the wrong amount of letters
    elif len(guess) != temple_lenght:
        print("Sorry, the guess must have the same number of letters as the secret word.")
    
    else:
        # 4. I'm creaiting the new hint based on the guess
        new_hint = ""
        
        for i in range(0, temple_lenght, 1):
            letter_guess = guess[i]
            letter_secret = secret_word[i]

            if letter_guess == letter_secret:
                # Same letter, same spot: UPPERCASE
                new_hint = new_hint + letter_guess.upper() + " "
            
            elif letter_guess in secret_word:
                # In the word, but wrong spot: lowercase
                new_hint = new_hint + letter_guess.lower() + " "
            
            else:
                # Not in the word at all: underscore
                new_hint = new_hint + "_ "
        
        print(f"Your hint is: {new_hint}")

# 5. Final message outside the loop
print(f"It took you {guess_count} guesses.")