from tkinter import *
import sqlite3
from tkinter import ttk

root = Tk()

root.title('Student Management System')
root.geometry('1050x650')
root.iconbitmap('icon.ico')

conn = sqlite3.connect('StudentAddressBook.db')
c= conn.cursor()

'''
#Table Creation for database
c.execute("""CREATE TABLE addresses1(
      first_name text, 
      last_name text,
      gender text,
      DOB integer,   
      address text, pp
      contact integer,
      email text,   
      city text,     
      state text        
) """)
print('Table created succesfully')
'''

def add():
    conn= sqlite3.connect('StudentAddressBook.db')
    c= conn.cursor()

    c.execute("INSERT INTO addresses1 VALUES (:FirstName, :LastName, :Gender, :DOB, :Address, :Contact, :Email, :City, :State)",
     {
        'FirstName': firstname_entry.get(),
        'LastName': lastname_entry.get(),
        'Gender': gender_entry.get(),
        'DOB' : DOB_entry.get(),
        'Address': address_entry.get(),
        'Contact': contact_entry.get(),
        'Email' : email_entry.get(),
        'City': city_entry.get(),
        'State': state_entry.get()
    })
    print('Address inserted succesfully')

    conn.commit()
    fetch_data()
    conn.close()

    firstname_entry.delete(0,END)
    lastname_entry.delete(0,END)
    gender_entry.delete(0,END)
    DOB_entry.delete(0,END)
    address_entry.delete(0,END)
    contact_entry.delete(0,END)
    email_entry.delete(0,END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)

'''
global print_record
def showrecs():
    conn = sqlite3.connect('StudentAddressBook.db') #Connect to the default database

    c= conn.cursor() #create a cursor

    c.execute("SELECT *, oid FROM addresses1")
    records= c.fetchall()
    print(records)

    #Loop through results
    global print_record
    print_record=''
    for record in records:

        print_record+= str(record[9]) +'.' + ' '+ 'Firstname:' + str(record[0]) + ' ' +  str(record[1]) + ' ' + str(record[3])+ ' '+ '\t'   + "\n"

    query_label = Label(Frame3, bd =2,relief=RIDGE,height=2,font='lucida 10',text=print_record)
    query_label.place(x=10,y=20)

    conn.commit()
    conn.close()
'''

def clear():
    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    gender_entry.delete(0, END)
    DOB_entry.delete(0, END)
    address_entry.delete(0, END)
    contact_entry.delete(0, END)
    email_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)

def fetch_data():
    conn = sqlite3.connect('StudentAddressBook.db')  # Connect to the default database
    c = conn.cursor()  # create a cursor
    c.execute("SELECT *, oid FROM addresses1")
    global rows
    rows=c.fetchall()


    if len(rows)!=0:
        Records_table.delete(*Records_table.get_children())
        global row
        for row in rows:
            Records_table.insert('',END,values=row)

        conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('StudentAddressBook.db')
    c = conn.cursor()
    c.execute("DELETE from addresses1 WHERE oid = " + deleteid_entry.get())
    deleteid_entry.delete(0, END)

    print('Given Record Deleted Successfully')

    conn.commit()
    fetch_data()
    clear()
    conn.close()

def search_data():
    conn = sqlite3.connect('StudentAddressBook.db')  # Connect to the default database
    c = conn.cursor()  # create a cursor
    c.execute("select * from addresses1 where "+ str(search_byy.get())+" LIKE '%"+str(search_txt.get())+"%'")

    rows=c.fetchall()

    if len(rows)!=0:
        Records_table.delete(*Records_table.get_children())
        global row
        for row in rows:
            Records_table.insert('',END,values=row)

        conn.commit()
    conn.close()



title = Label(root,text="Student Management System",bd=10,relief=GROOVE,fg='crimson',bg='yellow',font=('times new roman',30,'bold'))
title.pack(side=TOP,fill=X)

first_name_var=StringVar()
last_name_var=StringVar()
gender_var=StringVar()
DOB_var=StringVar()
address_var=StringVar()
contact_var=StringVar()
email_var=StringVar()
city_var=StringVar()
state_var=StringVar()
search_byy=StringVar()
search_txt=StringVar()


Frame = LabelFrame(root,bd=5,relief=RIDGE,bg='white')
Frame.place(x=7,y=72,width=350,height=570)

Frame2 = LabelFrame(root,bd=5,relief=RIDGE,bg='crimson')
Frame2.place(x=370,y=72,width=680,height=570)

heading = Label(Frame,text="Add Records",fg='crimson',bg='white',font=('lucida',15,'bold'))
heading.grid(row=0,columnspan=2,padx=80,pady=10)

# Assigning entries and details
first_name = Label(Frame,text="First Name",fg='black',bd=5,bg='white',font=('times new roman',16))
first_name.grid(row=1,column=0,padx=5,pady=5,sticky="w")

firstname_entry = Entry(Frame,font='lucida 15 bold',bd=3,bg='white',fg='black')
firstname_entry.place(x=120,y=57,height=30,width=200)

last_name = Label(Frame,text="Last Name",fg='black',bd=5,bg='white',font=('times new roman',16))
last_name.grid(row=2,column=0,padx=5,pady=5,sticky="w")

lastname_entry= Entry(Frame,font='lucida 15 bold',bd=3,bg='white',fg='black')
lastname_entry.place(x=120,y=100,height=30,width=200)

Gender = Label(Frame,text="Gender",fg='black',bd=5,bg='white',font=('times new roman',16))
Gender.grid(row=3,column=0,padx=5,pady=5,sticky="w")

gender_entry= ttk.Combobox(Frame,font='lucida 14 bold',state='readonly')
gender_entry['values']=("male","female","other")
gender_entry.place(x=120,y=143,height=30,width=200)

DOB = Label(Frame,text="DOB",fg='black',bd=5,bg='white',font=('times new roman',16))
DOB.grid(row=4,column=0,padx=5,pady=5,sticky="w")

DOB_entry= Entry(Frame,font='lucida 15 bold',bd=3,bg='white',fg='black')
DOB_entry.place(x=120,y=186,height=30,width=200)

address = Label(Frame,text="Address",fg='black',bd=5,bg='white',font=('times new roman',16))
address.grid(row=5,column=0,padx=5,pady=5,sticky="w")

address_entry = Entry(Frame,font='lucida 13 bold',bd=3,bg='white',fg='black')
address_entry.place(x=120,y=235,height=30,width=200)

contact = Label(Frame,text='Contact No.',fg='black',bd=5,bg='white',font=('times new roman',16))
contact.grid(row=6,column=0,padx=5,pady=5,sticky="w")

contact_entry = Entry(Frame,font='lucida 13 bold',bd=3,bg='white',fg='black')
contact_entry.place(x=120,y=283,height=30,width=200)

email=  Label(Frame,text='Email',fg='black',bd=5,bg='white',font=('times new roman',16))
email.grid(row=7,column=0,padx=5,pady=5,sticky="w")

email_entry = Entry(Frame,width=10,bd=3,fg='red',font=('times new roman',13))
email_entry.place(x=120,y=320,height=50,width=200)

city = Label(Frame,text='City',fg='black',bd=5,bg='white',font=('times new roman',16))
city.grid(row=8,column=0,padx=5,pady=20,sticky="w")

city_entry = Entry(Frame,font='lucida 13 bold',bd=3,bg='white',fg='black')
city_entry.place(x=120,y=388,height=30,width=200)

state =  Label(Frame,text='State',fg='black',bd=5,bg='white',font=('times new roman',16))
state.place(x=5,y=435)

state_entry = ttk.Combobox(Frame,font='lucida 14 bold',state='readonly')
state_entry['values']=("Bagmati","Gandaki","Koshi","Mechi","Sagarmatha","Janakapur","Narayani","Lumbini","Rapti","Bheri","Seti","Mahakali","Karnali","Dhawalagiri")
state_entry.place(x=120,y=433,height=30,width=200)

buttonframe = LabelFrame(Frame,bd=3,bg='grey',relief=RIDGE)
buttonframe.place(x=2,y=480,width=339,height=80)

addbutton = Button(buttonframe, text='Add',bd=3,fg='green',font='lucida 13 bold',width=16,command=add).place(x=1,y=1,height=39)

#updatebutton = Button(buttonframe, text='Update',bd=3,fg='green',font='lucida 13 bold',width=16).place(x=1,y=43,height=39)

deleteid_entry = Entry(buttonframe,font=('time new roman',13,'bold'),width=10,bd=4,relief=RIDGE,bg='white',fg='black')
deleteid_entry.place(x=1,y=40,height=35)
deletebutton = Button(buttonframe, text='Delete',bd=3,fg='green',font='lucida 13 bold',width=22,command=delete).place(x=100,y=40,height=35)
clearbutton = Button(buttonframe, text='Clear',bd=3,fg='green',font='lucida 13 bold',width=15,command=clear).place(x=175,y=1,height=39)

search_by1 = Label(Frame2,text='Search By:',font=('times new roman',13,'bold'),bg='crimson',fg='white')
search_by1.grid(row=0,column=0,padx=3)

search_option = ttk.Combobox(Frame2,textvariable=search_byy,width=12,font=('times new roman',13,'bold'),state = 'readonly')
search_option['values'] = ('first_name','DOB','Contact','Address')
search_option.grid(row=0,column=1,padx=5)

search_entry = Entry(Frame2,textvariable=search_txt,width=18,font=('lucida',9,'bold'),bg='white',bd=2,relief=GROOVE,fg='black')
search_entry.grid(row=0,column=2,padx=3,ipadx=20,ipady=2)

search_btn = Button(Frame2,text='Search',font=('times new roman',13,'bold'),bg='white',fg='black',command=search_data)
search_btn.grid(row=0,column=3,padx=3)

showall_btn = Button(Frame2,text='Show All',font=('times new roman',13,'bold'),bg='white',fg='black',command=fetch_data)
showall_btn.grid(row=0,column=4,padx=9,ipadx=5)

Frame3 = LabelFrame(root,bd=5,relief=RIDGE,bg='crimson')
Frame3.place(x=380,y=125,width=660,height=505)

scroll_bar1 = Scrollbar(Frame3,orient=HORIZONTAL)
scroll_bar1.pack(side=BOTTOM,fill=X)

scroll_bar2 = Scrollbar(Frame3,orient=VERTICAL)
scroll_bar2.pack(side=RIGHT,fill=Y)

Records_table = ttk.Treeview(Frame3,columns=('First Name','Last Name', 'Gender','DOB','Address','Contact','Email','City','State',),xscrollcommand=scroll_bar1,yscrollcommand=scroll_bar2)

scroll_bar1.config(command=Records_table.xview)
scroll_bar2.config(command=Records_table.yview)

Records_table.heading('First Name',text="First Name")
Records_table.heading('Last Name',text="Last Name")
Records_table.heading('Gender',text="Gender")
Records_table.heading('DOB',text="DOB")
Records_table.heading('Address',text="Address")
Records_table.heading('Contact',text="Contact")
Records_table.heading('Email',text="Email")
Records_table.heading('City',text="City")
Records_table.heading('State',text="State")
Records_table['show']='headings'
Records_table.column('First Name',width=130)
Records_table.column('Last Name',width=130)
Records_table.column('Gender',width=100)
Records_table.column('DOB',width=100)
Records_table.column('Address',width=100)
Records_table.column('Contact',width=100)
Records_table.column('Email',width=130)
Records_table.column('City',width=100)
Records_table.column('State',width=100)
Records_table.pack(fill=BOTH,expand=1)

fetch_data()



root.mainloop()

