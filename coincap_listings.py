import requests

listings_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?convert=INR'

request = requests.get(url=listings_url, headers={'X-CMC_PRO_API_KEY': 'Your_API_Key'})
result = request.json()
data = result['data']

for currency in data:
    rank = currency['id']
    name = currency['name']
    symbol = currency['symbol']
    print(str(rank) + ': ' + name + ' (' + symbol + ')')
