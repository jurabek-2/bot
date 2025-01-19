from db.connect import conn,cur

"""Foydalanuvchilarga javob beradigan class"""
class Base:
    def int(self,table):
        self.table=table

    def create_data(self,telegram_id):
            query=f'INSERT INTO {self.table} (telegram_id) VALUES (%s)'
            cur.execute(query,(telegram_id,))
            conn.commit()

    def get_data(self,telegram_id):
            query=f'SELECT * FROM {self.table} WHERE telegram_id = %s'
            cur.execute(query, (str(telegram_id,)))
            return cur.fetchone()

    def delet_data(self,telegram_id):
            query=f'DELETE FROM {self.table} WHERE telegram_id = %s'
            cur.execute(query, (telegram_id,))
            conn.commit()

    def get_datas(self):
            query=f'SELECT * FROM {self.table}'
            cur.execute(query)
            return cur.fetchall()

    def statistika(self):
        query=f"SELECT * FROM {self.table} WHERE created_at >= DATE_TRUNC('month',CURRENT_DATE)- INTERVAL '1 month' "
        cur.execute(query)
        month=cur.fetchall()
        query_week=f"SELECT * from {self.table} WHERE created_at >= DATE_TRUNC('week',CURRENT_DATE ) - INTERVAL 1 week "
        cur.execute(query_week)
        week=cur.fetchall()
        query_day = f"SELECT * from {self.table} WHERE created_at >= DATE_TRUNC('day',CURRENT_DATE ) - INTERVAL 1 day "
        cur.execute(query_day)
        day = cur.fetchall()
        return {'month':month,'week':week,'day':day}

"""Kinolarga javob beradigan class"""
class MediaClass(Base):

    def create_data(self,post_id:int,file_id:str,caption:str):
        query=f"INSERT INTO {self.table} (post_id ,file_id , caption) VALUES (%s , %s , %s)"
        cur.execute(query,(post_id,file_id,caption))
        conn.commit()

    def get_data(self,post_id:int):
        query=f"SELECT * FROM {self.table} WHERE post_id = %s"
        cur.execute(query,(post_id,))
        return cur.fetchone()

    def delet_data(self, post_id:int):
        query = f'DELETE FROM {self.table} WHERE post_id = %s'
        cur.execute(query, (post_id,))
        conn.commit()

    def get_moies(self, file_id:int):
        query = f'SELECT * FROM {self.table} WHERE file_id = %s'
        cur.execute(query, (file_id,))
        conn.commit()

class Channle(Base):

    def create_data(self,username:str,channle_id:str):
        query=f"INSERT INTO {self.table} (username , channel_id ) VALUES (%s , %s) "
        cur.execute(query,(username,channle_id))
        conn.commit()

    def get_data(self,chennle_id):
        query=f"SELECT * FROM {self.table} WHERE channle_id = %s"
        cur.execute(query, (chennle_id,))
        return cur.fetchone()

    def delet_data(self, chennle_id:int):
        query = f'DELETE FROM {self.table} WHERE chennle_id = %s'
        cur.execute(query, (chennle_id,))
        conn.commit()