
# File: adventure_game.py
#Author: [Nathan Almeida]
#Purpose: W03 Final Project - Complete Adventure Game.

#Creativity: 
#I added a third hidden option in the first level (FLYING CAR) to exceed 
#the 'two-choice' requirement and created multiple ending scenarios 
#based on Harry Potter.


print("--- WELCOME TO THE WIZARDING WORLD ---")
print("You are standing at Platform 9 3/4. The Hogwarts Express is about to leave!")

# LEVEL 1
choice1 = input("Do you board the TRAIN, stay on the PLATFORM, or look for a FLYING CAR? ").lower()

if choice1 == "train":
    print("\nYou find a cabin with a boy named Harry. The trolley witch arrives with snacks.")
    
    # LEVEL 2 (Nested)
    choice2 = input("Do you buy a CHOCOLATE FROG, a PUMPKIN PASTY, or NOTHING? ").lower()
    
    if choice2 == "chocolate frog":
        print("\nThe frog jumps out! You try to catch it.")
        # LEVEL 3 (Nested)
        choice3 = input("Do you JUMP after it or let it ESCAPE? ").lower()
        if choice3 == "jump":
            print("\nYou caught it! Inside is a rare Dumbledore card. YOU WIN!")
        elif choice3 == "escape":
            print("\nYou lost your snack, but Harry shares his beans with you. YOU WIN!")
        else:
            print("\nYou sat there confused and the witch moved on. GAME OVER.")

    elif choice2 == "pumpkin pasty":
        print("\nIt's delicious, but you feel very sleepy.")
        # LEVEL 3
        choice3 = input("Do you take a NAP or STAY awake? ").lower()
        if choice3 == "nap":
            print("\nYou missed the arrival at Hogwarts! Hagrid has to wake you up. GAME OVER.")
        elif choice3 == "stay":
            print("\nYou see the castle glowing in the dark. It is magical! YOU WIN!")
        else:
            print("\nInvalid choice. You fall off your seat. GAME OVER.")

    else:
        print("\nYou arrived at Hogwarts very hungry. You fainted during the ceremony! GAME OVER.")

elif choice1 == "platform":
    print("\nThe train leaves. You are stranded. You see a familiar giant man named Hagrid.")
    
    # LEVEL 2
    choice2 = input("Do you ASK for help or HIDE from him? ").lower()
    
    if choice2 == "ask":
        print("\nHagrid takes you on his flying motorcycle!")
        # LEVEL 3
        choice3 = input("Do you hold on TIGHT or look at the VIEW? ").lower()
        if choice3 == "tight":
            print("\nYou safely arrive at the Great Hall. Everyone is impressed! YOU WIN!")
        elif choice3 == "view":
            print("\nYou got dizzy and almost fell, but Hagrid caught you. YOU WIN!")
        else:
            print("\nHagrid couldn't hear you over the engine. You got lost. GAME OVER.")
    else:
        print("\nYou stayed at the station all night. Muggles are staring at your owl. GAME OVER.")

elif choice1 == "flying car":
    print("\nYou and Ron jump in the car! You are flying high above the train.")
    
    # LEVEL 2
    choice2 = input("Do you fly HIGHER into the clouds or stay LOW? ").lower()
    
    if choice2 == "higher":
        print("\nThe car starts to freeze and the engine stalls!")
        # LEVEL 3
        choice3 = input("Do you use a SPELL or KICK the dashboard? ").lower()
        if choice3 == "spell":
            print("\n'Reparo!' The car works and you land at the castle. YOU WIN!")
        elif choice3 == "kick":
            print("\nIt worked! The car wakes up and flies you to school. YOU WIN!")
        else:
            print("\nThe car crashed into the lake. The giant squid is hungry. GAME OVER.")
    else:
        print("\nThe Muggles saw you! The Ministry of Magic is waiting for you. GAME OVER.")

else:
    print("\nOh, no!!!! You couldn't decide yourself, the Dementors have surrounded the platform and you feel a big chill. GAME OVER.")

print("\nThank you for playing!")
  