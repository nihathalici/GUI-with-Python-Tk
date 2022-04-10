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

# DEBUGGING FUNCS
def dropRefresh():
  items.drop()
  items = db.create_table('items', primary_id='id', primary_type='Integer')

# print all items in the table
def debugPrint():
  print("---------------------------")
  for item in db['items']:
    print(item['id'], item['node'], sep='. ')

# delete all nodes in table
def deleteAll():
  items.delete()

# insert a new item into our table
def newItem(item):
  curTime = str(date.day) + '/' + str(date.month) + '/' + str(date.year)
  items.insert(dict(node=item, creationtime=curTime))

# remove an item from our table
def removeItem(identifier):
  items.delete(id=identifier)

class Todo(tkinter.Tk):
  def __init__(self):
    tkinter.Tk.__init__(self)
    self.title("Todo")

    self.todoList = tkinter.Listbox()
    #self.todoList('<<ListboxSelect', self.deleteFromList())
    self.todoList.pack(fill=tkinter.BOTH, expand=0)

    # entry box & button for new todo items
    self.entry = tkinter.Entry()
    self.entry.pack(fill=tkinter.BOTH, expand=0)

    entryButton = tkinter.Button(text="Enter", command=self.addToList)
    entryButton.pack(fill=tkinter.BOTH, expand=0)




  def refreshList(self):
    pass

  def addToList(self):
    pass

  def deleteFromList(self):
    pass

if __name__ == "__main__":
  application = Todo()
  application.mainloop()
