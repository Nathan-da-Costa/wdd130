"""
File: adventure_game.py
Author: [Nathan Almeida]
Purpose: W03 Milestone - Adventure Game First Step.
"""

print("--- WELCOME TO THE WIZARDING WORLD ---")
print("You are standing at Platform 9 3/4. The Hogwarts Express is about to leave!")

# Level 1 Choice
# I used .lower() to make sure TRAIN, train, and Train all work.
choice1 = input("Do you board the TRAIN, stay on the PLATFORM, or look for a FLYING CAR? ").lower()

if choice1 == "train":
    print("\nYou jump onto the train just as it starts to move! You look for a place to sit.")
    # For the milestone, I have to stop here. In the final version, Level 2 goes here.

elif choice1 == "platform":
    print("\nThe train leaves without you. You are stuck at the station with your trunk.")
    # For the milestone, I have to stop here.

elif choice1 == "flying car":
    print("\nYou see a blue Ford Anglia nearby. It looks like it could fly!")
    # For the milestone, I have to stop here.

else:
    print("\n Oh, no!!!You could not decide yourself. A Dementor appears and you feel a sudden chill!")
    # For the milestone, I have to stop here.