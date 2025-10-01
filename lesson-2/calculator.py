import operator

def calculate(a: float, b: float, action: str) -> float:
    actions = {
        "-": operator.sub,
        "+": operator.add,
        "*": operator.mul,
        "/": operator.truediv,
        "**": operator.pow,
        "%": operator.mod,
    }
    if action not in actions:
        raise ValueError(f"Invalid action. Allowed: {', '.join(actions.keys())}")
    if action == "/" and b == 0:
        raise ZeroDivisionError("divide by zero")
    return actions[action](a, b)

def get_number(prompt: str):
    while True:
        value = input(prompt)
        if value == "exit":
            print("Goodbye")
            exit()
        try:
            return float(value)
        except ValueError:
            print("Please enter a number.")


if __name__ == "__main__":
    while True:
        a = get_number("Insert value for A: ")
        b = get_number("Insert value for B: ")
        action = input("Insert action: ")
        if action == "exit":
            print("Goodbye")
            break

        try:
            result = calculate(a, b, action)
            print("Result: ", result)
        except Exception as e:
            print("Error: ", e)