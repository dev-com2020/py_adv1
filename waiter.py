import asyncio
import time
import random


async def kelner(name):
    for _ in range(4):
        time_to_sleep = random.randint(1, 3) / 4
        # time.sleep(time_to_sleep)
        await asyncio.sleep(time_to_sleep)
        print(f"{name} oczekiwał {time_to_sleep} s")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.gather(kelner("pierwszy"), kelner("drugi"))
    )
    loop.close()
