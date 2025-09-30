import operator

def calculate(a: int, b: int, action: str) -> float:
    actions = {
        "-": operator.sub,
        "+": operator.add,
        "*": operator.mul,
        "/": operator.truediv,
    }
    if action not in actions:
        raise ValueError("invalid action")
    if action == "/" and b == 0:
        raise ZeroDivisionError("divide by zero")
    return actions[action](a, b)


a = float(input("Insert value for A: "))
b = float(input("Insert value for B: "))
action = input("Insert action: ")

try:
    result = calculate(a, b, action)
    print("Result: ", result)
except Exception as e:
    print("Error: ", e)