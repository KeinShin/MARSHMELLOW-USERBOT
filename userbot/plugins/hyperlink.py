# For UniBorg
# By Priyam Kalra
# Syntax (.hl <link>)

from telethon import events
from userbot.utils import mellow_cmd
import asyncio
from telethon.tl import functions, types

@mellow.on(mellow_cmd(pattern="hl ?(.*)"))
async def _(event):
        if event.fwd_from:
            return
        input = event.pattern_match.group(1)
        await event.edit("[ㅤㅤㅤㅤㅤㅤㅤ](" + input + ")")
