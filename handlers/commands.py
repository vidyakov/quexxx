"""
Handlers for bot_original commands and to start and stop bot_original
"""
from aiogram import types

from states.game import Game
from keyboards.game import get_buttons
from conf import ADMIN, FIRST_QUESTION
from main import bot, dp
from data import text as tx
from data import get_user_stickers, save_user


async def bot_start(dp):
    await bot.send_message(
        ADMIN,
        tx.for_admin_msg
    )


@dp.message_handler(commands=['start'])
async def command_start(msg: types.Message):
    await msg.answer(tx.start_msg.format(msg.from_user.first_name))
    save_user(
        msg.from_user.id,
        msg.from_user.first_name,
        msg.from_user.username
    )


@dp.message_handler(commands=['help'])
async def command_help(msg: types.Message):
    await msg.answer(tx.help_msg)


@dp.message_handler(commands=['new_game'], state=None)
async def new_game(msg: types.Message):
    await msg.answer(tx.start_game)

    bot_msg = FIRST_QUESTION['text'][0]['question']
    girl_msg = FIRST_QUESTION['text'][1]['direct speech']
    answer1 = FIRST_QUESTION['answer1']
    answer2 = FIRST_QUESTION['answer2']
    await msg.answer(
        bot_msg,
        reply_markup=get_buttons(answer1, answer2)
    )
    await bot.forward_message(
        msg.from_user.id,
        girl_msg['account'],
        girl_msg['message']
    )
    await Game.GAME.set()


@dp.message_handler(commands=['my_achievements'])
async def show_user_stickers(msg: types.Message):
    user_stickers = get_user_stickers(msg.from_user.id)
    # дописать отпраку стикеров
    for sticker in user_stickers:
        await bot.send_sticker(msg.from_user.id, sticker)


@dp.message_handler(content_types=['text'])
async def command_help(msg: types.Message):
    await msg.answer(tx.help_msg)
