from model.orm import Base,MediaClass,Channle

user=Base("users")
movie=MediaClass("movies")
channel=Channle("channels")


#foydalanuvchilarni qo'shish uchun funksiya
def create_user(telegram_id:int):
    data=user.get_data(telegram_id)
    if not data:
        user.create_data(telegram_id=str(telegram_id))
        return True
    else:
        return False

def get_users():
    return user.get_datas()



def statistika_user():
    data=user.statistika()
    all_data=user.get_datas()

    if data:
        return (f"Adminlar uchun Userlar statistikasi\n\n"
                f"Oxirgi 30 kun ichida ro'yxatan o'tgan userlar soni {len(data['month'])} ta \n"
                f"Oxirgi 7 kun ichida ro'yxatan o'tgan userlar soni {len(data['week'])} ta \n"
                f"Oxirgi 24 soat ichida ro'yxatan o'tgan userlar soni {len(data['day'])} ta \n\n"
                f"Barcha foydalanuvchi soni {len(all_data)} ta"
                )
    else:
        return False


def create_movie(post_id:int,file_id:str,caption:str):
    data=movie.get_moies(file_id)
    if not data:
        movie.create_data(post_id,file_id,caption)
        return post_id
    else:
        return data.get('post_id',None)

def get_movie(post_id:int):
    data=movie.get_datas(post_id)
    if data:
        return [data['file_id']],[data['caption']]
    else:
        return False

def delete_movie(post_id:int):
    data=movie.get_data(post_id=post_id)
    if data:
        try:
            movie.delete_movie(post_id=post_id)
            return f"Kino muvaffaqiyatli o'chirildi"
        except:
            return f"Kino o'chirishda xatolik yuzaga keldi"
    else:
        return f"{post_id} - ID bilan kino topilmadi"

def statistika_movie():
    data=movie.statistika()
    all_data=movie.get_datas()
    if data:
        return (f"Adminlar uchun Userlar statistikasi\n\n"
                f"Oxirgi 30 kun ichida ro'yxatan o'tgan userlar soni {len(data['month'])} ta \n"
                f"Oxirgi 7 kun ichida ro'yxatan o'tgan userlar soni {len(data['week'])} ta \n"
                f"Oxirgi 24 soat ichida ro'yxatan o'tgan userlar soni {len(data['day'])} ta \n\n"
                f"Barcha kinolar  soni {len(all_data)} ta"
                )
    else:
        return False

