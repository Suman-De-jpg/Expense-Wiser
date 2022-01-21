from tkinter import *
mycon = None
cursor = None

def db_connection_objects_assign(con,cur):
    global mycon
    global cursor
    mycon = con
    cursor = cur

def db_connection_objects_takeout():
    return mycon,cursor

uid = None
name = None
cur = None
con = None
def welcome_connector(_uid,_name,_cur,_con):
    global uid,name,cur,con
    uid = _uid
    name= _name
    cur = _cur
    con = _con

def welcome_window_connector():
    return name,uid,cur,con

def data_added():
    da = Tk()
    exp_label_data_added = Label(da, text="Data Added")
    exp_label_data_added.pack()

    but_ok = Button(da, text='OK',command=lambda: da.destroy())
    but_ok.pack()

    da.mainloop()

def err_sqlpwd_handler():
    wrong_pwd = Tk()
    wrong_pwd.title('Error')
    wrong_pwd.geometry('100x100')

    pwd_label = Label(wrong_pwd, text = 'Wrong Password. Try Again').pack()

    wrong_pwd.mainloop()


def error_general():
    gen_error = Tk()
    gen_error.title('Error')
    gen_error.geometry('100x100')

    gen_error_label = Label(gen_error, text = 'Something went wrong. Try Again').pack()

    gen_error.mainloop()

def username_pwd_error():
    upwd_error = Tk()
    upwd_error.title('Error')

    upwd_error_label = Label(upwd_error, text = 'Wrong Username or password').pack()

    upwd_error.mainloop()

def value_error():
    ve_error = Tk()
    ve_error.title('Error')

    ve_error_label = Label(ve_error, text = 'Give the details according to the format').pack()

    ve_error.mainloop()
