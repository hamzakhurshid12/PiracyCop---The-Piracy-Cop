from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests, tkinter
from tkinter import *

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
def main():
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
    'lenov',
    'tutuapp',
    'katcr',
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
    'dropbox'
    ]
    product="Microsoft Word"
    product=product.replace('+','%2B')
    product=product.replace(" ","+")
    for x in range(5):
        page=x
        url="http://www.google.com.pk/search?q="+product+"+"+"Download"+"&start="+str(page*10)
        #print(url)
        bsObj=getBsObj(url)
        for x in bsObj.findAll('h3'):
            try:
                print(x.get_text())
                print(x)
                x=x.find('a')['href'][7:]
                saIndex=x.index('&sa')
                x=x[:saIndex]
                print(x)
                try:
                    bsObj2=getHTML(x)
                except:
                    pass
                #bsText=bsObj2.get_text()
                for y in sites:
                    if(y in bsObj2.text.lower()):
                        print('infected')
                        print(y)
                        break;
            except:
                continue
            print()
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
f1.config(width=60,height=50)
#The Code for login Form:
label1=Label(f1,text="Username:")
username=StringVar()
username.set("")
entry1=Entry(f1,textvariable=username)
password=StringVar()
password.set("")
label2=Label(f1,text="Password:")
entry2=Entry(f1,textvariable=password)
button1=Button(f1,text="Login",width=10, command=login1)
label1.grid(column=0,row=0)
entry1.grid(column=1,row=0)
label2.grid(column=0, row=1)
entry2.grid(column=1,row=1)
button1.grid(column=1,row=2,columnspan=1)
##The code for main form:


#End
raise_frame(f1)
root.mainloop()
