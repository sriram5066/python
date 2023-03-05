from tkinter import *
import socket 
from tkinter import messagebox
from time import sleep
from threading import Thread
from tkinter.messagebox import askyesno
import sys
from tkinter.scrolledtext import ScrolledText
class gui_cli:
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
        self.button=Button(self.frame2,text="submit",font=("bold",20),relief=GROOVE,command=self.connection_check)
        self.button.place(x=200,y=340,width=130,height=40)
    def thread_con(self):
        self.t1=Thread(target=self.connection_check)
        self.t1.start()
    def connection_check(self):
        try:
            self.t=0
            self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.ip="192.168.248.174"
            self.port=4444
            r=askyesno("report","server is not open do you want to wait for few min")
            if(r):
                self.sock.settimeout(130)
            else:
                sys.exit(0)
            self.r=self.sock.connect((self.ip,self.port))
            self.t=1
        except Exception as ex:
            print(str(ex))
            
        finally:
            if(self.t==0):
                messagebox.showerror("error","server is not opend")
            else:
                self.main_page() 
    def main_page(self):
        self.frame3=Frame(self.frame1)
        self.frame3.place(x=0,y=0,width=2600,height=1600)
        self.text=ScrolledText(self.frame3,cursor="arrow",font=("bold",16))
        self.text.place(x=10,y=0,height="690",width="1500")
        self.text1=ScrolledText(self.frame3,font=("bold",19),fg="black",bg="white",wrap="word")
        self.text1.place(x=150,y=704,width=1250,height=40)
        self.label4=Label(self.frame3,text="message:",font=("bold",22))
        self.label4.place(x=10,y=705)
        self.t2=Thread(target=self.rcv)
        self.t2.start()
        self.button1=Button(self.frame3,text=">>>",font=("bold",15),bg="light green",command=self.sends)
        self.button1.place(x=1400,y=705,width=100,height=40) 
    def insert_into(self):
        self.t2=Thread(target=self.rcv)
        self.t2.start()
    def sends(self):
        self.text.config(state=NORMAL)
        self.send_data=self.text1.get(1.0,END)
        self.send_data=self.send_data.encode()
        self.sock.send(self.send_data)
        self.t=self.text.get("1.0",END)
        self.text.insert("1.0", self.send_data)
        self.text.tag_config("right",justify="right")
        self.text.tag_add("right","1.0","end")
        self.text1.delete(1.0,END)
        self.text.config(state=DISABLED)
        self.insert_into()
    def rcv(self):
        self.r=self.sock.recv(1000)
        self.r=self.r.decode()
        self.text.config(state=NORMAL)
        while(self.r):
            self.text.insert(INSERT,self.r)
            self.r=self.sock.recv(1000)
        self.text.config(state=DISABLED)
        sleep(1)
root=Tk()
root.geometry("2600x1600")
o=gui_cli(root)
root.mainloop()