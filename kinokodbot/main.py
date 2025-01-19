from aiogram import Bot,Dispatcher,executor,types
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext, storage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text
from dp.connect import startup_table
from model.models import create_user,get_users,delet_user,get_movie
from buttons.reply_keyboard import admin_btn,movie_btn,channel_btn
from states.state import ReklmaState,AddChannelsState,AddKino,DleteChannelState,DeleteMovieState

logging.basicConfig(level=logging.INFO)
# ADMIN
ADMINS = [378741756]
# Bot token
API_TOKEN="6911702263:AAH_yDuDChRLzsqYBjPaqOySTwu_fF4qUcw"
bot=Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands="start")
async def start_menu(messege:types.Message):
    user=messege.from_user.first_name
    create_user(messege.from_user.id)
    text=f"Assalomu alekum{user}\n"
    text+=f"kodli kino botga qush kelipsiz\n"
    text+=f"iltimos botga kino kodini yuboring\n"
    await messege.answer(text)



@dp.message_handler(commands="user")
async def start_menu(messege:types.Message):
    if str(messege.from_user.id)==str(ADMINS[0]):
        user=get_users()
        await messege.answer(user)
    else:
        await messege.answer("siz admin emasiz")

@dp.message_handler(commands="admin")
async def admin_function(message:types.Message):
    try:
        if str(message.from_user.id)==str(ADMINS[0]):
            pass

        else:
            await message.answer("Siz admin emassiz")
    except Exception as e:
        await message.answer(f"{e}")


@dp.message_handler(Text("Kinolar"))
async def admin_function(message:types.Message):
    try:
        if str(message.from_user.id)==str(ADMINS[0]):
           await message.answer("Xush kelisiz kinolar sahifasiga \n",reply_markup=admin_btn())
        else:
            await message.answer("Siz admin emassiz")
    except Exception as e:
        await message.answer(f"{e}")

@dp.message_handler(Text("Kanallar"))
async def admin_function(message:types.Message):
    try:
        if str(message.from_user.id)==str(ADMINS[0]):
           await message.answer("Xush kelisiz kanallar sahifasiga \n",reply_markup=channel_btn())
        else:
            await message.answer("Siz admin emassiz")
    except Exception as e:
        await message.answer(f"{e}")


@dp.message_handler(Text("Kino Qo'shish"))
async def addkino_function(message:types.Message):
    try:
        if str(message.from_user.id)==str(ADMINS[0]):
            await AddKino.media.set()
            await message.answer("Kinoni yuborishingiz mumkin 🎬")

        else:
            await message.answer("Siz admin emassiz ❌")
    except Exception as e:
        await message.answer(f"{e}")

@dp.message_handler(state=AddKino.media,content_types=types.ContentType.ANY)
async def addkino_function(message:types.Message,state:FSMContext):
    try:
        if message.text=="Chiqish":
            await message.answer("Kino qo'shish to'xtatildi")
            await state.finish()
        else:
            async with state.proxy() as data:
                data['file_id']=message.video.file_id
                data['caption']=message.caption()

            await AddKino.media_id.set()
            await message.answer("Iltimos kino kodini yuboring")


    except Exception as e:
        await message.answer(f"{e}")


@dp.message_handler(state=AddKino.media_id, content_types=types.ContentType.ANY)
async def addkino_f(message: types.Message, state: FSMContext):
        if message.text == "Chiqish":
            await message.answer("Kino qo'shish to'xtatildi")
            await state.finish()
        elif not get_movie(int(message.text)):
            async with state.proxy() as data:






@dp.message_handler(commands="info",chat_id=ADMINS[0])
async def info_users(message:types.Message):
    text=f"<b> Hamma Foydalanuvchilardan Malumotlarni </b> \n\n"
    users=get_users()
    for user in users:
        text+=f"<b>Telegram ID</b>: {user[1]}\n"
    await message.answer(text)






@dp.message_handler(commands="delet")
async def delet_menu(messege:types.Message):
    if str(messege.from_user.id)==str(ADMINS[0]):
        user=delet_user()
        await messege.answer(user)
    else:
        await messege.answer("user uchirildi")


async def start(dp):
    startup_table()

#Foydalanuvchiga Reklama Yuboruvchi handler
class ReklamaState(StatesGroup):
    reklamacontent=State()

@dp.message_handler(commands='reklama',chat_id=ADMINS[0])
async def send_reklama(message:types.Message):
    await message.answer("Reklama Yuborish uchun matn yoki Faylni yuboring")
    await ReklamaState.reklamacontent.set()

@dp.message_handler(content_types=[types.ContentType.ANY],state=ReklamaState.reklamacontent)
async def send_reklama_content(message:types.Message,state:FSMContext):
    content_type=message.content_type
    await state.finish()
    users=get_users()
    if content_type==types.ContentType.TEXT:
        text=message.text
        for user in users:
            try:
                await bot.send_message(chat_id=user[1],text=text)
            except Exception as e:
                await bot.send_message(chat_id=ADMINS[0],text=f"Matnni foydalanuvchga yuborishda qandeydir xatolik bor {e}")

    elif content_type==types.ContentType.PHOTO:
        photo=message.photo[-1]
        text=message.caption
        for user in users:
            try:
                await bot.send_photo(chat_id=user[1],photo=photo.file_id,caption=text)
            except Exception as e:
                await bot.send_message(chat_id=ADMINS[0],text=f"Rasmni foydalanuvchga yuborishda qandeydir xatolik bor {e}")

    elif content_type==types.ContentType.VIDEO:
        video=message.video
        text=message.caption
        for user in users:
            try:
                await bot.send_video(chat_id=user[1],video=video.file_id,caption=text)
            except Exception as e:
                await bot.send_message(chat_id=ADMINS[0],text=f'Videoni foydalanuvchga yuborishda qandeydir xatolik bor {e}')












async def start(dp):
    startup_table()


if __name__=='__main__':
    executor.start_polling(dp,on_startup=start,skip_updates=True)
