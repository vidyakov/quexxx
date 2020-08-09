"""
Game's handlers and functions
"""

from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from keyboards.game import get_buttons, share_button
from states.game import Game
import data.text as tx
from data import QUESTIONS, ANSWERS, add_sticker, is_sticker_at_user
from main import dp, bot
from conf import STICKERS
from .commands import command_start


@dp.message_handler(state=Game.GAME)
async def make_step(msg: types.Message, state: FSMContext):
    answer = ANSWERS.get(msg.text)
    if answer:  # Is answer valid?
        if answer['question']:  # Is answer last?
            next_question = QUESTIONS[answer['question']]
            for question in next_question['text']:
                if question.get('question'):  # Is it direct speech or bot_original message?
                    buttons = get_buttons(next_question['answer1'], next_question['answer2'])
                    await msg.answer(
                        question['question'],
                        reply_markup=buttons
                    )
                else:
                    chat_id = question['direct speech']['account']
                    message_id = question['direct speech']['message']
                    await bot.forward_message(
                        msg.from_user.id,
                        chat_id,
                        message_id
                    )
        else:
            await msg.answer(
                answer['farewell text'],
                reply_markup=ReplyKeyboardRemove()
            )
            sticker_id = STICKERS[answer['achievement']]
            await bot.send_sticker(msg.from_user.id, sticker_id)

            if not is_sticker_at_user(msg.from_user.id, sticker_id):
                add_sticker(msg.from_user.id, sticker_id)
                await msg.answer(
                    tx.new_sticker,
                    reply_markup=share_button
                )
            await state.finish()
    else:
        if msg.text == '/start':
            await state.finish()
            await command_start(msg)
        else:
            await msg.reply(tx.please_touch_button)
