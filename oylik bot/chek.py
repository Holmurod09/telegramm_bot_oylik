from typing import Any
from aiogram.filters import Filter
from config import kanal_1_id
from aiogram import Bot
from aiogram.types import Message


class chek_chanal(Filter):
    async def __call__(self,m:Message, bot:Bot):
        user_sta = await bot.get_chat_member(kanal_1_id, m.from_user.id)
        if user_sta.status in ["creator", "administrator", "member"]:
            return False
        return True
    