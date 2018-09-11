import sqlite3
conn = sqlite3.connect('devopstalks.db')
curr = conn.cursor()

curr.execute('drop table MEDIUM_USERS')
curr.execute('''CREATE TABLE MEDIUM_USERS (ID INTEGER PRIMARY KEY AUTOINCREMENT, MUSER_ID TEXT,MSTATUS INTEGER DEFAULT 1)''')
#curr.execute('''CREATE TABLE MUSER_PUBLICATIONS (ID INTEGER PRIMARY KEY AUTOINCREMENT, MUSER_ID TEXT, MUSERPUB_ID TEXT)''')
#conn.commit()

#curr.execute('''INSERT INTO MEDIUM_USERS(MUSER_ID) VALUES("hacizade.faqani")''')
#curr.execute('''INSERT INTO MEDIUM_USERS(MUSER_ID) VALUES("komport")''')
curr.execute('''INSERT INTO MEDIUM_USERS(MUSER_ID) VALUES("gokhansengun")''')
conn.commit()

#curr.execute('''DROP TABLE MUSER_PUBLICATIONS''')
#curr.execute('''CREATE TABLE MUSER_PUBLICATIONS (ID INTEGER PRIMARY KEY AUTOINCREMENT, MUSER_ID INTEGER, MUSERPUB_ID TEXT)''')
result = curr.execute('''SELECT * FROM MUSER_PUBLICATIONS''')

result = curr.execute('''SELECT * FROM MEDIUM_USERS''')

users = result.fetchall()


class dbopr:

    _conn = None

    def __init__(self):
        self._conn = sqlite3.connect("devopstalks.db")

    def __exit__(self,exc_type, exc_val, exc_tb):
        self._conn.close()

    def get_muserid(self,username):
        cur = self._conn.cursor()
        cid = cur.execute('SELECT ID FROM MEDIUM_USERS WHERE MUSER_ID=?',(username,))
        uid = cid.fetchone()
        return uid

    def insert_user(self,username):
        cur = self._conn.cursor()
        if len(username) > 0:
            cur.execute('INSERT INTO MEDIUM_USERS (MUSER_ID) VALUES (?)',(username,))
            self._conn.commit()
        else:
            print("Username parameter is empty")

    def disable_user(self, username):
        cur = self._conn.cursor()
        if len(username) > 0:
            uid = self.get_muserid(username)
            cur.execute('UPDATE MEDIUM_USERS SET MSTATUS=0 WHERE ID=?', uid)
            self._conn.commit()

    def enable_user(self, username):
        cur = self._conn.cursor()
        if len(username) > 0:
            uid = self.get_muserid(username)
            cur.execute('UPDATE MEDIUM_USERS SET MSTATUS=1 WHERE ID=?', uid)
            self._conn.commit()

    def get_userlist(self):
        cur = self._conn.cursor()
        ucur = cur.execute('SELECT ID,MUSER_ID,MSTATUS FROM MEDIUM_USERS')
        userlist = ucur.fetchall()
        return userlist

