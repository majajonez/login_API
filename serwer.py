import os
import psycopg2
from flask import Flask, Response, redirect, url_for, request, make_response, render_template
from flask_caching import Cache
import json

config = {
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 999999999
}
app = Flask(__name__)
# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='postgres',
                            user="postgres",
                            password="mysecretpassword")
    return conn


def get_user(x):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM logowanie_uzytkownikow'
                f' WHERE login = \'{x}\'')
    uzytkownik = cur.fetchall()
    cur.close()
    conn.close()
    return uzytkownik


@app.route('/')
def index():
    uzytkownicy = get_users()
    return json.dumps(uzytkownicy)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        args = request.args
        uzytkownik = get_user(args.get("user", ""))
        if uzytkownik:
            if args.get("password", "") == uzytkownik[0][2]:
                return "<b>Witaj " + args["user"] + "</b>"
            else:
                return "<b>bledne haslo</b>"
        else:
            return "<b>Użytkownik nie istnieje</b>"
    else:
        return "<b>Nie zalogowany</b>"


@app.route('/register', methods=['GET', 'POST'])
def register():
    get_db_connection()
    args = request.args
    user = args.get("user", None)
    password = args.get("password", None)
    if user and password:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO logowanie_uzytkownikow (login, haslo)'
                    'VALUES (%s, %s)',
                    (user,
                     password)
                    )
        conn.commit()
        cur.close()
        conn.close()
        return make_response("<i>rejestracja przebiegla pomyslnie</i>", 200)
    else:
        return make_response("<i> rejestracja sie nie udala</i>")


@app.route('/aa')
def aa():
    args = request.args
    app.logger.error(args.get("kasper"))
    return json.dumps(args)


if __name__ == '__main__':
    app.run()