from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import backend

select_row = None

def view_command():
    lb1.delete(0,END)
    for row in backend.view():
        lb1.insert(END, row)

def search_command():
    lb1.delete(0,END)
    for row in backend.search(title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get()):
        lb1.insert(END, row)

def insert_command():
    backend.insert(title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get())
    lb1.delete(0,END)
    lb1.insert(END,(title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get()))
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    view_command()

def get_selected_row(event):
    global select_row
    try:
        index=lb1.curselection()[0]
        select_row=lb1.get(index)
        e1.delete(0, END)
        e1.insert(END, select_row[1])
        e2.delete(0, END)
        e2.insert(END, select_row[2])
        e3.delete(0, END)
        e3.insert(END, select_row[3])
        e4.delete(0, END)
        e4.insert(END, select_row[4])
    except IndexError:
        pass

def update_command():
    backend.update(select_row[0],title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get())
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    view_command()

def delete_command():
    backend.delete(select_row[0])
    

window = Tk(className=' Book Inventory ')

l1 = Label(text='Title')
l1.grid(row=0,column=0)

title_entry=StringVar()
e1 = Entry(window,textvariable=title_entry)
e1.grid(row=0,column=1)

l2 = Label(text='Author')
l2.grid(row=0,column=2)

author_entry=StringVar()
e2 = Entry(window,textvariable=author_entry)
e2.grid(row=0,column=3)

l3 = Label(text='Year')
l3.grid(row=1,column=0)

year_entry=StringVar()
e3 = Entry(window,textvariable=year_entry)
e3.grid(row=1,column=1)

l4 = Label(text='ISBN')
l4.grid(row=1,column=2)

isbn_entry=StringVar()
e4 = Entry(window,textvariable=isbn_entry)
e4.grid(row=1,column=3)

lb1 = Listbox(window,justify='left', height=6, width=40)
lb1.grid(row=3,column=0,rowspan=6, columnspan=2)
lb1.bind('<<ListboxSelect>>', get_selected_row)
sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb1.yview)

b1 = Button(window, text='View All', width=20, command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window, text='Search Entry', width=20, command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window, text='Add Entry', width=20, command=insert_command)
b3.grid(row=4,column=3)

b4 = Button(window, text='Update Selected', width=20, command=update_command)
b4.grid(row=5,column=3)

b5 = Button(window, text='Delete Selected', width=20, command=delete_command)
b5.grid(row=6,column=3)

b6 = Button(window, text='Close Program', width=20, command=window.destroy)
b6.grid(row=7,column=3)


window.mainloop()