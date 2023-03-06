import socket
import subprocess
from time import sleep
import pyautogui
from PIL import Image
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from threading import Thread
import sqlite3 as sq
class pc:
    def __init__(self,root):
        try:
            self.con=sq.connect("pos.db",check_same_thread=False)
        except:
            pass
        self.c=self.con.cursor()
        self.frame=Frame(root)
        self.frame.place(x=0,y=0,width=1200,height=800)
        self.l1=Label(root,text="Show Ip:",font=("Bold",20))
        self.l1.place(x=300,y=70)
        self.but=Button(text="Click to show  server ip",font=("bold",20),command=self.show_ip)
        self.but.place(x=470,y=50)
        self.l=Label(text="enter the icon_name: \n\t(Eg:windows) ",font=("Bold",20))
        self.l.place(x=55,y=130)
        self.ent=Entry(root,font=("bold",20))
        self.ent.place(x=470,y=130,width=335,height=40)
        self.but1=Button(root,text="Submit",font=("bold",20),command=self.find_cursor)
        self.but1.place(x=470,y=230,width=200,height=50)
        self.but=Button(text="open connection",font=("bold",20),command=self.connect)
        self.but.place(x=890,y=50)
    def find_cursor(self):
        if(self.ent.get()):
            messagebox.showinfo(title="info",message=f"point the cursor to {self.ent.get()} icon\nview for the photo refernce")
            self.but1=Button(root,text="Help",font=("bold",20),command=self.display)
            self.but1.place(x=470,y=330,width=200,height=50)
            self.create_table(self.ent.get())
        else:  
            messagebox.showerror(title="error",message="icon name should not empty")
    def display(self):
        messagebox.showinfo(title="help",message=f"move the cursor to {self.ent.get()} icon on your pc")
    def show_ip(self):
        self.host=socket.gethostname()
        self.ip=socket.gethostbyname(self.host)
        messagebox.showinfo(title="ip",message=f"ip address of server is {self.ip}")
    def connect(self):
        self.t=Thread(target=self.run_con)
        self.t.start()
    def run_con(self):
        try:
            self.host=socket.gethostname()
            self.ip=socket.gethostbyname(self.host)
            self.soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.soc.bind((str(self.ip),4444))
            messagebox.showinfo(title="info",message="wiatig for client to conect")
            self.soc.listen(0)
            self.soc,self.add=self.soc.accept()
            messagebox.showinfo(title="connected",message="connected")
            self.t2=Thread(target=self.recive)
            self.t2.start()
        except(Exception):
            pass
    def create_table(self,data):
        try:
            self.create="create table position(name varchar,pos_x int ,pos_y int)";
            self.c.execute(self.create)
            print("tale created")
            self.store_name_pos(data)
        except(Exception):
            self.store_name_pos(data)
    def store_name_pos(self,data):
        self.get_name=data
        messagebox.showinfo(title="info",message=f"please move cursor to {self.ent.get()} icon in 5sec\n wait until pop is appeard")
        sleep(5)
        self.pos=pyautogui.position()
        messagebox.showinfo(title="pos",message=f"the pos of {self.ent.get()} is {self.pos[0]} {self.pos[1]}")
        self.insert="insert into position(name,pos_x,pos_y)values('{}','{}','{}');".format(self.ent.get(),self.pos[0],self.pos[1])
        self.c.execute(self.insert)
        messagebox.showinfo(title="inserted",message="inserted the name and pos")
        self.get="select * from position;"
        self.c.execute(self.get)
        self.con.commit()
    def recive(self):
        self.rcv()
    def rcv(self):
            self.list=['shutdown','logout','restart','sleep']
            self.r=self.soc.recv(10)
            self.r=self.r.decode()
            while(self.r):
                if(self.r =='shutdown'):
                    subprocess.call("shutdown -s -t 00",shell=True)
                elif(self.r=='restart'):
                    subprocess.call("shutdown -r -t 00",shell=True)
                elif(self.r=="logout"):
                    subprocess.call("shutdown -l -t 00",shell=True)
                else:
                    self.ex=f"select pos_x,pos_y from position where name='{self.r}'"
                    self.res=self.c.execute(self.ex)
                    self.res=self.c.fetchall()
                    sleep(3)
                    self.p=pyautogui.leftClick(self.res[0][0],self.res[0][1])
                    self.r=self.soc.recv(1000)

            
root=Tk()
root.geometry("1200x400")
root.resizable(0,0)
o=pc(root)
root.mainloop()