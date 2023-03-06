import subprocess
import socket
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from threading import Thread
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout
from kivy.uix.layout import Layout
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from time import sleep
from kivy.clock import Clock
class mainwid(PageLayout):
    def connect(self):
        self.layout=BoxLayout(padding=50,spacing=20,orientation="vertical")
        self.l=Label(text="please enter the ip of pc")
        self.layout.add_widget(self.l)
        self.text=TextInput(size_hint=(.7,.1),pos_hint={"center_x":.5})
        self.layout.add_widget(self.text)
        self.but=Button(text="close",size_hint=(.2,.2),pos_hint={"center_x":.5,"y":.4})
        self.layout.add_widget(self.but)
        
        self.pop=Popup(title=("get_ip"),content=self.layout)
        self.pop.open()
        self.but.bind(on_press=self.dis)
    def dis(self,i):
        self.ip=self.text.text
        if(self.ip):
            self.pop.dismiss()
            self.connects(str(self.ip))
        else:
            self.lay=BoxLayout(orientation="vertical")
            self.ls=Label(text="please enter the ip")
            self.lay.add_widget(self.ls)
            self.buts=Button(text="close",size_hint=(.2,.2),pos_hint={"center_x":.5,"y":.4})
            self.lay.add_widget(self.buts)
            self.pops=Popup(title="error ip",content=self.lay)
            self.pops.open()
            self.buts.bind(on_press=self.end)
    def connects(self,ip):
        self.soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ip=ip
        self.port=4444
        self.soc.connect((self.ip,self.port))
    def end(self,i):
        self.pops.dismiss()
            
    def ishutdown(self):
        try:
            self.msg="ishut"
            self.msg=self.msg.encode()
            self.soc.send(self.msg)
        except(Exception):
            return mainwid()
    def irestart(self):
        try:
            self.msg="irestart"
            self.msg=self.msg.encode()
            self.soc.send(self.msg)
        except(Exception):
            return mainwid()
    def whatsapp(self):
        try:
            self.msg="whatsapp"
            self.msg=self.msg.encode()
            self.soc.send(self.msg)
        except(Exception):
            return mainwid()
    def wifi(self):
        try:
            self.msg="wifi"
            self.msg=self.msg.encode()
            self.soc.send(self.msg)
        except(Exception):
            return mainwid()
    def document(self):
        try:
            self.msg="document"
            self.msg=self.msg.encode()
            self.soc.send(self.msg)
        except(Exception):
            return mainwid()
    def desktop(self):
        try:
            self.msg="desktop"
            self.msg=self.msg.encode()
            self.soc.send(self.msg)
        except(Exception):
            return mainwid()
    def sleep(self):
        try:
            self.msg="sleep"
            self.msg=self.msg.encode()
            self.soc.send(self.msg)
        except(Exception):
            return mainwid()
    def logout(self):
        try:
            self.msg="logout"
            self.msg=self.msg.encode()
            self.soc.send(self.msg)
        except(Exception):
            return mainwid()
    def devc(self):
        try:
            self.msg="devc"
            self.msg=self.msg.encode()
            self.soc.send(self.msg)
        except(Exception):
            return mainwid()
class mainapp(App):
    def build(self):
        return mainwid()
mainapp().run()