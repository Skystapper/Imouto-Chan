#(漏)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>⛩️ My Beloved Onee-Chan : /n   <a href='https://t.me/hanimeverse'>🍥Ecchi Senpai🍥</a>\n🎋 My Other Siblings : \n  <a href='https://t.me/+B2imbmmmuR84OTJl'>🍡3D-Waifus</a>\n    <a href='https://t.me/+3jP7uPeF43s4MDY1'>🍡Cosplay Kouhai</a>\n      <a href='https://t.me/Hanimeland_requestbot'>🍡Erome-San</a>\n🎍 My Family : <a href='https://t.me/Notice_meSenpai'>Notice Me?Senpai!!!</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🎐 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
