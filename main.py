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



if computer == player_choice:
    print(f"The computer chose {computer}. You chose {player_choice}")
    print(f"It is a tie")
elif computer == 0 and player_choice == 1:
    print(f"The computer chose {computer}. You chose {player_choice}")
    print(f"You win. {paper} covers rock")
elif computer == 0:
    if player_choice == 2:
        print(f"The computer chose {computer}. You chose {player_choice}")
        print(f"You lose. {rock}breaks scissors")
elif computer == 1:
    if player_choice == 0:
        print(f"The computer chose {computer}. You chose {player_choice}")
        print(f"You Lose!! {paper}covers rock")
    elif player_choice == 2:
        print(f"The computer chose {computer}. You chose {player_choice}")
        print(f"You Win!! {scissors} cut paper")
if computer == 2:
    if player_choice == 1:
        print(f"The computer chose {computer}. You chose {player_choice}")
        print(f"You lose.  {scissors} cut paper")
