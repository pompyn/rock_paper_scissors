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
if computer == 0:
    print(f"The computer chose: {rock}")
elif computer == 1:
    print(f"The computer chose: {paper}")
elif computer == 2:
    print(f"The computer chose: {scissors}")

if player_choice == 0:
    print(f"Player chose: {rock}")
elif player_choice == 1:
    print(f"Player chose: {paper}")
elif player_choice == 2:
    print(f"Player chose: {scissors}")

if computer == player_choice:
    print("It's a draw")
elif computer > player_choice:
    print("Computer Wins!")
elif computer < player_choice:
    print("You win")
