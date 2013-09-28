import socket,sys
from thread import *
def handleClient(conn,addr):
    while True:
        print "data recieved from:",addr
        x=conn.recv(1024)
        print "data received=",x
        
def main():
    if len(sys.argv)!=2:
        print "Usage MultiClientServer.py <port number>"
        sys.exit(0)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    HOST=''
    PORT=int(sys.argv[1])
    s.bind((HOST,PORT))
    s.listen(5)
    while True:
        conn,addr=s.accept()
        start_new_thread(handleClient,(conn,addr,))
if __name__=='__main__':
    main()
