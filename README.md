# market-data-fetcher

A simple Python tool to automatically fetch and send market data, including:

- USD/JPY exchange rate  
- US stock indices: S&P 500, Dow Jones, NASDAQ  
- Nikkei 225 index  

## Features

- Fetches the latest market data using the `yfinance` library  
- Formats numerical output with two decimal places and comma separators  
- Sends the formatted table to Slack via webhook (requires `SLACK_WEBHOOK_URL` environment variable)  
- Prints a confirmation message in the terminal upon successful Slack delivery  

## Prerequisites

- Python 3.7 or later  
- Internet connection  
- A Slack incoming webhook URL set in `SLACK_WEBHOOK_URL`  

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Murasan/market-data-fetcher.git
   cd market-data-fetcher
   ```

2. **Create a virtual environment** (optional but recommended)  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install --upgrade pip
   pip install yfinance pandas schedule requests
   ```

## Usage

1. **Set your Slack webhook URL**:  
   ```bash
   export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/XXX/YYY/ZZZ"
   ```

2. **Run the script**:  
   ```bash
   python auto-market-watcher.py
   ```

   You should see a confirmation message like:

   ```
   Slackへの送信が完了しました
   ```

## Customization

- Adjust the `period` parameter in `history()` calls to fetch different time ranges.  
- Schedule periodic execution using `cron`, Windows Task Scheduler, or the `schedule` Python library.  
- Extend or modify the Slack payload format in `send_to_slack()` as needed.  

## Author

**Murasan**  
[https://murasan-net.com/](https://murasan-net.com/)
