import asyncio


async def echo_client() -> None:
    reader, writer = await asyncio.open_connection("127.0.0.1", 8888)

    while True:
        msg = input("Type your message: ")
        if msg.strip() == "":
            print("No message, closing connection.")
            break
        writer.write(msg.encode())
        await writer.drain()
        data = await reader.read(100)
        print(f"Received: {data.decode()!r}")

    writer.close()


if __name__ == "__main__":
    asyncio.run(echo_client())
