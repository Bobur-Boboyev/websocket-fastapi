import asyncio
import websockets
import json


async def main():
    async with websockets.connect("ws://127.0.0.1:8000/ws") as ws:
        print("Connected")

        while True:
            message = await ws.recv()
            order = json.loads(message)

            print("\n=== NEW ORDER ===")
            print(f"Food : {order['food']}")
            print(f"Count: {order['count']}")


asyncio.run(main())