# Program: CSE 110 - Guessing Game
# Author: Nathan da Costa

secret_word = "temple"
temple_lenght = len(secret_word)

# 1. I'll create the initial hint (The __ line)
# I'm  starting with nothing and add to it, just like counting
hint = ""
for i in range(0, temple_lenght, 1):
    hint = hint + "_ "

print("Welcome to the word guessing game!")
print(f"Your hint is: {hint}")

# 2. Setup the game variables
guess = ""
guess_count = 0

# 3. The main game loop (Like the one in my notes from the teacher)
while guess != secret_word:
    print() # Just adds a space
    guess = input("What is your guess? ")
    guess_count = guess_count + 1

    # to Check if they got it exactly right
    if guess == secret_word:
        print("Congratulations! You guessed it!")
    
    # to check if the guess has the wrong amount of letters
    elif len(guess) != temple_lenght:
        print("Sorry, the guess must have the same number of letters as the secret word.")
    
    else:
        # 4. I'm creaiting the new hint based on the guess
        # I'm starting with a fresh blank hint for this turn
        new_hint = ""
        
        # Loop through every position [i] (start, stop, step)
        for i in range(0, temple_lenght, 1):
            
            # Using the position [i] logic from my notes:
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