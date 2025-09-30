from logging import exception

a = int(input("Insert value for A: "))
b = int(input("Insert value for B: "))
action = input("Insert action: ")

result = 0

allowed_actions = ['-', '+', '*', '/']
if action in allowed_actions:
    if action == "-":
        result = a-b
        print(result)
    elif action == "+":
        result = a+b
        print(result)
    elif action == "*":
        result = a*b
        print(result)
    elif action == "/":
        if b == 0:
            exception("devide by zero")
        else:
            result = a/b
            print(result)
else:
    exception("invalid action")
