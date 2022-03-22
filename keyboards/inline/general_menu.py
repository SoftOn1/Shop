from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import ADMINS


# ======================== MAIN MENU MARKUP ========================
def main_menu(user_id):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🛒 Каталог", callback_data="catalog"),
                InlineKeyboardButton(text="💳 Пополнить ", callback_data="deposit")
            ],
            [
                InlineKeyboardButton(text="📒 История покупок", callback_data="order_history"),
                InlineKeyboardButton(text="👥 Рефералы", callback_data="affiliate")
            ],
            [
                InlineKeyboardButton("ℹ️ Информация", callback_data="info"),
                InlineKeyboardButton(text="🆘 Помощь", callback_data="sos")
            ],
            [
                InlineKeyboardButton(text="👑 Админ панель", callback_data="back_admin")
            ] if user_id in ADMINS else []
        ]
    )
    return keyboard


sos_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📊 Накрутка ", callback_data="sos:smm")
        ],
        [
            InlineKeyboardButton(text="💳 Оплата ", callback_data="sos:payment")
        ],
        [
            InlineKeyboardButton(text="📦 Товар ", callback_data="sos:product")
        ],
        [
            InlineKeyboardButton(text="❓Другой вопрос ", callback_data="sos:other")
        ],
        [
            InlineKeyboardButton(text="⬅️Назад", callback_data="back_to_main_menu")
        ]
    ]
)

# ======================== BACK TO MAIN MENU BUTTON ========================
back_to_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️Назад", callback_data="back_to_main_menu")
        ]
    ]
)


async def invite_menu(invite_link):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="↗️ Подписаться ↗️", url=invite_link)
            ],
            [
                InlineKeyboardButton(text="✅ Подписался ✅", callback_data="subscribed")
            ]
        ]
    )
    return keyboard


# ======================== ORDER HISTORY MENU ========================
order_history_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📦 Товары", callback_data="history:product"),
            InlineKeyboardButton(text="📊 Накрутка ", callback_data="history:smm")
        ],
        [
            InlineKeyboardButton(text="⬅️Назад", callback_data="back_to_main_menu")
        ]
    ]
)
