from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests, tkinter, threading, webbrowser, random, datetime, time
from tkinter import *
import tkinter.ttk as ttk


index_so_far=0
links_data=[]
def getBsObj(url):
    session = requests.Session()
    headers={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}
    req = session.get(url, headers=headers)
    return BeautifulSoup(req.text,"html.parser")

def getHTML(url):
    session = requests.Session()
    headers={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}
    req = session.get(url, headers=headers)
    return req
def getContactEmail(url):
    bsObj=getBsObj("http://api.bulkwhoisapi.com/whoisAPI.php?domain="+url+"&token=usemeforfree")
    return bsObj

def openWebpage():
    if tree.focus()=="":
        tkinter.messagebox.showerror("Error","Please select a valid detection")
    else:
        print(tree.focus())
        print(int(tree.focus()[1:], 16)-1-index_so_far)
        webbrowser.open(links[int(tree.focus()[1:], 16)-1-index_so_far], new=2)

def generateReport():
    if(status.get()=="Status: Idle"):
        name="report"+str(random.randint(99999,9999999))+".txt"
        if(len(links_data)==0):
            tkinter.messagebox.showerror("Error","There are no results to generate report")
        else:
            file=open(name,'w+')
            file.write("PiroCop report generated on "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\n\n\n")
            for x in links_data:
                file.write(x+"\n\n")
            file.close()
            tkinter.messagebox.showinfo("Success","the Report is generated successfully with filename "+name)
    else:
        tkinter.messagebox.showinfo("Error","Please wait for the process to finish! ")



class mainThread (threading.Thread):
    global index_so_far
    def run(self):
        global index_so_far
        status.set("Status: Searching...")
        for row in tree.get_children():
            tree.delete(row)
        del links[:]
        del links_data[:]
        count=0
        sites=['thepiratebay',
        'rarbgmirror',
        'yts',
        'torrentz2',
        '1337x',
        'sabercathost',
        'mega.nz',
        'dropbox',
        'onedrive',
        'zippyshare',
        'filecrop',
        'rapidshare',
        '4shared',
        'mediafire',
        'load.to',
        'sendmyway.com',
        'sendspace.com',
        'mediafire.com',
        'uploaded.net',
        '2shared.com',
        'filefactory.com',
        'upstore.net',
        'ge.tt',
        'share-online.biz',
        'gigapeta.com',
        'turbobit.net',
        'uploading.com',
        'rapidgator.net',
        'hightail',
        'sendspace',
        'googledrive',
        'docs.google',
        'depositfiles',
        'icloud',
        'ruTracker',
        'pcgames-download',
        'skidrowgamesreloaded',
        'skidrowreloaded',
        'deca-games',
        'fitgirl-repacks',
        'gamestorrent',
        'warez-bb',
        'cs.rin',
        'rg-mechanics',
        'nosteam',
        '1337x',
        'oceanofgames',
        'soulseekqt',
        'demonoid',
        'gen.lib.rus',
        'b-ok',
        'forum.mobilism',
        'onhax',
        'acmarket',
        'revdl',
        'tutuapp',
        'katcr',
        'kat.cr',
        'sadeempc',
        'crackingpatching',
        'tb.rg-adguard',
        'mycomicpost',
        'omicscodes',
        'rarbg',
        'yts',
        'moviemagnet',
        'vstitorrent',
        'audioz.download',
        'macgames-download',
        'mac-torrent-download',
        'tapochek',
        'binsearch',
        'cgpersia',
        'audiobookbay',
        'freetutorials',
        'the-eye',
        'snowfl'
        'dropbox',
        'putlocker'
        ]
        products=product.get()
        levels=level.get()
        products=products.replace('+','%2B')
        products=products.replace(" ","+")
        for x in range(levels):
            page=x
            url="http://www.google.com.pk/search?q="+products+"+"+"Download"+"&start="+str(page*10)
            #print(url)
            while(1):
                try:
                    bsObj=getBsObj(url)
                    break
                except:
                        print("Connection Error")
                        status.set("There is Some Connection problem, trying Again...")
                        time.sleep(1)
                        status.set("Status: Searching...")
            for x in bsObj.findAll('h3'):
                #try:
                t=x.get_text()
                print(t)
                x=x.find('a')['href'][7:]
                saIndex=x.index('&sa')
                x=x[:saIndex]
                print(x)
                while(1):
                    try:
                        bsObj2=getHTML(x)
                        break
                    except:
                        print("Connection Error")
                        status.set("There is Some Connection problem, trying Again...")
                        time.sleep(1)
                        status.set("Status: Searching...")
                #bsText=bsObj2.get_text()
                for y in sites:
                    if(y in bsObj2.text.lower()):
                        #print('infected')
                        #t=title
                        #x=link
                        tree.insert("",'end',text="Entry",
                                values=(t,x,y))
                        print(y) #filehost
                        index_so_far=index_so_far+1
                        print("index: "+str(index_so_far))
                        links.append(x)
                        links_data.append("Title="+t+"\nAddress="+x+"\nFileHost="+y)
                        break;
                #except:
                #    continue
                print()
        status.set("Status: Idle")

def main():
    thread1=mainThread()
    thread1.start()

def raise_frame(frame):
    frame.tkraise()

def login1():
    if(username.get()=="admin" and password.get()=="admin"):
        tkinter.messagebox.showinfo("Success","Login Successful")
        #print("Success")
        f2.tkraise()
    else:
        tkinter.messagebox.showerror("Error","Invalid Credentials. Please try again!")
        #print("Failed")


#GUI starts from here
root=Tk(className=" Login")
f1 = Frame(root)
f2 = Frame(root)
for frame in (f1, f2):
    frame.grid(row=0, column=0, sticky='news')
f1.config(width=20,height=20)
#The Code for login Form:
#Space Fillers:
Label(f1,text=" "*90).grid(row=0,column=0)
Label(f1,text=" "*10).grid(row=0,column=1)
Label(f1,text=" "*10).grid(row=1,column=1)
Label(f1,text=" "*10).grid(row=2,column=1)
Label(f1,text=" "*10).grid(row=3,column=1)
Label(f1,text=" "*10).grid(row=4,column=1)
Label(f1,text=" "*10).grid(row=5,column=1)
#Space fillers end
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
#label4=tkinter.Label(f2, text="End at Page Number: ")
#ending_page=tkinter.IntVar()
#ending_page.set(10)
#entry3=tkinter.Entry(f2, textvariable=ending_page, width=30)
#label5=tkinter.Label(f2, text="Show Only After year: ")
#year_var=tkinter.StringVar()
#year_var.set("2000")
#entry4=tkinter.Entry(f2, textvariable=year_var,width=30)
label2.grid(row=1, column=0)
entry1.grid(row=1, column=1)
label3.grid(row=2,column=0)
entry2.grid(row=2,column=1)
#label4.grid(row=3,column=0)
#entry3.grid(row=3, column=1)
#label5.grid(row=4,column=0)
#entry4.grid(row=4,column=1)
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
button3=tkinter.Button(f2, text="File a Claim",width=35)
button3.grid(column=1,row=8)
button4=tkinter.Button(f2, text="Generate Report",command=generateReport,width=35)
button4.grid(column=2,row=8)
status=tkinter.StringVar()
status.set("Status: Idle")
label6=tkinter.Label(f2, textvariable=status)
label6.grid(column=0,row=9, columnspan=15)
#End
raise_frame(f1)
root.mainloop()
