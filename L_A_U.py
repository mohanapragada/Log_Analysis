#! /usr/bin/env

import psycopg2
import time


def connect():
    return psycopg2.connect("dbname=news")

qe1 = ''' SELECT title, views FROM most_art INNER JOIN articles ON  
      articles.slug = most_art.slug ORDER BY views desc LIMIT 3'''
qe2 = '''
    SELECT authors_N.name AS author,
    sum(most_art.views) AS views FROM most_art INNER JOIN authors_N
    ON authors_N.slug=most_art.slug
    GROUP BY authors_N.name ORDER BY views  limit 4'''
qe3 = '''
    SELECT error_down.date ,(error_down.count*100.00 / analy_total.count) AS
    percentage FROM error_down INNER JOIN analy_total
    ON error_down.date = analy_total.date
    AND (error_down.count*100.00 / analy_total.count) >1
    ORDER BY (error_down.count*100.00 /analy_total.count);'''
    

def pop_art(qe1):
    db = connect()
    c1 = db.cursor()
    c1.execute(qe1)
    rss = c1.fetchall()
    for i in range(len(rss)):
        t1 = rss[i][0]
        views = rss[i][1]
        print("  *  %s  ---->  %d" % (t1, views))
    db.close()


def mt_auth_N(qe2):
    db = connect()  
    c1 = db.cursor()
    c1.execute(qe2)
    rss = c1.fetchall()
    for i in range(len(rss)):
        n1 = rss[i][0]
        views = rss[i][1]
        print("  *  %s  ---->  %d" % (n1, views))
    db.close()


def error_fall_down(qe3):
    db = connect()
    c1 = db.cursor()
    c1.execute(qe3)
    rss = c1.fetchall()
    for i in range(len(rss)):
        d1 = rss[i][0]
        err_prc = rss[i][1]
        print("  *  %s  ---->  %.1f %%" % (d1, err_prc))

if __name__ == "__main__":
    print(" 1.THE LIST OF POPULAR ARTICLES ARE: \n")
    pop_art(qe1)
    print("\n")
    print(" 2.THE LIST OF POPULAR AUTHORS ARE: \n")
    mt_auth_N(qe2)
    print("\n")
    print(" 3.PERCENT ERROR MORE THAN 1.0: \n")
    error_fall_down(qe3)
    print("\n")
    
     
