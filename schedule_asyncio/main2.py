import schedule
import asyncio
import time
async def func():
    print(time.asctime(time.localtime(time.time())))
    await asyncio.sleep(2)
async def func2():
    # schedule.every(1).seconds.do(func)
    # while True:
    #     await schedule.run_pending()
    #     await asyncio.sleep(1)
    sche = schedule.Scheduler()
    sche.every(1).seconds.do(func)
    sche.every(1).seconds.do(func)
    while True:
        # await sche.run_pending()
        await sche.run_pending_parallel()
        await asyncio.sleep(1)
if __name__ == "__main__":
    asyncio.run(func2())