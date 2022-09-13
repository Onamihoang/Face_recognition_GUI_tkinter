# from tkinter import *
# import tkinter
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo


root = tk.Tk()
root.title("Điểm danh khuôn mặt DEMO")
root.geometry("800x600")

# Add lable
lbel = tk.Label(root, text="Hello, world!", bg="white", fg='red',\
         font=('Arial', 50))
lbel.grid(column=0, row=0, padx = 10, pady = 25)


# Add Textbox
txt = tk.Entry(root, width=20)
txt.grid(column=0, row=1)

def handleBtnHello():
    lbel.configure(text="HI " + txt.get())
    return

# Add botton
btnHello = tk.Button(root, text="Say Hello", command=handleBtnHello)
btnHello.grid(column=1, row=1)




# create the root window

# create a list box
langs = ('Java', 'C#', 'C', 'C++', 'Python',
         'Go', 'JavaScript', 'PHP', 'Swift')

var = tk.Variable(value=langs)

listbox = tk.Listbox(
    root,
    listvariable=var,
    height=6,
    selectmode=tk.EXTENDED)

listbox.grid(column=0, row=2)

# link a scrollbar to a list
scrollbar = ttk.Scrollbar(
    root,
    orient=tk.VERTICAL,
    command=listbox.yview
)

# listbox['yscrollcommand'] = scrollbar.set

# scrollbar.pack(side=tk.LEFT, expand=True, fill=tk.Y)


def items_selected(event):
    # get selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'

    showinfo(title='Information', message=msg)


listbox.bind('<<ListboxSelect>>', items_selected)

root.mainloop()
