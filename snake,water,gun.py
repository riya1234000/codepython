import random
"""
1 for snake,
-1 for water,
0 for gun

"""
computer= random.choice([1,-1,0])
youstr= input("enter the choice of the user: ")
yourDict= {"s":1, "w":-1, "g":0}
reverseDict= {1:"snake", -1:"water",0 : "gun" }
you= yourDict[youstr]
print(f"your choice: {reverseDict[you]} \n computer choice: {reverseDict[computer]}")

if computer==you:
    print("it's a tie baby......!")
elif(computer==1 and you==0):
    print('you win it baby.....!')
elif(computer==-1 and you==0):
    print('you loss it baby..........!')
elif(computer==0 and you==-1):
    print("you win baby.....!")
elif(computer==1 and you==-1):
    print("you loss it baby....!")
elif(computer==0 and you==1):
    print('you loss it baby......!')
elif(computer==-1 and you==1):
    print('you win it baby........!')
else:
    print('something went wrong here \n try again next time baby.......!')
