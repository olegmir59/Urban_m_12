#  2024/01/15 00:00|Домашнее задание по теме "Асинхронность на практике"
# Цель: приобрести навык использования асинхронного запуска функций на практике
#
# Задача "Асинхронные силачи":
import asyncio


async def start_strongman(name, power):
    for ball_num in range(0, 6):
        if ball_num == 0:
            print(f"Силач {name} начал соревнования.")
        else:
            await asyncio.sleep(1/power)
            print(f'Силач {name} поднял {ball_num} шар')
    print(f"Силач {name} закончил соревнования.")


async def start_tournament():
    task1 = asyncio.create_task(start_strongman("Pasha", 3))
    task2 = asyncio.create_task(start_strongman("Denis", 4))
    task3 = asyncio.create_task(start_strongman("Apollon", 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())