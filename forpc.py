import socket
import subprocess
from time import sleep
import pyautogui
from PIL import Image
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox  
class pc:
    def __init__(self,root):
        self.soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.hostname=socket.gethostname()
        self.ip=socket.gethostbyname(self.hostname)
        self.ip=str(self.ip)
        self.port=4444
        self.create_ip()
    def create_ip(self):
        self.button=Button(root,text="show ip",command=self.ips)
        self.button.place(x=0,y=0,height=500,width=500)
    def ips(self):
            messagebox.showinfo(title="message for ip address",message=f"the ip address of client is {self.ip}")
            messagebox.showinfo(title="wait",message="wait until if client connected you get a message")
            root.destroy()
            self.connect()
    def connect(self):
            self.soc.bind((str(self.ip),self.port))
            self.soc.listen(10)
            self.con,self.add=self.soc.accept()
            self.get_execute()
    def get_execute(self):
        r=self.con.recv(1000)
        while(r):
            r=r.decode()
            if(r=="shutdown"):
                subprocess.call("shutdown /s",shell=True)
            elif(r=="logout"):
                subprocess.call("shutdown /l",shell=True)
            elif(r=="sleep"):
                subprocess.call("shutdown /h",shell=True)
            elif(r=="restart"):
                subprocess.call("shutdown /r",shell=True)
            elif(r=="desktop"):
                sleep(2)
                pyautogui.moveTo(1919,1042)
                pyautogui.leftClick()
            elif(r=="devc"):
                sleep(1)
                pyautogui.moveTo(1359,1059)
                pyautogui.leftClick()
            elif(r=="whatsapp"):
                sleep(1)
                pyautogui.moveTo(1300,1046)
                pyautogui.leftClick()
            elif(r=="document"):
                sleep(1)
                pyautogui.moveTo(1084,1052)
                pyautogui.leftClick()
            elif(r=="wifi"):
                sleep(1)
                pyautogui.moveTo(1730,1049)
                pyautogui.leftClick()
                sleep(1)
                pyautogui.leftClick(1787,693)
            elif(r=="ishut"):
                sleep(1)
                pyautogui.moveTo(497,1043)
                pyautogui.leftClick()
                sleep(1)
                pyautogui.leftClick(1266,952)
                sleep(1)
                pyautogui.leftClick(1287,857)
                sleep(1)
                pyautogui.leftClick(1266,952)
            elif(r=="irestart"):
                sleep(1)
                pyautogui.leftClick(493,1049)
                sleep(1)
                pyautogui.leftClick(1265,964)
                sleep(1)
                pyautogui.leftClick(1255,904)
            else:
                pass
            r=self.con.recv(1000)
root=Tk()
root.geometry("500x500")
o=pc(root)
root.mainloop()