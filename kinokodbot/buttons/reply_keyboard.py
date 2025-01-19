from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


def admin_btn():
    btn=ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True,row_width=3)
    statistika=KeyboardButton("Statistika")
    moview=KeyboardButton("Kinolar")
    reklama=KeyboardButton("Reklama")
    add_channel=KeyboardButton("Kanallar")
    return btn.add(statistika,moview,reklama,add_channel)

def movie_btn():
    btn=ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True,row_width=3)
    statistika=KeyboardButton("Kino Statistika")
    addmoview=KeyboardButton("Kino Qo'shish")
    dell_movie=KeyboardButton("Kinoni O'chirish")
    exits_btn=KeyboardButton("Chiqish")
    return btn.add(statistika,addmoview,dell_movie,exits_btn)

def channel_btn():
    btn = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
    add_channel = KeyboardButton("Kanal Qo'shish")
    del_channel = KeyboardButton("Kanal O'chirish")
    exits_btn = KeyboardButton("Chiqish")
    return btn.add(add_channel,del_channel,exits_btn)

def exit_btn():
    btn = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
    return btn.add("Chiqish")


