import random

rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_img = [rock, paper, scissors]
u_input = int(input("0 for rock, 1 for paper  and 2 for scissors: "))
print(game_img[u_input])
c_choice = random.randint(0, 2)
print("Computer's choice: ")
print(game_img[c_choice])

if u_input == 0 and c_choice == 1:
    print("You Lose!")
elif u_input == 0 and c_choice == 0:
    print("It's a Draw")
elif u_input == 1 and c_choice == 1:
    print("It's a Draw")
elif u_input == 2 and c_choice == 2:
    print("It's a Draw")
elif u_input == 0 and c_choice == 2:
    print("You Win!") 
elif u_input == 1 and c_choice == 2:
    print("You Lose!")  
elif u_input == 2 and c_choice == 1:
    print("You Win!")     
elif u_input == 1 and c_choice == 0:
    print("You Win!")     