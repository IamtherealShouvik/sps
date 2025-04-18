# 🪨📄✂️ - Simple Game, simple rule.

import random
choices=["stone","paper","scissor"]
print("Stone vs Paper vs Scissor")
while True:
    user=input("\nChoose one. Type 'quit' to stop: ").lower()
    if user == 'quit':
        print('\nBye.')
        break
    if user not in choices:
        print("\nInvalid choice. Try again")
        continue
    computer = random.choice(choices)
    print("\nComputer chose" ,computer)
    if user == computer:
     print("\nTie!")
    elif (user == "stone" and computer == "scissor") or \
     (user == "paper" and computer == "stone") or \
     (user == "scissor" and computer == "paper"):
     print("\nYou won.")

    else:
     print("\nComputer won.")   