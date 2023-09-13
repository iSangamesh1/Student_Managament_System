import sqlite3

def connect():
    con = sqlite3.connect('fee.db')
    cur = con.cursor()

    cur.execute('Create table if not exists fee(Id integer primary key, reciept integer, name text, admission text, date integer, branch text, sem text, total integer, due integer)')

    con.commit()
    con.close()

def insert(receipt = ' ', name = ' ', addmission = ' ', date = ' ', branch = ' ', semester = ' ', total = ' ', paid = ' ', due = ' '):
    con = sqlite3.connect('fee.db')
    cur = con.cursor()

    cur.execute('Insert into fee values (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(receipt, name, addmission, date, branch, semester, total, paid, due))

    con.commit()
    con.close()

def Display():
    con = sqlite3.connect('fee.db')
    cur = con.cursor()
    cur.execute('SELECT * from fee')
    row = cur.fetchall()
    return row

    con.commit()

def delete(id):
    con = sqlite3.connect('fee.db')
    cur = con.cursor()
    cur.execute('Delete from fee where id = ?', (id,))

    con.commit()
    con.close()

def search(receipt = ' ', name = ' ', addmission = ' ', date = ' ', branch = ' ', semester = ' ', total = ' ', paid = ' ', due = ' '):
    con = sqlite3.connect('fee.db')
    cur = con.cursor()

    cur.execute('select * from fee where receipt = ? or name = ? or addmission = ? or date = ? or branch = ? or sem = ? or total = ? or paid = ? or due = ?', (receipt, name, addmission, date, branch, semester, total, paid, due))
    row = cur.fetchall()
    return row

    con.commit()

def Update(id, receipt=' ', name = ' ', addmission = ' ', date = ' ', branch = ' ', semester = ' ', total = ' ', paid = ' ', due = ' '):
    con = sqlite3.connect('fee.db')
    cur = con.cursor()

    cur.execute('update fee set receipt = ? or name = ? or addmission = ? or date = ? or branch = ? or semester = ? or total = ? or paid = ? or due = ?',(receipt, name, addmission, date, branch, semester, total, paid, due) )

    con.commit()
    con.close()

 
connect()