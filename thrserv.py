from socket import *
from threading import *
from tkinter import *

port=0
host=""

my_alias=""
your_alias=""
class Receive(Thread):
    def run(self):
       while True:
        x=sk.recv(1000)
        if (x!=b''):
            x=x.decode()
            
            global root
            x=your_alias+">"+x
            db.insert(END,x)
            db.itemconfig(END,{"fg":"red"})
            db.pack(side=LEFT)     
def fix(hx,px):
    global host
    global port
    host=hx
    port=px

def connect(port):
    wait_box=Tk()
    l=Label(wait_box,text="Waiting for connection")
    l.pack()
    global sk
    global my_alias
    global your_alias
    c=socket(AF_INET,SOCK_STREAM)
    c.bind((host,port))
    c.listen(1)
    sk,addr=c.accept()
    y=my_alias
    y=y.encode()
    sk.send(y)
    x=sk.recv(100)
    x=x.decode()
    your_alias=x
    wait_box.destroy()  
def thread_start():
    obj1=Receive()
    obj1.start()

def send_msg():
    global root
    x=sendmsg.get()
    x=x.encode()
    sk.send(x)
    x=x.decode()
    x=my_alias+">"+x
    db.insert(END,x)
    db.itemconfig(END,{"fg":"blue"})
    db.pack(side=LEFT)
  
def create_root():
    global root
    global sendmsg
    global flag
    global db
    root=Tk()
    sendmsg=StringVar(root)
    root.title("Connected!!")   
    m_sent=Label(root,text="Type a message")
    m_entry=Entry(root,textvariable=sendmsg)
    send_button=Button(root,text="Send",command=send_msg)
    m_sent.pack()
    m_entry.pack()
    send_button.pack()
    scroll = Scrollbar(root)
    scroll.pack(side=RIGHT,fill=Y)
    db=Listbox(root,yscrollcommand=scroll.set)
    db.pack(side=LEFT)
    scroll.config(command=db.yview)
    root.mainloop()

def main_f(hx,px,ax):
    global my_alias
    my_alias=ax
    fix(hx,px)
    connect(port)
    thread_start()
    create_root()