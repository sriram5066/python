import socket
import sqlite3 as mysql
from threading import Thread
from time import sleep
try:
    mysql.connect('store.db')
except:
    pass
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect(("192.168.43.174",4444))
print("connected")
def sends():
    while(True):
        data=input("enter a data")
        data=data.encode()
        soc.send(data)
def recvs():
    data=soc.recv(1000)
    while(data):
        print(f"\t\t\t\t\t{data.decode()}")
        data=soc.recv(1000)
    sleep(1)
t1=Thread(target=recvs)
t1.start()
sends()
soc.close()


