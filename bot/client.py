from binance.client import Client


class BinanceClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(
            api_key,
            api_secret,
            testnet=True
        )

        # Futures testnet base URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"


    def place_market_order(self, symbol, side, quantity):
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )


    def place_limit_order(self, symbol, side, quantity, price):
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
