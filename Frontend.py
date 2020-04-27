"""
A program that stores this book information:
Title,Author
Year,ISBN

User can:
View all records
Search an entry
Add Entry
Update Entry
Delete
Close
"""
from tkinter import *
import Backend

def view_command():
    list1.delete(0,END)
    for row in Backend.view():
        list1.insert(END,row)
def search_command():
    list1.delete(0,END)
    for row in Backend.search(titletext.get(),authortext.get(),yeartext.get(),ISBNtext.get()):
        list1.insert(END,row)
def add_command():
    Backend.insert(titletext.get(),authortext.get(),yeartext.get(),ISBNtext.get())
    list1.delete(0,END)
    list1.insert(END,(titletext.get(),authortext.get(),yeartext.get(),ISBNtext.get()))
def getselectedrow(event):
    global selectedtuple
    index=list1.curselection()[0]
    selectedtuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selectedtuple[1])
    e2.delete(0,END)
    e2.insert(END,selectedtuple[2])
    e3.delete(0,END)
    e3.insert(END,selectedtuple[3])
    e4.delete(0,END)
    e4.insert(END,selectedtuple[4])


def delete_command():
    Backend.delete(selectedtuple[0])

def update_command():
    Backend.update(selectedtuple[0],titletext.get(),authortext.get(),yeartext.get(),ISBNtext.get())

window=Tk()
window.wm_title("BookStore")
l1=Label(window,text='Title')
l1.grid(row=0,column=0)

l2=Label(window,text='Author')
l2.grid(row=0,column=2)

l3=Label(window,text='Year')
l3.grid(row=1,column=0)

l4=Label(window,text='ISBN')
l4.grid(row=1,column=2)

titletext=StringVar()
e1=Entry(window,textvariable=titletext)
e1.grid(row=0,column=1)

authortext=StringVar()
e2=Entry(window,textvariable=authortext)
e2.grid(row=0,column=3)

yeartext=StringVar()
e3=Entry(window,textvariable=yeartext)
e3.grid(row=1,column=1)

ISBNtext=StringVar()
e4=Entry(window,textvariable=ISBNtext)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>',getselectedrow)



b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=3)
b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)
b4=Button(window,text="Update",width=12,command=update_command)
b4.grid(row=5,column=3)
b5=Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=6,column=3)
b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)


window.mainloop()
