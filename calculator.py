#Command Line supportive simple calculator app 
#Uses functions, takes user input, loops until user chooses to exit.
#Operation like:- +,-, *, /

#Addition
def add(a,b):
    return a+b

#Subtraction
def subtract(a,b):
    return a-b

#Multiplication
def multiply(a,b):
    return a*b

#Division
def divide(a,b):
    if b!=0:
        return a/b
    
#loop through functions
while True:
    print("----------Simple Calculator App--------")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    choice = input("Enter Your choice(1-5):")
    if choice=='5':
        print("Exiting the APP📴")
        break
    if choice in ['1','2','3','4']:
        a = float(input("Enter First Number  :"))
        b = float(input("Enter Second Number  :"))
        if choice=='1':
            print("Result:", add(a,b))
        elif choice=='2':
            print("Result:", subtract(a,b))
        elif choice=='3':
            print("Result:",multiply(a,b))
        elif choice=='4':
            print("Result:", divide(a,b))
    else:
        print("Invalid Choice! Try again.😐")
    
    