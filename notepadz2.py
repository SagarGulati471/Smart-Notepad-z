from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import colorchooser
from tkinter import simpledialog
# import tkinter as tk

import os
import datetime


def newfile():
    tmsg.Message()
    ans = tmsg.askquestion("save it", "do you want to save changes ?")
    if ans == "yes":
        savefile()
    # tmsg._show("save changes","hello")
    sagar.title("untitled")
    textarea.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        sagar.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()


'''
def savefile():
    global file
    if file == "":

        file = askopenfilename(initialfile='Untitled.txt',defaultextensions='.txt',filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f=open(file,'w')
            f.write(textarea.get(1.0,END))
            f.close()
            sagar.title(os.path.basename(file)+"-Notepad")
    else:
        f = open(file, 'w')
        f.write(textarea.get(1.0, END))
        f.close()


'''


def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()

            sagar.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()


def cut():
    textarea.event_generate(("<<Cut>>"))


def copy():
    textarea.event_generate(("<<Copy>>"))


def paste():
    textarea.event_generate(("<<Paste>>"))


def iquit():
    a = tmsg.askquestion("confirmation", "Are you sure to to exit ?")
    if a:
        exit()


def about():
    tmsg.showinfo("About Notepad",
                  "Well,this our first Gui being created in python if you like it then do rate it!!\n Thank You :)")


def capital():
    if file == None:
        d1 = textarea.get(1.0, END)
        textarea.delete(1.0, END)
        textarea.insert(1.0, d1.upper())
    else:
        with open(file, 'w') as f1:
            f1.write(textarea.get(1.0, END).upper())
            f1.close()
            with open(file, 'r') as f:
                s = f.read()
                textarea.delete(1.0, END)
                # print(s)
                textarea.insert(1.0, s)


def lower():
    if file == None:
        d1 = textarea.get(1.0, END)
        textarea.delete(1.0, END)
        textarea.insert(1.0, d1.lower())
    else:
        with open(file, 'w') as f1:
            f1.write(textarea.get(1.0, END).lower())
            f1.close()
            with open(file, 'r') as f:
                s = f.read()
                textarea.delete(1.0, END)
                print(s)
                textarea.insert(1.0, s)


def datetimee():
    now = datetime.datetime.now()
    dt_time = now.strftime("%Y-%m-%d %H:%M:%S")
    if file == None:
        textarea.insert(INSERT, dt_time)

    else:
        f = open(file, 'a')
        f.write(dt_time)
        f.close()

        f1 = open(file, "r")
        # f.write(textarea.get(1.0, END))
        textarea.delete(1.0, END)
        textarea.insert(1.0, f1.read())
        f1.close()


def read1():
    def read_it(data):
        # data=textarea.get(1.0, END)
        from win32com.client import Dispatch
        read_it = Dispatch("SAPI.SpVoice")
        read_it.Speak(data)

    read_it(str(textarea.get(1.0, END)))


def sharemail():
    mail = Tk()
    mail.wm_iconbitmap("icon.ico")
    mail.geometry('333x233')
    mail.title('Sharing Options')
    heading = Label(mail, text='Sharing via mail', fg="blue", font="comicsansms 13 bold")
    heading.pack()

    def choice():
        print(var.get())

    def sendmail():
        mails = [e1.get(), e2.get(), e3.get(), e4.get()]
        s = open(file, 'r')
        k = s.read()
        # print(k)
        # print(file)
        s.close()

        import smtplib
        connection = smtplib.SMTP('smtp.gmail.com', 587)
        connection.ehlo()
        connection.starttls()  # transfer layer security
        connection.login('sagargulati471', 'fasttrack')

        for i in range(len(mails)):
            connection.sendmail('sagargulati471', mails[i], k)

        connection.close()

    var = StringVar()
    var.set("hello")  # value is initialised so all options are not selected
    Label(mail, text="choose no. of recipients").pack()
    # Radiobutton(mail,text="one",variable=var,value="dosa 124",command=choice).pack(anchor="w")
    # Radiobutton(mail,text="many",variable=var,value="pav bhaji",command=choice).pack(anchor="w")
    f1 = Frame(mail, background='yellow')
    f1.pack(anchor='w', pady=10, fill=BOTH)

    Label(f1, text='1').pack(anchor='n', side=LEFT)
    e1 = Entry(f1, width=30)
    e1.pack(anchor='w', pady=5, padx=7)

    Label(f1, text='2').pack(anchor='n', side=LEFT)
    e2 = Entry(f1, width=30)
    e2.pack(anchor='w', pady=5, padx=7)

    Label(f1, text='3').pack(anchor='n', side=LEFT)
    e3 = Entry(f1, width=30)
    e3.pack(anchor='w', pady=5, padx=7)

    Label(f1, text='4').pack(anchor='n', side=LEFT)
    e4 = Entry(f1, width=30)
    e4.pack(anchor='w', pady=5)

    b1 = Button(f1, text='Send', command=sendmail)
    b1.pack(side=LEFT, anchor='w')


if __name__ == '__main__':
    sagar = Tk()

    # rgb_color, web_color = colorchooser.askcolor(parent=sagar,initialcolor=(255, 0, 0))

    sagar.geometry("444x555")
    sagar.title("Untitled Notepad")
    sagar.wm_iconbitmap("icon2.ico")
    file = None
    textarea = Text(sagar, font="lucida 13")
    textarea.pack(expand=True, fill=BOTH)

    mainmenu = Menu(sagar)
    filemenu = Menu(mainmenu, tearoff=0)

    filemenu.add_command(label="New", command=newfile)
    filemenu.add_command(label="Open", command=openfile)
    filemenu.add_command(label="Save", command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=iquit)

    mainmenu.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(mainmenu, tearoff=0)
    editmenu.add_command(label="Cut", command=cut)
    editmenu.add_command(label="Copy", command=copy)
    editmenu.add_command(label="Paste", command=paste)
    editmenu.add_separator()
    editmenu.add_command(label="Date&Time", command=datetimee)
    editmenu.add_command(label="Capital ALL", command=capital)
    editmenu.add_command(label="Lower ALL", command=lower)
    mainmenu.add_cascade(label="Edit", menu=editmenu)

    xtra_func = Menu(mainmenu, tearoff=0)
    xtra_func.add_command(label='read txt', command=read1)
    xtra_func.add_command(label='share', command=sharemail)

    mainmenu.add_cascade(label='xtraa', menu=xtra_func)

    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label="About notepad", command=about)
    mainmenu.add_cascade(label="Help", menu=helpmenu)

    # Scroll bar********************************
    scroll = Scrollbar(textarea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)
    # ******************************************8

    sagar.config(menu=mainmenu)

    # STATUS BAR
    statusvar = StringVar()
    statusvar.set('Notepad Z ~~Version 1.0')
    sbar = Label(sagar, textvariable=statusvar, anchor='w', relief=SUNKEN)
    sbar.pack(side=BOTTOM, fill='x')

    sagar.mainloop()
