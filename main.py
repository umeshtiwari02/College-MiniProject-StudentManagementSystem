##########

def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")
        addedtime = time.strftime("%H:%M:%S")


        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (id, name, mobile, email, address, gender, dob, addeddate, addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notifications', 'Id {} Name {} added successfully... and want to clean the form'.format(id, name), parent=addroot)
            if(res == True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')

        except:
            messagebox.showerror('Notifications', 'Id Already Exists try new Id...', parent=addroot)
        strr = 'select * from studentdata1;'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)



    addroot = Toplevel(master=DataEntryFrame)
    # addroot.grab_set()
    addroot.geometry('460x470+330+260')
    addroot.title('Student Management System')
    addroot.config(bg='turquoise')
    # addroot.iconbitmap('image.ico')
    addroot.resizable(False, False)
    #------------------ Add Student Labels
    idlabel = Label(addroot, text="Enter Id : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot, text="Enter Name : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(addroot, text="Enter Mobile : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(addroot, text="Enter Email : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(addroot, text="Enter Address : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(addroot, text="Enter Gender : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(addroot, text="Enter D.O.B : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    doblabel.place(x=10,y=370)

    #----------------Add Student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot, font=('roman', 15, 'bold'), bd=4, textvariable=idval, width=13)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=4, textvariable=nameval, width=13)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=4, textvariable=mobileval, width=13)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=4, textvariable=emailval, width=13)
    emailentry.place(x=250,y=190)

    addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=4, textvariable=addressval, width=13)
    addressentry.place(x=250,y=250)

    genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=4, textvariable=genderval, width=13)
    genderentry.place(x=250,y=310)

    dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=4, textvariable=dobval, width=13)
    dobentry.place(x=250,y=370)

    ##-------------------Add Button
    submitbtn = Button(addroot, text='Submit', font=('roman', 15, 'bold'), width=13, bd=5, activebackground='blue', activeforeground='white',
                       bg='red', command=submitadd)
    submitbtn.place(x=120, y=415)


    addroot.mainloop()

#################################

def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")

        if(id != ''):
            strr = 'select * from studentdata1 where id=%s'
            mycursor.execute(strr, (id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(name != ''):
            strr = 'select * from studentdata1 where name=%s'
            mycursor.execute(strr, (name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(mobile != ''):
            strr = 'select * from studentdata1 where mobile=%s'
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(email != ''):
            strr = 'select * from studentdata1 where email=%s'
            mycursor.execute(strr, (email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(address != ''):
            strr = 'select * from studentdata1 where address=%s'
            mycursor.execute(strr, (address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(gender != ''):
            strr = 'select * from studentdata1 where gender=%s'
            mycursor.execute(strr, (gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(dob != ''):
            strr = 'select * from studentdata1 where dob=%s'
            mycursor.execute(strr, (dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(addeddate != ''):
            strr = 'select * from studentdata1 where addeddate=%s'
            mycursor.execute(strr, (addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)


    searchroot = Toplevel(master=DataEntryFrame)
    # searchroot.grab_set()

    searchroot.geometry('460x535+330+260')
    searchroot.title('Student Management System')
    searchroot.config(bg='lightskyblue')
    # searchroot.iconbitmap('image.ico')
    searchroot.resizable(False, False)
    #------------------ Add Student Labels
    idlabel = Label(searchroot, text="Enter Id : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text="Enter Name : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text="Enter Mobile : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(searchroot, text="Enter Email : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(searchroot, text="Enter Address : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(searchroot, text="Enter Gender : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot, text="Enter D.O.B : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(searchroot, text="Enter Date : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    datelabel.place(x=10, y=430)

    #----------------Add Student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot, font=('roman', 15, 'bold'), bd=4, textvariable=idval, width=13)
    identry.place(x=250, y=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=4, textvariable=nameval, width=13)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=4, textvariable=mobileval, width=13)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=4, textvariable=emailval, width=13)
    emailentry.place(x=250, y=190)

    addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=4, textvariable=addressval, width=13)
    addressentry.place(x=250, y=250)

    genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=4, textvariable=genderval, width=13)
    genderentry.place(x=250, y=310)

    dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=4, textvariable=dobval, width=13)
    dobentry.place(x=250, y=370)

    dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=4, textvariable=dateval, width=13)
    dateentry.place(x=250, y=430)

    ##-------------------Add Button
    submitbtn = Button(searchroot, text='Submit', font=('roman', 15, 'bold'), width=13, bd=5, activebackground='blue', activeforeground='white',
                       bg='red', command=search)
    submitbtn.place(x=120, y=478)


def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr, (pp))
    con.commit()
    messagebox.showinfo('Notifications', 'Id {} deleted successfully...'.format(pp))

    strr = 'select * from studentdata1;'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)

############------Update

def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata1 set name=%s, mobile=%s, email=%s, address=%s, gender=%s, dob=%s, date=%s, time=%s where id=%s'
        mycursor.execute(strr, (name, mobile, email, address, gender, dob, date, time, id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} modified successfully...'.format(id), parent=updateroot)
        strr = 'select * from studentdata1;'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    # updateroot.grab_set()

    updateroot.geometry('460x590+330+200')
    updateroot.title('Student Management System')
    updateroot.config(bg='lightskyblue')
    # updateroot.iconbitmap('image.ico')
    updateroot.resizable(False, False)
    #------------------ Add Student Labels
    idlabel = Label(updateroot, text="Update Id : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text="Update Name : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text="Update Mobile : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text="Update Email : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text="Update Address : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text="Update Gender : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text="Update D.O.B : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text="Update Date : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    datelabel.place(x=10, y=430)

    datelabel = Label(updateroot, text="Update Time : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    datelabel.place(x=10, y=490)

    #----------------Add Student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot, font=('roman', 15, 'bold'), bd=4, textvariable=idval, width=13)
    identry.place(x=250, y=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=4, textvariable=nameval, width=13)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=4, textvariable=mobileval, width=13)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=4, textvariable=emailval, width=13)
    emailentry.place(x=250, y=190)

    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=4, textvariable=addressval, width=13)
    addressentry.place(x=250, y=250)

    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=4, textvariable=genderval, width=13)
    genderentry.place(x=250, y=310)

    dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=4, textvariable=dobval, width=13)
    dobentry.place(x=250, y=370)

    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=4, textvariable=dateval, width=13)
    dateentry.place(x=250, y=430)

    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=4, textvariable=timeval, width=13)
    timeentry.place(x=250, y=490)

    ##-------------------Add Button
    submitbtn = Button(updateroot, text='Submit', font=('roman', 15, 'bold'), width=13, bd=5, activebackground='blue', activeforeground='white',
                       bg='red', command=update)
    submitbtn.place(x=120, y=535)

    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])


    updateroot.mainloop()

def showstudent():

    strr = 'select * from studentdata1;'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)


def exportstudent():

    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id, name, mobile, email, address, gender, dob, addeddata, addedtime = [], [], [], [], [], [], [], [], [],
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]), name.append(pp[1]), mobile.append(pp[2]), email.append(pp[3]), address.append(pp[4]), \
            gender.append(pp[5]), dob.append(pp[6]), addeddata.append(pp[7]), addedtime.append(pp[8])
    dd = ['Id', 'Name', 'Mobile', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time']
    df = pandas.DataFrame(list(zip(id, name, mobile, email, address, gender, dob, addeddata, addedtime)), columns=dd)
    paths = r'{}.csv'.format(ff)        # csv -> comma separated values
    df.to_csv(paths, index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved'.format(paths))


def exitstudent():
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    if(res == True):
        root.destroy()

########################################### Connect Database
def Connectdb():
    def submitdb():
        global con, mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()

        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications', 'Data is incorrect. Please enter correct data.', parent=dbroot)
            return
        try:
            strr = 'create database studentmanagementsystem4'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem4'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int(11), name varchar(20), mobile varchar(12), email varchar(30), ' \
                   'address varchar(100), gender varchar(8), dob varchar(20), date varchar(20), time varchar(20))'
            mycursor.execute(strr)
            strr ='alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Database created and now you are connected to the database...', parent=dbroot)
        except:
            strr = 'use studentmanagementsystem4'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Now you are connected to the database...', parent=dbroot)
        dbroot.destroy()

    dbroot = Toplevel()
    # dbroot.grab_set()    # it is used for prioritize or focusing the new tab
    # dbroot.iconbitmap('image.ico')
    dbroot.geometry('470x250+900+260')
    dbroot.resizable(False, False)
    dbroot.config(bg='turquoise')
    #------Connectdb Lables
    hostlable = Label(dbroot, text='Enter Host : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=15, anchor='w')
    hostlable.place(x=10, y=10)

    userlable = Label(dbroot, text='Enter User : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=5, width=15, anchor='w')
    userlable.place(x=10, y=70)

    passwordlable = Label(dbroot, text='Enter Password : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=5, width=15, anchor='w')
    passwordlable.place(x=10, y=130)

    #----------Connectdb Entry
    hostval = StringVar()
    # hostval.set("Hello")      #for checking the string
    userval = StringVar()
    passwordval = StringVar()
    hostentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=4, width=14, textvariable=hostval)
    hostentry.place(x=250, y=10)

    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=4, width=14, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=4, width=14, textvariable=passwordval)
    passwordentry.place(x=250, y=130)

    #---------- Connectdb Button
    submitbutton = Button(dbroot, text='Submit', font=('roman', 15, 'bold'), bg='red', bd=5, width=11, activebackground='blue', activeforeground='white',
                          command=submitdb)
    submitbutton.place(x=150, y=190)

    dbroot.mainloop()

###########################################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :' + date_string + "\n" + 'Time : ' + time_string)
    clock.after(200, tick)

######################## intro slider
import random
colors = ['red', 'green', 'blue', 'yellow', 'pink', 'red2', 'gold2']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2, IntroLabelColorTick)

def IntroLabelTick():
    global count, text
    if(count >= len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text=text+ss[count]
        SliderLabel.config(text=text)
        count +=1
    SliderLabel.after(200, IntroLabelTick)

##############################################

from tkinter import *
from tkinter import Toplevel, messagebox, filedialog
from  tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time
root = Tk()
root.title('Student Management System')
root.config(bg='aquamarine')
root.geometry('1180x700+300+100')
# root.iconbitmap(bitmap='/home/umesh/PycharmProjects/pythonProject/image.ico')
root.resizable(False, False)

######################  Frame
DataEntryFrame = Frame(root, bg='paleturquoise', relief=GROOVE, borderwidth=5,)
DataEntryFrame.place(x=10, y=80, height=600, width=500)
###########----- DataEntry Intro
frontlavel = Label(DataEntryFrame, text='------------------Welcome-----------------', width=30, font=('arial', 22, 'italic bold'), foreground="gold2", bg='cornflowerblue')
frontlavel.pack(side=TOP, expand=True)

addbtn = Button(DataEntryFrame, text='1. Add Student', width=15, font=('chiller', 17, 'bold'), bd=6, bg='skyblue3', activebackground='blue',
                relief=RIDGE, activeforeground='white', command=addstudent)
addbtn.pack(side=TOP, expand=True)

rearchbtn = Button(DataEntryFrame, text='2. Search Student', width=15, font=('chiller', 17, 'bold'), bd=6, bg='skyblue3', activebackground='blue',
                relief=RIDGE, activeforeground='white', command=searchstudent)
rearchbtn.pack(side=TOP, expand=True)

deletebtn = Button(DataEntryFrame, text='3. Delete Student', width=15, font=('chiller', 17, 'bold'), bd=6, bg='skyblue3', activebackground='blue',
                relief=RIDGE, activeforeground='white', command=deletestudent)
deletebtn.pack(side=TOP, expand=True)

updatebtn = Button(DataEntryFrame, text='4. Update Student', width=15, font=('chiller', 17, 'bold'), bd=6, bg='skyblue3', activebackground='blue',
                relief=RIDGE, activeforeground='white', command=updatestudent)
updatebtn.pack(side=TOP, expand=True)

showbtn = Button(DataEntryFrame, text='5. Show All', width=15, font=('chiller', 17, 'bold'), bd=6, bg='skyblue3', activebackground='blue',
                relief=RIDGE, activeforeground='white', command=showstudent)
showbtn.pack(side=TOP, expand=True)

exportbtn = Button(DataEntryFrame, text='6. Export Data', width=15, font=('chiller', 17, 'bold'), bd=6, bg='skyblue3', activebackground='blue',
                relief=RIDGE, activeforeground='white', command=exportstudent)
exportbtn.pack(side=TOP, expand=True)

exitbtn = Button(DataEntryFrame, text='7. Exit', width=15, font=('chiller', 17, 'bold'), bd=6, bg='skyblue3', activebackground='blue',
                relief=RIDGE, activeforeground='white', command=exitstudent)
exitbtn.pack(side=TOP, expand=True)

#####################################  Show data frame
ShowDataFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=5,)
ShowDataFrame.place(x=550, y=80, height=600, width=620)

#######################----------ShowData Frame

style = ttk.Style()
style.configure('Treeview.Heading', font=('chiller', 14, 'bold'), foreground='blue')
style.configure('Treeview', font=('times', 12, 'bold'), foreground='black', background='lightgray',)  # foreground color and background color is remaining
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
studenttable = Treeview(ShowDataFrame, columns=('Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time'),
                        yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id', text='Id')
studenttable.heading('Name', text='Name')
studenttable.heading('Mobile No', text='Mobile No')
studenttable.heading('Email', text='Email')
studenttable.heading('Address', text='Address')
studenttable.heading('Gender', text='Gender')
studenttable.heading('D.O.B', text='D.O.B')
studenttable.heading('Added Date', text='Added Date')
studenttable.heading('Added Time', text='Added Time')
studenttable['show'] = 'headings'
studenttable.column('Id', width=100)
studenttable.column('Name', width=200)
studenttable.column('Email', width=270)
studenttable.column('Address', width=200)
studenttable.column('Gender', width=100)
studenttable.column('D.O.B', width=150)
studenttable.column('Added Date', width=150)
studenttable.column('Added Time', width=150)

studenttable.pack(fill=BOTH, expand=1)

############################## slider
ss = 'Welcome To Student Management System'
count = 0
text = ''
################################
SliderLabel = Label(root, text=ss, font=('chiller', 19, 'italic bold'), relief=RIDGE,  borderwidth=4, width=36, bg='paleturquoise')
SliderLabel.place(x=230, y=0, height=52)
IntroLabelTick()
IntroLabelColorTick()
###################################### clock
clock = Label(root, font=('times', 14, 'bold'), relief=RIDGE, borderwidth=4, bg='lime')
clock.place(x=0, y=0, height=52)
tick()

######################################## Connect DataBase Button
connectbutton = Button(root, text='Connect To Database', width=16, font=('chiller', 14, 'italic bold'), relief=RIDGE, borderwidth=4, bg='lime',
                       activebackground='blue', activeforeground='white',
                       command=Connectdb)
connectbutton.place(x=935, y=0, height=52)


root.mainloop()
