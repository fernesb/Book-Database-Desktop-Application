import sqlite3


def connect():
    conn=sqlite3.connect('books.db')
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect('books.db')
    cursor=conn.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect('books.db')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM book")
    rows=cursor.fetchall()
    conn.close()
    return rows

def search(title='',author='',year='',isbn=''):
    conn=sqlite3.connect('books.db')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows=cursor.fetchall()
    conn.close()
    return rows


connect()
