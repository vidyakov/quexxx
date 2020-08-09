"""Handlers for admin panel"""


from aiogram import types
from aiogram.dispatcher import FSMContext

from main import dp, bot
from conf import ADMIN
from states.admin import Mailing
from data import get_all_users, count_users
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Рассылка", callback_data="mailing")
        ]
    ]
)

BLOCKED_USERS = 0


def auth(func):
    async def inner(msg: types.Message):
        if msg.from_user.id == ADMIN:
            return await func(msg)
    return inner


@dp.message_handler(commands=['admin'])
@auth
async def admin_panel(msg: types.Message):
    await msg.answer(
        f'Количество пользователей: <b>{count_users()}</b>\nКоличество плохих пользователей: <b>{BLOCKED_USERS}</b>',
        reply_markup=admin_menu
    )


@dp.callback_query_handler(text='mailing')
async def mailing(query: types.CallbackQuery):
    await query.answer('Введите текст для рассылки')
    await Mailing.first()


@dp.message_handler(state=Mailing.MAILING)
async def make_mailing(msg: types.Message, state: FSMContext):
    global BLOCKED_USERS
    BLOCKED_USERS = 0
    users = get_all_users()
    for user in users:
        try:
            if user != str(ADMIN):
                await bot.send_message(user, msg.text)
        except Exception as e:
            print(e)
            BLOCKED_USERS += 1
    await msg.answer('Сообщение успешно отправлено')
    await state.finish()
