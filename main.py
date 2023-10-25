num1 = None
znak = None
num2 = None
while True:
    try:
        if num1 == None:
            num1 = int(input("Enter first number: "))
        if znak == None:
            znak = input("Enter sign: ")
        if num2 == None:
            num2 = int(input("Enter second number: "))
        if znak == '+':
            print(num1 + num2)
            num1, num2, znak = None, None, None
        elif znak == '-':
            print(num1 - num2)
            num1, num2, znak = None, None, None
        elif znak == "*":
            print(num1 * num2)
            num1, num2, znak = None, None, None
        elif znak == "/":
            print(num1 / num2)
            num1, num2, znak = None, None, None    
        else:
            print("The sign was specified incorrectly") 
            znak == None 
    except ValueError:
        print("We can enter only numbers")
    except ZeroDivisionError:
        print("You can't divide by zero")
        num2 = None
