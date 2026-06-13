import requests

def get_rates(base_currency="USD"):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    response = requests.get(url, timeout=5)
    data = response.json()
    return data.get("rates", {})


def convert(amount, from_currency, to_currency):
    amount = float(amount)

    if from_currency == to_currency:
        return amount

    rates = get_rates(from_currency)

    if to_currency not in rates:
        return amount  # fallback (safe)

    return amount * rates[to_currency]