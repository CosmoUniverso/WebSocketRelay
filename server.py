import asyncio
import websockets

clients = set()

async def handler(websocket):
    clients.add(websocket)
    print(f"🟢 Nuovo client. Totale: {len(clients)}")
    try:
        async for message in websocket:
            print(f"📨 Ricevuto: {message}")
            for client in clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("🔌 Connessione chiusa")
    finally:
        clients.remove(websocket)
        print(f"🔴 Client disconnesso. Totale: {len(clients)}")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 10000):
        print("🚀 Server WebSocket avviato sulla porta 10000")
        await asyncio.Future()  # resta in ascolto

if __name__ == "__main__":
    asyncio.run(main())
