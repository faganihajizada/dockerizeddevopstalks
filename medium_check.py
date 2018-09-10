

import sqlite3
import requests
import json

class medium_parser:
    
    _conn = None
    muser = None
    muser_id = 0

    def __init__(self,userdetails):
        self.muser = userdetails[1]
        self.muser_id = userdetails[0]
        self._conn = sqlite3.connect('devopstalks.db')
    def __exit__(self,exc_type, exc_val, exc_tb):
        self._conn.close()

    def get_username(self):
        return self.muser

    def clean_json_response(self,response):
        return json.loads(response.text.split('])}while(1);</x>')[1])

    def get_list_of_latest_posts_ids(self):
        post_ids = []
        MEDIUM = 'https://medium.com'
        url = MEDIUM + '/@' + self.muser + '/latest?format=json'
        response = requests.get(url)
        response_dict = self.clean_json_response(response)
        try:
            posts = response_dict['payload']['references']['Post']
        except:
            posts = []
        if posts:
            for key in posts.keys():
                post_ids.append(posts[key]['id'])
            return post_ids

    def get_list_of_user_posts(self):
        curr = self._conn.cursor()
        upub_list = []
        pubs = curr.execute('''SELECT MUSERPUB_ID FROM MUSER_PUBLICATIONS WHERE MUSER_ID = ?''',(self.muser_id,))
        pub_list = pubs.fetchall()
        
        if len(pub_list) > 0:
            for pub in pub_list:
                upub_list.append(pub[0])
        
        return upub_list


    def get_post_url(self,post_id):
        MEDIUM = 'https://medium.com'
        url = MEDIUM + '/@' + self.muser + '/' + post_id
        return url


    def insert_new_pubs(self,publist):
        curr = self._conn.cursor()
        for pub in publist:
            curr.execute('''INSERT INTO MUSER_PUBLICATIONS (MUSER_ID,MUSERPUB_ID) VALUES (?, ?)''',(self.muser_id,pub,))
            self._conn.commit()

    def get_new_pubs(self):
        latest = self.get_list_of_latest_posts_ids()
        stored = self.get_list_of_user_posts()
        pub_dif = set(latest).difference(stored)
        return list(pub_dif)




