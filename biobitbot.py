import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.markdown import text
from dotenv import load_dotenv
import os
import keyboards as kb
import handlers

load_dotenv()
TelegramToken = os.getenv("TOKEN")

# Turn on logging so you don't miss important messages
logging.basicConfig(filename='bot.log', level=logging.INFO)

# Bot object
bot = Bot(token=TelegramToken)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))(lambda callback_query:
                                                                         handlers.
                                                                         process_callback_button1(bot, callback_query))

dp.message_handler(commands=['start'])(handlers.handler_start)

dp.message_handler(commands=['remove'])(handlers.handler_remove)

dp.message_handler(commands=['help'])(handlers.handler_help)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())
