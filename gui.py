from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import tkinter
from tkinter.scrolledtext import ScrolledText
from socket import *
from time import sleep
import socket
from threading import Thread
from tkinter.messagebox import askyesno
import sys
class gui_main:
    def __init__(self,root):
        self.frame1=Frame(root,bg="#90EE90")
        self.frame1.place(x=0,y=0,width=2600,height=1600)
        self.login()
    def login(self):
        self.frame2=Frame(self.frame1)
        self.frame2.place(x=500,y=100,height=600,width=600)
        self.label3=Label(self.frame2,text="login",font=("bold",32))
        self.label3.place(x=250,y=20)
        self.label1=Label(self.frame2,text="username:",font=("bold",25))
        self.label1.place(x=70,y=140)
        self.label2=Label(self.frame2,text="otp          :",font=("bold",25))
        self.label2.place(x=70,y=240)
        self.entry=Entry(self.frame2,font=("bold"))
        self.entry.place(x=240,y=149,width=230,height=30)
        self.entry2=Entry(self.frame2,font=("bold"))
        self.entry2.place(x=240,y=249,width=230,height=30)
        self.button=Button(self.frame2,text="submit",font=("bold",20),relief=GROOVE,command=self.check_login)
        self.button.place(x=200,y=340,width=130,height=40)
    def check_login(self):
        self.getname=[]
        self.getvar1=self.entry.get()
        self.getvar2=self.entry2.get()
        if('a'<=self.getvar1[0]<='z' or 'A'<=self.getvar1[0]<='Z'):
            self.getname.append(self.getvar1)
        else:
            messagebox.showerror("error","username starting letter should only start with letter a-z A-Z")
        if(self.getvar2=="a"):
            messagebox.showerror("error ","client not connected wait for 60 sec")
            self.connect_to()
        else:
            messagebox.showerror("error","enter otp correctly")
    def connect_to(self):
        t1=Thread(target=self.con)
        t1.start()
    def con(self):
        try:
            self.t=0
            self.soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            r=askyesno("info","do you want to wait for 60s or exit ")
            if(r):
                self.soc.settimeout(120)
            else:
                sys.exit(0)
            print("wairting")
            self.ip="192.168.43.174"
            self.port=4444
            self.soc.bind((self.ip,self.port))
            self.soc.listen(0)
            self.cons,self.add=self.soc.accept()
            print("connected")
            self.t=1
        except:
            print("what")
        if(self.t==0):
            messagebox.showerror("error ","sorry client is not reponded")
            self.login()
        else:
            messagebox.showinfo("sucess","connected")
            self.main_page()

    def main_page(self):
        self.frame3=Frame(self.frame1)
        self.frame3.place(x=0,y=0,width=2600,height=1600)
        self.text=ScrolledText(self.frame3,cursor="arrow",font=("bold",16))
        self.text.place(x=10,y=0,height="690",width="1500")
        self.text1=ScrolledText(self.frame3,font=("bold",19),fg="black",bg="white")
        self.text1.place(x=150,y=704,width=1250,height=40)
        self.label4=Label(self.frame3,text="message:",font=("bold",22))
        self.label4.place(x=10,y=705)
        self.t2=Thread(target=self.recive_data)
        self.t2.start()
        self.button1=Button(self.frame3,text=">>>",font=("bold",15),bg="light green",command=self.insert_into)
        self.button1.place(x=1400,y=705,width=100,height=40)
    def rcvt(self):
        self.t2=Thread(target=self.recive_data)
        self.t2.start()
    def insert_into(self):
        n=100
        self.text.config(state=NORMAL)
        self.tex=self.text1.get(1.0,END)
        self.text1.delete(1.0,END)
        self.rcvt()
        self.send_data(self.tex)
    def send_data(self,data):
        self.data=data.encode()
        self.cons.send(self.data)
        self.text.insert(INSERT,f"\t\t\t\t\t\t\t\t\t\t\t\t\t{self.tex}")
        self.text.config(state=DISABLED)
    def recive_data(self):
        self.rc=self.cons.recv(1000)
        self.text.config(state=NORMAL)
        while(self.rc):
            self.data=self.rc.decode()
            self.text.insert(INSERT,f"{self.data}")
            self.rc=self.cons.recv(1000)
        self.text.config(state=DISABLED)
        sleep(1)
        
root=tkinter.Tk()
root.geometry("2600x1600")
gui_main(root)
root.mainloop()