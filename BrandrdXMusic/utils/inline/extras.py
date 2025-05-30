from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_9"], url=SUPPORT_CHAT),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="🍬 𝐂𝐋𝐎𝐒𝐄 🍬"),
        ],
    ]
    return buttons


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                 InlineKeyboardButton(
                text="🍹 𝐒𝐔𝐏𝐏𝐎𝐑𝐓🍹", url=f"https://t.me/+SFB9vAp52SAxZGE1"
            ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl


def supp_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_9"],
                    url=SUPPORT_CHAT,
                ),
            ]
        ]
    )
    return upl
