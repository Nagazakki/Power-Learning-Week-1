number1 = int(input(("Enter First Number: ")))
number2 = int(input(("Enter Second Number: ")))
symbol = input("Enter valid symbol : + , - , * , / .")


def sum(number1, number2):
    return number1+number2

def subtraction(number1, number2):
    return number1-number2

def multiplication(number1, number2):
    return number1*number2

def division(number1, number2):
    try: 
        return number1/number2
    except ZeroDivisionError:
        return "You can't divide by zero"

    
operations = {"+": sum, "-": subtraction, "*": multiplication, "/": division}

if symbol == "+":
    print(number1, "+", number2, "=", operations[symbol](number1, number2))
    print(sum(int(number1), int(number2)))
if symbol == "-":
    print(number1, "-", number2, "=", operations[symbol](number1, number2))
    print(subtraction(int(number1), int(number2)))
if symbol == "*":
    print(number1, "*", number2, "=", operations[symbol](number1, number2))
    print(multiplication(int(number1), int(number2)))
if symbol == "/":
    print(number1, "/", number2, "=", operations[symbol](number1, number2))
    print(division(int(number1), int(number2)))
else: 
    if number2 == 0:
        print("You can't divide by zero")

    
print("Thank you for using our calculator")