from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from db import Database
db = Database("Employee.db")

root = Tk()
root.title('Employee Management system')
root.geometry('1300x615+0+0')
root.resizable(False,False)
root.configure(bg='#222831')


name = StringVar()
age = StringVar()
job = StringVar()
gender = StringVar()
email = StringVar()
mobile = StringVar()

#-----------  Entries Frame -----------#  
input_frame = Frame(root,bg='#31363F')
input_frame.place(x=1,y=1,width=360,height=610)
title = Label(input_frame,text='Employee data',font=('Calibri',18,'bold'),bg='#76ABAE',fg='white')
title.place(x=1,y=1)

#enter name 
Emp_Name = Label(input_frame,text="Name :",font=('Calibri',16),bg='#31363F',fg='white')
Emp_Name.place(x=10,y=50)
NameBox = Entry(input_frame,textvariable=name,width=15,font=('calibri',15))
NameBox.place(x=100,y=50)

#jop label 
jop_Label = Label(input_frame,text='Job title :',font=('Calibri',16),bg='#31363F',fg='white')
jop_Label.place(x=10,y=90)
JopBox = Entry(input_frame,textvariable=job,width=15,font=('calibri',15))
JopBox.place(x=100,y=90)

#Enployee gender
Emp_Gender = Label(input_frame,text='Gender :',font=('calibri',16),bg='#31363F',fg='white')
Emp_Gender.place(x=10,y=130)
GenderCombo = ttk.Combobox(input_frame,textvariable=gender,width=16,state='readonly',font=('calibri',15))
GenderCombo['values'] = ("Male" , "Female")
GenderCombo.place(x=100,y=130)

#Emppoyee Age
Emp_Age = Label(input_frame,text='Age :',font=('calibri',16),bg='#31363F',fg='white')
Emp_Age.place(x=10,y=170)
AgeBox = Entry(input_frame,textvariable=age,width=15,font=('calibri',15))
AgeBox.place(x=100,y=170)

#Employee Email
Emp_Email = Label(input_frame,text='Email :',font=('calibri',16),bg='#31363F',fg='white')
Emp_Email.place(x=10,y=210)
EmailBox = Entry(input_frame,textvariable=email,width=15,font=('calibri',15))
EmailBox.place(x=100,y=210)

#Employee Phone number
Emp_Phone_number = Label(input_frame,text='Mobile :',font=('calibri',16),bg='#31363F',fg='white')
Emp_Phone_number.place(x=10,y=250)
PhoneBox = Entry(input_frame,textvariable=mobile,width=15,font=('calibri',15))
PhoneBox.place(x=100,y=250)

#Address
Emp_Address = Label(input_frame,text='Address :',font=('calibri',16),bg='#31363F',fg='white')
Emp_Address.place(x=10,y=290)
AddressBox = Text(input_frame,width=30,height=2,font=('calibri',15))
AddressBox.place(x=10,y=330)

#------------ [Define] --------------
def hide():
    root.geometry("360x610+0+0")
def show():
     root.geometry("1300x615+0+0")

btn_hide = Button(input_frame,cursor='hand2',bg='white',bd=1,relief=SOLID,text='Hide',command=hide,width=8,height=1,font=('calibri',12),fg='#322C2B')
btn_hide.place(x=110,y=550)
btn_show = Button(input_frame,text='Show',cursor='hand2',bg='white',bd=1,relief=SOLID,command=show,width=8,height=1,font=('calibri',12),fg='#322C2B')
btn_show.place(x=190,y=550)

def getData(event):
     selected_row = tv.focus()
     data = tv.item(selected_row)
     global row 
     row = data["values"]
     name.set(row[1])
     age.set(row[2])
     job.set(row[3])
     email.set(row[4])
     gender.set(row[5])
     mobile.set(row[6])
     AddressBox.delete(1.0,END)
     AddressBox.insert(END,row[7])

def delete():
      db.remove(row[0])
      clear()
      displayAll()
def clear():
      name.set("")
      age.set("")
      job.set("")
      gender.set("")
      email.set("")
      mobile.set("")
      AddressBox.delete(1.0,END)

def displayAll():
          tv.delete(*tv.get_children())
          for row in db.fetch():
               tv.insert("",END,values=row)

def add_employee():
          if NameBox.get() =="" or AgeBox.get()=="" or JopBox.get()=="" or EmailBox.get()=="" or GenderCombo.get()=="" or PhoneBox.get()=="" or AddressBox.get(1.0,END)=="":
               messagebox.showerror("Error","Please fill all the entry boxes")
               return
          db.insert(
               NameBox.get(),
               AgeBox.get(),
               JopBox.get(),
               EmailBox.get(),
               GenderCombo.get(),
               PhoneBox.get(),
               AddressBox.get(1.0,END))
          messagebox.showinfo("Success","New employee has been added")
          clear()
          displayAll()
def update():
          if NameBox.get() =="" or AgeBox.get()=="" or JopBox.get()=="" or EmailBox.get()=="" or GenderCombo.get()=="" or PhoneBox.get()=="" or AddressBox.get(1.0,END)=="":
               messagebox.showerror("Error","Please fill all the entry boxes")
               return
          db.update(row[0],
               NameBox.get(),
               AgeBox.get(),
               JopBox.get(),
               EmailBox.get(),
               GenderCombo.get(),
               PhoneBox.get(),
               AddressBox.get(1.0,END))
          messagebox.showinfo("Success","employee data updated successfuly")
          clear()
          displayAll()
#--------- Buttone Frame -------
btn_frame = Frame(input_frame,bg='#31363F',bd=1,relief=SOLID)
btn_frame.place(x=10,y=430,width=335,height=100)

Add_Emp= Button(btn_frame,
               text='Add Employee',
               width=14,
               height=1,
               font=('calibri',16),
               fg='white',
               bg='#F97300',
               bd=0,
               command=add_employee
                )
Add_Emp.place(x=4,y=5)

Edit_Emp= Button(btn_frame,
               text='Update Emp Data',
               width=14,
               height=1,
               font=('calibri',16),
               fg='white',
               bg='#524C42',
               bd=0,
               command=update
                )
Edit_Emp.place(x=4,y=50)

Delete_Emp= Button(btn_frame,
               text='Delete Employee',
               width=14,
               height=1,
               font=('calibri',16),
               fg='white',
               bg='#750E21',
               bd=0,
               command=delete
                )
Delete_Emp.place(x=170,y=5)

ClearData= Button(btn_frame,
               text=' Clear data',
               width=14,
               height=1,
               font=('calibri',16),
               fg='white',
               bg='#803D3B',
               bd=0,
               command=clear
                )
ClearData.place(x=170,y=50)

#-------[Table Frame] --------
tree_frame = Frame(root,bg='white')
tree_frame.place(x=365,y=1,width=940,height=610)
scroll_x = Scrollbar(tree_frame, orient=HORIZONTAL)
scroll_x.pack(side=BOTTOM, fill=X)

style = ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',15),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=('Calibri',13))

tv = ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview",xscrollcommand=scroll_x.set)
tv.heading("1",text="ID")
tv.column("1",width="50")
tv.heading("2",text="Name")
tv.column("2",width="150")
tv.heading("3",text="Age")
tv.column("3",width="50")
tv.heading("4",text="Job")
tv.column("4",width="100")
tv.heading("5",text="Email")
tv.column("5",width="150")
tv.heading("6",text="Gender")
tv.column("6",width="80")
tv.heading("7",text="Moblie")
tv.column("7",width="150")
tv.heading("8",text="Address")
tv.column("8",width="190")

tv['show']= 'headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=BOTH, expand=1)
displayAll()
root.mainloop()