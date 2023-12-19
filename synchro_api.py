import time
import requests

SYMBOLS = ("USD", "EUR", "PLN", "NOK", "CZK")
BASES = ("USD", "EUR", "PLN", "NOK", "CZK")


# response = requests.get("https://api.vatcomply.com/rates?base=USD")
# print(response.json())


def fetch_rates(base):
    response = requests.get(f'https://api.vatcomply.com/rates?base={base}')
    response.raise_for_status()
    rates = response.json()['rates']

    rates[base] = 1.0

    rates_line = ", ".join([f"{rates[symbol]:7.03} {symbol}" for symbol in SYMBOLS])
    print(f"1 {base} = {rates_line}")


def main():
    for base in BASES:
        fetch_rates(base)


if __name__ == '__main__':
    started = time.time()
    main()
    elapsed = time.time() - started
    print()
    print("Upłynęło: {:.2f}s".format(elapsed))
