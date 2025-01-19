from aiogram.types import  InlineKeyboardButton,InlineKeyboardMarkup
from model.models import channel


def forced_channel():
    channels=channel.get_datas()
    btn=InlineKeyboardMarkup(row_width=2)
    for i,v in enumerate(channels):
        btn.add(InlineKeyboardButton(f"{int(i)+1}- kanal ",url=f"{v['username']}"))
        return
