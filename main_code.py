import tkinter 
from tkinter import *
import math
global n,op
r=Tk()
r.geometry("700x700")
c=Canvas(r)
def equal1():
    global n,op
    y=t1.get()
    if(op=='+'):
        z=float(n)+float(y)
        t1.delete(0,END)               
        t1.insert(0,z)
    elif(op=='-'):
        z=float(n)-float(y)
        t1.delete(0,END)
        t1.insert(0,z)
    elif(op=='*'):
        z=float(n)*float(y) 
        t1.delete(0,END)
        t1.insert(0,z)
    elif(op=="/"):
        z=float(n)/float(y)
        t1.delete(0,END)
        t1.insert(0,z)      
    elif(op=='pow'):
        z=float(n)**float(y)
        t1.delete(0,END)
        t1.insert(0,z)
def operator(x):
    global n , op
    n=t1.get()
    op=x
    t1.delete(0,END)
def back1():
    y=t1.get()
    j=len(y)
    y=y[:j-1]
    t1.delete(0,END)
    t1.insert(0,y)
def clear1():
    t1.delete(0,END)
def point1():
    y=t1.get()
    if(y==""):
        t1.insert(0,"0.")
    else:
        j=y.find('.')
        if(j==-1):
            t1.delete(0,END)
            t1.insert(0,y+".")
def zero1():
    y=t1.get()
    if(y!=""):
        t1.delete(0,END)
        t1.insert(0,y+"0") 
def sq():
    y=float(t1.get())
    if (y>=0):
        s=math.sqrt(y)
        t1.delete(0,END)
        t1.insert(0,s) 
        

def number(x):
    y=t1.get()
    if(y==""):
        t1.insert(0,x)
    else:
        t1.delete(0,END)
        t1.insert(0,y+x)
t1=Entry(r)
t1.place(relx=0.1,rely=0.1,relwidth=.46,relheight=0.1)
b1=Button(r,text="1",command=lambda:number("1"))
b1.place(relx=0.1,rely=0.22,relwidth=0.1,relheight=0.1)
b2=Button(r,text="2",command=lambda:number("2"))
b2.place(relx=0.22,rely=0.22,relwidth=0.1,relheight=0.1)
b3=Button(r,text="3",command=lambda:number("3"))
b3.place(relx=0.34,rely=0.22,relwidth=0.1,relheight=0.1)
b4=Button(r,text='+',command=lambda:operator("+"))
b4.place(relx=0.46,rely=0.22,relwidth=0.1,relheight=0.1)
b5=Button(r,text="4",command=lambda:number("4"))
b5.place(relx=0.1,rely=0.34,relwidth=0.1,relheight=0.1)
b6=Button(r,text='5',command=lambda:number("5"))
b6.place(relx=0.22,rely=0.34,relwidth=0.1,relheight=0.1)
b7=Button(r,text='6',command=lambda:number("6"))
b7.place(relx=0.34,rely=0.34,relwidth=0.1,relheight=0.1)
b8=Button(r,text='-',command=lambda:operator("-"))
b8.place(relx=0.46,rely=0.34,relwidth=0.1,relheight=0.1)
b9=Button(r,text='7',command=lambda:number("7"))
b9.place(relx=0.1,rely=0.46,relwidth=0.1,relheight=0.1)
b10=Button(r,text='8',command=lambda:number("8"))
b10.place(relx=0.22,rely=0.46,relwidth=0.1,relheight=0.1)
b11=Button(r,text='9',command=lambda:number("9"))
b11.place(relx=0.34,rely=0.46,relwidth=0.1,relheight=0.1)
b12=Button(r,text='*',command=lambda:operator("*"))
b12.place(relx=0.46,rely=0.46,relwidth=0.1,relheight=0.1)
b13=Button(r,text='0',command=lambda:zero1())
b13.place(relx=0.1,rely=0.58,relwidth=0.1,relheight=0.1)
b14=Button(r,text='.',command=lambda:point1())
b14.place(relx=0.22,rely=0.58,relwidth=0.1,relheight=0.1)
b15=Button(r,text='=',command=lambda:equal1())
b15.place(relx=0.34,rely=0.58,relwidth=0.1,relheight=0.1)
b16=Button(r,text='/',command=lambda:operator("/"))
b16.place(relx=0.46,rely=0.58,relwidth=0.1,relheight=0.1)
b17=Button(r,text='c',bg='red',fg='black',command=lambda:clear1())
b17.place(relx=0.1,rely=0.70,relwidth=0.1,relheight=0.1)
b18=Button(r,text='B',bg='yellow',fg='black',command=lambda:back1())
b18.place(relx=0.22,rely=0.70,relwidth=0.1,relheight=0.1)
b19=Button(r,text='sq',bg="#f69",fg="black",command=lambda:sq())
b19.place(relx=0.34,rely=0.70,relwidth=0.1,relheight=0.1)
b20=Button(r,text='pow',bg="green",fg='black',command=lambda:operator("pow"))
b20.place(relx=0.46,rely=0.70,relwidth=0.1,relheight=0.1)

r.mainloop()
