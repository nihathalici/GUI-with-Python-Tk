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
  global edit
  global r, n

  conn = sqlite3.connect('todo.db')
  c = conn.cursor()

  r = to_entry.get()
  n = edit_entry_edit.get()

  c.execute("""UPDATE todo SET task=:tasky WHERE oid=:oid""",{
    'tasky':r,
    'oid':n})
  edit.destroy()

  show_labelframe.destroy()
  labelframe_content.destroy()
  conn.commit()
  conn.close()
  show()

def edit():
  try:
    global to_entry
    global edit_entry_edit
    global r, n
    global edit
    global edit_entry 
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    edit = Tk()
    edit.title("Edit Task")

    edit_entry_label = Label(edit, text="Task ID:")
    edit_entry_edit = Entry(edit, width=5)
    to_label = Label(edit, Text="To:")
    to_entry = Entry(edit, width=60)

    c.execute("SELECT task FROM todo WHERE oid="+edit_entry.get())
    r1=c.fetchone()
    r= str(r1[0])
    n = edit_entry.get()

    edit_entry_edit.insert(0,n)
    to_entry.insert(0,r)

    edit_btn_edit = Button(edit, text="edit task", fg="white", bg="#1E90FF",border=2,command=update)
    edit_entry_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
    edit_entry_edit.grid(row=0, column=1, padx=5, pady=5, sticky=W)
    to_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
    to_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)
    edit_btn_edit.grid(row=1, column=0, columnspan=4, padx=10, pady=5, ipadx=169, ipady=10)

    conn.commit()
    conn.close()

  except sqlite3.OperationalError as e:
    edit.destroy()
    editpopup1()

  except TypeError as e:
    edit.destroy()
    editpopup2()

  edit_entry.delete(0, END)
  edit.mainloop()


show()

conn.commit()
conn.close()
root.mainloop()
