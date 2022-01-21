import os
import sys
from datetime import datetime
import mysql.connector as sqlcon
from connectors import *
import csv

def connect_sql_server(pwd,sql):
    try :
        con = sqlcon.connect(host='localhost', user='root', passwd=str(pwd))
        cur = con.cursor()
        cur.execute('Create database if not exists expense_wiser')
        con.commit()
        cur.execute('use expense_wiser')
        sql.destroy()
        db_connection_objects_assign(con,cur)
    except sqlcon.Error as e:
        err_sqlpwd_handler()




def register(name,email, password,con,cur,reg):
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS accounts(\
        uid integer NOT NULL UNIQUE auto_increment, \
        name char(40) NOT NULL,\
        email char(40) NOT NULL,\
        password char(40) NOT NULL\
        )')
        con.commit()

        cur.execute('insert into accounts(name, email, password)\
        values(\'{0}\',\'{1}\',\'{2}\')'.format(str(name).strip(), str(email).strip(), str(password)))
        con.commit()
        cur.execute('select uid from accounts where password = \'{0}\''.format(password))
        uid = (cur.fetchall())[0][0]
        cur.execute('create table if not exists a{0}(\
        temp_id integer NOT NULL UNIQUE auto_increment, \
        who_spent char(40) NOT NULL,\
        where_spent char(40) NOT NULL,\
        how_much_spent integer NOT NULL,\
        date DATE NOT NULL)'.format(uid))
        con.commit()
    except sqlcon.Error as e:
        error_general()

def list_maker(tup):
    lst=[]
    for i in tup:
        lst.append(i[0])
    return lst

def people_list_updater(uid,cur):
    cur.execute('select distinct who_spent from a{0}'.format(uid))
    return(list_maker(cur.fetchall()))


def loginn(email,password,con,cur,log):
    try:
        cur.execute('select password from accounts where email = \'{0}\''.format(email))
        if cur.fetchall()[0][0] == password:
            cur.execute('select uid from accounts where password = \'{0}\''.format(password))
            uid = (cur.fetchall())[0][0]
            log.destroy()
            cur.execute('select name from accounts where uid = \'{0}\''.format(uid))
            name = (cur.fetchall())[0][0]
            cur.execute('select distinct who_spent from a{0}'.format(uid))
            who_spent_list = list_maker(cur.fetchall())
            return (name, uid,cur,con, who_spent_list)
    except IndexError as ie:
        username_pwd_error()

def exp_add(uid,who,where,how,date,cur,con,exp):
    try:
        who = who.lower()
        where = where.lower()
        cur.execute('INSERT INTO a{0}(date,who_spent,where_spent,how_much_spent) VALUES(\'{1}\',\'{2}\',\'{3}\',\'{4}\')'.format(uid,date,who,where,how))
        con.commit()
    except sqlcon.Error as e:
        value_error()

def make_nested_list(tup):
    lst = []
    lstTemp = []
    for i in tup:
        lstTemp=[]
        for j in i:
            lstTemp.append(j)
        lst.append(lstTemp)
    return lst

def name_export_to_csv(uid, name, cur):
    with open("Name_Export_{0}.csv".format(name), 'w+') as fh:
        cwriter = csv.writer(fh)
        cur.execute('select date, where_spent, how_much_spent from a{0} where who_spent = \'{1}\''.format(uid,name.lower()))
        lst = make_nested_list(cur.fetchall())
        cwriter.writerow(['Date', 'Place', 'Amount'])
        cwriter.writerows(lst)

def complete_export_to_csv(uid, cur):
    with open("Complete_Export.csv", 'w+') as fh:
        cwriter = csv.writer(fh)
        cur.execute('select date, who_spent, where_spent, how_much_spent from a{0}'.format(uid))
        lst = make_nested_list(cur.fetchall())
        cwriter.writerow(['Date', 'Name','Place', 'Amount'])
        cwriter.writerows(lst)
