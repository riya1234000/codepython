                         # simple calculator with the help of functions...!

def calculator(a,b):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self):
        return f' the sum of the two numbers are; {self.a + self.b} '
    
    def __sub__(self):
        return f' the subtraction of the numbers are: {self.a - self.b}'
    def __mul__(self):
        return f' the multiplication of the number is: {self.a * self.b}'
    def __div__(self):
        return f' the division of the numbers are: {self.a / self.b}'
    
a= int(input('enter the number of a :  '))
b= int(input(" enter the number of b is: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

    
        # create simple calculator with the help of try and exception or match case...!
try:
    a= int(input('enter the number of a:  '))
    b= int(input('enter the number of b: '))
    while True:
       print("enter the operation u wanna use:\n press + for addition\n, press - for subtraction \n, press * for multiplication \n , press / for division")
       o= input('enter the operation :  ')
  
       match o:
        case "+":
            print(f' the result of the addition is : {a+b}')
        case "-":
            print(f' the result of the subtraction is: {a-b}')
        case "*":
            print(f' the result of the multiplication is : {a*b}')
        case "/":
            print(f' the result of the division is : {a/b}')
        case _:
            print(f' something went wrong.........!')

except Exception as e:
    print('enter the valid number of a and b:  ')
     

                                 # run this function with the exceptions handling , match- case and con for running yes or no.....!
try:
    a= int(input('enter the number of a:  '))
    b= int(input('enter the number of b: '))
    while True:
      print("enter the operation u wanna use:\n press + for addition\n, press - for subtraction \n, press * for multiplication \n , press / for division")
      o= input('enter the operation :  ')
   
      match o:
        case "+":
            print(f' the result of the addition is : {a+b}')
        case "-":
            print(f' the result of the subtraction is: {a-b}')
        case "*":
            print(f' the result of the multiplication is : {a*b}')
        case "/":
            print(f' the result of the division is : {a/b}')
       
      con= input('uh want to exit or not (yes/ no)')
      if  con=="yes":
          print("thank you for using the calculator")    
      else:
          print('thanku so much for exting.!')
          break  
except Exception as e:
    print("enter the valid number of a and b:  ") 
except ZeroDivisionError as e:
    print('the number valid :  a and b')
except ValueError as v:
    print('the number should be integer:  ')
