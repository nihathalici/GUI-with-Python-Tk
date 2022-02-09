# 003-Python-Tk-Label.py

import tkinter as tk

app = tk.Tk()
#app.title('Simple Label')

label = tk.Label(app, text = 'Some fixed text')
label.pack()

app.mainloop()
