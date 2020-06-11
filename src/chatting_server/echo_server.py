import asyncio


async def echo_server(
    reader: asyncio.StreamReader, writer: asyncio.StreamWriter
) -> None:
    print(f'{writer.get_extra_info("peername")} connected.')
    while True:
        data = await reader.read(100)
        if data.rstrip() == b"":
            break
        writer.write(data)
        await writer.drain()

    print(f'{writer.get_extra_info("peername")} disconnected.')
    writer.close()


async def echo_server_main() -> None:
    server = await asyncio.start_server(echo_server, "127.0.0.1", 8888)

    # mypy complains - server.sockets is `Optional[List[socket]]`, but I don't care
    addr = server.sockets[0].getsockname()  # type: ignore
    print(f"Serving on {addr}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(echo_server_main())
