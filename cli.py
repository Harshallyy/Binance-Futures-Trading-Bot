import argparse
import os

from bot.client import BinanceClient
from bot.orders import place_order
from bot.logging_config import setup_logger


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if api_key is None or api_secret is None:
        print("Set BINANCE_API_KEY and BINANCE_API_SECRET first")
        return

    logger = setup_logger()

    client = BinanceClient(api_key, api_secret)

    place_order(
        client,
        logger,
        args.symbol.upper(),
        args.side,
        args.type,
        args.qty,
        args.price,
    )


if __name__ == "__main__":
    main()
