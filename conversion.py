import pandas as pd
from configparser import ConfigParser

def config(filename='config.ini',section='postgresql'):
    parser = ConfigParser()
    db ={}
    parser.read(filename)
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]]= param[1]


    return db

import psycopg2
def connect(query):
    conn =None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        db_version = cur.fetchall()
        cur.close()
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cur is not None:
            conn.close()
            print("connection Closed")
            return 








