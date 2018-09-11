import sqlite3

class dbopr:

    _conn = None

    def __init__(self):
        self._conn = sqlite3.connect("devopstalks.db")

    def __exit__(self,exc_type, exc_val, exc_tb):
        self._conn.close()
    def help(self):
        print("Available commands:")
        print("add_user(<username>) - Add new Medium userid to database.")
        print("disable_user(<username>) - Disable Medium user publications to be publiched on telegram channel.")
        print("enable_user(<username>) - Enable Medium user publications to be published on telegram channel.")
        print("get_userlist() - Print existing users.")

    def get_muserid(self,username):
        cur = self._conn.cursor()
        uid = []
        cid = cur.execute('SELECT ID FROM MEDIUM_USERS WHERE MUSER_ID=?',(username,))
        ucid = cid.fetchone()
        if ucid is not None:
            uid = ucid
        return uid

    def add_user(self,username):
        cur = self._conn.cursor()

        if len(username) > 0:
            uid = self.get_muserid(username)
            if len(uid) == 0:
                cur.execute('INSERT INTO MEDIUM_USERS (MUSER_ID) VALUES (?)',(username,))
                self._conn.commit()
                print (username, " added.")
            else:
                print (username, " already exists. You can enable user with enable_user(<username>) method.")
        else:
            print("Username parameter is empty")

    def disable_user(self, username):
        cur = self._conn.cursor()
        
        if len(username) > 0:
            uid = self.get_muserid(username)
            if len(uid) > 0:
                cur.execute('UPDATE MEDIUM_USERS SET MSTATUS=0 WHERE ID=?', uid)
                self._conn.commit()
                print ("Done!")
            else:
                print (username, " not exists. Use add_user(<username>) method to add.")

    def enable_user(self, username):
        cur = self._conn.cursor()

        if len(username) > 0:
            uid = self.get_muserid(username)
            if len(uid) > 0:
                cur.execute('UPDATE MEDIUM_USERS SET MSTATUS=1 WHERE ID=?', uid)
                self._conn.commit()
                print ("Done!")
            else:
                print (username, " not exists. Use add_user(<username>) method to add.")

    def get_userlist(self):
        cur = self._conn.cursor()
        ucur = cur.execute('SELECT ID,MUSER_ID,MSTATUS FROM MEDIUM_USERS')
        userlist = ucur.fetchall()
        for mid,muser,mstatus in userlist:
            print ("------------------------------------")
            print (str(mid)," - ",muser," - ",str(mstatus))
