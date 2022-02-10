# 003-Python-Tk-Label-font-size-and-color.py

import tkinter as tk

app = tk.Tk()
app.title('Label with font')

label = tk.Label(app, text = 'Some text with larger letters')
label.pack()

label.config(font=("Courier", 44))
label.config(fg="#0000FF")
label.config(bg="yellow")

app.mainloop()
