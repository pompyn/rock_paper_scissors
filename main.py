import random
choice = input(f"Choose rock, paper or scissors. For rock type 0, for paper type 1 or for scissors type 2\n")
player_choice = int(choice)
computer = random.randint(0, 2)

if computer == player_choice:
    print(type(player_choice))
    print(f"It is a tie")
elif computer == 0 and player_choice == 1:
    print(f"You win. Paper covers rock")
elif computer == 0:
    if player_choice == 1:
        print(f"You win!! Paper covers rock")
    elif player_choice == 2:
        print(f"You lose. Rock breaks scissors")
elif computer == 1:
    if player_choice == 0:
        print(f"You Lose!! Paper covers rock")
    elif player_choice == 2:
        print(f"You Win!! Scissors cut paper")
if computer == 2:
    if player_choice == 0:
        print("You Win!! Rock smashes scissors")
    elif player_choice == 1:
        print(f"You lose. Scissors cut paper")
