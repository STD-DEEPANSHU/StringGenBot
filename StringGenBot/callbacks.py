import traceback
from data import Data
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
from StringGenBot.generate import generate_session, ask_ques, buttons_ques


# Callbacks
@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    # user_id = callback_query.from_user.id
    mention = user.mention
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.START.format(callback_query.from_user.mention, mention),
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )
    elif query == "generate":
        await callback_query.answer()
        await callback_query.message.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await callback_query.answer("» ᴛʜᴇ ᴩʏʀᴏɢʀᴀᴍ ᴠ2 sᴛʀɪɴɢ sᴇssɪᴏɴ ᴡɪʟʟ ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ᴛʜᴇ ʙᴏᴛ's ᴡʜɪᴄʜ ᴀʀᴇ ᴜᴩɢʀᴀᴅᴇᴅ ᴀᴛ ᴩʏʀᴏɢʀᴀᴍ ᴠ2 !", show_alert=True)
                await generate_session(bot, callback_query.message)
            elif query == "pyrogram1":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, old_pyro=True)
            elif query == "pyrogram_bot":
                await callback_query.answer("» ᴛʜᴇ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴡɪʟʟ ʙᴇ ᴏғ ᴩʏʀᴏɢʀᴀᴍ ᴠ2.", show_alert=True)
                await generate_session(bot, callback_query.message, is_bot=True)
            elif query == "telethon_bot":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True, is_bot=True)
            elif query == "telethon":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True)
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))


ERROR_MESSAGE = "ᴡᴛғ ! sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ. \n\n**ᴇʀʀᴏʀ** : {} " \
            "\n\n**ᴩʟᴇᴀsᴇ ғᴏʀᴡᴀʀᴅ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴛᴏ @Tricky_Deepanshu**, ɪғ ᴛʜɪs ᴍᴇssᴀɢᴇ " \
            "ᴅᴏᴇsɴ'ᴛ ᴄᴏɴᴛᴀɪɴ ᴀɴʏ sᴇɴsɪᴛɪᴠᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ " \
            "ʙᴇᴄᴀᴜsᴇ ᴛʜɪs ᴇʀʀᴏʀ ɪs **ɴᴏᴛ ʟᴏɢɢᴇᴅ ʙʏ ᴛʜᴇ ʙᴏᴛ** !"
