#!/usr/bin/env python

import sqlite3
import datatime as dt
import time
import praw



day = 24*3600
dbconnect = sqlite3.connect('mentalhealth.db')
dbcursor = dbconnect.cursor()

def collect_data(limit=10000):
    reddit = praw.Reddit(client_id='8FJ4EPZ6l-4Gtg', client_secret='jp9oweovOFZkMavGmOJCyP03Umw', user_agent='Emmanuel Nsanga')
    reddit_posts = reddit.subreddit('depression_help')

    posts_text = []

    for posts in reddit_posts.top(limit=limit):
        posts_text.append((posts.text,))

    date = dt.datatime.now().date()
    dbcursor.execute('''CREATE TABLE mentalhealth (mentalhealth%s)'''%date)
    dbcursor.executemany('INSERT INTO mentalhealth VALUES (mentalhealth%s)'%date, posts_text)
    dbcursor.commit()




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



