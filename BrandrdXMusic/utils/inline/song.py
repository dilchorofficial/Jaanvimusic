from pyrogram.types import InlineKeyboardButton
import config

def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🍹 𝐒𝐔𝐏𝐏𝐎𝐑𝐓🍹", url=f"{config.SUPPORT_CHAT}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="🍬 𝐂𝐋𝐎𝐒𝐄 🍬"
            ),
        ],
    ]
    return buttons
