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

# Source: https://github.com/ReconCubed/todo.py

import dataset
import tkinter
import datetime

# connect to the todo database
db = dataset.connect('sqlite:///todo.db')

# define the var items as our table
#items = db.create_table('items', primary_id='id', primary_type='Integer')
items = db['items']

# time management
date_time = datetime.datetime.now()
date = date_time.date()  # gives date
time = date_time.time()  # gives time

def dropRefresh():
  pass

def debugPrint():
  pass

def deleteAll():
  pass

def newItem(item):
  pass

def removeItem(identifier):
  pass

class Todo(tkinter.Tk):
  def __init__(self):
    pass

  def refreshList(self):
    pass

  def addToList(self):
    pass

  def deleteFromList(self):
    pass

if __name__ == "__main__":
  application = Todo()
  application.mainloop()