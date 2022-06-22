import random

player=str(input("Your name here please"))
no1=int(input("enter the first number between which random number will be generated"))
no2=int(input("enter the second number"))
number=(random.randint(no1,no2))
print(number)

chances = 0

while chances<3:
    guess=int(input("enter your guess!"))
    if guess == number :
        print("Congratulations " +player+ " You have won!!")
        break
    if guess != number :
       
        chances=chances+1
    
if chances==3:
    print("failure! the number was",number)
          

