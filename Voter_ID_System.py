
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import sqlite3
from sqlite3 import Error
from tkinter import messagebox

window = Tk()
database = "C:\\Users\\Sankett\\Desktop\\inform.db"

v = StringVar()
s2=StringVar()
s1=StringVar()
s3=StringVar()
s4=StringVar()
s8=StringVar()
s10=StringVar()
s11=StringVar()
s12=StringVar()
s13=StringVar()

Top = Frame(window, width=1200, height=50, bd=8, relief="solid")
Top.pack(side=TOP)
Left = Frame(window, width=300, height=500, relief="solid", bg="ghost white")
Left.pack(side=LEFT)

BUTTON = Frame(Left, width=20, height=30, relief="raise", pady=2)
BUTTON.pack(side=BOTTOM)
Right = Frame(window, width=1000, height=530, bd=8, relief="solid", bg="ghost white")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=50, height=500, bg="ghost white")
Forms.pack(side=TOP)



#variable declration
def Exit():
  result = tkMessageBox.askquestion('Are you sure you want to exit?', icon="warning")
  if result == 'yes':
    window.destroy()

def create_connection(db_file):

  try:
    conn = sqlite3.connect(db_file)
    return conn
  except Error as e:
    print(e)

  return None

def create_table(conn, create_table_sql):
  2
  try:
    c = conn.cursor()
    c.execute(create_table_sql)
  except Error as e:
    print(e)

def create_project(conn, project):
  sql = ''' INSERT INTO data(aadhar,firstname,lastname,fathername,age,dob,gender,address,state1,district,pincode,email,phoneno)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) '''
  cur = conn.cursor()
  cur.execute(sql, project)
  return cur.lastrowid

def read():
  conn = create_connection(database)
  cursor = conn.cursor()
  tree.delete(*tree.get_children())
  cursor.execute("SELECT * FROM `data`")
  fetch = cursor.fetchall()
  for data in fetch:
    tree.insert('', 'end',
                values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11],data[12]))
  cursor.close()
  conn.close()

def get_data():
  aadhar = str(e1.get())
  firstname = str(e2.get())
  lastname = str(e3.get())
  fathername = str(e4.get())
  age = date.get()
  dob = str(D2.get() + "-" + months.get() + "-" + years.get())
  gender = str(v.get())
  address = e8.get()
  state1 = str(state.get())
  district = e10.get()
  pincode = e11.get()
  email = e12.get()
  phoneno = e13.get()
  tkMessageBox.showinfo("Succesfull!", "Information saved succesfully")
  project = [aadhar,firstname,lastname,fathername,age,dob,gender,address,state1,district,pincode,email,phoneno]
  return project

def Clear():
  # text.set(value=" ")
  years.set("Year")
  months.set("Month")
  D2.set("Day")

def submit() -> object:
  sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS data (aadhar TEXT PRIMARY KEY NOT NULL,
                                                                      firstname TEXT NOT NULL,
                                                                      lastname TEXT NOT NULL, fathername TEXT NOT NULL,
                                                                      age TEXT NOT NULL, dob TEXT NOT NULL,
                                                                      gender TEXT NOT NULL, address TEXT NOT NULL, state1 TEXT NOT NULL, district TEXT NOT NULL, pincode TEXT NOT NULL, email TEXT NOT NULL, phoneno TEXT NOT NULL
                                                                  ); """
  conn = create_connection(database)
  cursor = conn.cursor()
  condtion = True
  if check():
    data = get_data()
    if conn is not None:
      # create projects table
      create_table(conn, sql_create_projects_table)
    else:
      print("Error! cannot create the database connection.")
    with conn:
      create_project(conn, data)

  tree.delete(*tree.get_children())
  cursor.execute("SELECT * FROM `data`")
  fetch = cursor.fetchall()
  for data in fetch:
    tree.insert('', 'end',values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12]))
  cursor.close()
  conn.close()
  Clear()

def delete():
  conn = create_connection(database)
  cursor = conn.cursor()
  if not tree.selection():
    print("ERROR")
  else:
    result = tkMessageBox.askquestion('Delete this record?', icon="warning")
    if result == 'yes':
      curItem = tree.focus()
      print(str(curItem))
      contents = (tree.item(curItem))
      print(contents)
      selecteditem = contents['values']
      print(selecteditem)

      tree.delete(curItem)
      cursor.execute("DELETE FROM data WHERE aadhar = ?", (selecteditem[0],))
      conn.commit()
      cursor.close()
      conn.close()
      Clear()
      read()
def enter(selecteditem):
    reset()

    s1.set(selecteditem[0])
    s2.set(selecteditem[1])
    s3.set(selecteditem[2])
    s4.set(selecteditem[3])
    date.set(selecteditem[4])
    dob = " ".join(str(x) for x in str(selecteditem[5]).split("-"))
    dob = dob.split(" ")
    D2.set(dob[0])
    months.set(dob[1])
    years.set(dob[2])


    if selecteditem[6] == 'Male':
        rb1.select()
    else:
        rb2.select()
    s8.set(selecteditem[7])
    state.set(selecteditem[8])
    s10.set(selecteditem[9])
    s11.set(selecteditem[10])
    s12.set(selecteditem[11])
    s13.set(selecteditem[12])






def sel(a):
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    enter(selecteditem)
def update():
  conn = create_connection(database)
  if not tree.selection():
    print("ERROR")
  else:
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(selecteditem)
    data = get_data()
    sql = ''' UPDATE data SET aadhar = ? ,firstname = ? ,lastname = ?,fathername= ?,age= ?,dob= ?,gender= ?,address= ?,state1= ?,district= ?,pincode= ?,email= ?,phoneno= ? WHERE aadhar = ?'''
    data.append(selecteditem[0])
    print(data)
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()
    Clear()
    read()
def find(Variable):
    reset()
    conn = create_connection(database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `data`")
    fetch = cursor.fetchall()
    found=False
    for data in fetch:
        if str(data[1]) == str(Variable):
            tkMessageBox.showinfo("Found!","Data Found")
            found=True
            enter(data)
    if not  found:
            tkMessageBox.showinfo("Error","No data found")
    cursor.close()
    conn.close()

searchid=StringVar()
searchTop = Frame(Right,height=3,relief="ridge")
searchTop.pack(side=BOTTOM)
searchLable = Label(searchTop,border=2,text="Enter search parameter:")
searchLable.grid(row=1,column=0,sticky=W,pady=1,padx=2)
searchText = Entry(searchTop,font=('Helvetica','15'),textvariable=searchid,border=2,bd=5)
searchText.grid(row=1,column=1,sticky=W,pady=1,padx=2)
searchbutton = Button(searchTop,text="Search",bg="gray63",width=18,height=2,border=5,command=lambda: find(searchid.get()))
searchbutton.grid(row=2,column=0,columnspan=2,sticky=N,pady=1,padx=2)
txt_title = Label(Top,width=900,font=('Helvetica',24),text="VOTER ID INFORMATION SYSTEM")
txt_title.pack()

# delete button
def reset():
  e1.delete(0, 'end')
  e2.delete(0, 'end')
  e3.delete(0, 'end')
  e4.delete(0, 'end')
  v.set('')
  date.delete(0, 'end')
  D2.delete(0, 'end')
  months.delete(0, 'end')
  years.delete(0, 'end')
  state.set('')
  e8.delete(0, 'end')
  e10.delete(0, 'end')
  e11.delete(0, 'end')
  e12.delete(0, 'end')
  e13.delete(0, 'end')
#name
Label(Forms, font=('ariel',13,'bold'), text='ADDHAR NO:').grid(row=1,padx=7,pady=9,sticky=W)
Label(Forms,font=('ariel',13,'bold'), text='FIRST NAME:').grid(row=2,padx=7,pady=9,sticky=W)
Label(Forms,font=('ariel',13,'bold'), text='LAST NAME:').grid(row=3,padx=7,pady=9,sticky=W)
Label(Forms,font=('ariel',13,'bold'),text='FATHER/HUSBAND NAME:').grid(row=4,padx=7,pady=9,sticky=W)
#age
Label(Forms,font=('ariel',13,'bold'),text="AGE:").grid(row=5,padx=7,pady=9,sticky=W)
date = [int(a) for a in range(18,81)]
date = ttk.Combobox(Forms,values=date,width=17,font=('Helvetica','15'))
date.grid(row=5,column=1)
#date of birth
Label(Forms,font=('ariel',13,'bold'),text='DATE OF BIRTH:').grid(row=6,padx=7,pady=9,sticky=W)
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
months = ttk.Combobox(Forms,values=months,width=17,font=('Helvetica','15'))
months.grid(row=6,column=1)
D2 = [int(a) for a in range(1,32)]
D2 = ttk.Combobox(Forms,values=D2,width=17,font=('Helvetica','15'))
D2.grid(row=6,column=2)
years = [int(a) for a in range(1999,2050)]
years = ttk.Combobox(Forms,values=years,width=17,font=('Helvetica','15'))
years.grid(row=6,column=3)
#gender
Label(Forms,font=('ariel',13,'bold'),text="GENDER").grid(padx=7,pady=9,sticky=W)
rb1 = Radiobutton(Forms,font=('ariel',13,'bold'),text="MALE",variable=v,value='Male')
rb1.grid(row=7,column=1,sticky=W)
rb2 = Radiobutton(Forms,font=('ariel',13,'bold'),text="FEMALE",variable=v,value='Female')
rb2.grid(row=7,column=2,sticky=W)
#state,district,email id,address
Label(Forms,font=('ariel',13,'bold'), text='ADDRESS:').grid(row=8,padx=7,pady=9,sticky=W)
Label(Forms,font=('ariel',13,'bold'),text='STATE:').grid(row=9,padx=7,pady=9,sticky=W)
state = ['Maharashtra','Delhi','West Bengal','Rajashthan','Gujarat','Goa','Andhra Pradesh','U.P','M.P.']
state=ttk.Combobox(Forms,values=state,width=17,font=('Helvetica','15'))
state.grid(row=9,column=1)
Label(Forms, font=('ariel',13,'bold'), text='DISTRICT:').grid(row=10,padx=7,pady=9,sticky=W)
Label(Forms, font=('ariel',13,'bold'), text='PIN CODE:').grid(row=11,padx=7,pady=9,sticky=W)
Label(Forms, font=('ariel',13,'bold'), text='EMAIL ID:').grid(row=12,padx=7,pady=9,sticky=W)
Label(Forms, font=('ariel',13,'bold'), text='PHONE NO:').grid(row=13,padx=7,pady=9,sticky=W)
#text box
e1 = Entry(Forms,font=('Helvetica','15'),border=2,textvariable=s1,bd=5)
e1.grid(row=1, column=1)
e2 = Entry(Forms,font=('Helvetica','15'),border=2,textvariable=s2,bd=5)
e2.grid(row=2, column=1)
e3 = Entry(Forms,font=('Helvetica','15'),border=2,textvariable=s3,bd=5)
e3.grid(row=3, column=1)
e4 = Entry(Forms,font=('Helvetica','15'),border=2,textvariable=s4,bd=5)
e4.grid(row=4, column=1)
e8 = Entry(Forms,font=('Helvetica','15'),border=2,textvariable=s8,bd=5)
e8.grid(row=8, column=1)
e10 = Entry(Forms,font=('Helvetica','15'),border=2,textvariable=s10,bd=5)
e10.grid(row=10, column=1)
e11 = Entry(Forms,font=('Helvetica','15'),border=2,textvariable=s11,bd=5)
e11.grid(row=11, column=1)
e12 = Entry(Forms,font=('Helvetica','15'),border=2,textvariable=s12,bd=5)
e12.grid(row=12, column=1)
e13 = Entry(Forms,font=('Helvetica','15'),border=2,textvariable=s13,bd=5)
e13.grid(row=13, column=1)
yscroll = Scrollbar(Right)
yscroll.pack(side=RIGHT,fill=Y)

xscroll = Scrollbar(Right,orient="horizontal")
xscroll.pack(side=BOTTOM,fill=X)
style = ttk.Style(Right)
# set ttk theme to "clam" which support the fieldbackground option
style.theme_use("clam")
style.configure("Treeview",background="#bbc4ef",
                fieldbackground="#bbc4ef",foreground="black")
tree = ttk.Treeview(Right,selectmode="browse",height=100,yscrollcommand=yscroll.set,xscrollcommand=xscroll.set)
tree.pack(side='left')
yscroll.config(command=tree.yview)
xscroll.config(command=tree.xview)

tree["columns"] = ("ADHARCARD NO","FIRST NAME","LAST NAME","FATHER NAME" ,"AGE" ,"DOB","GENDER", "ADDRESS" ,"STATE", "DISTRICT","PINCODE","EMAIL ID","PHONE NO")
tree['show'] = 'headings'
tree.heading("ADHARCARD NO",text="ADHARCARD NO",anchor=W)
tree.heading("FIRST NAME",text="FIRST NAME",anchor=W)
tree.heading("LAST NAME",text="LAST NAME",anchor=W)
tree.heading("FATHER NAME",text="FATHER NAME",anchor=W)
tree.heading("AGE",text="AGE",anchor=W)
tree.heading('DOB',text="DOB",anchor=W)
tree.heading('GENDER',text="GENDER",anchor=W)
tree.heading("ADDRESS",text="ADDRESS",anchor=W)
tree.heading("STATE",text="STATE",anchor=W)
tree.heading("DISTRICT",text="DISTRICT",anchor=W)
tree.heading("PINCODE",text="PINCODE",anchor=W)
tree.heading("EMAIL ID",text="EMAIL ID",anchor=W)
tree.heading("PHONE NO",text="PHONE NO",anchor=W)
tree.column('#0',stretch=NO,minwidth=0,width=0)
tree.column('#1',stretch=NO,minwidth=0,width=120)
tree.column('#2',stretch=NO,minwidth=0,width=120)
tree.column('#3',stretch=NO,minwidth=0,width=120)
tree.column('#4',stretch=NO,minwidth=0,width=120)
tree.column('#5',stretch=NO,minwidth=0,width=120)
tree.column('#6',stretch=NO,minwidth=0,width=120)
tree.column('#7',stretch=NO,minwidth=0,width=120)
tree.column('#8',stretch=NO,minwidth=0,width=120)
tree.column('#9',stretch=NO,minwidth=0,width=120)
tree.column('#10',stretch=NO,minwidth=0,width=120)
tree.column('#11',stretch=NO,minwidth=0,width=120)
tree.column('#12',stretch=NO,minwidth=0,width=120)
tree.bind('<ButtonRelease-1>', sel)
def che(self):
   if e1.get()=='' or not e1.get().isdigit() or not len(e1.get())== 12:
      e1.focus()
      tkMessageBox.showerror('Error','Fill Adhar number')
   elif e2.get()=='':
      e2.focus()
      tkMessageBox.showerror('Error','Fill your first name')
e3.bind('<Button-1>', che)
def ch(self):
   if e1.get()=='' or not e1.get().isdigit() or not len(e1.get())== 12:
      e1.focus()
      tkMessageBox.showerror('Error','Fill Adhar number')
   elif e2.get()=='':
      e2.focus()
      tkMessageBox.showerror('Error','Fill your first name')
   elif e3.get() == '':
      e3.focus()
      tkMessageBox.showerror('Error', 'Fill your Last name')
e4.bind('<Button-1>', ch)
def c(self):
   if e1.get()=='' or not e1.get().isdigit() or not len(e1.get())== 12:
      e1.focus()
      tkMessageBox.showerror('Error','Fill Adhar number')
   elif e2.get()=='':
      e2.focus()
      tkMessageBox.showerror('Error','Fill your first name')
   elif e3.get() == '':
      e3.focus()
      tkMessageBox.showerror('Error', 'Fill your Last name')
   elif e4.get() == '':
      e4.focus()
      tkMessageBox.showerror('Error', 'Fill your Father/husband name')
date.bind('<Button-1>', c)
def ca(self):
   if e1.get()=='' or not e1.get().isdigit() or not len(e1.get())== 12:
      e1.focus()
      tkMessageBox.showerror('Error','Fill Adhar number')
   elif e2.get()=='':
      e2.focus()
      tkMessageBox.showerror('Error','Fill your first name')
   elif e3.get() == '':
      e3.focus()
      tkMessageBox.showerror('Error', 'Fill your Last name')
   elif e4.get() == '':
      e4.focus()
      tkMessageBox.showerror('Error', 'Fill your Father/husband name')
   elif date.get() == '':
      date.focus()
      tkMessageBox.showerror('Error', 'Fill your Age')
D2.bind('<Button-1>', ca)
months.bind('<Button-1>', ca)
years.bind('<Button-1>', ca)
def ce(self):
   if e1.get()=='' or not e1.get().isdigit() or not len(e1.get())== 12:
      e1.focus()
      tkMessageBox.showerror('Error','Fill Adhar number')
   elif e2.get()=='':
      e2.focus()
      tkMessageBox.showerror('Error','Fill your first name')
   elif e3.get() == '':
      e3.focus()
      tkMessageBox.showerror('Error', 'Fill your Last name')
   elif e4.get() == '':
      e4.focus()
      tkMessageBox.showerror('Error', 'Fill your Father/husband name')
   elif date.get() == '':
      date.focus()
      tkMessageBox.showerror('Error', 'Fill your Age')
   elif D2.get() == 'Day' or months.get() == "Month" or years.get() == 'Year' or D2.get() == '' or months.get() == "" or years.get() == '':
      D2.focus()
      months.focus()
      years.focus()
      tkMessageBox.showerror('Error', 'Fill your Date of Birth')
rb1.bind('<Button-1>', ce)
rb2.bind('<Button-1>', ce)
def ci(self):
   if e1.get()=='' or not e1.get().isdigit() or not len(e1.get())== 12:
      e1.focus()
      tkMessageBox.showerror('Error','Fill Adhar number')
   elif e2.get()=='':
      e2.focus()
      tkMessageBox.showerror('Error','Fill your first name')
   elif e3.get() == '':
      e3.focus()
      tkMessageBox.showerror('Error', 'Fill your Last name')
   elif e4.get() == '':
      e4.focus()
      tkMessageBox.showerror('Error', 'Fill your Father/husband name')
   elif date.get() == '':
      date.focus()
      tkMessageBox.showerror('Error', 'Fill your Age')
   elif D2.get() == 'Day' or months.get() == "Month" or years.get() == 'Year' or D2.get() == '' or months.get() == "" or years.get() == '':
      D2.focus()
      months.focus()
      years.focus()
      tkMessageBox.showerror('Error', 'Fill your Date of Birth')
   elif v.get()=="":
      rb1.focus()
      rb2.focus()
      tkMessageBox.showerror('Error', 'Fill your gender')
e8.bind('<Button-1>', ci)
def cs(self):
   if e1.get()=='' or not e1.get().isdigit() or not len(e1.get())== 12:
      e1.focus()
      tkMessageBox.showerror('Error','Fill Adhar number')
   elif e2.get()=='':
      e2.focus()
      tkMessageBox.showerror('Error','Fill your first name')
   elif e3.get() == '':
      e3.focus()
      tkMessageBox.showerror('Error', 'Fill your Last name')
   elif e4.get() == '':
      e4.focus()
      tkMessageBox.showerror('Error', 'Fill your Father/husband name')
   elif date.get() == '':
      date.focus()
      tkMessageBox.showerror('Error', 'Fill your Age')
   elif D2.get() == 'Day' or months.get() == "Month" or years.get() == 'Year' or D2.get() == '' or months.get() == "" or years.get() == '':
      D2.focus()
      months.focus()
      years.focus()
      tkMessageBox.showerror('Error', 'Fill your Date of Birth')
   elif v.get()=="":
      rb1.focus()
      rb2.focus()
      tkMessageBox.showerror('Error', 'Fill your gender')
   elif e8.get() == '':
      e8.focus()
      tkMessageBox.showerror('Error', 'Fill your Address')
state.bind('<Button-1>', cs)
def cr(self):
   if e1.get()=='' or not e1.get().isdigit() or not len(e1.get())== 12:
      e1.focus()
      tkMessageBox.showerror('Error','Fill Adhar number')
   elif e2.get()=='':
      e2.focus()
      tkMessageBox.showerror('Error','Fill your first name')
   elif e3.get() == '':
      e3.focus()
      tkMessageBox.showerror('Error', 'Fill your Last name')
   elif e4.get() == '':
      e4.focus()
      tkMessageBox.showerror('Error', 'Fill your Father/husband name')
   elif date.get() == '':
      date.focus()
      tkMessageBox.showerror('Error', 'Fill your Age')
   elif D2.get() == 'Day' or months.get() == "Month" or years.get() == 'Year' or D2.get() == '' or months.get() == "" or years.get() == '':
      D2.focus()
      months.focus()
      years.focus()
      tkMessageBox.showerror('Error', 'Fill your Date of Birth')
   elif v.get()=="":
      rb1.focus()
      rb2.focus()
      tkMessageBox.showerror('Error', 'Fill your gender')
   elif e8.get() == '':
      e8.focus()
      tkMessageBox.showerror('Error', 'Fill your Address')
   elif state.get() == '':
      state.focus()
      tkMessageBox.showerror('Error', 'Fill your State')
e10.bind('<Button-1>', cr)
def cb(self):
   if e1.get()=='' or not e1.get().isdigit() or not len(e1.get())== 12:
      e1.focus()
      tkMessageBox.showerror('Error','Fill Adhar number')
   elif e2.get()=='':
      e2.focus()
      tkMessageBox.showerror('Error','Fill your first name')
   elif e3.get() == '':
      e3.focus()
      tkMessageBox.showerror('Error', 'Fill your Last name')
   elif e4.get() == '':
      e4.focus()
      tkMessageBox.showerror('Error', 'Fill your Father/husband name')
   elif date.get() == '':
      date.focus()
      tkMessageBox.showerror('Error', 'Fill your Age')
   elif D2.get() == 'Day' or months.get() == "Month" or years.get() == 'Year' or D2.get() == '' or months.get() == "" or years.get() == '':
      D2.focus()
      months.focus()
      years.focus()
      tkMessageBox.showerror('Error', 'Fill your Date of Birth')
   elif v.get()=="":
      rb1.focus()
      rb2.focus()
      tkMessageBox.showerror('Error', 'Fill your gender')
   elif e8.get() == '':
      e8.focus()
      tkMessageBox.showerror('Error', 'Fill your Address')
   elif state.get() == '':
      state.focus()
      tkMessageBox.showerror('Error', 'Fill your State')
   elif e10.get() == '':
      e10.focus()
      tkMessageBox.showerror('Error', 'Fill your District')
e11.bind('<Button-1>', cb)
def chb(self):
   if e1.get()=='' or not e1.get().isdigit() or not len(e1.get())== 12:
      e1.focus()
      tkMessageBox.showerror('Error','Fill Adhar number')
   elif e2.get()=='':
      e2.focus()
      tkMessageBox.showerror('Error','Fill your first name')
   elif e3.get() == '':
      e3.focus()
      tkMessageBox.showerror('Error', 'Fill your Last name')
   elif e4.get() == '':
      e4.focus()
      tkMessageBox.showerror('Error', 'Fill your Father/husband name')
   elif date.get() == '':
      date.focus()
      tkMessageBox.showerror('Error', 'Fill your Age')
   elif D2.get() == 'Day' or months.get() == "Month" or years.get() == 'Year' or D2.get() == '' or months.get() == "" or years.get() == '':
      D2.focus()
      months.focus()
      years.focus()
      tkMessageBox.showerror('Error', 'Fill your Date of Birth')
   elif v.get()=="":
      rb1.focus()
      rb2.focus()
      tkMessageBox.showerror('Error', 'Fill your gender')
   elif e8.get() == '':
      e8.focus()
      tkMessageBox.showerror('Error', 'Fill your Address')
   elif state.get() == '':
      state.focus()
      tkMessageBox.showerror('Error', 'Fill your State')
   elif e10.get() == '':
      e10.focus()
      tkMessageBox.showerror('Error', 'Fill your District')
   elif e11.get() == '' or not e11.get().isdigit() or not len(e11.get())==6:
      e11.focus()
      tkMessageBox.showerror('Error', 'Fill your Pincode')
e12.bind('<Button-1>', chb)
def chx(self):
   if e1.get()=='' or not e1.get().isdigit() or not len(e1.get())== 12:
      e1.focus()
      tkMessageBox.showerror('Error','Fill Adhar number')
   elif e2.get()=='':
      e2.focus()
      tkMessageBox.showerror('Error','Fill your first name')
   elif e3.get() == '':
      e3.focus()
      tkMessageBox.showerror('Error', 'Fill your Last name')
   elif e4.get() == '':
      e4.focus()
      tkMessageBox.showerror('Error', 'Fill your Father/husband name')
   elif date.get() == '':
      date.focus()
      tkMessageBox.showerror('Error', 'Fill your Age')
   elif D2.get() == 'Day' or months.get() == "Month" or years.get() == 'Year' or D2.get() == '' or months.get() == "" or years.get() == '':
      D2.focus()
      months.focus()
      years.focus()
      tkMessageBox.showerror('Error', 'Fill your Date of Birth')
   elif v.get()=="":
      rb1.focus()
      rb2.focus()
      tkMessageBox.showerror('Error', 'Fill your gender')
   elif e8.get() == '':
      e8.focus()
      tkMessageBox.showerror('Error', 'Fill your Address')
   elif state.get() == '':
      state.focus()
      tkMessageBox.showerror('Error', 'Fill your State')
   elif e10.get() == '':
      e10.focus()
      tkMessageBox.showerror('Error', 'Fill your District')
   elif e11.get() == '' or not e11.get().isdigit() or not len(e11.get())==6:
      e11.focus()
      tkMessageBox.showerror('Error', 'Fill your Pincode')
   elif e12.get() == '' or '@' not in e12.get()  or  '.' not in e12.get() :
        e12.focus()
        messagebox.showerror('Error', 'Enter the email')
e13.bind('<Button-1>', chx)


def check():
   if e1.get()=='' or not e1.get().isdigit() or not len(e1.get())== 12:
      e1.focus()
      tkMessageBox.showerror('Error','Fill Adhar number')
   elif e2.get()=='':
      e2.focus()
      tkMessageBox.showerror('Error','Fill your first name')
   elif e3.get() == '':
      e3.focus()
      tkMessageBox.showerror('Error', 'Fill your Last name')
   elif e4.get() == '':
      e4.focus()
      tkMessageBox.showerror('Error', 'Fill your Father/husband name')
   elif date.get() == '':
      date.focus()
      tkMessageBox.showerror('Error', 'Fill your Age')
   elif D2.get() == 'Day' or months.get() == "Month" or years.get() == 'Year' or D2.get() == '' or months.get() == "" or years.get() == '':
      D2.focus()
      months.focus()
      years.focus()
      tkMessageBox.showerror('Error', 'Fill your Date of Birth')
   elif v.get()=="":
      rb1.focus()
      rb2.focus()
      tkMessageBox.showerror('Error', 'Fill your gender')
   elif e8.get() == '':
      e8.focus()
      tkMessageBox.showerror('Error', 'Fill your Address')
   elif state.get() == '':
      state.focus()
      tkMessageBox.showerror('Error', 'Fill your State')
   elif e10.get() == '':
      e10.focus()
      tkMessageBox.showerror('Error', 'Fill your District')
   elif e11.get() == '' or not e11.get().isdigit() or not len(e11.get())==6:
      e11.focus()
      tkMessageBox.showerror('Error', 'Fill your Pincode')
   elif e12.get() == '' or '@' not in e12.get()  or  '.' not in e12.get() :
        e12.focus()
        messagebox.showerror('Error', 'Enter the email')
   elif e13.get() == '' or not e13.get().isdigit() or not len(e13.get())==10:
      e13.focus()
      tkMessageBox.showerror('Error', 'Fill your Number')
   else:
      return True
   return False
def chec(self):
   if e1.get()=='' or not e1.get().isdigit() or not len(e1.get())== 12:
      e1.focus()
      tkMessageBox.showerror('Error','Fill Adhar number')
e2.bind('<Button-1>', chec)
#buttons
Button(BUTTON,font=('ariel',10,'bold'),text='SUBMIT', width=20,command=submit,relief='solid',bg="#58AD69",fg='#feffff').grid(row=14,column=0)
Button(BUTTON,font=('ariel',10,'bold'),text='RESET', width=20,command=reset,relief='solid',bg="#E2574C",fg='#feffff').grid(row=14,column=1)
Button(BUTTON,font=('ariel',10,'bold'),text='DELETE', width=20,command=delete,relief='solid',bg="#E2574C",fg='#feffff').grid(row=14,column=4)
Button(BUTTON,font=('ariel',10,'bold'),text='EXIT', width=20,command=Exit,relief='solid').grid(row=14,column=5)
Button(BUTTON,font=('ariel',10,'bold'),text='UPDATE', width=20,command=update,relief='solid',bg="#58AD69",fg='#feffff').grid(row=14,column=3)

window.mainloop()
