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
  root.destroy()

def delpopup1():
  messagebox.showinfo("INFO", "ENTER TASK ID TO DELETE")

def editpopup1():
  messagebox.showinfo("INFO", "ENTER TASK ID TO EDIT")

def editpopup2():
  messagebox.showinfo("INFO", "ENTER VALID TASK ID TO EDIT")

def add():
  global show_labelframe
  global labelframe_content
  global j

  conn = sqlite3.connect('todo.db')
  c = conn.cursor()
  if (add_entry.get()==""):
    response = messagebox.askyesno("warning","wanna enter empty Task?")
    if (response==1):
      c.execute("INSERT INTO todo VALUES (:task)",
              {
              'task':add_entry.get()
              })
      show_labelframe.destroy()
      labelframe_content.destroy()
    else:
      pass
  else:
    c.execute("INSERT INTO todo VALUES (:task)",
                    {
                    'task':add_entry.get()
                    }
  add_entry.delete(0,END)
  show_labelframe.destroy()
  labelframe_content.destroy()

  conn.commit()
  conn.close()
  show()


def delete():
  global show_labelframe
  global labelframe_content
  global j

  conn = sqlite3.connect('todo.db')
  c = conn.cursor()

  try:
    c.execute("DELETE FROM todo WHERE oid="+del_entry.get())
    del_entry.delete(0,END)
    j = j - 1

  except sqlite3.OperationalError as e:
    delpopup1()

  show_labelframe.destroy()
  labelframe_content.destroy()

  conn.commit()
  conn.close()
  show()


def show():
  global show_labelframe
  global labelframe_content
  global j

  conn = sqlite3.connect('todo.db')
  c = conn.cursor()
  c.execute("SELECT task,oid FROM todo")
  records = c.fetchall()
  print_records = ''
  for record in records:
    print_records += "   "+str(record[1])+"   "+str(record[0])+","

  a = print_records.split(",")
  show_labelframe = LabelFrame(root, text="Your Tasks To Do")
  show_labelframe.grid(row=0, column=2, rowspan=6, columnspan=2)
  default_label = Label(show_labelframe, text="  ID  TASK")
  default_label.grid(row=0, column=0, sticky=W)
  for i in a:
    labelframe_content = Label(show_labelframe, text=i)
    labelframe_content.grid(row=j, column=0, columnspan=2, sticky=W)
    j = j + 1

  conn.commit()
  conn.close()

def update():
  pass

def edit():
  pass

show()

conn.commit()
conn.close()
root.mainloop()
