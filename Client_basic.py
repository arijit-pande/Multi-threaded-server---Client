#!usr/bin/python
import socket,sys
def main():
    if(len(sys.argv)!=3):
        print "Usage:Client_basic <server ip> <port number> "
        sys.exit(0) 
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((sys.argv[1],int(sys.argv[2])))
    while True:
        print "send a msg(type exit to terminate)"
        x=raw_input()
        if x=='exit':
            break
        else:
            s.send(x)
        

if __name__=='__main__':
    main()
    
