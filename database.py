import sqlite3
from datetime import datetime

def initilize_db():
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()

        ddl = """CREATE TABLE IF NOT EXISTS USERS (
                    CHAT_ID   INTEGER,
                    USER_ID INTEGER,
                    USERNAME   TEXT,
                    AMOUNT  FLOAT,
                    LAST_TIME   INTEGER,
                    PRIMARY KEY (CHAT_ID, USER_ID))"""

        cursor.execute(ddl)
        db.commit()



def upsert_info(new_id: int,new_username: str,new_amount: float,timestamp: int):
    with sqlite3.connect("users.db") as db:
        db.execute("""
                    INSERT INTO USERS (ID,USERNAME,AMOUNT,LAST_TIME)
                    VALUES (?, ?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET
                        AMOUNT = excluded.AMOUNT,
                        LAST_TIME = excluded.LAST_TIME
        """, (new_id,new_username,new_amount,timestamp))

        db.commit()

def check_info(user_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute('SELECT AMOUNT, LAST_TIME FROM USERS WHERE ID = ?', (user_id,))
        row = cursor.fetchone()
        if row:
            AMOUNT = row[0]       
            LAST_TIME = row[1]  
            return AMOUNT, LAST_TIME
        return None

def get_all_usernames():
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        

        cursor.execute("SELECT USERNAME FROM USERS")
    
        rows = cursor.fetchall() 

        usernames = [row[0] for row in rows if row[0] is not None]
        
        return usernames
def get_all_info():
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        
        cursor.execute("SELECT * FROM USERS")
        raw_info = cursor.fetchall()

        return raw_info

def sort_raw_info(raw_info):
    users_id = [row[0] for row in raw_info if row[0] is not None]
    usernames = [str(row[1]) if row[1] is not None else "" for row in raw_info]
    user_amount = [row[2] if row[2] is not None else 0 for row in raw_info]
    timestamp = [row[3] for row in raw_info]
    
    print(users_id, usernames, user_amount, timestamp)
    return users_id, usernames, user_amount, timestamp

def get_db_screen():
    return sort_raw_info(get_all_info())
