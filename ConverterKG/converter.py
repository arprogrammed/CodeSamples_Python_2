from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

window = Tk(className=' Kilo Converter ')

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

def conv():
    kg2gr=float(e1_value.get())*1000
    t1.insert(END,kg2gr)
    kg2lb=float(e1_value.get())*2.20462
    t2.insert(END,kg2lb)
    kg2oz=float(e1_value.get())*35.274
    t3.insert(END,kg2oz)

l1 = Label(text='Enter Amount of Kilograms')
l1.grid(row=0,column=0)

e1_value=StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

b1 = Button(window, text = 'Convert',command=conv)
b1.grid(row=0,column=2)

br1 = Label(text='')
br1.grid(row=1,column=0,columnspan=3)

l2 = Label(text='Conversions Below')
l2.grid(row=2,column=0,columnspan=3)

lc1 = Label(text='Grams')
lc1.grid(row=3,column=0)
t1 = Text(window,height=1,width=20)
t1.grid(row=4,column=0)

lc2 = Label(text='Pounds')
lc2.grid(row=3,column=1)
t2 = Text(window,height=1,width=20)
t2.grid(row=4,column=1)

lc1 = Label(text='Ounces')
lc1.grid(row=3,column=2)
t3 = Text(window,height=1,width=20)
t3.grid(row=4,column=2)

window.mainloop()