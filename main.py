from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from order import Order
app = FastAPI()

clients = []
orders = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
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
    except WebSocketDisconnect:
        clients.remove(websocket)


@app.post("/order")
async def create_order(order: Order):
    orders.append(order)

    for client in clients:
        await client.send_json(order.model_dump())

    return {"message": "Order created"}