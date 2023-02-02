import socket
import sqlite3 as mysql
from threading import Thread
from time import sleep
try:
    mysql.connect('store.db')
except:
    pass
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind(("192.168.43.174",4444))
print("waiting for connection")
soc.listen(0)
con,addr=soc.accept()
print("connection got from:",addr)
def sends():
    while(True):
        data=input("enetr a data")
        data=data.encode()
        con.send(data)
def recive():
    data=con.recv(1000)
    while(data):
        print("\t\t\t\t",data.decode())
        data=con.recv(1000)
    sleep(5)

t1=Thread(target=recive)
t1.start()
sends()
con.close()


