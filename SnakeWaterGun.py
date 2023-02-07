print("\t\t***Welcome to the Snake Water Gun Game***")
print("\tChoose Your favourite Number:\n"
      "\t1 for Snake\n"
      "\t2 for Water\n"
      "\t3 for Gun\n")
import random
count=0
cnt=10
usr=0
num=0
comp = random.randint(1, 3)
while cnt>count:
  user = int(input("Enter your Number="))
  print("The Computer Number is=", comp)
  print("\n")
  if user==1:
     if user==1 and comp==1:
       print("Match is Tie!\n")
       count=count+1
     elif user==1 and comp==2:
       print("You Win!\n")
       usr=usr+1
       count=count+1
     elif user==1 and comp==3:
       print("Computer Win!\n")
       num=num+1
       count=count+1
  elif user==2:
     if user==2 and comp==1:
       print("Computer Win!\n")
       num=num+1
       count=count+1
     elif user==2 and comp==2:
       print("Match is Tie!\n")
       count=count+1
     elif user==2 and comp==3:
       print("You Win!\n")
       usr=usr+1
       count=count+1
  elif user==3:
     if user==3 and comp==1:
       print("You Win!\n")
       usr=usr+1
       count=count+1
     elif user==3 and comp==2:
       print("Computer Win!\n")
       num=num+1
       count=count+1
     elif user==3 and comp==3:
       print("Match is Tie!\n")
       count=count+1
  else:
     print("You Enter Invali Number!\n"
           "Kindly Try Again!\n")
  # sum=cnt-count
  print(f"You Win {usr} Matches!\n")
  print(f"Computer Win {num} Matches!\n")
  print(f"{cnt-count} Chances Left Out Off {cnt}!\n")
print("Game Over!!!!!\n")
if usr==num:
  print("Match is Tie!!\n")
elif usr>num:
  print("You Win The Match!\n")
else:
  print("Computer Win The Match!\n")
print(f"Your Total Point is {usr} "
      f"Computer Total Point is {num}\n")
