import math
def sum(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2
def sin(num):
    return math.sin(num)
def cos(num):
    return math.cos(num)
def tan(num):
    return math.tan(num)
solution = 0
operation = str(input())
try:
    if operation == "sin" or operation == "cos" or operation == "tan":
        num = int(input())
    else:
        num1 = int(input())
        num2 = int(input())
except ValueError:
    print("wrong number")
match operation:
    case "+":
        solution += sum(num1, num2)    
    case "-":
        solution += sub(num1, num2)   
    case "*":
        solution += mul(num1, num2) 
    case "/":
        solution += div(num1, num2) 
    case "sin":
        solution += sin(num)
    case "cos":
        solution += cos(num)
    case "tan":
        solution += tan(num)
    case _:
        print("wrong operation")
print(solution)