from telegram_bot import poster
import sqlite3
from medium_check import medium_parser
import time
p = poster()
conn = sqlite3.connect('devopstalks.db')

curr = conn.cursor()

us = curr.execute('SELECT ID,MUSER_ID FROM MEDIUM_USERS')
us_result = us.fetchall()

for user in us_result:
    mp = medium_parser(user)
    result = mp.get_new_pubs()
    if len(result) > 0:
        for post in result:
            url = mp.get_post_url(post)
            p.send_message(url)
            time.sleep(2)
        mp.insert_new_pubs(result)

    


