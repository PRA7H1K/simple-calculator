first = input("First Number: ")
operator = input("Operator: ")

last = input("Last Number: ")

first = float(first)
last = float(last)

# 0 / 0 Error Handler
if operator == "/" and first == 0 and last == 0:
    first = print("Error: You cannot divide 0 and 0")
    first = input("First Number: ")

    operator = input("Operator: ")

    last = input("Last Number: ")

    first = float(first)
    last = float(last)

    if "+" in operator:
        print(first + last)
    elif "-" in operator:
        print(first - last)
    elif "*" in operator:
        print(first * last)
    elif "/" in operator:
        print(first / last)

# 2 / 0 Error Handler
elif operator == "/" and first == 2 and last == 0:
    first = print("Error: You cannot divide 2 and 0")
    first = input("First Number: ")

    operator = input("Operator: ")

    last = input("Last Number: ")

    first = float(first)
    last = float(last)

    if "+" in operator:
        print(first + last)
    elif "-" in operator:
        print(first - last)
    elif "*" in operator:
        print(first * last)
    elif "/" in operator:
        print(first / last)

# Normal
else:
    if "+" in operator:
        print(first + last)
    elif "-" in operator:
        print(first - last)
    elif "*" in operator:
        print(first * last)
    elif "/" in operator:
        print(first / last)
        
    # Invalid Operator Error Handler
    else:
        first = print("Error: Invalid Operator")
        first = input("First Number: ")
        operator = input("Operator: ")

        last = input("Last Number: ")

        first = float(first)
        last = float(last)

        if "+" in operator:
            result = first + last
            print(result)
        elif "-" in operator:
            result = first - last
            print(result)
        elif "*" in operator:
            result = first * last
            print(result)
        elif "/" in operator:
            result = first / last
            print(result)