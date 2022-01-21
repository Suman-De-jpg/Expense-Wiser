from tkinter import *
from ExpenseWiser_v2 import *
from connectors import *


def sql_connecter():
    sql = Tk()
    sql.title('mySQL-DB Connector')
    sql.geometry('400x400')

    sql_pwd_label1 = Label(sql,text='You must have MySQL with Python Connector installed to use this app. ')
    sql_pwd_label1.grid(row=0,column=0,columnspan = 3)

    sql_pwd_label = Label(sql,text='Enter your MySQL Password : ')
    sql_pwd_label.grid(row=1,column=0)

    sql_pwd_entry = Entry(sql, width = "10")
    sql_pwd_entry.grid(row=1,column=1)

    sql_pwd_botton = Button(sql,text="GO", command = lambda: connect_sql_server(sql_pwd_entry.get(),sql))
    sql_pwd_botton.grid(row=1,column=2)

    sql.mainloop()

def login_backend(email,password,con,cur,log):
    try:
        name, uid,cur,con, who_spent_list = loginn(email,password,con,cur,log)
        welcome_window(name, uid,cur,con, who_spent_list)
    except TypeError as te:
        username_pwd_error()

def about():
    abt = Tk()
    abt.title('About Developer')
    abt.geometry('350x300')

    abt_label = Label(abt, text='About the Developer',font=('Comic Sans MS', 25))
    abt_label.grid(row=0,column=0)
    abt_label = Label(abt, text='Name : Suman De',font=('Comic Sans MS', 20))
    abt_label.grid(row=1,column=0)
    abt_label = Label(abt, text='Class : XII G',font=('Comic Sans MS', 20))
    abt_label.grid(row=2,column=0)
    abt_label = Label(abt, text='Roll No.: 35',font=('Comic Sans MS', 20))
    abt_label.grid(row=3,column=0)



def login():
    log = Tk()
    log.title("Login/Signup")
    log.geometry('500x500')

    greet_label = Label(log, text = "Expense Wiser")
    greet_label.grid(row=0,column=0, columnspan=2)
    greet_label.config(font=('Helvatical bold',12))


    log_label_login = Label(log,text="Login")
    log_label_login.grid(row =1,column=0)

    log_label_email = Label(log,text="Enter your email : ")
    log_label_email.grid(row=2,column=0)

    log_entry_email = Entry(log, width = 40)
    log_entry_email.grid(row=2,column=1)

    log_label_passwd = Label(log,text="Password :")
    log_label_passwd.grid(row=3,column =0)

    log_entry_passwd = Entry(log,width=40)
    log_entry_passwd.grid(row=3,column =1)

    log_button_go = Button(log,text="Go",command= lambda: login_backend(log_entry_email.get(),log_entry_passwd.get(),mycon,cursor,log))
    log_button_go.grid(row=4,column=1)

    sign_label_login = Label(log,text="Signup")
    sign_label_login.grid(row =5,column=0)

    sign_label_email = Label(log,text="Enter your email : ")
    sign_label_email.grid(row=6,column=0)

    sign_entry_email = Entry(log, width = 40)
    sign_entry_email.grid(row=6,column=1)

    sign_label_passwd = Label(log,text="Password :")
    sign_label_passwd.grid(row=7,column =0)

    sign_entry_passwd = Entry(log,width=40)
    sign_entry_passwd.grid(row=7,column =1)

    sign_label_name = Label(log,text="Full Name :")
    sign_label_name.grid(row=8,column =0)

    sign_entry_name = Entry(log,width=40)
    sign_entry_name.grid(row=8,column =1)

    sign_button_go = Button(log,text="Go(After Registration do login)",command= lambda: register(sign_entry_name.get(),sign_entry_email.get(),sign_entry_passwd.get(),mycon,cursor,log))
    sign_button_go.grid(row=9,column=1)
    log.mainloop()

def clear_txt(edate, ename, eplace, eamount):
    edate.delete(0,'end')
    ename.delete(0,'end')
    eplace.delete(0,'end')
    eamount.delete(0,'end')

def add_exp(name, uid, cur, con, wc,who_spent_list):
    wc.destroy()
    exp = Tk()
    exp.title("ExpenseWiser - Add Expenditure Wizard")
    exp.geometry('450x400')

    exp_label_date = Label(exp, text="Date of Expenditure (yyyy-mm-dd): ")
    exp_label_date.grid(row=1,column=0)

    exp_entry_date = Entry(exp, width = 40 )
    exp_entry_date.grid(row=1,column=1)

    exp_label_name = Label(exp, text = "Who Spent? ")
    exp_label_name.grid(row=2,column=0)

    exp_entry_name = Entry(exp, width = 40)
    exp_entry_name.grid(row=2,column=1)

    exp_label_place = Label(exp, text = "Reason : ")
    exp_label_place.grid(row=3,column=0)

    exp_entry_place = Entry(exp, width = 40)
    exp_entry_place.grid(row=3, column = 1)

    exp_label_amount = Label(exp, text = "Amount Spent? ")
    exp_label_amount.grid(row=4,column = 0)

    exp_entry_amount = Entry(exp, width=40)
    exp_entry_amount.grid(row=4,column = 1)

    exp_button_clear = Button(exp, text="Clear Fields",command=lambda: clear_txt(exp_entry_date, exp_entry_name, exp_entry_place, exp_entry_amount))
    exp_button_clear.grid(row=5, column=0)

    exp_button_back = Button(exp, text="Go Back to Homepage",command=lambda: welcome_window(name, uid,cur,con, who_spent_list))
    exp_button_back.grid(row=6, column=1)

    exp_button_addexp = Button(exp, text="Add Expenditure", command = lambda: exp_add(uid,exp_entry_name.get(),exp_entry_place.get(),exp_entry_amount.get(),exp_entry_date.get(),cursor,mycon,exp))
    exp_button_addexp.grid(row=5,column=1)

    exp.mainloop()

def data_takeout(uid,cur,con,who_spent_list):
    tkout = Tk()
    tkout.geometry('500x500')
    tkout.title("Export Data")

    greet_label = Label(tkout, text = "Welcome to Export Data Section of ExpenseWiser")
    greet_label.grid(row=0,column=0, columnspan=3)
    greet_label.config(font=('Helvatical bold',12))


    name_label = Label(tkout, text = "People who have registered their payments are as follows:{0}".format(who_spent_list))
    name_label.grid(row = 1, column=0, columnspan=3)
    # name_label.config(font=('Helvatical bold',10))

    name = Label(tkout,text="Name").grid(row=2,column=0)

    entryname_export = Entry(tkout, width = 10)
    entryname_export.grid(row=3,column=0)

    name_export_button = Button(tkout, text="Export Data of\nthe individual to\na csv file",command=lambda: name_export_to_csv(uid, entryname_export.get(), cur))
    name_export_button.grid(row=4,column=0)

    complete_export = Button(tkout, text="Export Entire Account Data", command = lambda: complete_export_to_csv(uid, cur))
    complete_export.grid(row=3,column = 2)



    tkout.mainloop()


def welcome_window(name, uid,cur,con,who_spent_list):
    who_spent_list = people_list_updater(uid,cur)

    welc = Tk()
    welc.title("Welcome to ExpenseWiser")
    welc.geometry('500x500')

    welc_label_greet = Label(welc,text="Hello "+name+", what do you want to do today?",font = ('Comic Sans MS', 14))
    welc_label_greet.grid(row=0,column=0,columnspan=2)

    welc_button_exp = Button(welc,text="Add Expenditures", command = lambda: add_exp(name,uid,cur,con,welc,who_spent_list), padx = 20, pady = 10)
    welc_button_exp.grid(row=1, column=0)

    welc_button_data = Button(welc,text="Export Data", command = lambda: data_takeout(uid,cur,con,who_spent_list), padx = 20, pady = 10)
    welc_button_data.grid(row=1, column=1)

    abt_button = Button(welc,text='About the Developer', command = about, padx = 20, pady = 10)
    abt_button.grid(row = 1,column=2)
    welc.mainloop()




sql_connecter()
mycon,cursor = db_connection_objects_takeout()
login()
