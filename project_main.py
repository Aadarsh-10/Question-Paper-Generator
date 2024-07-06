# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:54:33 2021

@author: Jijin
"""

ent1=0
ent2=0
ent3=0
ent4=0
ent5=0
ent6=0
ent7=0
ent8=0
ent9=0
ent10=0
ent11=0
ent12=0
ent13=0
ent14=0
ent15=0
ent16=0
ent17=0
ent18=0
ent19=0
ent20=0

import tkinter as tk
from PIL import ImageTk, Image
from fpdf import FPDF
import os

def change(*args):
    print('hurray')
# win2=''
# win3=''
# win4=''
# win5=''
# win6=''
# win7=''
# win8=''
# win9=''
# win10=''
# win11=''
# win12=''
#definitions
import mysql.connector as sc

def classes():
    a='create table userclasses(Sno integer primary key,class integer(2) NOT NULL,subject varchar(20) NOT NULL)'
    cur.execute(a)

def createdatabase():
    cur.execute('create database AVA')

def logintable():
    
    a='create table logintable(userID integer primary key,user_name varchar(30) NOT NULL,password varchar(30) NOT NULL)'
    cur.execute(a) 
    
def cd():
    con_obj=sc.connect(host='localhost',user='root',passwd='mysql')
    cur=con_obj.cursor()
    query='drop database if exists ava'
    cur.execute(query)
    cur.execute('create database AVA')
try:
    con_obj=sc.connect(host='localhost',user='root',passwd='mysql',database="AVA")
    cur=con_obj.cursor()
except:
    cd()
    con_obj=sc.connect(host='localhost',user='root',passwd='mysql',database="AVA")
    cur=con_obj.cursor()  
    logintable()
    classes()
    cur=con_obj.cursor()
# con_obj=sc.connect(host='localhost',user='root',passwd='',database="AVA")
    
if con_obj.is_connected:
    print('successful connection')
    


def create_sub_table(a,b):
    c=str(a)+b
    a='create table '+c+'_questions(sno integer primary key,CH_NAME varchar(50),QUESTION varchar(500),ANSWER varchar(10000),MARK integer,LEVEL varchar(15),YEAR integer )'
    cur.execute(a)
    create_obj_table(d,e)
def create_obj_table(a,b):
    c=str(a)+b
    a='create table '+c+'obj_questions(sno integer primary key,CH_NAME varchar(50),QUESTION varchar(500),OPTION_1 varchar(100),OPTION_2 varchar(100),OPTION_3 varchar(100),OPTION_4 varchar(100),ANSWER varchar(10000),CORRECT_OPT varchar(1),LEVEL varchar(15),YEAR integer)'
    cur.execute(a)
    select_class(2)
def add_new_class():
    global ent1,ent2,win1
    win1=tk.Tk()
    win1.title('SELECT CLASS WINDOW')
    win1.geometry("1920x1080")  
    win1.configure(background='white')
    win7.destroy()
    frame=tk.Frame(win1,relief= tk.RAISED,bg='#c2e4ff')
    frame.place(relx=0.1,rely=0.1,relwidth=0.80,relheight=0.8)
    label1=tk.Label(win1,text="ADD CLASS",bg='#0069a3',fg='white',font=('ariel',20))
    label1.place(relx=0.25,rely=0.1,relwidth=0.50,relheight=0.1)
    label1=tk.Label(frame,text="ENTER THE CLASS",bg='#0069a3',fg='white',font=('ariel',20))
    label1.place(relx=0.1,rely=0.4,relwidth=0.30,relheight=0.1)
    label2=tk.Label(frame,text="ENTER THE SUBJECT",bg='#0069a3',fg='white',font=('ariel',20))
    label2.place(relx=0.1,rely=0.55,relwidth=0.30,relheight=0.1)
    ent1=tk.Entry(frame,width=15,borderwidth=5,font=('Calculator',27,'bold'),bg='#e0f4ff',fg='black')
    ent1.place(relx=0.4,rely=0.4,relwidth=0.50,relheight=0.1)
    ent2=tk.Entry(frame,width=15,borderwidth=5,font=('Calculator',27,'bold'),bg='#e0f4ff',fg='black')
    ent2.place(relx=0.4,rely=0.55,relwidth=0.50,relheight=0.1)
    but_equal=tk.Button(frame,text='SUBMIT',padx=134,pady=12,fg='black',bg='#66ff99',font=('ariel',10),command=enter_new_class)
    but_equal.place(relx=0.6,rely=0.8,relwidth=0.30,relheight=0.08)
    but4=tk.Button(frame,text='BACK',font=('ariel',15),height=3,width=15,bg='#ff4d4d',command=lambda :select_class(2),relief= tk.RIDGE)
    but4.place(relx=0.1,rely=0.8,relwidth=0.30,relheight=0.08)
    

    
def enter_new_class():
    global d,e
    z="select count(*) from userclasses"
    cur.execute(z)
    y=cur.fetchall()
    global d,e
    d=ent1.get()
    e=ent2.get()
    query="insert into userclasses(Sno,class,subject) values(%s,%s,%s)"
    data=(y[0][0]+1,d,e.lower())
    try:
        cur.execute(query,data)
        con_obj.commit()
    except:
        con_obj.rollback()
    create_sub_table(d,e)
 


# logintable()
def add_to_login():
    global ent1,ent2,ent3,win3
    a=ent1.get()
    b=ent2.get()
    c=ent3.get()
    query="insert into logintable(userID,user_name,password) values(%s,%s,%s)"
    data=(a,b,c)
    try:
        cur.execute(query,data)
        con_obj.commit()
    except:
        con_obj.rollback()
    startingwindow('win3')
    
def options_window(n):
    global but1,but2,win4
    if n==20:
        win20.destroy()
    elif n==30:
        win5.destroy()
    elif n==40:
        win12.destroy()
    elif n==2:
        win10.destroy()
    elif n==4:
        win8.destroy()
    elif n==5:
        win100.destroy()
    win4=tk.Tk()
    win4.title('option window')
    win4.geometry("1920x1080")  
    win4.configure(background='white')
    frame=tk.Frame(win4,relief= tk.RAISED,height=100,width=150,bg='#c2e4ff')
    frame.place(relx=0.0,rely=0.0,relwidth=0.10,relheight=1)
    frame=tk.Frame(win4,relief= tk.RAISED,height=100,width=150,bg='#c2e4ff')
    frame.place(relx=0.9,rely=0.0,relwidth=0.10,relheight=1)
    frame=tk.Frame(win4,relief= tk.RAISED,height=100,width=150,bg='#d9eeff')
    frame.place(relx=0.05,rely=0.0,relwidth=0.06,relheight=1)
    frame=tk.Frame(win4,relief= tk.RAISED,height=100,width=150,bg='#d9eeff')
    frame.place(relx=0.89,rely=0.0,relwidth=0.06,relheight=1)
    frame=tk.Frame(win4,relief= tk.RAISED,height=100,width=150,bg='#ffffff')
    frame.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.6)
    frame=tk.Frame(win4,relief= tk.RAISED,bg='#ffffff')
    frame.place(relx=0.3,rely=0.2,relwidth=0.4,relheight=0.1)
    frame2=tk.Frame(win4,relief= tk.RAISED,bg='#ffffff')
    frame2.place(relx=0.2,rely=0.4,relwidth=0.6,relheight=0.4)
    label=tk.Label(frame,text="Menu",bg='#00059e',fg='white',font=('ariel',20))
    label.place(relx=0,rely=0,relwidth=1,relheight=1)

    but3=tk.Button(frame2,text='INSERT QUESTION',font=('ariel',15),bg="#ceff99",command=lambda :window8(3),relief= tk.RIDGE)
    but3.place(relx=0,rely=0,relwidth=1,relheight=0.2)
    but1=tk.Button(frame2,text='SEARCH QUESTION',font=('ariel',15),height=3,width=25,bg="#ceff99",command=lambda : window9(3),relief= tk.RIDGE)
    but1.place(relx=0,rely=0.25,relwidth=1,relheight=0.2)
    but2=tk.Button(frame2,text='CREATE TEST PAPER',font=('ariel',15),height=3,width=25,bg='#ceff99',command=lambda :create_test_paper(1),relief= tk.RIDGE)
    but2.place(relx=0,rely=0.50,relwidth=1,relheight=0.2)
    but4=tk.Button(frame2,text='BACK',font=('ariel',15),height=3,width=15,bg='#ff4d4d',command=lambda :select_class(4),relief= tk.RIDGE)
    but4.place(relx=0.25,rely=0.85,relwidth=0.5,relheight=0.15)
    backbut=tk.Button(win4,text='LOG OUT',font=('ariel',15),bg='#aa00e3',fg='black',command=lambda: startingwindow('win4'))
    backbut.place(relx=0.9,rely=0.01,relwidth=0.09,relheight=0.05)
    win4.mainloop()

def window9(n):
    global win10
    win10=tk.Tk()
    win10.title('SELECT CLASS WINDOW')
    win10.geometry("1920x1080")  
    win10.configure(background='#b8e6ff')
    
    frame=tk.Frame(win10,relief= tk.RAISED,bg='white')
    frame.place(relx=0.15,rely=0.15,relwidth=0.70,relheight=0.7)
    frame=tk.Frame(win10,relief= tk.RAISED)
    frame.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.1)
    frame2=tk.Frame(win10,relief= tk.RAISED,bg='white')
    frame2.place(relx=0.25,rely=0.4,relwidth=0.50,relheight=0.3)
    label1=tk.Label(frame,text='WHAT TYPE OF QUESTION DO YOU LIKE TO SEARCH',font=('Times New Roman',20),relief= tk.RAISED,bg='#abf7cc')
    label1.place(relx=0,rely=0,relwidth=1,relheight=1)
    but1=tk.Button(frame2,text='SUBJECTIVE',font=('ariel',15),bg="#ffebb3",command=lambda :search_question_sub(Class, subject),relief= tk.RIDGE)
    but1.place(relx=0,rely=0,relwidth=1,relheight=0.25)
    but2=tk.Button(frame2,text='OBJECTIVE',font=('ariel',15),bg="#ffebb3",command=lambda :search_question_obj(Class,subject) ,relief= tk.RIDGE)
    but2.place(relx=0,rely=0.40,relwidth=1,relheight=0.25)
    but3=tk.Button(frame2,text='BACK',font=('ariel',15),bg="#ff4d4d",command=lambda : options_window(2),relief= tk.RIDGE)
    but3.place(relx=0.25,rely=0.80,relwidth=0.5,relheight=0.15)
    if n==1:
        win5.destroy()
    elif n==2:
        win6.destroy()
    elif n==3:
        win4.destroy()
    elif n==4:
        win100.destroy()
    elif n==200:
        win200.destroy()

def window8(n):
    global win10
    win10=tk.Tk()
    win10.title('SELECT CLASS WINDOW')
    win10.geometry("1920x1080")  
    win10.configure(background='#b8e6ff')
    frame=tk.Frame(win10,relief= tk.RAISED,bg='white')
    frame.place(relx=0.15,rely=0.15,relwidth=0.70,relheight=0.7)
    frame=tk.Frame(win10,relief= tk.RAISED,bg='#1c99ff')
    frame.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.1)
    frame2=tk.Frame(win10,relief= tk.RAISED,bg='white')
    frame2.place(relx=0.25,rely=0.4,relwidth=0.50,relheight=0.3)
    label1=tk.Label(frame,text='WHAT TYPE OF QUESTION DO YOU LIKE TO INSERT',font=('Times New Roman',20),relief= tk.RAISED,bg='#abf7cc')
    label1.place(relx=0,rely=0,relwidth=1,relheight=1)
    but1=tk.Button(frame2,text='SUBJECTIVE',font=('ariel',15),bg="#ffebb3",command=insert_question,relief= tk.RIDGE)
    but1.place(relx=0,rely=0,relwidth=1,relheight=0.25)
    but2=tk.Button(frame2,text='OBJECTIVE',font=('ariel',15),bg="#ffebb3",command=insert_obj,relief= tk.RIDGE)
    but2.place(relx=0,rely=0.40,relwidth=1,relheight=0.25)
    but3=tk.Button(frame2,text='BACK',font=('ariel',15),bg="#ff4d4d",command=lambda : options_window(2),relief= tk.RIDGE)
    but3.place(relx=0.25,rely=0.80,relwidth=0.5,relheight=0.15)
    if n==1:
        win5.destroy()
    elif n==2:
        win12.destroy()
    elif n==3:
        win4.destroy()
    
        


def insert_question():
    global frame2,win5,ent1,ent2,ent3,ent4,ent5,ent6,LEVEL,L
    win5=tk.Tk()
    win5.title('INSERT QUESTION')
    win5.geometry("1920x1080")
    win5.configure(background='white')
    lable=tk.Label(win5,text='INSERT QUESTION',font=('Calculator',27,'bold'),bg='#2ab3b5',fg='white')
    lable.place(relx=0.35,rely=0.03,relwidth=0.30,relheight=0.08)
    frame2=tk.Frame(win5,relief= tk.RAISED)
    frame2.place(relx=0.1,rely=0.15,relwidth=0.8,relheight=0.8)
    lable1=tk.Label(frame2,text='ENTER THE Ch_NAME')
    query='select distinct CH_NAME from '+Class+subject+'_questions'
    cur.execute(query)
    result=cur.fetchall()
    op2=['ALL CHAPTERS']
    for i in result:
        op2.append(str(i[0]))
    L=tk.StringVar(win5)
    L.set(op2[0])
    L.trace("w",change)
    drop=tk.OptionMenu(frame2,L,*op2)
    drop.config(width = 20)
    drop.place(relx=0.8,rely=0.1,relwidth=0.20,relheight=0.08)
    lable1.place(relx=0,rely=0.1,relwidth=0.30,relheight=0.08)
    lable2=tk.Label(frame2,text='ENTER THE QUESTION')
    lable2.place(relx=0,rely=0.2,relwidth=0.30,relheight=0.08)
    lable3=tk.Label(frame2,text='ENTER THE ANSWER')
    lable3.place(relx=0,rely=0.3,relwidth=0.30,relheight=0.08)
    lable4=tk.Label(frame2,text='ENTER THE MARK')
    lable4.place(relx=0,rely=0.4,relwidth=0.30,relheight=0.08)
    lable5=tk.Label(frame2,text='ENTER THE LEVEL')
    lable5.place(relx=0,rely=0.5,relwidth=0.30,relheight=0.08)
    lable6=tk.Label(frame2,text='ENTER THE YEAR')
    lable6.place(relx=0,rely=0.6,relwidth=0.30,relheight=0.08)
    ent1=tk.Entry(frame2,width=15,borderwidth=5,font=('Calculator',27,'bold'),bg='#2ab3b5',fg='white')
    ent1.place(relx=0.3,rely=0.1,relwidth=0.50,relheight=0.08)
    ent2=tk.Entry(frame2,width=15,borderwidth=5,font=('Calculator',27,'bold'),bg='#2ab3b5',fg='white')            
    ent2.place(relx=0.3,rely=0.2,relwidth=0.70,relheight=0.08)
    ent3=tk.Entry(frame2,width=15,borderwidth=5,font=('Calculator',27,'bold'),bg='#2ab3b5',fg='white')
    ent3.place(relx=0.3,rely=0.3,relwidth=0.70,relheight=0.08)
    ent4=tk.Entry(frame2,width=15,borderwidth=5,font=('Calculator',27,'bold'),bg='#2ab3b5',fg='white')            
    ent4.place(relx=0.3,rely=0.4,relwidth=0.70,relheight=0.08)
    op=['EASY','MEDIUM','HARD','HOTS']
    LEVEL=tk.StringVar(win5)
    LEVEL.set(op[0])
    LEVEL.trace("w",change)
    drop1=tk.OptionMenu(frame2,LEVEL,*op)
    drop1.config(width = 20)
    drop1.place(relx=0.3,rely=0.5,relwidth=0.70,relheight=0.08)
    ent6=tk.Entry(frame2,width=15,borderwidth=5,font=('Calculator',27,'bold'),bg='#2ab3b5',fg='white')            
    ent6.place(relx=0.3,rely=0.6,relwidth=0.70,relheight=0.08)
    but_equal=tk.Button(frame2,text='SUBMIT',padx=134,pady=12,fg='black',bg='#66ff99',font=('ariel',10),command=lambda: add_questions(Class,subject))
    but_equal.place(relx=0.55,rely=0.8,relwidth=0.40,relheight=0.07)
    but2=tk.Button(frame2,text='BACK',font=('ariel',15),height=3,width=15,bg="#ff4d4d",command=lambda :window8(1),relief= tk.RIDGE)
    but2.place(relx=0.05,rely=0.8,relwidth=0.40,relheight=0.07)

    win10.destroy()


def insert_obj():
    global win12,ent1,ent2,ent3,ent4,ent5,ent6,OPT,ent7,ent8,LEVEL
    win12=tk.Tk()
    win12.title('Objective question ')
    win12.geometry("1920x1080")
    lable=tk.Label(win12,text='INSERT QUESTION',font=('Calculator',27,'bold'),bg='#2ab3b5',fg='white')
    lable.place(relx=0.35,rely=0.05,relwidth=0.30,relheight=0.08)
    frame2=tk.Frame(win12,relief= tk.RAISED)

    frame2.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.7)

    query='select distinct CH_NAME from '+Class+subject+'_questions'
    cur.execute(query)
    result=cur.fetchall()
    op2=['ALL CHAPTERS']
    for i in result:
        op2.append(str(i[0]))
    L=tk.StringVar(frame2)
    L.set(op2[0])
    L.trace("w",change)
    drop=tk.OptionMenu(frame2,L,*op2)
    drop.config(width = 20)
    drop.place(relx=0.8,rely=0.0,relwidth=0.20,relheight=0.08)
    lable=tk.Label(frame2,text='ENTER THE CH_NAME')
    lable.place(relx=0.0,rely=0,relwidth=0.30,relheight=0.08)
    lable=tk.Label(frame2,text='ENTER THE QUESTION')
    lable.place(relx=0.0,rely=0.1,relwidth=0.30,relheight=0.08)
    lable0=tk.Label(frame2,text='ENTER THE OPTIONS')
    lable0.place(relx=0.4,rely=0.2,relwidth=0.30,relheight=0.08)
    lable1=tk.Label(frame2,text='A',bg='cyan')
    lable1.place(relx=0.05,rely=0.3,relwidth=0.05,relheight=0.08)
    lable2=tk.Label(frame2,text='B',bg='cyan')
    lable2.place(relx=0.55,rely=0.3,relwidth=0.05,relheight=0.08)
    lable3=tk.Label(frame2,text='C',bg='cyan')
    lable3.place(relx=0.05,rely=0.4,relwidth=0.05,relheight=0.08)
    lable4=tk.Label(frame2,text='D',bg='cyan')
    lable4.place(relx=0.55,rely=0.4,relwidth=0.05,relheight=0.08)
    lable5=tk.Label(frame2,text='ENTER THE ANSWER')
    lable5.place(relx=0.0,rely=0.5,relwidth=0.30,relheight=0.08)
    lable7=tk.Label(frame2,text='ENTER THE YEAR')
    lable7.place(relx=0.0,rely=0.6,relwidth=0.30,relheight=0.08)
    lable7=tk.Label(frame2,text='ENTER THE LEVEL')
    lable7.place(relx=0.0,rely=0.7,relwidth=0.30,relheight=0.08)
    op=['EASY','MEDIUM','HARD','HOTS']
    LEVEL=tk.StringVar(win12)
    LEVEL.set(op[0])
    LEVEL.trace("w",change)
    drop1=tk.OptionMenu(frame2,LEVEL,*op)
    drop1.config(width = 20)
    drop1.place(relx=0.3,rely=0.7,relwidth=0.30,relheight=0.08)
    op=['A','B','C','D']
    OPT=tk.StringVar(win12)
    OPT.set(op[0])
    OPT.trace("w",change)
    drop1=tk.OptionMenu(frame2,OPT,*op)
    drop1.config(width = 20)
    drop1.place(relx=0.8,rely=0.5,relwidth=0.2,relheight=0.08)
    ent7=tk.Entry(frame2,width=10,borderwidth=5,font=('Calculator',27,'bold'),bg='#2ab3b5',fg='white')
    ent7.place(relx=0.3,rely=0.1,relwidth=0.70,relheight=0.08)
    ent1=tk.Entry(frame2,width=10,borderwidth=5,font=('Calculator',27,'bold'),bg='#2ab3b5',fg='white')
    ent1.place(relx=0.3,rely=0,relwidth=0.50,relheight=0.08)
    ent2=tk.Entry(frame2,width=5,borderwidth=5,font=('Calculator',27,'bold'),bg='#2ab3b5',fg='white')            
    ent2.place(relx=0.1,rely=0.3,relwidth=0.40,relheight=0.08)
    ent3=tk.Entry(frame2,width=5,borderwidth=5,font=('Calculator',27,'bold'),bg='#2ab3b5',fg='white')            
    ent3.place(relx=0.6,rely=0.3,relwidth=0.40,relheight=0.08)
    ent4=tk.Entry(frame2,width=5,borderwidth=5,font=('Calculator',27,'bold'),bg='#2ab3b5',fg='white')            
    ent4.place(relx=0.1,rely=0.4,relwidth=0.40,relheight=0.08)
    ent5=tk.Entry(frame2,width=5,borderwidth=5,font=('Calculator',27,'bold'),bg='#2ab3b5',fg='white')            
    ent5.place(relx=0.6,rely=0.4,relwidth=0.40,relheight=0.08)
    ent6=tk.Entry(frame2,width=20,borderwidth=5,font=('Calculator',27,'bold'),bg='#2ab3b5',fg='white')
    ent6.place(relx=0.3,rely=0.5,relwidth=0.50,relheight=0.08)
    ent8=tk.Entry(frame2,width=20,borderwidth=5,font=('Calculator',27,'bold'),bg='#2ab3b5',fg='white')
    ent8.place(relx=0.3,rely=0.6,relwidth=0.50,relheight=0.08)

    but_equal1=tk.Button(frame2,text='submit',padx=134,pady=12,fg='black',bg='#66ff99',font=('ariel',10),command=lambda :add_questions_obj(Class,subject))
    but_equal1.place(relx=0.65,rely=0.9,relwidth=0.30,relheight=0.08)
    but_equal2=tk.Button(frame2,text='back',padx=134,pady=12,fg='black',bg='#ff4d4d',font=('ariel',10),command=lambda :window8(2))
    but_equal2.place(relx=0.05,rely=0.9,relwidth=0.30,relheight=0.08)

    win10.destroy()
def search_question_sub(d,e):
    global level,level1,level2,level3,ent1
    global win6
    win6=tk.Tk()
    win6.title('SEARCH QUESTION')
    win6.geometry("1920x1080")  
    win6.configure(background='white')
    win10.destroy()
    lable20=tk.Label(win6,text='SEARCH QUESTION',font=('ariel',15))
    lable20.place(relx=0.4,rely=0.1,relwidth=0.20,relheight=0.05)

    lable21=tk.Label(win6,text='SELECT THE LEVEL',bg='#b3e0ff')
    lable21.place(relx=0.25,rely=0.3,relwidth=0.20,relheight=0.05)
    lable22=tk.Label(win6,text='SELECT THE CHAPTER',bg='#b3e0ff')
    lable22.place(relx=0.55,rely=0.3,relwidth=0.20,relheight=0.05)
    lable23=tk.Label(win6,text='SELECT THE MARK',bg='#b3e0ff')
    lable23.place(relx=0.25,rely=0.5,relwidth=0.20,relheight=0.05)
    lable24=tk.Label(win6,text='SELECT THE YEAR',bg='#b3e0ff')
    lable24.place(relx=0.55,rely=0.5,relwidth=0.20,relheight=0.05)
    # query='select QUESTION from
    op1=['EASY','MEDIUM','HARD','HOTS']
    query='select distinct CH_NAME from '+Class+subject+'_questions'
    cur.execute(query)
    result=cur.fetchall()
    op2=['ALL CHAPTERS']
    for i in result: 
        op2.append(str(i[0]))
    query='select distinct mark from '+Class+subject+'_questions'
    cur.execute(query)
    result2=cur.fetchall()
    op3=['ALL MARKS']
    for i in result2:
        op3.append(str(i[0]))
    query='select distinct YEAR from '+Class+subject+'_questions'
    cur.execute(query)
    result1=cur.fetchall()
    op4=['ALL YEARS']
    for i in result1:
        op4.append(str(i[0]))
    level=tk.StringVar(win6)
    level.set(op1[0])
    level.trace("w",change)
    drop1=tk.OptionMenu(win6,level,*op1)
    drop1.config(width = 20)
    drop1.place(relx=0.25,rely=0.35,relwidth=0.20,relheight=0.05)
    level1=tk.StringVar(win6)
    level1.set(op2[0])
    level1.trace("w",change)
    drop2=tk.OptionMenu(win6,level1,*op2)
    drop2.config(width = 20)
    drop2.place(relx=0.55,rely=0.35,relwidth=0.20,relheight=0.05)
    level2=tk.StringVar(win6)
    level2.set(op3[0])
    level2.trace("w",change)
    drop3=tk.OptionMenu(win6,level2,*op3)
    drop3.config(width = 20)
    drop3.place(relx=0.25,rely=0.55,relwidth=0.20,relheight=0.05)
    level3=tk.StringVar(win6)
    level3.set(op4[0])
    level3.trace("w",change)
    drop4=tk.OptionMenu(win6,level3,*op4)
    drop4.config(width = 20)
    drop4.place(relx=0.55,rely=0.55,relwidth=0.20,relheight=0.05)    
    but_equal1=tk.Button(win6,text='submit',padx=134,pady=12,fg='black',bg='#66ff99',font=('ariel',10),command=searchcheck1)
    but_equal1.place(relx=0.525,rely=0.8,relwidth=0.20,relheight=0.05)
    but_equal1=tk.Button(win6,text='ALL QUESTIONS',padx=134,pady=12,fg='black',bg='#f0654f',font=('ariel',10),command=allquestions_sub)
    but_equal1.place(relx=0.4,rely=0.9,relwidth=0.20,relheight=0.05)
    but_equal2=tk.Button(win6,text='BACK',padx=134,pady=12,fg='black',bg='#ff4d4d',font=('ariel',10),command=lambda : window9(2))
    but_equal2.place(relx=0.275,rely=0.8,relwidth=0.20,relheight=0.05)

def searching():
    global lst_ques
    lst_ques=[]
    ch=level1.get()
    mk=level2.get()
    y=level3.get()

    # win6.destroy()
    if y=='ALL YEARS':
        query='select question from '+Class+subject+'_questions where MARK='+str(mk)+' and ch_name="'+ch+'"'
    else:
        query='select question from '+Class+subject+'_questions where MARK='+str(mk)+' and YEAR='+str(y)+' and ch_name="'+ch+'"'
        print('shit')
    cur.execute(query)
    L=cur.fetchall()
    for i in L:
        lst_ques.append(i[0])
    print(lst_ques)
    scroll(1)
    # if level1.get()=='ALL CHAPTERS':
    #     if level2,get()=='ALL MARKS'
    #     if level3.get()=='ALL YEARS':
    # if level2,get()=='ALL MARKS':
    #     if level3.get()=='ALL YEARS':
    # if level3.get()=='ALL YEARS':
    #     if level2,get()=='ALL MARKS'
    # if ent1.get()=='':
def search_question_obj(d,e):
    global win6,level,level1,level3,ent1
    win6=tk.Tk()
    win6.title('SEARCH QUESTION OBJECTIVE')
    win6.geometry("1920x1080")  
    win6.configure(background='white')
    win10.destroy()
    
    lable20=tk.Label(win6,text='SEARCH QUESTION',font=('ariel',15))
    lable20.place(relx=0.4,rely=0.1,relwidth=0.20,relheight=0.05)

    lable21=tk.Label(win6,text='SELECT THE LEVEL',bg='#b3e0ff')
    lable21.place(relx=0.25,rely=0.3,relwidth=0.20,relheight=0.05)
    lable22=tk.Label(win6,text='SELECT THE CHAPTER',bg='#b3e0ff')
    lable22.place(relx=0.55,rely=0.3,relwidth=0.20,relheight=0.05)

    lable24=tk.Label(win6,text='SELECT THE YEAR',bg='#b3e0ff')
    lable24.place(relx=0.4,rely=0.5,relwidth=0.20,relheight=0.05)


    op1=['EASY','MEDIUM','HARD','HOTS']
    query='select distinct CH_NAME from '+Class+subject+'obj_questions'
    cur.execute(query)
    result=cur.fetchall()
    op2=['ALL CHAPTERS']
    for i in result:
        op2.append(str(i[0]))

    query='select distinct YEAR from '+Class+subject+'obj_questions'
    cur.execute(query)
    result1=cur.fetchall()
    op4=['ALL YEARS']
    for i in result1:
        op4.append(str(i[0]))
    level=tk.StringVar(win6)
    level.set(op1[0])
    level.trace("w",change)
    drop1=tk.OptionMenu(win6,level,*op1)
    drop1.config(width = 20)
    drop1.place(relx=0.25,rely=0.35,relwidth=0.20,relheight=0.05)
    level1=tk.StringVar(win6)
    level1.set(op2[0])
    level1.trace("w",change)
    drop2=tk.OptionMenu(win6,level1,*op2)
    drop2.config(width = 20)
    drop2.place(relx=0.55,rely=0.35,relwidth=0.20,relheight=0.05)
    # level2=tk.StringVar(win6)
    # level2.set(op3[0])
    # level2.trace("w",change)
    # drop3=tk.OptionMenu(win6,level2,*op3)
    # drop3.config(width = 20)
    # drop3.place(relx=0.275,rely=0.675,relwidth=0.20,relheight=0.05)
    level3=tk.StringVar(win6)
    level3.set(op4[0])
    level3.trace("w",change)
    drop4=tk.OptionMenu(win6,level3,*op4)
    drop4.config(width = 20)
    drop4.place(relx=0.4,rely=0.55,relwidth=0.20,relheight=0.05)    
    but_equal1=tk.Button(win6,text='submit',padx=134,pady=12,fg='black',bg='#f0654f',font=('ariel',10),command=searchcheck)
    but_equal1.place(relx=0.525,rely=0.8,relwidth=0.20,relheight=0.05)
    but_equal1=tk.Button(win6,text='ALL QUESTIONS',padx=134,pady=12,fg='black',bg='#f0654f',font=('ariel',10),command=allquestions_obj)
    but_equal1.place(relx=0.4,rely=0.9,relwidth=0.20,relheight=0.05)
    but_equal2=tk.Button(win6,text='BACK',padx=134,pady=12,fg='black',bg='#ff4d4d',font=('ariel',10),command=lambda : window9(2))
    but_equal2.place(relx=0.275,rely=0.8,relwidth=0.20,relheight=0.05)
 
def allquestions_sub():
    global lst_ques
    lst_ques=[]
    query='select question from '+Class+subject+'_questions'
    cur.execute(query)
    L=cur.fetchall()
    for i in L:
        lst_ques.append(i[0])
    scroll(1)
def allquestions_obj():
    global lst_ques
    lst_ques=[]
    query='select question from '+Class+subject+'obj_questions'
    cur.execute(query)
    L=cur.fetchall()
    for i in L:
        lst_ques.append(i[0])
    scroll_obj(1)
    # z='select distinct(MARK) from '+str(Class.get())+str(subject.get())+'_questions;'
    # P=cur.execute(z)
    # print(P)
def searching2():
    global lst_ques
    lst_ques=[]
    ch=level1.get()
    y=level3.get()

    # win6.destroy()
    if y=='ALL YEARS':
        query='select question from '+Class+subject+'obj_questions where ch_name="'+ch+'"'
    else:
        query='select question from '+Class+subject+'obj_questions where YEAR='+str(y)+' and ch_name="'+ch+'"'
    cur.execute(query)
    L=cur.fetchall()
    for i in L:
        lst_ques.append(i[0])

    scroll_obj(1)
def searchcheck():
    if level1.get()!='ALL CHAPTERS':
        searching2()
    if level1.get()=='ALL CHAPTERS':
        lable20=tk.Label(win6,text='CHAPTER IS COMPLUSARY',bg='#ff3333')
        lable20.place(relx=0.4,rely=0.25,relwidth=0.20,relheight=0.05)
       
def searchcheck1():
    if level1.get()!='ALL CHAPTERS' and level2.get()!='ALL MARKS':
        searching()
    if level1.get()=='ALL CHAPTERS':
        lable20=tk.Label(win6,text='MARK AND CHAPTER ARE COMPLUSARY',bg='#ff3333')
        lable20.place(relx=0.4,rely=0.25,relwidth=0.20,relheight=0.05)
       
    if level2.get()=='ALL MARKS':
        lable20=tk.Label(win6,text='MARK AND CHAPTER ARE COMPLUSARY',bg='#ff3333')
        lable20.place(relx=0.4,rely=0.25,relwidth=0.20,relheight=0.05)
    
    
def scroll_obj(n):
    global listbox,win200
    win200=tk.Tk()
    win200.title('SEARCH QUESTION')
    win200.geometry("1920x1080")
    if n==2:
        win100.destroy()
    elif n==1:
        win6.destroy()
        
    frame=tk.Frame(win200,padx=10,pady=10)
    frame.place(relx=0.1,rely=0.1,relwidth=0.80,relheight=0.8)
    label=tk.Label(frame,text="QUESTIONS",bg='white',fg='blue',font=('Helvetica',20))
    label.place(relx=0.3,rely=0.0,relwidth=0.40,relheight=0.1)
    scrollbar =tk.Scrollbar(frame)
    scrollbar.place(relx=0.91,rely=0.2,relwidth=0.03,relheight=0.6)
    listbox =tk.Listbox(frame,yscrollcommand = scrollbar.set)
    listbox.place(relx=0.05,rely=0.2,relwidth=0.85,relheight=0.6)
    but=tk.Button(frame,text='GET ANSWER',width=10,borderwidth=2,relief="ridge",command=get2)
    but.place(relx=0.05,rely=0.9,relwidth=0.30,relheight=0.05)
    but=tk.Button(frame,text='BACK',width=10,borderwidth=2,relief="ridge",command=lambda :window9(200))
    but.place(relx=0.65,rely=0.9,relwidth=0.30,relheight=0.05)
    p=0
    # L='select questions from' +Class+subject+'_questions'
    # cur.execute(L)
    # L=cur.fetchall()
    for values in lst_ques:
        listbox.insert(n,values)
        p+=1
    listbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox.yview)
def answer_obj():
    global win100
    query='select answer,OPTION_1,OPTION_2,OPTION_3,OPTION_4,CORRECT_OPT from '+Class+subject+'obj_questions where question="'+userline+'"'
    cur.execute(query)
    L=cur.fetchall()
    win200.destroy()
    win100=tk.Tk()
    win100.title('search question')
    win100.geometry("1920x1080")
    label=tk.Label(win100,text='QUESTION',bg='white',fg='blue',font=('Helvetica',20))
    label.place(relx=0.1,rely=0.2,relwidth=0.20,relheight=0.08)
    label1=tk.Label(win100,text=userline,bg='white',fg='blue',font=('Courier',20))
    label1.place(relx=0.3,rely=0.2,relwidth=0.50,relheight=0.08)  
    label=tk.Label(win100,text='OPTIONS',bg='white',fg='blue',font=('Helvetica',20))
    label.place(relx=0.1,rely=0.3,relwidth=0.30,relheight=0.08)
    lable1=tk.Label(win100,text='A',bg='cyan')
    lable1.place(relx=0.05,rely=0.4,relwidth=0.05,relheight=0.08)
    label1=tk.Label(win100,text=L[0][1],bg='white',fg='blue',font=('Courier',20))
    label1.place(relx=0.1,rely=0.4,relwidth=0.20,relheight=0.08)    
    lable2=tk.Label(win100,text='B',bg='cyan')
    lable2.place(relx=0.55,rely=0.4,relwidth=0.05,relheight=0.08)
    label1=tk.Label(win100,text=L[0][2],bg='white',fg='blue',font=('Courier',20))
    label1.place(relx=0.6,rely=0.4,relwidth=0.20,relheight=0.08)  
    lable3=tk.Label(win100,text='C',bg='cyan')
    lable3.place(relx=0.05,rely=0.5,relwidth=0.05,relheight=0.08)
    label1=tk.Label(win100,text=L[0][3],bg='white',fg='blue',font=('Courier',20))
    label1.place(relx=0.1,rely=0.5,relwidth=0.20,relheight=0.08)  
    lable4=tk.Label(win100,text='D',bg='cyan')
    lable4.place(relx=0.55,rely=0.5,relwidth=0.05,relheight=0.08)
    label1=tk.Label(win100,text=L[0][4],bg='white',fg='blue',font=('Courier',20))
    label1.place(relx=0.6,rely=0.5,relwidth=0.20,relheight=0.08)  
    label=tk.Label(win100,text='ANSWER',bg='white',fg='blue',font=('Helvetica',20))
    label.place(relx=0.1,rely=0.7,relwidth=0.20,relheight=0.08)
    label1=tk.Label(win100,text=L[0][0],bg='white',fg='blue',font=('Courier',20))
    label1.place(relx=0.1,rely=0.8,relwidth=0.80,relheight=0.08)   
    label=tk.Label(win100,text='correct option',bg='white',fg='blue',font=('Helvetica',20))
    label.place(relx=0.1,rely=0.6,relwidth=0.20,relheight=0.08)
    label1=tk.Label(win100,text=L[0][5],bg='white',fg='blue',font=('Courier',20))
    label1.place(relx=0.4,rely=0.6,relwidth=0.30,relheight=0.08)   
    but_equal2=tk.Button(win100,text='MAIN MENU',padx=134,pady=12,fg='WHITE',bg='#aa00ff',font=('ariel',10),command=lambda :options_window(5))
    but_equal2.place(relx=0.91,rely=0.02,relwidth=0.08,relheight=0.05)
    but=tk.Button(win100,text='SEARCH ANOTHER QUESTION',width=10,borderwidth=2,relief="ridge",bg="#ff4d4d",command=lambda :window9(4))
    but.place(relx=0.43,rely=0.02,relwidth=0.14,relheight=0.05)
    but=tk.Button(win100,text='BACK',width=10,borderwidth=2,relief="ridge",bg="#ff4d4d",command=lambda :scroll_obj(2))
    but.place(relx=0.01,rely=0.02,relwidth=0.08,relheight=0.05)


def get1():
    global userline
    userline=listbox.get('active')
    answer()
def get2():
    global userline
    userline=listbox.get('active')
    answer_obj()

def answer():
    global win100
    query='select answer,question from '+Class+subject+'_questions where question="'+userline+'"'
    cur.execute(query)
    L=cur.fetchall()
    # win6.destroy()
    win200.destroy()
    win100=tk.Tk()
    win100.title('ANSWER')
    win100.geometry("1920x1080")
    win100.configure(background='#8c8c8c')
    label=tk.Label(win100,text='ANSWER',bg='black',fg='white',font=('Helvetica',20))
    label.place(relx=0.1,rely=0.54,relwidth=0.40,relheight=0.06)
    label1=tk.Label(win100,text=L[0][0],bg='white',fg='blue',font=('Courier',20))
    label1.place(relx=0.1,rely=0.6,relwidth=0.80,relheight=0.3)
    label=tk.Label(win100,text='QUESTION',bg='black',fg='white',font=('Helvetica',20))
    label.place(relx=0.1,rely=0.14,relwidth=0.40,relheight=0.06)
    label1=tk.Label(win100,text=L[0][1],bg='white',fg='blue',font=('Courier',20))
    label1.place(relx=0.1,rely=0.2,relwidth=0.80,relheight=0.3)
    but=tk.Button(win100,text='SEARCH ANOTHER QUESTION',width=10,borderwidth=2,relief="ridge",bg="#ff4d4d",command=lambda :window9(4))
    but.place(relx=0.43,rely=0.02,relwidth=0.14,relheight=0.05)
    but_equal2=tk.Button(win100,text='MAIN MENU',padx=134,pady=12,fg='WHITE',bg='#aa00ff',font=('ariel',10),command=lambda :options_window(5))
    but_equal2.place(relx=0.91,rely=0.02,relwidth=0.08,relheight=0.05)
    
    but=tk.Button(win100,text='BACK',width=10,borderwidth=2,relief="ridge",bg="#ff4d4d",command=lambda :scroll(2))
    but.place(relx=0.01,rely=0.02,relwidth=0.08,relheight=0.05)
    
def scroll(n):
    global listbox,win200
    win200=tk.Tk()
    win200.title('SEARCH QUESTION')
    win200.geometry("1920x1080")
    win200.configure(background='#8c8c8c')
    if n==1:
        win6.destroy()
    elif n==2:
        win100.destroy()
    frame=tk.Frame(win200,padx=10,pady=10)
    frame.place(relx=0.1,rely=0.1,relwidth=0.80,relheight=0.8)
    label=tk.Label(frame,text="QUESTIONS",bg='white',fg='blue',font=('Helvetica',20))
    label.place(relx=0.3,rely=0.0,relwidth=0.40,relheight=0.1)
    scrollbar =tk.Scrollbar(frame)
    scrollbar.place(relx=0.91,rely=0.2,relwidth=0.03,relheight=0.6)
    listbox =tk.Listbox(frame,yscrollcommand = scrollbar.set)
    listbox.place(relx=0.05,rely=0.2,relwidth=0.85,relheight=0.6)
    but=tk.Button(frame,text='GET ANSWER',width=10,borderwidth=2,relief="ridge",command=get1)
    but.place(relx=0.05,rely=0.9,relwidth=0.30,relheight=0.05)

    p=0
    # L='select questions from' +Class+subject+'_questions'
    # cur.execute(L)
    # L=cur.fetchall()
    
    for values in lst_ques:
        listbox.insert(n,values)
        p+=1
    listbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox.yview)


# scroll('12','maths')
def show_questions(a,b):
    global listbox
    win14=tk.Tk()
    win14.title('SEARCH QUESTION')
    win14.geometry("1920x1080")
    win14.configure(background='black')
    win14.destroy()
    frame=tk.Frame(win14,padx=10,pady=10)
    frame.place(relx=0.1,rely=0.0,relwidth=0.80,relheight=0.8)
    label=tk.Label(frame,text="QUESTIONS",bg='white',fg='blue',font=('Helvetica',20))
    label.place(relx=0.3,rely=0.2,relwidth=0.40,relheight=0.1)
    scrollbar =tk.Scrollbar(frame)
    scrollbar.place(relx=0.91,rely=0.3,relwidth=0.03,relheight=0.5)
    listbox =tk.Listbox(frame,yscrollcommand = scrollbar.set)
    listbox.place(relx=0.05,rely=0.3,relwidth=0.85,relheight=0.5)
    but=tk.Button(frame,text='GET ANSWER',width=10,borderwidth=2,relief="ridge",command=get1)
    but.place(relx=0.05,rely=0.9,relwidth=0.30,relheight=0.05)
    n=0
    # L='select questions from' +a+b+'_questions'
    # cur.execute(L)
    # L=cur.fetchall()
    for values in L:
        listbox.insert(n,values)
        n+=1
    listbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox.yview)
    tk.mainloop()
    

def window111(n):
    if n==1:
        win5.destroy()
    elif n==2:
        win12.destroy()
    elif n==3:
        win4.destroy()
    elif n==4:
        win22.destroy()  
    elif n==5:
        win99.destroy()
    elif n==100:
        win100.destroy()
    global win13
    global updated
    win13=tk.Tk()
    
    updated=[]
    win13.title('SELECT CLASS WINDOW')
    win13.geometry("1920x1080")  
    win13.configure(background='#ccf3ff')
    frame=tk.Frame(win13,relief= tk.RAISED)
    frame.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.1)
    frame2=tk.Frame(win13,relief= tk.RAISED,bg='white')
    frame2.place(relx=0.25,rely=0.4,relwidth=0.50,relheight=0.3)
    label1=tk.Label(frame,text='WHAT TYPE OF QUESTION PAPER WOULD YOU LIKE TO CREATE',font=('Times New Roman',20),relief= tk.RAISED,bg='#b2ff24')
    label1.place(relx=0,rely=0,relwidth=1,relheight=1)
    but1=tk.Button(frame2,text='SUBJECTIVE',font=('ariel',15),bg="#003399",fg='white',relief= tk.RIDGE,command=lambda :window222_sub(4))
    but1.place(relx=0.1,rely=0.03,relwidth=0.8,relheight=0.22)
    but2=tk.Button(frame2,text='OBJECTIVE',font=('ariel',15),bg="#003399",fg='white',relief= tk.RIDGE,command=lambda :window333_obj(4))
    but2.place(relx=0.1,rely=0.40,relwidth=0.8,relheight=0.22)
    but3=tk.Button(frame2,text='BACK',font=('ariel',15),bg="#ff4d4d",command=lambda :create_test_paper(5),relief= tk.RIDGE)
    but3.place(relx=0.25,rely=0.80,relwidth=0.5,relheight=0.15)

def checksss():
    global inst
    print(entries)
    for i in range(entries):
        inst.append(e[i].get())
    window111(4)
    
def instructions():
    
    global win22,ent1,ent2,ent3,ent4,ent5,ent6,ent7,ent8,ent9,ent10
    global ent11,ent12,ent13,ent14,ent15,ent16,ent17,ent18,ent19
    global ent20,entries,e,ti,tm,su,cl,da,tim,inst,P
    ti=ele1.get()
    tm=ele2.get()
    su=ele3.get()
    cl=ele4.get()
    da=ele5.get()
    tim=ele6.get()
    inst=[]
    print(tim)
    win22=tk.Tk()
    win8.destroy()
    win22.title('Next window of create')
    win22.geometry("1920x1080")
    win22.configure(background='#8c8c8c')
    lable7=tk.Label(win22,text='ENTER THE INSTRUCTIONS',font=('Calculator',40,'bold'))
    lable7.place(relx=0.1,rely=0.02,relwidth=0.8,relheight=0.1)
    n=le.get()
    P=1
    x=0
    entries=0
    c=1
    j=0
    e=[ent1,ent2,ent3,ent4,ent5,ent6,ent7,ent8,ent9,ent10,ent11,ent12,ent13,ent14,ent15,ent16,ent17,ent18,ent19,ent20]

    if int(n)%2!=0:
        n=int(n)-1
        x=1
        c=0
    nu=0

    k=int(int(n)/2)
    for i in range(2):
        
        for j in range(k):
            if i==1:
                cu=0.52
                ci=0.57
              
                if c==0:
                    c=nu
                    nu=j+2+k
                elif c==1:
                    nu=j+1+k
                else:
                    nu=j+2+k
            else:
                cu=0.05
                ci=0.1
                nu=j+1
            
            ny=(j+2)*0.07
            lable=tk.Label(win22,text=str(nu))
            lable.place(relx=cu,rely=ny,relwidth=0.05,relheight=0.06)
            e[nu-1]=tk.Entry(win22,font=('ariel',20,'bold'),bg='#ffe6e6',fg='black')
            e[nu-1].place(relx=ci,rely=ny,relwidth=0.38,relheight=0.06)
            entries+=1
    if x==1:
        if int(n)==1:
            ny=0.14
        else:
            ny=(j+3)*0.07
        nu=c+1
        cu=0.05
        ci=0.1
        
        lable=tk.Label(win22,text=str(nu))
        lable.place(relx=cu,rely=ny,relwidth=0.05,relheight=0.06)
        e[nu-1]=tk.Entry(win22,font=('Calculator',20,'bold'),bg='#ffe6e6',fg='black')
        e[nu-1].place(relx=ci,rely=ny,relwidth=0.38,relheight=0.06)
        entries+=1

    
    but_equal1=tk.Button(win22,text='submit',padx=134,pady=12,fg='black',bg='#66ff99',font=('ariel',10),command=checksss)
    but_equal1.place(relx=0.6,rely=0.9,relwidth=0.2,relheight=0.06)
    but_equal2=tk.Button(win22,text='back',padx=134,pady=12,fg='black',bg='#ff4d4d',font=('ariel',10),command=lambda :create_test_paper(2))
    but_equal2.place(relx=0.2,rely=0.9,relwidth=0.2,relheight=0.06)

    
def create_test_paper(n):
    global win8,le,ele1,ele2,ele3,ele4,ele5,ele6,ctp,pentsss,updated
    if n==1:
        win4.destroy()
    if n==2:
        win22.destroy()
    if n==5:
        win13.destroy()
    pentsss=[]
    updated=[]
    win8=tk.Tk()
    win8.title('Next window of create')
    win8.geometry("1920x1080")
    win8.configure(background='#ffffff')
    frame2=tk.Frame(win8,relief= tk.RAISED,bg='#474747')
    frame4=tk.Frame(win8,relief= tk.RAISED,bg='#474747')
    lable1=tk.Label(win8,text='ENTER THE DETAILS',bg='#000099',fg='white',font=('Times',25,'bold'))
    lable1.place(relx=0.35,rely=0.05,relwidth=0.3,relheight=0.09)
    frame2.place(relx=0.15,rely=0.15,relwidth=0.70,relheight=0.5)
    frame4.place(relx=0.15,rely=0.75,relwidth=0.70,relheight=0.2)
    lable1=tk.Label(frame2,text='ENTER THE TITLE(type of test)')
    lable1.place(relx=0.1,rely=0.08,relwidth=0.3,relheight=0.1)
    lable2=tk.Label(frame2,text='ENTER THE TOTAL MARKS')
    lable2.place(relx=0.6,rely=0.06,relwidth=0.3,relheight=0.1)
    ele1=tk.Entry(frame2,width=8,borderwidth=3,font=('Calculator',22,'bold'),bg='#d9d9d9',fg='#0d0d0d')
    ele1.place(relx=0.1,rely=0.16,relwidth=0.3,relheight=0.15)
    ele2=tk.Entry(frame2,width=8,borderwidth=3,font=('Calculator',22,'bold'),bg='#d9d9d9',fg='#0d0d0d')            
    ele2.place(relx=0.6,rely=0.16,relwidth=0.3,relheight=0.15)
    lable3=tk.Label(frame2,text='ENTER THE CLASS')
    lable3.place(relx=0.1,rely=0.37,relwidth=0.3,relheight=0.1)
    lable4=tk.Label(frame2,text='ENTER THE SUBJECT')
    lable4.place(relx=0.6,rely=0.37,relwidth=0.3,relheight=0.1)
    ele4=tk.Entry(frame2,width=8,borderwidth=3,font=('Calculator',22,'bold'),bg='#d9d9d9',fg='#0d0d0d')            
    ele4.place(relx=0.1,rely=0.47,relwidth=0.3,relheight=0.15)
    ele3=tk.Entry(frame2,width=8,borderwidth=3,font=('Calculator',22,'bold'),bg='#d9d9d9',fg='#0d0d0d')            
    ele3.place(relx=0.6,rely=0.47,relwidth=0.3,relheight=0.15)
    lable5=tk.Label(frame2,text='ENTER THE DATE')
    lable5.place(relx=0.1,rely=0.68,relwidth=0.3,relheight=0.1)
    lable6=tk.Label(frame2,text='ENTER THE TIME LIMIT')
    lable6.place(relx=0.6,rely=0.68,relwidth=0.3,relheight=0.1)
    ele5=tk.Entry(frame2,width=8,borderwidth=3,font=('Calculator',22,'bold'),bg='#d9d9d9',fg='#0d0d0d')            
    ele5.place(relx=0.1,rely=0.78,relwidth=0.3,relheight=0.15)
    ele6=tk.Entry(frame2,width=8,borderwidth=3,font=('Calculator',22,'bold'),bg='#d9d9d9',fg='#0d0d0d')
    ele6.place(relx=0.6,rely=0.78,relwidth=0.3,relheight=0.15)
    but_equal1=tk.Button(frame4,text='submit',padx=134,pady=12,fg='black',bg='#66ff99',font=('ariel',10),command=instructions)
    but_equal1.place(relx=0.6,rely=0.6,relwidth=0.3,relheight=0.3)
    but_equal2=tk.Button(frame4,text='back',padx=134,pady=12,fg='black',bg='#ff4d4d',font=('ariel',10),command=lambda :options_window(4))
    but_equal2.place(relx=0.1,rely=0.6,relwidth=0.3,relheight=0.3)
    op2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    lable17=tk.Label(frame4,text='ENTER THE NUMBER OF INSTRUCTIONS')
    lable17.place(relx=0.1,rely=0.1,relwidth=0.4,relheight=0.3)
    le=tk.StringVar(frame4)
    le.set(op2[0])
    le.trace("w",change)
    drop2=tk.OptionMenu(frame4,le,*op2)
    drop2.config(width = 20)
    drop2.place(relx=0.5,rely=0.1,relwidth=0.4,relheight=0.3)
    ctp=[ele1,ele2,ele3,ele4,ele5,ele6]
   



def checksss1():
    global pentsss
    for i in range(entries):
        pentsss.append(e[i].get())
    after_questions()

def questionsss(n):
    global win22,ent1,ent2,ent3,ent4,ent5,ent6,ent7,ent8,ent9,ent10
    global ent11,ent12,ent13,ent14,ent15,ent16,ent17,ent18,ent19
    global ent20,entries,e,f,P
    win22=tk.Tk()
    P=2
    
    win22.title('Next window of create')
    win22.geometry("1920x1080")
    win22.configure(background='#8c8c8c')
    if n==1:
        win99.destroy()
    f=0
    j=0


    lable7=tk.Label(win22,text='ENTER THE QUESTIONS',font=('Calculator',40,'bold'))
    lable7.place(relx=0.1,rely=0.02,relwidth=0.8,relheight=0.1)
    n=le.get()

    x=0
    entries=0
    c=1
    e=[ent1,ent2,ent3,ent4,ent5,ent6,ent7,ent8,ent9,ent10,ent11,ent12,ent13,ent14,ent15,ent16,ent17,ent18,ent19,ent20]

    if int(n)%2!=0:
        n=int(n)-1
        x=1
        c=0
    nu=0

    k=int(int(n)/2)
    for i in range(2):
        
        
        for j in range(k):
            if i==1:
                cu=0.52
                ci=0.57
              
                if c==0:
                    c=nu
                    nu=j+2+k
                elif c==1:
                    nu=j+1+k
                else:
                    nu=j+2+k
            else:
                cu=0.05
                ci=0.1
                nu=j+1
            
            ny=(j+2)*0.07
            lable=tk.Label(win22,text=str(nu))
            lable.place(relx=cu,rely=ny,relwidth=0.05,relheight=0.06)
            e[nu-1]=tk.Entry(win22,font=('Calculator',20,'bold'),bg='#2ab3b5',fg='white')
            e[nu-1].place(relx=ci,rely=ny,relwidth=0.38,relheight=0.06)
            entries+=1
    if x==1:
        if int(n)==1:
            ny=0.14
        else:
            ny=(j+3)*0.07
            
        nu=c+1
        cu=0.05
        ci=0.1
        lable=tk.Label(win22,text=str(nu))
        lable.place(relx=cu,rely=ny,relwidth=0.05,relheight=0.06)
        e[nu-1]=tk.Entry(win22,font=('Calculator',20,'bold'),bg='#2ab3b5',fg='white')
        e[nu-1].place(relx=ci,rely=ny,relwidth=0.38,relheight=0.06)
        entries+=1

    
    but_equal1=tk.Button(win22,text='SUBMIT',padx=134,pady=12,fg='black',bg='#66ff99',font=('ariel',10),command=checksss1)
    but_equal1.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.06)
    but_equal2=tk.Button(win22,text='BACK',padx=134,pady=12,fg='black',bg='#ff4d4d',font=('ariel',10),command=create_test_subjective)
    but_equal2.place(relx=0.2,rely=0.85,relwidth=0.2,relheight=0.06)
 
def create_test_subjective():
    global win99,le,drop22,pentsss
    win99=tk.Tk()
    win99.title('Next window of create')
    win99.geometry("1920x1080")
    win99.configure(background='#8c8c8c')
    win100.destroy()
    
    but_equal1=tk.Button(win99,text='SUBMIT',padx=134,pady=12,fg='black',bg='#66ff99',font=('ariel',10),command=lambda :questionsss(1))
    but_equal1.place(relx=0.6,rely=0.7,relwidth=0.2,relheight=0.06)
    but_equal2=tk.Button(win99,text='BACK',padx=134,pady=12,fg='black',bg='#ff4d4d',font=('ariel',10),command=lambda :window222_sub(6))
    but_equal2.place(relx=0.2,rely=0.7,relwidth=0.2,relheight=0.06)
    op2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    lable17=tk.Label(win99,text='ENTER THE NUMBER OF QUESTIONS YOU WANT TO ENTER')
    lable17.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.07)
    le=tk.StringVar(win99)
    le.set(op2[0])
    le.trace("w",change)
    drop22=tk.OptionMenu(win99,le,*op2)
    drop22.config(width = 20)
    drop22.place(relx=0.3,rely=0.3,relwidth=0.4,relheight=0.07)
    
    
def after_questions():
    global win999,le,drop22,link
    win999=tk.Tk()
    win999.title('Next window of create')
    win999.geometry("1920x1080")
    win999.configure(background='#8c8c8c')
    link=[]
    



    but_equal1=tk.Button(win999,text='CREATE PAPER',padx=134,pady=12,fg='black',bg='#f0654f',font=('ariel',10),command=lambda :naming(P))
    but_equal1.place(relx=0.2,rely=0.5,relwidth=0.25,relheight=0.06)
    but_equal2=tk.Button(win999,text='ADD MORE QUESTIONS',padx=134,pady=12,fg='black',bg='#f0654f',font=('ariel',10),command=lambda :window222_sub(5))
    but_equal2.place(relx=0.55,rely=0.5,relwidth=0.25,relheight=0.06)


def naming(n):
    global win15,NAME
    if n==1:
        win999.destroy()
    elif n==2:
        win999.destroy()
        win22.destroy()
    win15=tk.Tk()
    win15.title('SAVE AS')
    win15.geometry("960x540")
    win15.configure(background='#8c8c8c')
    label1=tk.Label(win15,text='SAVE PDF AS',font=('Times New Roman',20),relief= tk.RAISED,bg='#b2ff24')
    label1.place(relx=0.35,rely=0.3,relwidth=0.3,relheight=0.1)
    NAME=tk.Entry(win15,width=8,borderwidth=3,font=('Calculator',25,'bold'),bg='#d9d9d9',fg='#0d0d0d')
    NAME.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.1)
    but_equal1=tk.Button(win15,text='SUBMIT',padx=134,pady=12,fg='black',bg='#66ff99',font=('ariel',10),command=naming2)
    but_equal1.place(relx=0.4,rely=0.8,relwidth=0.20,relheight=0.1)
def naming2():
    global name
    name=NAME.get()+'.pdf'
    win15.destroy()
    thepdfthing()
def thepdfthing():
    global ele1,ele2,ele3,ele4,ele5,ele6
    

    pdf=FPDF(format='A4')
    pdf.add_page()
    pdf.set_font('Arial',size=18,style='B')
    

    pdf.cell(200,5,txt='AIR FORCE SCHOOL HEBBAL',border=1,ln=2,align='C')
    pdf.set_font('Arial',size=15,style='B')
    pdf.cell(200,5,txt=str(ti),ln=2,align='C')
    pdf.set_font_size(11)
    pdf.cell(100,5,txt='Total Marks:'+(str(tm).title()),ln=2,align='L')
    pdf.cell(100,5,txt='Subject:'+(str(su).title()),ln=2,align='L')
    pdf.cell(100,5,txt='Class'+(str(cl).title()),ln=2,align='L')
    pdf.cell(100,5,txt='Date:'+(str(da).title()),ln=2,align='L')
    pdf.cell(100,5,txt='Time Limit:'+(str(tim).title()),ln=2,align='L')
    pdf.set_font('Arial',size=13,style='U')
    pdf.cell(100,5,txt='INSTRUCTIONS',ln=2,align='C')
    pdf.set_font('Arial',size=11)
    o=1
    txt1=''
    for i in inst:
        txt1+='('+str(o)+')'+'  '+(i.capitalize())+'\n'
        o+=1
    pdf.multi_cell(100,5,txt=txt1,border=1,align='L')
    pdf.cell(0,10,txt='-'*1000,ln=2)
    pdf.cell(0,10,txt='-'*1000,ln=2)
    pdf.set_font('Arial',size=8,style='B')
    b=''
    o=1
    for i in updated:
        b+='('+str(o)+')'+'  '+(str(i).capitalize())+'\n'   
        o+=1
    for i in pentsss:

        b+='('+str(o)+')'+'  '+(str(i).capitalize())+'\n'
        o+=1


    pdf.multi_cell(100,5,txt=b,align='L')    
        
        
    
    pdf.output(str(name))
    options_window(0)
        
        
    





def window222_sub(n):
    global win100,updated
    if n==1:
        win5.destroy()
    elif n==2:
        win6.destroy()
    elif n==3:
        win6.destroy()
    elif n==4:
        win13.destroy()
    elif n==5:
        win999.destroy()
    elif n==6:
        win99.destroy()
    win100=tk.Tk()
    win100.title('SELECT CLASS WINDOW')
    win100.geometry("1920x1080") 
    win100.configure(background='#ccf3ff')
    frame=tk.Frame(win100,relief= tk.RAISED)
    frame.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.1)
    frame2=tk.Frame(win100,relief= tk.RAISED,bg='white')
    frame2.place(relx=0.25,rely=0.4,relwidth=0.50,relheight=0.3)
    label1=tk.Label(frame,text='HOW DO YOU WANT TO ENTER THE QUESTION',font=('Times New Roman',20),relief= tk.RAISED,bg='#ff0066',fg='white')
    label1.place(relx=0,rely=0,relwidth=1,relheight=1)
    but1=tk.Button(frame2,text='TYPE QUESTION',font=('ariel',15),bg="#003399",fg='white',relief= tk.RIDGE,command=create_test_subjective)
    but1.place(relx=0.1,rely=0.03,relwidth=0.8,relheight=0.22)
    but2=tk.Button(frame2,text='SEARCH FROM QUESTIONBANK',font=('ariel',15),bg="#003399",fg='white',relief= tk.RIDGE,command=lambda :search_question_testpaper(Class,subject,1))
    but2.place(relx=0.1,rely=0.40,relwidth=0.8,relheight=0.22)
    but3=tk.Button(frame2,text='BACK',font=('ariel',15),bg="#ff4d4d",command=lambda :window111(100),relief= tk.RIDGE)
    but3.place(relx=0.25,rely=0.80,relwidth=0.5,relheight=0.15)

link=[]
def update():
    global updated,link
    win200.destroy()
    win6.destroy()
    for i in link:
        updated.append(i)
    print(updated)
    after_questions()
def search_question_testpaper(d,e,n):
    global level,level1,level2,level3,ent1,updated
    global win6
    if n==1:
        win100.destroy()

    win6=tk.Tk()
    win6.title('AVA QUESTION BANK')
    win6.geometry("1920x1080")  
    lable20=tk.Label(win6,text='SEARCH QUESTION',font=('Helvetica',20))
    lable20.place(relx=0.4,rely=0.1,relwidth=0.20,relheight=0.05)
    
    lable21=tk.Label(win6,text='SELECT THE LEVEL')
    lable21.place(relx=0.25,rely=0.4,relwidth=0.20,relheight=0.05)
    lable22=tk.Label(win6,text='SELECT THE CHAPTER')
    lable22.place(relx=0.55,rely=0.4,relwidth=0.20,relheight=0.05)
    lable23=tk.Label(win6,text='SELECT THE MARK')
    lable23.place(relx=0.25,rely=0.6,relwidth=0.20,relheight=0.05)
    lable24=tk.Label(win6,text='SELECT THE YEAR')
    lable24.place(relx=0.55,rely=0.6,relwidth=0.20,relheight=0.05)

    op1=['EASY','MEDIUM','HARD','HOTS']
    query='select distinct CH_NAME from '+Class+subject+'_questions'
    cur.execute(query)
    result=cur.fetchall()
    op2=['ALL CHAPTERS']
    for i in result: 
        op2.append(str(i[0]))
    query='select distinct mark from '+Class+subject+'_questions'
    cur.execute(query)
    result2=cur.fetchall()
    op3=['ALL MARKS']
    for i in result2:
        op3.append(str(i[0]))
    query='select distinct YEAR from '+Class+subject+'_questions'
    cur.execute(query)
    result1=cur.fetchall()
    op4=['ALL YEARS']
    for i in result1:
        op4.append(str(i[0]))
    level=tk.StringVar(win6)
    level.set(op1[0])
    level.trace("w",change)
    drop1=tk.OptionMenu(win6,level,*op1)
    drop1.config(width = 20)
    drop1.place(relx=0.25,rely=0.35,relwidth=0.20,relheight=0.05)
    level1=tk.StringVar(win6)
    level1.set(op2[0])
    level1.trace("w",change)
    drop2=tk.OptionMenu(win6,level1,*op2)
    drop2.config(width = 20)
    drop2.place(relx=0.55,rely=0.35,relwidth=0.20,relheight=0.05)
    level2=tk.StringVar(win6)
    level2.set(op3[0])
    level2.trace("w",change)
    drop3=tk.OptionMenu(win6,level2,*op3)
    drop3.config(width = 20)
    drop3.place(relx=0.25,rely=0.55,relwidth=0.20,relheight=0.05)
    level3=tk.StringVar(win6)
    level3.set(op4[0])
    level3.trace("w",change)
    drop4=tk.OptionMenu(win6,level3,*op4)
    drop4.config(width = 20)
    drop4.place(relx=0.55,rely=0.55,relwidth=0.20,relheight=0.05)    
    but_equal1=tk.Button(win6,text='SUBMIT',padx=134,pady=12,fg='black',bg='#66ff99',font=('ariel',10),command=searchcheck_test)
    but_equal1.place(relx=0.525,rely=0.8,relwidth=0.20,relheight=0.05)

    but_equal2=tk.Button(win6,text='BACK',padx=134,pady=12,fg='black',bg='#ff4d4d',font=('ariel',10),command=lambda : window222_sub(3))
    but_equal2.place(relx=0.275,rely=0.8,relwidth=0.20,relheight=0.05)   

def searchcheck_test():
    if level1.get()!='ALL CHAPTERS' and level2.get()!='ALL MARKS':
        searching_test()
    if level1.get()=='ALL CHAPTERS':
        lable20=tk.Label(win6,text='MARK AND CHAPTER ARE COMPLUSARY',bg='#ff3333')
        lable20.place(relx=0.4,rely=0.25,relwidth=0.20,relheight=0.05)
       
    if level2.get()=='ALL MARKS':
        lable20=tk.Label(win6,text='MARK AND CHAPTER ARE COMPLUSARY',bg='#ff3333')
        lable20.place(relx=0.4,rely=0.25,relwidth=0.20,relheight=0.05)
def searching_test():
    global lst_ques,link
    lst_ques=[]
    ch=level1.get()
    mk=level2.get()
    y=level3.get()

    # win6.destroy()
    if y=='ALL YEARS':
        query='select question from '+Class+subject+'_questions where MARK='+str(mk)+' and ch_name="'+ch+'"'
    else:
        query='select question from '+Class+subject+'_questions where MARK='+str(mk)+' and YEAR='+str(y)+' and ch_name="'+ch+'"'
    cur.execute(query)
    L=cur.fetchall()
    for i in L:
        lst_ques.append(i[0])
    print(lst_ques)

    scroll_test()
def scroll_test():
    global listbox,win200,link,listbox2
    win200=tk.Tk()
    win200.title('search question')
    win200.geometry("1920x1080")
    frame=tk.Frame(win200,padx=10,pady=10,bg='#80bfff')
    frame.place(relx=0.1,rely=0.1,relwidth=0.80,relheight=0.8)
    label=tk.Label(frame,text="QUESTIONS",fg='white',font=('Helvetica',20),bg='#004d99')
    label.place(relx=0.1,rely=0.0,relwidth=0.30,relheight=0.05)
    scrollbar =tk.Scrollbar(frame)
    scrollbar.place(relx=0.91,rely=0.06,relwidth=0.03,relheight=0.44)
    listbox =tk.Listbox(frame,yscrollcommand = scrollbar.set)
    listbox.place(relx=0.05,rely=0.06,relwidth=0.85,relheight=0.44)
    label2=tk.Label(frame,text="SELECTED QUESTIONS",fg='white',font=('Helvetica',20),bg='#004d99')
    label2.place(relx=0.1,rely=0.55,relwidth=0.30,relheight=0.05)
    scrollbar2 =tk.Scrollbar(frame)
    scrollbar2.place(relx=0.91,rely=0.61,relwidth=0.03,relheight=0.2)
    listbox2=tk.Listbox(frame,yscrollcommand = scrollbar2.set)
    listbox2.place(relx=0.05,rely=0.61,relwidth=0.85,relheight=0.2)
    but=tk.Button(frame,text='SELECT QUESTION',width=10,borderwidth=2,relief="ridge",command=get_test)
    but.place(relx=0.05,rely=0.93,relwidth=0.30,relheight=0.05)
    but1=tk.Button(frame,text='NEXT',width=10,borderwidth=2,relief="ridge",command=update)
    but1.place(relx=0.65,rely=0.93,relwidth=0.30,relheight=0.05)

    n=0

    
    for values in lst_ques:
        listbox.insert(n,values)
        n+=1
    listbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox.yview)
    n=0
    for values in link:
        listbox2.insert(n,values)
        n+=1
    listbox2.config(yscrollcommand = scrollbar2.set)
    scrollbar2.config(command = listbox2.yview)
def get_test():
    global userline,link
    userline=listbox.get('active')
    link.append(userline)
    win200.destroy()
    scroll_test()


def window333_obj(n):
    global win200
    win200=tk.Tk()
    win200.title('SELECT CLASS WINDOW')
    win200.geometry("1920x1080")  
    if n==111:
        win10.destroy()
    if n==4:
        win13.destroy()
    # img1=Image.open('C:/Users/91789/Pictures/aval2.png')
    # img1=img1.resize((1920,1080), Image.ANTIALIAS)
    # img1=ImageTk.PhotoImage(img1)
    # panel1=tk.Label(win200, image=img1)
    # panel1.image= img1
    # panel1.place(relx=0.0,rely=0.0,relwidth=1,relheight=1)
    frame=tk.Frame(win200,relief= tk.RAISED)
    frame.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.1)

    label1=tk.Label(frame,text='COMMING SOON',font=('Times New Roman',20),relief= tk.RAISED,bg='#b2ff24')
    label1.place(relx=0,rely=0,relwidth=1,relheight=1)
    but3=tk.Button(win200,text='BACK',font=('ariel',15),bg="#ff4d4d",command=window111(200),relief= tk.RIDGE)
    but3.place(relx=0.4,rely=0.60,relwidth=0.2,relheight=0.1)
    














def add_questions(d,e):
    
    global frame2,win1,ent1,ent2,ent3,ent4,ent5,ent6
    
    z="select count(*) from "+str(d)+e+'_questions'
    if L.get()!='ALL CHAPTERS':
        CH_NAME=L.get()
    else:
        CH_NAME=ent1.get()
    cur.execute(z)
    y=cur.fetchall()
    
    QUESTION=ent2.get()
    ANSWER=ent3.get()
    MARK=ent4.get()
    LEVEL1=str(LEVEL.get())
    YEAR=ent6.get()
    print(YEAR)
    query='insert into '+str(d)+e+'_questions(sno,CH_NAME,QUESTION,ANSWER,MARK,LEVEL,YEAR) values(%s,%s,%s,%s,%s,%s,%s)'
    data=(y[0][0]+1,CH_NAME,QUESTION,ANSWER,MARK,LEVEL1,YEAR)
    
    try:
        cur.execute(query,data)
        con_obj.commit()
        print('1')
    except:
        con_obj.rollback()
    options_window(30)
    

def add_questions_obj(d,e):
    global A,B,C,D
    z="select count(*) from "+str(d)+e+'obj_questions'
    cur.execute(z)
    y=cur.fetchall()
    CH_NAME=ent1.get()
    QUESTION=ent7.get()
    A=ent2.get()
    B=ent3.get()
    C=ent4.get()
    D=ent5.get()
    ANSWER=ent6.get()
    LEVEL1=str(LEVEL.get())
    OPT1=str(OPT.get())
    YEAR=ent8.get()

          
    query='insert into '+str(d)+e+'obj_questions(sno,CH_NAME,QUESTION,OPTION_1,OPTION_2,OPTION_3,OPTION_4,ANSWER,CORRECT_OPT,LEVEL,YEAR) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    data=(y[0][0]+1,CH_NAME,QUESTION,A,B,C,D,ANSWER,OPT1,LEVEL1,YEAR)

    # try:

    cur.execute(query,data)

    con_obj.commit()

    options_window(40)

    # except:
    #     con_obj.rollback()
    #     print('query not executed')
        


   



def login_check():

    global entry1,entry2,win2,userID
    userID=entry1.get()
    passwd=entry2.get()
    z1="select userID from logintable"
    cur.execute(z1)
    y1=cur.fetchall()
    L=[]
    for i in y1:
        L.append(str(i[0]))
    
    if str(userID) in L:
        print('hey')
        z2="select userID,password from logintable where userID="+str(userID)
        cur.execute(z2)
        y=cur.fetchall()
        if int(userID)==y[0][0] and str(passwd)==y[0][1]:
            select_class(1)
        else:

            lab0=tk.Label(frame2,text='incorrect password',bg='#ff4d4d',fg='white',font=('ariel',10))
            lab0.place(relx=0.3,rely=0.45,relwidth=0.6,relheight=0.1)
    else:
        lab0=tk.Label(frame2,text="User ID doesn't exist[register]",bg='#ff4d4d',fg='white',font=('ariel',10))
        lab0.place(relx=0.3,rely=0.45,relwidth=0.6,relheight=0.1)
            


def login_entry():
    global win2,frame2,but,entry1,entry2
    lable=tk.Label(frame2,text='USER_ID',fg='white',bg='#4d4d4d')
    lable.place(relx=0.1,rely=0.05,relwidth=0.2,relheight=0.15)
    lab1=tk.Label(frame2,text='PASSWORD',fg='white',bg='#4d4d4d')
    lab1.place(relx=0.1,rely=0.2,relwidth=0.2,relheight=0.15)
    entry1=tk.Entry(frame2,width=15,borderwidth=5,font=('Calculator',27,'bold'),bg='white')
    entry1.place(relx=0.3,rely=0.05,relwidth=0.6,relheight=0.15)
    entry2=tk.Entry(frame2,width=15,borderwidth=5,font=('Calculator',27,'bold'),bg='white',show='*')
    entry2.place(relx=0.3,rely=0.2,relwidth=0.6,relheight=0.15)
    but=tk.Button(frame2,text='SUBMIT',padx=134,pady=12,fg='black',bg='#66ff99',font=('ariel',12),command=login_check)
    but.place(relx=0.55,rely=0.8,relwidth=0.4,relheight=0.1)
    backbut=tk.Button(frame2,text='BACK',font=('ariel',12),height=2,width=50,bg='#ff4d4d',command=lambda: startingwindow('win2'))
    backbut.place(relx=0.05,rely=0.8,relwidth=0.4,relheight=0.1)

def login():
    
    #login window
    global win2,frame2
    win2=tk.Tk()
    win2.title('AVA LOGIN')
    win2.geometry("1920x1080")
    win2.configure(background='#8c8c8c')
    # img1=Image.open('C:/Users/91789/Downloads/book-5077895_1920.jpg')
    # img1=img1.resize((1520,970))
    # img1=ImageTk.PhotoImage(img1)
    # img_back=tk.Label(win2, image=img1)
    # img_back.place(x=0,y=0)
    frame=tk.Frame(win2,relief= tk.RAISED,height=100,width=150,bg='#1a1a1a')
    frame.place(relx=0.0,rely=0.0,relwidth=0.10,relheight=1)
    frame=tk.Frame(win2,relief= tk.RAISED,height=100,width=150,bg='#1a1a1a')
    frame.place(relx=0.9,rely=0.0,relwidth=0.10,relheight=1)
    frame=tk.Frame(win2,relief= tk.RAISED,height=100,width=150,bg='#595959')
    frame.place(relx=0.1,rely=0.0,relwidth=0.10,relheight=1)
    frame=tk.Frame(win2,relief= tk.RAISED,height=100,width=150,bg='#595959')
    frame.place(relx=0.8,rely=0.0,relwidth=0.10,relheight=1)
    frame=tk.Frame(win2,relief= tk.RAISED,height=100,width=150)
    frame.place(relx=0.25,rely=0.1,relwidth=0.50,relheight=0.1)
    frame2=tk.Frame(win2,relief= tk.RAISED,bg='#d9d9d9')
    frame2.place(relx=0.2,rely=0.25,relwidth=0.60,relheight=0.55)

    login_l1=tk.Label(frame,text='LOGIN WINDOW',font=("Courier",25),height=1,width=70,relief= tk.RAISED,bg='#00ffff')
    login_l1.place(relx=0,rely=0,relwidth=1.0,relheight=1.0)
    win1.destroy()
    
    login_entry()


def window2():
    global ent1,ent2,ent3
    global win3,but_equal1,frame,frame2,frame1
    lable=tk.Label(frame1,text='ENTER THE userID',bg='#b3ffff')
    lable.place(relx=0,rely=0,relwidth=0.3,relheight=0.2)
    lable1=tk.Label(frame1,text='ENTER THE USERNAME',bg='#b3ffff')
    lable1.place(relx=0,rely=0.2,relwidth=0.3,relheight=0.2)
    lable2=tk.Label(frame1,text='ENTER THE PASSWORD',bg='#b3ffff')
    lable2.place(relx=0,rely=0.4,relwidth=0.3,relheight=0.2)
    ent1=tk.Entry(frame1,textvariable='v',width=15,borderwidth=5,font=('Calculator',27,'bold'),bg='#f2f2f2')
    ent1.place(relx=0.3,rely=0,relwidth=0.7,relheight=0.2)
    ent2=tk.Entry(frame1,width=15,borderwidth=5,font=('Calculator',27,'bold'),bg='#f2f2f2')            
    ent2.place(relx=0.3,rely=0.2,relwidth=0.7,relheight=0.2)
    ent3=tk.Entry(frame1,width=15,borderwidth=5,font=('Calculator',27,'bold'),bg='#f2f2f2')
    ent3.place(relx=0.3,rely=0.4,relwidth=0.7,relheight=0.2)
    but_equal=tk.Button(frame1,text='SUBMIT',padx=134,pady=12,fg='black',bg='#66ff99',font=('ariel',15),command=add_to_login)
    but_equal.place(relx=0.55,rely=0.85,relwidth=0.4,relheight=0.12)

    win3.mainloop() 


def registration():
   
    global win3,frame,frame1,frame2
    win3=tk.Tk()
    win3.title('AVA REGISTRATION')
    win3.geometry("1920x1080")
    win3.configure(background='#404040')
    # img =Image.open('C:/Users/91789/Downloads/abstract-1779608_1920.png')
    # img =img.resize((1520,970))
    # img =ImageTk.PhotoImage(img)
    # img_back=tk.Label(win3, image=img)
    # img_back.place(x=0,y=0)
    #ffe6ff


    win1.destroy()
    frame=tk.Frame(win3,height=10,width=200)
    frame.place(relx=0.2,rely=0.1,relwidth=0.60,relheight=0.1)
    frame1=tk.Frame(win3,relief= tk.RAISED,bg='#ffd6cc')
    frame1.place(relx=0.2,rely=0.3,relwidth=0.60,relheight=0.45)
    
    reg_l1=tk.Label(frame,text='REGISTER WINDOW',font=('Comic Sans MS',20),relief= tk.RAISED,bg='#33ffd6')
    reg_l1.place(relx=0,rely=0,relwidth=1.0,relheight=1.0)
    backbut=tk.Button(frame1,text='BACK',font=('ariel',15),bg='#ff4d4d',fg='black',command=lambda: startingwindow('win3'))
    backbut.place(relx=0.05,rely=0.85,relwidth=0.4,relheight=0.12)
    window2()

def show_classes():
    global listbox,win20

    win20=tk.Tk()
    win20.title('search question')
    win20.geometry("1920x1080")
    win20.configure(background='#c2e4ff')
    frame=tk.Frame(win20,padx=10,pady=10,bg='white')
    frame.place(relx=0.1,rely=0.05,relwidth=0.80,relheight=0.8)
    label=tk.Label(frame,text="ALL CLASSES",bg='#2929a3',fg='white',font=('Helvetica',20))
    label.place(relx=0.3,rely=0.0,relwidth=0.40,relheight=0.1)
    label=tk.Label(win20,text="click on the class you want and the press the select button",bg='white',fg='blue',font=('Helvetica',20))
    label.place(relx=0.1,rely=0.85,relwidth=0.80,relheight=0.08)
    scrollbar =tk.Scrollbar(frame)
    scrollbar.place(relx=0.91,rely=0.2,relwidth=0.03,relheight=0.6)
    listbox =tk.Listbox(frame,yscrollcommand = scrollbar.set)
    listbox.place(relx=0.05,rely=0.2,relwidth=0.85,relheight=0.6)
    but=tk.Button(frame,text='SELECT CLASS',width=10,borderwidth=2,relief="ridge",command=get,bg='#2355de',fg='WHITE')
    but.place(relx=0.05,rely=0.9,relwidth=0.30,relheight=0.08)
    but=tk.Button(frame,text='BACK',width=10,borderwidth=2,relief="ridge",command=lambda :select_class(20),bg='#ff4d4d',fg='black')
    but.place(relx=0.65,rely=0.9,relwidth=0.30,relheight=0.08)
    n=0
    L='select * from userclasses'
    cur.execute(L)
    L=cur.fetchall()
    for values in L:
        Class=str(values[1])
        subject=str(values[2])
        value=Class+' '+subject
        listbox.insert(n,value)
        n+=1
    listbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox.yview)
    win7.destroy()
def class_check():
    global Class,subject
    win7.destroy()
    if str(Class.get())=='SELECT CLASS' or str(subject.get())=='SELECT SUBJECT':
        select_class(10)

    
    else:

        query='select subject from userclasses where class='+str(Class.get())
        cur.execute(query)
        result=cur.fetchall()
        op2=[]

        for i in result:
            op2.append(str(i[0]))
        print(op2)
        print(subject.get())
        if str(subject.get()) in op2:
            Class=str(Class.get())
            subject=str(subject.get())
            options_window(1)
        else:
            Class=str(Class.get())
            subject=str(subject.get())
            select_class(0)
 
link=[]
def get():
    global userline,Class,subject
    userline=listbox.get('active')
    col=userline.split()
    Class=col[0]
    subject=col[1]
    options_window(20)


def select_class(n):
    global drop,drop1,Class,subject,win7,frame,j
    win7=tk.Tk()
    win7.title('SELECT CLASS WINDOW')
    win7.geometry("1920x1080")  
    win7.configure(background='#ffffff')
    if n==20:
        win20.destroy()
    if n==1:
        win2.destroy()  
    if n==2:
        win1.destroy()
    if n==4:
        win4.destroy()
    z2="select user_name from logintable where userID="+str(userID)
    cur.execute(z2)
    y=cur.fetchall()
    frame=tk.Frame(win7,relief= tk.RAISED,height=100,width=150,bg='#c2e4ff')
    frame.place(relx=0.0,rely=0.0,relwidth=0.10,relheight=1)
    frame=tk.Frame(win7,relief= tk.RAISED,height=100,width=150,bg='#c2e4ff')
    frame.place(relx=0.9,rely=0.0,relwidth=0.10,relheight=1)
    frame=tk.Frame(win7,relief= tk.RAISED,height=100,width=150,bg='#d9eeff')
    frame.place(relx=0.05,rely=0.0,relwidth=0.05,relheight=1)
    frame=tk.Frame(win7,relief= tk.RAISED,height=100,width=150,bg='#d9eeff')
    frame.place(relx=0.9,rely=0.0,relwidth=0.05,relheight=1)
    lab1=tk.Label(win7,text='HELLO '+y[0][0],font=('arial',20),relief= tk.RAISED,bg='#c4fff9')
    lab1.place(relx=0.35,rely=0.02,relwidth=0.3,relheight=0.1)
    frame=tk.Frame(win7,relief= tk.RAISED,bg='#005687')
    frame.place(relx=0.2,rely=0.2,relwidth=0.60,relheight=0.6)
    but_equal=tk.Button(frame,text='VIEW ALL CLASSES',fg='black',bg='#c2e4ff',font=('ariel',10),command=show_classes)
    but_equal.place(relx=0.3,rely=0.02,relwidth=0.4,relheight=0.08)
    lab1=tk.Label(frame,text='CLASS',font=('arial',20),relief= tk.RAISED,bg='#c4fff9')
    lab1.place(relx=0.05,rely=0.15,relwidth=0.4,relheight=0.15)
    lab2=tk.Label(frame,text='SUBJECT',font=('arial',20),relief= tk.RAISED,bg='#c4fff9')
    lab2.place(relx=0.55,rely=0.15,relwidth=0.4,relheight=0.15)
    cl='select distinct class from userclasses'
    cur.execute(cl)
    cla=cur.fetchall()
    su='select distinct subject from userclasses'
    cur.execute(su)
    sub=cur.fetchall()
    subj=['SELECT SUBJECT']
    clas=['SELECT CLASS']
    for i in cla:
        s=i[0]
        clas.append(s)
    for j in sub:
        s=j[0]
        subj.append(s)
    Class=tk.StringVar(win7)
    subject=tk.StringVar(win7)
    if len(cla)!=0 and len(sub)!=0:
        Class.set(clas[0])
        Class.trace("w",change)
        subject.set(subj[0])
        subject.trace("w",change)
        drop=tk.OptionMenu(frame,Class,*clas)
        drop.config(width = 20)
        drop.place(relx=0.05,rely=0.35,relwidth=0.4,relheight=0.1)
        drop1=tk.OptionMenu(frame,subject,*subj)
        drop1.config(width = 20)
        drop1.place(relx=0.55,rely=0.35,relwidth=0.4,relheight=0.1)
        if n==10:
            login_l1=tk.Label(frame,text='SELECT A CLASS AND SUBJECT',font=('arial',20),relief= tk.RAISED,bg='#69ff98')
            login_l1.place(relx=0.2,rely=0.5,relwidth=0.6,relheight=0.08)
        if n==0:
            login_l1=tk.Label(frame,text='THE SELECTED CLASS DOESNT EXIST',font=('arial',20),relief= tk.RAISED,bg='#69ff98')
            login_l1.place(relx=0.2,rely=0.5,relwidth=0.6,relheight=0.08)
    if len(cla)==0:
        login_l1=tk.Label(frame,text='NO CLASS EXIST\n ADD A CLASS',font=('arial',20),relief= tk.RAISED,bg='#69ff98')
        login_l1.place(relx=0.2,rely=0.33,relwidth=0.6,relheight=0.15)

    but_equal=tk.Button(frame,text='SUBMIT',fg='black',bg='#66ff99',font=('ariel',10),command=class_check)
    but_equal.place(relx=0.3,rely=0.65,relwidth=0.4,relheight=0.1)
    but_equal1=tk.Button(frame,text='ADD A CLASS',fg='white',bg='#9a00c9',font=('ariel',10),command=add_new_class)
    but_equal1.place(relx=0.3,rely=0.8,relwidth=0.4,relheight=0.1)
    win7.mainloop()
def startingwindow(window):
    global but1,but2,win1,img
    if window!='0':
        win1=tk.Tk()
        win1.title('AVA QUESTION BANK')
        win1.geometry("1920x1080")  
        win1.configure(background='white')
        # abstract-1779608_1920.png
    # canvas = tk.Canvas(win1,width=1550,height=1080,bg='black')
    # img =Image.open('C:/Users/91789/Downloads/book-5077895_1920.jpg')
    # img =img.resize((1535,970))
    # img =ImageTk.PhotoImage(img)
    # img_back=tk.Label(win1, image=img)
    # img_back.place(x=0,y=0)
    # frame=tk.Frame(win1,bg='#03f4fc')
    # frame.place(relx=0.0,rely=0.0,relwidth=0.1,relheight=1)
    # frame=tk.Frame(win1,bg='#03f4fc')
    # frame.place(relx=0.9,rely=0.0,relwidth=0.1,relheight=1)
    frame=tk.Frame(win1,bg='#1a1a1a')
    frame.place(relx=0.0,rely=0.0,relwidth=1,relheight=0.5)
    frame=tk.Frame(win1,bg='white')
    frame.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.35)
    frame=tk.Frame(win1,bg='#1a1a1a')
    frame.place(relx=0.0,rely=0.45,relwidth=1,relheight=0.55)
    frame=tk.Frame(win1,bg='white')
    frame.place(relx=0.05,rely=0.5,relwidth=0.9,relheight=0.4)
    # frame=tk.Frame(win1,bg='#03f4fc')
    # frame.place(relx=0.0,rely=0,relwidth=1,relheight=0.1)
    # frame=tk.Frame(win1,bg='#1a1a1a')
    # frame.place(relx=0.0,rely=0.0,relwidth=0.1,relheight=1)
    # frame=tk.Frame(win1,bg='#1a1a1a')
    # frame.place(relx=0.9,rely=0.0,relwidth=0.1,relheight=1)
    label1=tk.Label(win1,text='AVA QUESTION BANK',font=('Times New Roman',30),relief= tk.RAISED,bg='#00ffea')
    label1.place(relx=0.2,rely=0.15,relwidth=0.6,relheight=0.15)
    but1=tk.Button(win1,text='LOGIN',font=('ariel',15),height=3,width=15,bg="#69ff96",command=login,relief= tk.RIDGE,padx=50)
    but1.place(relx=0.35,rely=0.6,relwidth=0.3,relheight=0.08)
    but2=tk.Button(win1,text='REGISTER',font=('ariel',15),height=3,width=15,bg='#b978ff',command=registration,relief= tk.RIDGE,padx=50)
    but2.place(relx=0.35,rely=0.75,relwidth=0.3,relheight=0.08)
    # labelspace=tk.Label(frame2,text='',height=10,width=15,bg='black')
    # labelspace.grid(row=1,column=1)
    # labelspace1=tk.Label(frame2,text='',height=10,width=15,bg='black')
    # labelspace1.grid(row=1,column=3)
    # labelspace2=tk.Label(frame2,text='',height=10,width=15,bg='black')
    # labelspace2.grid(row=1,column=5)
    # img1 =Image.open('C:/Users/91789/Downloads/books-3446451_1920.png')
    # img1 =img1.resize((300, 300), Image.ANTIALIAS)
    # img1=ImageTk.PhotoImage(img1)
    # panel=tk.Label(win1, image=img1)
    # panel.image = img1
    # panel.place(relx=0.05,rely=0.6,relwidth=0.25,relheight=0.3)
    # img =Image.open('C:/Users/91789/Downloads/book-5077895_1920.jpg')
    # img =img.resize((300, 300), Image.ANTIALIAS)
    # img =ImageTk.PhotoImage(img)
    # panel=tk.Label(win1, image=img)
    # panel.image = img
    # panel.place(relx=0.7,rely=0.6,relwidth=0.25,relheight=0.3)

    if window=='win2':
        win2.destroy()
    elif window=='win3':
        win3.destroy()
    elif window=='win4':
        win4.destroy()
    elif window=='win4':
        win3.destroy()
    elif window=='win3':
        win3.destroy()
    win1.mainloop()



startingwindow('1')
 
