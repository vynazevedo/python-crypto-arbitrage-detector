import requests

def get_available_pairs():
    url = "https://api.kraken.com/0/public/AssetPairs"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Erro ao acessar a API da Kraken")
    
    data = response.json()
    if not data['error']:
        pairs = list(data['result'].keys())
        return pairs
    else:
        raise Exception(f"Erro na API da Kraken: {data['error']}")

def get_available_pairsf():
    url = "https://api.kraken.com/0/public/AssetPairs"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Erro ao acessar a API da Kraken")
    
    data = response.json()
    if not data['error']:
        raw_pairs = data['result'].keys()
        formatted_pairs = format_pairs(raw_pairs, data['result'])
        return formatted_pairs
    else:
        raise Exception(f"Erro na API da Kraken: {data['error']}")

def format_pairs(raw_pairs, data_result):
    formatted_pairs = []
    for pair in raw_pairs:
        if "wsname" in data_result[pair]:
            formatted_pair = data_result[pair]["wsname"]
            formatted_pairs.append(formatted_pair)
    return formatted_pairs

def generate_eur_arbitrage_routes(pairs):
    eur_pairs = [pair for pair in pairs if 'EUR' in pair]
    unique_cryptos = set()

    for pair in eur_pairs:
        base, quote = pair[:3], pair[3:]
        if base != 'EUR':
            unique_cryptos.add(base)
        if quote != 'EUR':
            unique_cryptos.add(quote)

    arbitrage_routes = []
    for first_crypto in unique_cryptos:
        for second_crypto in unique_cryptos:
            if first_crypto != second_crypto:
                route = ['EUR', first_crypto, second_crypto, 'EUR']
                arbitrage_routes.append(route)

    return arbitrage_routes

def filter_pairs_by_currency(pairs, currency):
    filtered_pairs = [pair for pair in pairs if currency in pair]
    return filtered_pairs
