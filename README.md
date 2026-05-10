# base-copy-trading-bot

> On-chain Copy Trading Bot for Base L2

Automatically mirror trades from top-performing wallets on Base. Monitors Uniswap v3 and Aerodrome swap events in real-time and executes proportional copy trades.

## Features
- 👁️ Real-time wallet monitoring via WebSocket RPC
- 🔄 Proportional trade sizing (% of leader position)
- ⚡ Fast execution via Flashbots Protect RPC
- 🛡️ Slippage protection (configurable max slippage)
- 📊 P&L tracking per copied wallet
- ⏹️ Stop-loss and take-profit automation
- 📱 Telegram notifications

## Setup
```bash
git clone https://github.com/fabt31/base-copy-trading-bot
cd base-copy-trading-bot
pip install -r requirements.txt
cp config.example.yml config.yml
# Edit config.yml with your settings
python main.py
```

## Configuration
```yaml
rpc_ws: wss://base-mainnet.g.alchemy.com/v2/YOUR_KEY
private_key: "0x..."
leaders:
  - address: "0xWalletToFollow"
    allocation: 0.1  # 10% of their trade size
    max_trade_usd: 500
slippage_bps: 100   # 1% max slippage
stop_loss_pct: 10   # stop copying if -10%
```

## Supported DEXes
- Uniswap v3 on Base
- Aerodrome Finance
- BaseSwap

## Disclaimer
Trading bots carry significant financial risk. Use at your own risk.

## License
MIT