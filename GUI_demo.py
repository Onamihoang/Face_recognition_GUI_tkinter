# from tkinter import *
# import tkinter
from tkinter import ttk
import tkinter as tk

window = tk.Tk()
window.title("Điểm danh khuôn mặt DEMO")
window.geometry("800x600")

# Add lable
lbel = tk.Label(window, text="Hello, world!", bg="white", fg='red',\
         font=('Arial', 50))
lbel.grid(column=0, row=0, padx = 10, pady = 25)


# Add Textbox
txt = tk.Entry(window, width=20)
txt.grid(column=0, row=1)

def handleBtnHello():
    lbel.configure(text="HI " + txt.get())
    return

# Add botton
btnHello = tk.Button(window, text="Say Hello", command=handleBtnHello)
btnHello.grid(column=1, row=1)


# Add Combobox
n = tk.StringVar()
name_nv_choosen = ttk.Combobox(window, width = 27, textvariable = n)
name_nv_choosen['value'] = ("Nhân viên 1", "Nhân viên 2", "Nhân viên 3")
name_nv_choosen.grid(column=0, row=2)
name_nv_choosen.current()

window.mainloop()