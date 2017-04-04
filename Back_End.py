import sqlite3

def connect(): #function for creating a table
    conn = sqlite3.connect('book.db') #create a connection and pass in db file
    cur = conn.cursor() #create cursor object
    cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)') #enter SQL quotes inside brackets
    conn.commit()
    conn.close()

def insert(title, author, year, isbn): #function for inserting data. needs param
    conn = sqlite3.connect('book.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn)) #good practice to put question marks followed by the variables
    conn.commit()
    conn.close()

def view(): #function to view db
    conn = sqlite3.connect('book.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""): #sets default values as blank
    conn = sqlite3.connect('book.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title =? OR author =? OR year = ? OR isbn = ?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('book.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?", (id, ))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect('book.db')
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()
#insert('The Sun', 'John Smith', 1999, 6115161565)
#delete(1)
update(5, 'The moon', 'John Smooth', 1917, 999999)
print(view())
print(search(author = 'John Smith'))
