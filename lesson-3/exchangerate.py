import requests
from datetime import datetime

def parse_input(client_request: str):
    parts = client_request.strip().split()
    if len(parts) != 4 or parts[2].lower() != "to":
        raise ValueError("Input must be in format: '<amount> <from> to <to>'")
    return float(parts[0]), parts[1].upper(), parts[3].upper()


def convert(amount: float, from_currency: str, to_currency: str, rates):
    if from_currency not in rates:
        raise ValueError(f"Currency {from_currency} not supported")

    if to_currency not in rates:
        raise ValueError(f"Currency {to_currency} not supported")
    amount_in_usd = amount / rates[from_currency]
    result = amount_in_usd * rates[to_currency]
    return result


amount, from_currency, to_currency = parse_input(input("Enter request (e.g. '100 USD to EUR', or 'exit'): "))

url = "https://open.er-api.com/v6/latest/USD"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    rates = data["rates"]

    converted = convert(amount, from_currency, to_currency, rates)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("currency_log.txt", "a") as f:
        f.write(f"{now} {amount} {from_currency} -> {converted:.2f} {to_currency}\n")
else:
    print("Error: ", response.status_code)

