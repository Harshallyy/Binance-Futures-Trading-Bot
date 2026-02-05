# Binance Futures Testnet Trading Bot

Simple CLI based trading bot to place MARKET and LIMIT orders on Binance Futures Testnet.

## Setup

1. Create virtual env
python -m venv venv

2. Activate
venv\Scripts\activate   (Windows)

3. Install deps
pip install -r requirements.txt

4. Set API keys
set BINANCE_API_KEY=your_key
set BINANCE_API_SECRET=your_secret

## Run

Market order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001

Limit order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 60000

## Logs
bot.log file contains all requests and responses.
