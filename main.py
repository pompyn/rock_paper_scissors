rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
choice = input(f"Choose rock, paper or scissors. For rock type 0, for paper type 1 or for scissors type 2\n")
player_choice = int(choice)
computer = random.randint(0, 2)
if player_choice > 2:
    message = input("Invalid Input!! Please enter 0,1, or 2")
if computer == player_choice:
    print(f"The computer chose {computer}.")
    print(f"It is a tie")
elif computer == 0 and player_choice == 1:
    print(f"The computer chose {rock}.")
    print(f"You win. {paper} Paper covers rock")
elif computer == 0:
    if player_choice == 2:
        print(f"The computer chose {rock}.")
        print(f"You lose. {rock} Rock breaks scissors")
elif computer == 1:
    if player_choice == 0:
        print(f"The computer chose {paper}.")
        print(f"You Lose!! {paper} Paper covers rock")
    elif player_choice == 2:
        print(f"The computer chose {paper}.")
        print(f"You Win!! {scissors} Scissors cut paper")
if computer == 2:
    if player_choice == 1:
        print(f"The computer chose {computer}. ")
        print(f"You lose.  {scissors} Scissors cut paper")


