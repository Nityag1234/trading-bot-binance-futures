import argparse
from html import parser
from bot.client import BinanceFuturesClient
from bot.orders import execute_order
from bot.logging_config import setup_logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    # parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument(
    "--type",
    required=True,
    choices=["MARKET", "LIMIT", "STOP_MARKET"],
    help="Order type: MARKET, LIMIT, STOP_MARKET")
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, help="Limit price (LIMIT / STOP_MARKET)")
    parser.add_argument("--stop-price", type=float, help="Stop price (STOP_MARKET only)")
    parser.add_argument("--reduce-only", action="store_true", help="Reduce-only order")


    args = parser.parse_args()

    logger = setup_logger()
    client = BinanceFuturesClient(logger)

    try:
        print("\nPlacing order...")
        execute_order(client, args, logger)
        print("✅ Order placed successfully")
    except Exception as e:
        print(f"❌ Failed to place order: {str(e)}")

if __name__ == "__main__":
    main()
