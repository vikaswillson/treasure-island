import random
user=int(input("what do you want to choose? Type ) for rock,1 for paper and 2 for scissors: "))
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
image=[rock,paper,scissors]
print(f"you choose{image[user]}")
computer=random.randint(0,2)

print(f"computer choose {image[computer]}")
if computer == user:
    print("its a draw")
elif((computer==0 and user==1) or (computer==1 and user==2) or (computer==2 and user==0)):
    print("you win!")
elif((computer==0 and user==2) or (computer==1 and user==0) or (computer==2 and user==1)):
    print("you lose!")


