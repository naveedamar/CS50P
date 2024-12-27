import requests, sys

try:

    number_of_coin = float(sys.argv[1])
    bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = bitcoin.json()
    rate = response["bpi"]["USD"]["rate_float"]
    total_value = number_of_coin * rate
    print(f"${total_value:,.4f}")

except (requests.RequestException, ValueError, KeyError) as e:
    print("Missing command-line argument")
    sys.exit(1)
