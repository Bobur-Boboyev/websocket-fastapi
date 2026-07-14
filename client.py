import asyncio
from websockets import connect

async def main():
    uri = "ws://localhost:8000/ws"
    async with connect(uri) as client:
        await client.send("Hello, WebSocket!")

        response = await client.recv()
        print(f"Received: {response}")


asyncio.run(main())