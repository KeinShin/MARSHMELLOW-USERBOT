''' Whatever Plugin by Noobs of Telegram i.e. @pureindialover '''

from telethon import events
import asyncio
import os
import sys
from uni@mellow.util import mellow_cmd

@mellow.on(mellow_cmd(pattern=r"lmoon"))
async def test(event):
    if event.fwd_from:
        return 
    await event.edit("🌕🌕🌕🌕🌕🌕🌕🌕\n🌕🌕🌖🌔🌖🌔🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌖🌓🌗🌔🌕🌕\n🌕🌕🌗🌑🌑🌓🌕🌕\n🌕🌕🌗👀🌑🌓🌕🌕\n🌕🌕🌘👄🌑🌓🌕🌕\n🌕🌕🌗🌑🌑🌒🌕🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌕🌘🌑🌑🌑🌑🌒🌕\n🌖🌑🌑🌑🌑🌑🌑🌔\n🌕🤜🏻🌑🌑🌑🌑🤛🏻🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌘🌑🌑🌑🌑🌑🌑🌒\n🌕🌕🌕🌕🌕🌕🌕🌕")

@mellow.on(mellow_cmd(pattern=r"city"))
async def test(event):
    if event.fwd_from:
        return 
    await event.edit("""☁☁🌞      ☁           ☁
       ☁  ✈         ☁    🚁    ☁    ☁        ☁          ☁     ☁   ☁

🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/  🚘 l  🏃 \🌴 👬                       👬  🌴/            l  🚔    \🌲
      🌲/   🚖     l               \
   🌳/🚶           |   🚍         \ 🌴🚴🚴
🌴/                    |                     \🌲""")


@mellow.on(mellow_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("🌺✨✨🌺✨🌺🌺🌺\n🌺✨✨🌺✨✨🌺✨\n🌺🌺🌺🌺✨✨🌺✨\n🌺✨✨🌺✨✨🌺✨\n🌺✨✨🌺✨🌺🌺🌺\n☁☁☁☁☁☁☁☁")

@mellow.on(mellow_cmd(pattern=r"cheer"))
async def cheer(event):
    if event.fwd_from:
        return
    await event.edit("💐💐😉😊💐💐\n☕ Cheer Up  🍵\n🍂 ✨ )) ✨  🍂\n🍂┃ (( * ┣┓ 🍂\n🍂┃*💗 ┣┛ 🍂 \n🍂┗━━┛  🍂🎂 For YOU  🍰\n💐💐😌😚💐💐")

@mellow.on(mellow_cmd(pattern=r"getwell"))
async def getwell(event):
    if event.fwd_from:
        return
    await event.edit("🌹🌹🌹🌹🌹🌹🌹🌹 \n🌹😷😢😓😷😢💨🌹\n🌹💝💉🍵💊💐💝🌹\n🌹 GetBetter Soon! 🌹\n🌹🌹🌹🌹🌹🌹🌹🌹")

@mellow.on(mellow_cmd(pattern=r"sprinkle"))
async def sprinkle(event):
    if event.fwd_from:
        return
    await event.edit("✨.•*¨*.¸.•*¨*.¸¸.•*¨*• ƸӜƷ\n🌸🌺🌸🌺🌸🌺🌸🌺\n Sprinkled with love❤\n🌷🌻🌷🌻🌷🌻🌷🌻\n ¨*.¸.•*¨*. ¸.•*¨*.¸¸.•*¨`*•.✨\n🌹🍀🌹🍀🌹🍀🌹🍀")
