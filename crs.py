from tkinter import *
from socket import *
import thrserv
#Initiating Socket
def con_main():
    hostx=hostname.get()
    portx=int(port.get())
    aliasx=alias.get()
    root.destroy()
    thrserv.main_f(hostx,portx,aliasx)    
#GUI_Devlopment  
def mainf():
    global root
    root=Tk()
    root.title("Connector")
    root.geometry("250x190")
    global port
    global alias
    global hostname
    port=StringVar(root)
    alias=StringVar(root)
    
    hostname=StringVar(root)
    host_label=Label(root,text="Enter Your Net IP :")
    host_entry=Entry(root,textvariable=hostname)
    
    port_label=Label(root,text="Enter Port :")
    port_entry=Entry(root,textvariable=port)
    alias_label=Label(root,text="Enter Your Alias :")
    alias_entry=Entry(root,textvariable=alias)
    
    main_button=Button(root,text="Start",command=con_main)

#Gridding
    
    host_label.grid(row=0,column=0,pady=5,padx=5,sticky=W)
    host_entry.grid(row=0,column=1,pady=5)
    
    port_label.grid(row=1,column=0,pady=5,padx=5,sticky=W)
    port_entry.grid(row=1,column=1,pady=5)
    alias_label.grid(row=2,column=0,pady=5,padx=5,sticky=W)
    alias_entry.grid(row=2,column=1,pady=5)
    
    main_button.grid(row=3,column=1,pady=4,sticky=W)
    root.mainloop()

