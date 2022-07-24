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
            text = f"<b>馃挐 My Beloved Onee-Chan : <a href='tg://user?id={OWNER_ID}'>Ecchi Senpai</a>\n馃挓 My Other Siblings : \n  <a href='tg://user?id={OWNER_ID}'>馃崱3D-Waifus</a>\n    <a href='tg://user?id={OWNER_ID}'>馃崱Cosplay Kouhai</a>\n      <a href='tg://user?id={OWNER_ID}'>馃崱Erome-San</a>\n馃帊 My Family : <a href='tg://user?id={OWNER_ID}'>Notice Me?Senpai!!!</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("馃敀 Close", callback_data = "close")
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
