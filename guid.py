from tkinter import *
import cns
import crs
root= Tk()

def qf():
    root.destroy()
def connect_s():
    root.destroy()
    cns.mainf()
def create_s():
    root.destroy()
    crs.mainf()
root.title("Socket Chat")
root.geometry("300x150")
welcome=Label(root,text="Welcome To The Socket Chat",pady=5)
welcome.pack()
connect_button=Button(root,text="Connect To A Server",width=18,command=connect_s)
connect_button.pack()
create_button=Button(root,text="Create A Local Server",width=18,command=create_s)
create_button.pack()
quit_button=Button(root,text="Quit",command=qf,width=18)
quit_button.pack()
root.mainloop()
