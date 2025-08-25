#calculator using tkinter
from tkinter import *

window =Tk()
window.geometry('500x500')
window.title('CALCULATOR')

#entry box
e = Entry(window,width=40,borderwidth=10)
e.place(x=0,y=0)

#buttons
def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0, str(result) + str(num))

b= Button(window, text='1', width=10, command= lambda :click(1) ,bg ='sky blue',fg='white', font=('bold',12), activebackground='black',activeforeground='white')
b.place(x=5,y=50)
b= Button(window, text='2', width=10, command= lambda :click(2),bg ='sky blue',fg='white', font=('bold',12), activebackground='black',activeforeground='white')
b.place(x=80,y=50)
b= Button(window, text='3', width=10, command= lambda :click(3),bg ='sky blue',fg='white', font=('bold',12), activebackground='black',activeforeground='white')
b.place(x=155,y=50)
b= Button(window, text='4', width=10, command= lambda :click(4),bg ='sky blue',fg='white', font=('bold',12), activebackground='black',activeforeground='white')
b.place(x=5,y=100)
b= Button(window, text='5', width=10, command= lambda :click(5),bg ='sky blue',fg='white', font=('bold',12), activebackground='black',activeforeground='white')
b.place(x=80,y=100)
b= Button(window, text='6', width=10, command= lambda :click(6),bg ='sky blue',fg='white', font=('bold',12), activebackground='black',activeforeground='white')
b.place(x=155,y=100)
b= Button(window, text='7', width=10, command= lambda :click(7),bg ='sky blue',fg='white', font=('bold',12), activebackground='black',activeforeground='white')
b.place(x=5,y=150)
b= Button(window, text='8', width=10, command= lambda :click(8),bg ='sky blue',fg='white', font=('bold',12), activebackground='black',activeforeground='white')
b.place(x=80,y=150)
b= Button(window, text='9', width=10, command= lambda :click(9),bg ='sky blue',fg='white', font=('bold',12), activebackground='black',activeforeground='white')
b.place(x=155,y=150)
b= Button(window, text='0', width=10, command= lambda :click(0),bg ='sky blue',fg='white', font=('bold',12), activebackground='black',activeforeground='white')
b.place(x=5,y=200)

#operators
def add():
    n1 = e.get()
    global math
    math = 'addition'
    global i
    i = int(n1)
    e.delete(0,END)

def sub():
    n1 = e.get()
    global math
    math ='subtraction'
    global i
    i = int(n1)
    e.delete(0,END)

def mul():
    n1 = e.get()
    global math
    math ='multiplication'
    global i
    i = int(n1)
    e.delete(0,END)

def div():
    n1 = e.get()
    global  math
    math ='division'
    global i
    i = int(n1)
    e.delete(0,END)

b= Button(window, text='+', width=10, command=add,bg ='brown',fg='white', font=('bold',12), activebackground='black',activeforeground='white')
b.place(x=80,y=200)
b= Button(window, text='-', width=10,command=sub,bg ='brown',fg='white', font=('bold',12), activebackground='black',activeforeground='white')
b.place(x=155,y=200)
b= Button(window, text='*', width=10, command=mul,bg ='brown',fg='white', font=('bold',12), activebackground='black',activeforeground='white')
b.place(x=5,y=250)
b= Button(window, text='/', width=10,command=div,bg ='brown',fg='white', font=('bold',12), activebackground='black',activeforeground='white')
b.place(x=80,y=250)

def equal():
    n2 = e.get()
    e.delete(0,END)
    if math =='addition':
        e.insert(0, i + int(n2))
    elif math =='subtraction':
        e.insert(0, i-int(n2))
    elif math =='multiplication':
        e.insert(0, i * int(n2))
    elif math == ' division':
        e.insert(0,i * int(n2))


b= Button(window, text='=', width=10,command=equal,bg ='white',fg='black', font=('bold',12), activebackground='black',activeforeground='white')
b.place(x=155,y=250)

def clear():
    e.delete(0,END)
b= Button(window, text='Clear', width=10, command=clear,bg ='white',fg='black', font=('bold',12), activebackground='black',activeforeground='white')
b.place(x=5,y=300)


mainloop()