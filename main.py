from fastapi import FastAPI, WebSocket

app = FastAPI()

clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket):
    await websocket.accept()
    clients.append(websocket)
    print("WebSocket connection accepted")

    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received: {data}")

            for client in clients:
                await client.send_text(f"Echo: {data}")
                print(f"Sent to client: {data}")
    except Exception as e:
        await websocket.close()