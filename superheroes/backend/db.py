import sqlite3
conn = sqlite3.connect('superheroes/backend/heroes.db', check_same_thread=False)
c = conn.cursor()

def get_all():
    c.execute('select * from heroes')
    heroes = c.fetchall()
    return heroes

def create(name, power):
    heroe = c.execute(f'insert into heroes (name, power) values("{name}","{power}");')
    conn.commit()
    return heroe.lastrowid


def delete(idx):
    conn.execute(f'delete from heroes where id = {idx}')
    conn.commit()
