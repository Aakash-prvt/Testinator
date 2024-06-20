from pyrogram import filters
import asyncio
from pyrogram.types import Message
from pyrogram.errors import MessageIdInvalid, ChatAdminRequired, EmoticonInvalid, ReactionInvalid 
from random import choice
from bot import TelegramBot
from bot.config import Telegram

@TelegramBot.on_message(filters.all)
async def send_reaction(_, msg: Message):
    try:
        await asyncio.sleep(Telegram.DELAY)
        await msg.react(choice(Telegram.EMOJIS))
    except (
        MessageIdInvalid,
        EmoticonInvalid,
        ChatAdminRequired,
        ReactionInvalid
    ):
        pass
