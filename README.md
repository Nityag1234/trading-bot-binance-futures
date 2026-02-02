# Binance Futures Testnet Trading Bot

## Overview
This project is a simple command-line trading bot written in Python for interacting with the Binance Futures Testnet (USDT-M).  
It supports placing basic futures orders while focusing on clean structure, validation, logging, and error handling.

The goal of this project is to demonstrate correct API usage, clear separation of responsibilities, and a maintainable codebase.

---

## Features
- Place **MARKET** and **LIMIT** orders on Binance Futures Testnet
- Supports **BUY** and **SELL** sides
- Command-line interface using argparse
- Input validation before sending requests
- Logging of API requests, responses, and errors
- Modular project structure (client, validation, order logic)

> Note: Stop-based orders were explored during development but are not relied upon due to Futures Testnet limitations.

---


## Setup Instructions

### 1. Create Binance Futures Testnet Account
- Visit: https://testnet.binancefuture.com
- Generate API Key and Secret

### 2. Clone Repository
```bash
git clone https://github.com/Nityag1234/trading-bot-binance-futures.git
cd trading-bot-binance-futures

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


### 3. Create .env file 
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret

**Usage Examples**
Market Order
python cli.py \
--symbol BTCUSDT \
--side BUY \
--type MARKET \
--quantity 0.002

Limit Order
python cli.py \
--symbol BTCUSDT \
--side SELL \
--type LIMIT \
--quantity 0.002 \
--price 60000


**LOGGING**
logs/trading_bot.log
