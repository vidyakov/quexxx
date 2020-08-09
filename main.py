"""
The best sex bot_original in telegram
Module main to start bot_original.
"""

import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor

from conf import TOKEN


logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)


if __name__ == '__main__':
    from handlers import dp
    from handlers.commands import bot_start
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=bot_start
    )
