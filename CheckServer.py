import socket
import ssl
from datetime import datetime 
import pickle
import subprocess
import platform
import requests


class Server():
    def __init__(self, name, port, connection, priority):
        self.name=name
        self.port=port
        self.connection=connection.lower()
        self.priority=priority.lower()
        self.history=[]
        self.alert=False
    
    def check_connection(self):
        msg=""
        success=False
        now=datetime.now()

        try:
            if(self.connection=="plain"):
                socket.create_connection((self.name, self.port), timeout=8)
                msg="{} is up on port {} with {}".format(self.name, self.port, self.connection)
                success=True
            elif (self.connection=="ssl"):
                ssl.wrap_socket(socket.create_connection((self.name, self.port), timeout=8))
                msg="{} is up on port {} with {}".format(self.name, self.port, self.connection)
                success=True
            else:
                if(self.ping()):
                    msg="{} is up on port {} with {}".format(self.name, self.port, self.connection)
                    success=True
                else:
                    msg="{} is not reachable".format(self.name)
        except socket.timeout:
            msg= "Server: {} timeout on port {}".format(self.name, self.port)
        except Exception as e:
            msg="Server had this error: {}".format(e)
        self.create_history(msg, success, now)
    
    def create_history(self, msg, success, time):
        with open("history.txt", 'a') as f:
            f.write(msg)
            f.write("\n")
            f.write("Time: {}\nSuccess Status: {}\n".format(time, success))
            f.write("___________________________")
            f.write("\n")

    def ping(self):
        try:
            request=requests.get(self.name, timeout=5)
            return True
        except:
            return False
            pass

if __name__ == '__main__':
    servers= [
        Server("reddit.com", 80, "plain", "low"),
        Server("anthonycalo.com", 443, "ssl", "low"),
        Server("calochess.com", 80, "plain", "low"),
        Server("192.168.1.18", 80, "ping", "high")
    ]
    addServer = input("Would you like to add a server(yes or no): ")
    if(addServer.lower()=="yes"):
        servername=input("Enter server name: ")
        port =int(input("Enter port number: "))
        connection=input("Enter a type ping/ssl/plain: ")
        priority=input("Enter priority high/ low: ")
        servers.append(Server(servername, port, connection, priority))
        
    for server in servers:
        server.check_connection()








