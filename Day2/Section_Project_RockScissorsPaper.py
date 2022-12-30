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

#Write your code below this line 👇
import random 
options = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,2)

if user < 0 or user >2:
    print("Error.")
elif user == computer:
    print(options[user])
    print("computer chose: ", options[computer], sep = '\n')
    print("It's a tie.")
elif user > computer:
    if computer == 0 and user == 20:
        print(options[user])
        print("computer chose: ", options[computer], sep = '\n')
        print("You lose.")
    else:
        print(options[user])
        print("computer chose: ", options[computer], sep = '\n')
        print("You win.")
else:
    if user == 0 and computer == 2:
        print(options[user])
        print("computer chose: ", options[computer], sep = '\n')
        print("You win.")
    else:
        print(options[user])
        print("computer chose: ", options[computer], sep = '\n')
        print("You lose.")


