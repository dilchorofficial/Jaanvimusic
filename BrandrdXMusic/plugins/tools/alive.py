import asyncio

from BrandrdXMusic import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME

@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/e999c40cb700e7c684b75.mp4",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention}\n\n🔮 ɪ ᴀᴍ {MUSIC_BOT_NAME}\n\n✨ ɪ ᴀᴍ ғᴀsᴛ ᴀɴᴅ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.\n\n💫 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴊᴏɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ🤍...\n\n━━━━━━━━━━━━━━━━━━❄",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="☆𝗗꯭ɪʟ꯭c፝֟͠ʜ꯭𝛔ʀ꯭  ", url=f"https://t.me/ANURAGMOD"
            ),
            InlineKeyboardButton(
                text=" 💌 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 💌 ", url=f"https://t.me/Sweet_chat_aao"
            ),
        ],
                [
            InlineKeyboardButton(
                text="☆ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/ANURAG_ABOUT"
            ),
                ],
                [
                    InlineKeyboardButton(
                        "✯ ᴄʟᴏsᴇ ✯", callback_data="🍬 𝐂𝐋𝐎𝐒𝐄 🍬"
                    )
                ],
            ]
        )
    )
