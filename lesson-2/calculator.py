import json
import operator

with open("config.json", "r") as f:
    config = json.load(f)

ALLOWED_ACTIONS = config["allowed_actions"]
RESULT_FILE = config["result_file"]

def calculate(a: float, b: float, action: str) -> float:
    actions = {
        "-": operator.sub,
        "+": operator.add,
        "*": operator.mul,
        "/": operator.truediv,
        "**": operator.pow,
        "%": operator.mod,
    }
    if action not in ALLOWED_ACTIONS:
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
            print("Result:", result)
            with open(RESULT_FILE, "a") as result_file:
                result_file.write(f"{a}{action}{b}={result}\n")
        except Exception as e:
            print("Error: ", e)