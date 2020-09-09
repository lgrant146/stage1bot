import asyncio


async def main():
    print("Hello world.")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())