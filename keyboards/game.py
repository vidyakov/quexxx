"""Keyboards for game"""

from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from conf import DONUT_URL
from data.text import for_donut, share_please, inline_query


def get_buttons(answer1, answer2):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=answer1)
            ],
            [
                KeyboardButton(text=answer2)
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )


share_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(share_please, switch_inline_query=inline_query)
        ],
        [
            InlineKeyboardButton(text=for_donut, url=DONUT_URL)
        ]
    ],
    row_width=2
)
