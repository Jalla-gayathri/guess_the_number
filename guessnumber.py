import random
target=random.randint(1,100)
while True:

    user_choice=input("guess the target or Quit:")
    if(user_choice=="Quit"):
        break


    user_choice=int(user_choice)
    if(user_choice==target):
        print("your guess is correct")
        break
    elif(user_choice<target):
        print("your choice is too small.take a bigger guess...")
    else:
        print("your choice is too big.take a smaller guess...")

print("----game over----")
