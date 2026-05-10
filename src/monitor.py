import asyncio
import json
from web3 import AsyncWeb3, WebSocketProvider
from eth_abi import decode

UNISWAP_V3_ROUTER = "0x2626664c2603336E57B271c5C0b26F421741e481"
SWAP_EVENT_SIG = "0xc42079f94a6350d7e6235f29174924f928cc2ac818eb64fed8004e115fbcca67"

async def monitor_wallet(ws_url: str, leader_address: str, callback):
    async with AsyncWeb3(WebSocketProvider(ws_url)) as w3:
        print(f"Monitoring {leader_address}...")
        subscription_id = await w3.eth.subscribe("logs", {
            "address": UNISWAP_V3_ROUTER,
            "topics": [SWAP_EVENT_SIG]
        })
        async for event in w3.socket.process_subscriptions():
            log = event["result"]
            tx_hash = log.get("transactionHash")
            tx = await w3.eth.get_transaction(tx_hash)
            if tx["from"].lower() == leader_address.lower():
                swap_data = parse_swap(log)
                print(f"Leader swap detected: {swap_data}")
                await callback(swap_data)

def parse_swap(log: dict) -> dict:
    data = bytes.fromhex(log["data"][2:])
    amount0, amount1, sqrtPriceX96, liquidity, tick = decode(
        ["int256", "int256", "uint160", "uint128", "int24"], data
    )
    return {
        "amount0": amount0,
        "amount1": amount1,
        "pool": log["address"],
        "tx": log.get("transactionHash")
    }

async def main():
    async def on_swap(data):
        print(f"Copying trade: {data}")

    await monitor_wallet(
        "wss://base-mainnet.g.alchemy.com/v2/demo",
        "0x0000000000000000000000000000000000000001",
        on_swap
    )

if __name__ == "__main__":
    asyncio.run(main())