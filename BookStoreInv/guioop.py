from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from backendoop import Database

database = Database("books.db")

class Window(object):

    select_row = None

    def view_command(self):
        self.lb1.delete(0,END)
        for row in database.view():
            self.lb1.insert(END, row)

    def search_command(self):
        self.lb1.delete(0,END)
        for row in database.search(self.title_entry.get(),self.author_entry.get(),self.year_entry.get(),self.isbn_entry.get()):
            self.lb1.insert(END, row)

    def insert_command(self):
        database.insert(self.title_entry.get(),self.author_entry.get(),self.year_entry.get(),self.isbn_entry.get())
        self.lb1.delete(0,END)
        self.lb1.insert(END,(self.title_entry.get(),self.author_entry.get(),self.year_entry.get(),self.isbn_entry.get()))
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.view_command()

    def get_selected_row(self,event):
        global select_row
        try:
            index=self.lb1.curselection()[0]
            select_row=self.lb1.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, select_row[1])
            self.e2.delete(0, END)
            self.e2.insert(END, select_row[2])
            self.e3.delete(0, END)
            self.e3.insert(END, select_row[3])
            self.e4.delete(0, END)
            self.e4.insert(END, select_row[4])
        except IndexError:
            pass

    def update_command(self):
        database.update(select_row[0],self.title_entry.get(),self.author_entry.get(),self.year_entry.get(),self.isbn_entry.get())
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.view_command()

    def delete_command(self):
        database.delete(select_row[0])

    def __init__(self, window):
        
        self.window = window        

        self.window.wm_title('Book Inventory')

        l1 = Label(text='Title')
        l1.grid(row=0,column=0)

        self.title_entry=StringVar()
        self.e1 = Entry(window,textvariable=self.title_entry)
        self.e1.grid(row=0,column=1)

        l2 = Label(text='Author')
        l2.grid(row=0,column=2)

        self.author_entry=StringVar()
        self.e2 = Entry(window,textvariable=self.author_entry)
        self.e2.grid(row=0,column=3)

        l3 = Label(text='Year')
        l3.grid(row=1,column=0)

        self.year_entry=StringVar()
        self.e3 = Entry(window,textvariable=self.year_entry)
        self.e3.grid(row=1,column=1)

        l4 = Label(text='ISBN')
        l4.grid(row=1,column=2)

        self.isbn_entry=StringVar()
        self.e4 = Entry(window,textvariable=self.isbn_entry)
        self.e4.grid(row=1,column=3)

        self.lb1 = Listbox(window,justify='left', height=6, width=40)
        self.lb1.grid(row=3,column=0,rowspan=6, columnspan=2)
        self.lb1.bind('<<ListboxSelect>>', self.get_selected_row)
        sb1 = Scrollbar(window)
        sb1.grid(row=3,column=2,rowspan=6)
        self.lb1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.lb1.yview)

        b1 = Button(window, text='View All', width=20, command=self.view_command)
        b1.grid(row=2,column=3)

        b2 = Button(window, text='Search Entry', width=20, command=self.search_command)
        b2.grid(row=3,column=3)

        b3 = Button(window, text='Add Entry', width=20, command=self.insert_command)
        b3.grid(row=4,column=3)

        b4 = Button(window, text='Update Selected', width=20, command=self.update_command)
        b4.grid(row=5,column=3)

        b5 = Button(window, text='Delete Selected', width=20, command=self.delete_command)
        b5.grid(row=6,column=3)

        b6 = Button(window, text='Close Program', width=20, command=window.destroy)
        b6.grid(row=7,column=3)

window=Tk()
Window(window)
window.mainloop()