first = input("Calculator: ")

if "+" in first:
    num1, num2 = first.split("+")
    print(float(num1) + float(num2))

elif "-" in first:
    num1, num2 = first.split("-")
    print(float(num1) - float(num2))

elif "*" in first:
    num1, num2 = first.split("*")
    print(float(num1) * float(num2))
    
elif "/" in first:
    num1, num2 = first.split("/")
    num1a = int(num1)
    num2a = int(num2)
    if num1a == 2 and num2a == 0:
        print("ERROR: You cannot divide 2 and 0")
    elif num1a == 0 and num2a == 0:
        print("ERROR: You cannot divide 0 and 0")
    else:
        print(float(num1) / float(num2))

else:
    print("Error: Please specify an operator")