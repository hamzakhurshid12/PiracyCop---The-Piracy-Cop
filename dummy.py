import tkinter
from tkinter import *
import tkinter.ttk as ttk


def openWebpage():
    pass
    #Your code for button here
def getContactEmail():
    pass
    #Your code for button here
def generateReport():
    pass
    #Your code for button here
def main():
    pass
    #Your code for button here

def login1():
    if(username.get()=="admin" and password.get()=="admin"):
        #tkinter.messagebox.showinfo("Success","Login Successful")
        #print("Success")
        f2.tkraise()
    else:
        tkinter.messagebox.showerror("Error","Invalid Credentials. Please try again!")
        #print("Failed")



#GUI starts from here
root=Tk(className=" PiroCop- The Piracy Cop")
f1 = Frame(root)
f2 = Frame(root)
for frame in (f1, f2):
    frame.grid(row=0, column=0, sticky='news')
f1.config(width=20,height=20)
#The Code for login Form:
background_label = Label(f1)
#Space Fillers:
Label(f1,text=" "*100).grid(row=0,column=0)
Label(f1,text=""*1).grid(row=0,column=1)
Label(f1,text=""*1).grid(row=1,column=1)
Label(f1,text=""*1).grid(row=2,column=1)
Label(f1,text=""*1).grid(row=3,column=1)
Label(f1,text=""*1).grid(row=4,column=1)
Label(f1,text=""*1).grid(row=5,column=1)
#Space fillers end
background_label.place(x=0, y=0, relwidth=1, relheight=1)
label1=Label(f1,text="Username:")
username=StringVar()
username.set("")
entry1=Entry(f1,textvariable=username)
password=StringVar()
password.set("")
label2=Label(f1,text="Password:")
entry2=Entry(f1,textvariable=password)
button1=Button(f1,text="Login",width=10, command=login1)
label1.grid(column=1,row=6)
entry1.grid(column=2,row=6)
label2.grid(column=1, row=7)
entry2.grid(column=2,row=7)
button1.grid(column=2,row=8,columnspan=1)

##The code for main form:
tree = ttk.Treeview(f2,selectmode='browse')
vsb = ttk.Scrollbar(f2,orient="vertical",command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsbx = ttk.Scrollbar(f2,orient="horizontal",command=tree.xview)
tree.configure(xscrollcommand=vsbx.set)
button1=tkinter.Button(f2,text="Search",command=main, width=50)
label2=tkinter.Label(f2, text="Select Level: ")
level=tkinter.IntVar()
level.set(10)
entry1=tkinter.Entry(f2, textvariable=level, width=30)
product=tkinter.StringVar()
product.set("")
entry2=tkinter.Entry(f2, textvariable=product, width=30)
label3=tkinter.Label(f2, text="Select Product: ")
label2.grid(row=1, column=0)
entry1.grid(row=1, column=1)
label3.grid(row=2,column=0)
entry2.grid(row=2,column=1)
button1.grid(column=0,row=5, columnspan=5)
tree.grid(column=0, row=6, columnspan=5)
vsb.grid(column=5, row=6)
vsbx.grid(column=0,row=7, columnspan=5)
tree["columns"] = ("1", "2","3")
tree['show'] = 'headings'
tree.column("1", width=450, anchor='c')
tree.column("2", width=250, anchor='c')
tree.column("3", width=60, anchor='c')
tree.heading("1", text="Detection Page Title")
tree.heading("2", text="Link")
tree.heading("3", text="File Host")
links=[]
button2=tkinter.Button(f2, text="Open Selected Webpage",command=openWebpage, width=35)
button2.grid(column=0,row=8)
button3=tkinter.Button(f2, text="File a Claim",command=getContactEmail,width=35)
button3.grid(column=1,row=8)
button4=tkinter.Button(f2, text="Generate Report",command=generateReport,width=35)
button4.grid(column=2,row=8)
status=tkinter.StringVar()
status.set("Status: Idle")
label6=tkinter.Label(f2, textvariable=status)
label6.grid(column=0,row=9, columnspan=15)
#End
f1.tkraise()
root.mainloop()
