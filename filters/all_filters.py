
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import ADMINS
from loader import bot
from utils.db_api.db_commands import select_settings


class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        return message.from_user.id in ADMINS


class IsNotSubscribed(BoundFilter):
    async def check(self, message: types.Message):
        settings = await select_settings()
        user = await bot.get_chat_member(settings[5], message.from_user.id)
        if user.status == "left":
            return True


class IsSubscribed(BoundFilter):
    async def check(self, call: types.CallbackQuery):
        settings = await select_settings()
        user = await bot.get_chat_member(settings[5], call.from_user.id)
        if user.status != "left":
            return True
