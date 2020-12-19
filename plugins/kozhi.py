import pyrogram
from pyrogram import InlineKeyboardMarkup, InlineKeyboardButton





@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def tip(bot, update):
        # logger.info(update)

    await bot.send_message(
        chat_id=update.chat.id,
        caption = """Hello🚴,
This is a Telegram URL Upload 🛸Bot!
<b>Please send me any direct download URL Link, i can upload to telegram as File/Video</b>
/help for more details..
Support Group :@TGB_Support""",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="DEV", url="https://t.me/Pr_o_To")],
                                                    [InlineKeyboardButton(text="GROUP", url="https://t.me/TGB_Support"),
                                                     InlineKeyboardButton(text="CHANNNEL", url="http://t.me/TG_BotZ")]]),
       
        reply_to_message_id=update.message_id
    )
