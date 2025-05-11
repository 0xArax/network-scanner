import socket
import threading
import argparse


def scanport(ip,port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip,port))
        print(f"[+] Port {port} is open {ip}")
        s.close()
    except:
        pass


def scan_range(ip):
    for port in range(1,1025):
        t = threading.Thread(target=scanport,args=(ip,port))
        t.start()

