import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class BinanceFuturesClient:
    def __init__(self, logger):
        self.logger = logger

        self.client = Client(
            api_key=os.getenv("BINANCE_API_KEY"),
            api_secret=os.getenv("BINANCE_API_SECRET"),
            testnet=True  
        )

        # Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

        # Sync time (avoids Invalid Response issues)
        self.client.TIME_OFFSET = self.client.get_server_time()["serverTime"] - int(
            __import__("time").time() * 1000
        )

    def place_order(self, **kwargs):
        try:
            self.logger.info(f"Placing order: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            self.logger.info(f"Order response: {response}")
            return response
        except Exception as e:
            self.logger.error(f"API error: {str(e)}")
            raise


    def set_leverage(self, symbol, leverage=1):
        self.client.futures_change_leverage(
            symbol=symbol,
            leverage=leverage
        )
        