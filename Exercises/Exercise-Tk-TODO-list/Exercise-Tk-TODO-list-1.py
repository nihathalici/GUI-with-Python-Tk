"""
Exercise: Tk TODO list

Create a Tk application to handle your TODO items.

* A Menu to be able to exit the application
* A List of current tasks.
* A way to add a new task. For a start each task has a title and a status.
  The status can be “todo” or “done”. (default is “todo”)
* A way to edit a task. (Primarily to change its title).
* A way to mark an item as “done” or mark it as “todo”.
* A way to move items up and down in the list.
* The application should automatically save the items in their most up-to-date state in a
  “database”. The database can be a JSON file or and SQLite database or anything else you feel
  fit.
"""

#####
# Solution source:
# https://github.com/kishore7403
#####

from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("TO DO LIST")

global j
j = 1
conn = sqlite3.connect('todo.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS todo""")

def rootclose():
  pass

def delpopup1():
  pass

def editpopup1():
  pass

def editpopup2():
  pass

def add():
  pass

def delete():
  pass

def show():
  pass

def update():
  pass

def edit():
  pass

show()

conn.commit()
conn.close()
root.mainloop()



