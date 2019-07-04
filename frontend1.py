import pymysql
from tkinter import *

def database(string):
    db = pymysql.connect("localhost","user","user@123","MOVIESDB")
    cursor = db.cursor()
    sql = "SELECT * FROM movies \
      WHERE name like '%s'" % (string)
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
      m_name = row[1]
      m_rate = row[2]
      fm2=Frame(root)
      fm2.pack()
      Label(fm2, text="Name: "+m_name).grid(row=0,column=1)
      Label(fm2, text="Rating: "+m_rate).grid(row=1,column=1)
      db.close()

def printtext():
    global e
    string=e.get()
    database(string)

root=Tk()

fm=Frame(root)
fm.pack(fill=BOTH)

fm1=Frame(root)
fm1.pack(fill=BOTH)

label_1=Label(fm)
label_1.grid(row=0)
e=Entry(fm)
e.grid(row=0,column=1)


Button(fm1,text="Search",fg="red",command=printtext).pack(side=LEFT)
root.mainloop()
