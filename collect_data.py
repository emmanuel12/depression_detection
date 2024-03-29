#!/usr/bin/env python

import sqlite3
import datetime as dt
import time
import praw



day = 24*3600
dbconnect = sqlite3.connect('mentalhealth.db')
dbcursor = dbconnect.cursor()

def collect_data(limit=10000):
    reddit = praw.Reddit(client_id='8FJ4EPZ6l-4Gtg', client_secret='jp9oweovOFZkMavGmOJCyP03Umw', user_agent='Emmanuel Nsanga')
    reddit_posts = reddit.subreddit('depression')

    posts_text = []

    for posts in reddit_posts.top(limit=limit):
        posts_text.append((posts.title,))

    date = dt.datetime.now().date()
    strdate = str(date).split('-')[0]+str(date).split('-')[2]
    dbcursor.execute('''CREATE TABLE mentalhealth%s (posts)'''%strdate)
    dbcursor.executemany('INSERT INTO mentalhealth%s VALUES (?)'%strdate, posts_text)
    dbconnect.commit()





def timed():
    days = 0
    while True:
        days = days+day
        if days//day <= 9:
            collect_data()

        else:
            dbcursor.close()
            break

        time.sleep(day)



if __name__ == '__main__':
    timed()



