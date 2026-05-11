import asyncio
import pytest
from src.pnl import Trade, PnLTracker

def test_pnl_positive():
    trade = Trade(token="0xABC", buy_price=1.0, sell_price=2.0, amount_usd=100)
    assert trade.pnl == 100.0

def test_pnl_loss():
    trade = Trade(token="0xABC", buy_price=1.0, sell_price=0.5, amount_usd=100)
    assert trade.pnl == -50.0

def test_win_rate():
    tracker = PnLTracker()
    tracker.add_trade(Trade("0x1", 1.0, 2.0, 100))
    tracker.add_trade(Trade("0x2", 1.0, 0.5, 100))
    assert tracker.win_rate() == 50.0
