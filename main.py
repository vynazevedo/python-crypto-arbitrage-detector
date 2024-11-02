import kraken_arbitrage_helpers as kraken_helpers
import websocket
import json
import threading

class KrakenArbitrageBotV2:
    def __init__(self):
        self.ws_url = "wss://ws.kraken.com"
        self.prices = {}
        self.pairs = kraken_helpers.get_available_pairs()
        self.pairs_formatted = kraken_helpers.get_available_pairsf()
        self.arbitrage_routes = kraken_helpers.generate_eur_arbitrage_routes(self.pairs)

    def on_message(self, ws, message):
        data = json.loads(message)
        if len(data) > 2 and data[2] == "ticker":
            pair = data[3]
            price_info = data[1]
            last_trade_price = float(price_info['c'][0])
            self.prices[pair] = last_trade_price
            self.check_arbitrage_opportunity()

    def on_error(self, ws, error):
        print(f"Error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        print("Conexão WebSocket fechada")

    def on_open(self, ws):
        def run():
            # print(kraken_helpers.filter_pairs_by_currency(self.pairs_formatted, 'EUR'))
            subscribe_message = {
                "event": "subscribe",
                "pair": ['XBT/EUR', 'ETH/EUR', 'XRP/USD', 'LTC/EUR', 'ETH/XBT'],
                "subscription": {"name": "ticker"}
            }
            ws.send(json.dumps(subscribe_message))
        threading.Thread(target=run).start()

    def check_arbitrage_opportunity(self):
        for route in self.arbitrage_routes:
            if self.are_prices_available(route):
                profit = self.calculate_arbitrage_profit(route)
                if profit > 0:
                    print(f"Oportunidade de Arbitragem Detectada na Rota {route}: Lucro potencial de {profit:.2f} EUR") 
    def are_prices_available(self, route):
        for i in range(len(route) - 1):
            pair = f"{route[i]}{route[i + 1]}"
            if pair not in self.prices or self.prices[pair] is None:
                return False
        return True

    def calculate_arbitrage_profit(self, route):
        amount = 1000
        for i in range(len(route) - 1):
            pair = f"{route[i]}{route[i + 1]}"
            price = self.prices[pair]

        return amount - 1000
   

    def start(self):
        ws = websocket.WebSocketApp(self.ws_url,
                                    on_open=self.on_open,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        ws.run_forever()

bot = KrakenArbitrageBotV2()
bot.start()