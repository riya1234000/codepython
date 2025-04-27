import random
""" stone : 1,
paper: -1
sizzer: 0

"""
computer = random.choice([1,-1,0])
youstr= input("enter the value of the user: ")
yourDict= {"s":1, "p":-1, "sr":0}
reverseDict= {1:"stone", -1: "paper", 0:"sizzer" }
you= yourDict[youstr]
print(f" your choice: {reverseDict[you]}\n computer choice: {reverseDict[computer]}")
if (computer==you):
    print("it's a tie.......!")
elif(computer==-1 and you==1):
    print("it's a loss .....!")
elif(computer==0 and you==1):
    print("you win it baby......!")
elif(computer==1 and you==-1):
    print(f"you win it baby.....!")
elif(computer==0 and you==-1):
    print('you loss it baby....!')
elif(computer==1 and you==0):
    print("you loss it baby...!")
elif(computer==-1 and you==0):
    print("you win it baby....!")
else:
    print('try it next time..........!')
