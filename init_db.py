import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="mysecretpassword")
try:
    cur = conn.cursor()

    try:
        cur.execute('DROP TABLE IF EXISTS logowanie_uzytkownikow;')
        cur.execute('CREATE TABLE logowanie_uzytkownikow (id serial PRIMARY KEY,'
                                         'login text NOT NULL,'
                                         'haslo text NOT NULL);'
                                         )

        cur.execute('INSERT INTO logowanie_uzytkownikow (id, login, haslo)'
                    'VALUES (%s, %s, %s)',
                    ('1',
                     'maja',
                     '123')
                    )

        conn.commit()

    finally:
        cur.close()

finally:
    conn.close()