# idea for the creating games...........
"""
import random number 
loop
ask from the user that wanna play or not.....!
if user says yes...!
toss the dice of 2
print theo oputput
if user says no....!
break the loop
else
print write invalid output.....!

"""

import random
count=0
while True:
     choice= input('enter the choice of the person is : yes/no:  ').lower()
     if choice=="yes":
      dice1= random.randint(1,6)
      dice2= random.randint(1,6)
      count+=1
      print(f" the dice1 is {count}: {dice1}\n the dice2 is: {dice2} \n their time of the toss is count: {count}") 
     elif choice=="no":
        print("Thanku So Much")
        break
     else:
      print('please try correct value...!')