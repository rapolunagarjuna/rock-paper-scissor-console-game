import random

rounds = 0
score = 0
while True :
    user_choice = input("Type your choice in rock, paper and scissors: ").lower
    computer_choice = random.randint(1, 3)
    if not (user_choice == "rock" or user_choice == "paper" or user_choice == "scissors"):
        print("Warning: Can't choose anything apart from rock, paper and scissors")
        continue
    else:
        if user_choice == "rock":
            user_choice = 1
        elif user_choice == "paper":
            user_choice = 2
        else:
            user_choice = 3

        rounds += 1
        
        if user_choice == computer_choice:
            print("Draw")
        elif (user_choice > computer_choice and user_choice - computer_choice == 1) or (user_choice == 1 and computer_choice == 3):
            score += 1
            print("You won")
        else:
            print("You lost")
        
        is_quit = input("Do you want to quit the game ? (y/ n)")
        if is_quit == "y" or is_quit == "Y":
            break

print("Total rounds played: ", rounds)
print("Your score: ", score)

        


