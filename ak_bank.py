
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import time
import datetime


connector=sqlite3.connect("bank_db.db")
cur=connector.cursor()

cur.execute('''create Table if not exists bank(NAME,USERID,PIN,DECE,ACNO,BALANCE);''')
cur.execute('''create Table if not exists transactions(SNAME,USERID,DATE,DECE,RACNO,AMOUNT);''')
cur.execute('''create Table if not exists LOGTAB(SNAME,USERID,DATE,LOGIN,LOGOUT);''')    


#============================================back end==================================================#


class bank:
    
       
    def credit(self):
        
        logged_screeen_destroy()
        cre_amount=IntVar(value="")
        
        balance=cur.execute('''select BALANCE from bank where USERID=?;''',(userid_var,))
        for i in balance:
            balance=i
        global ce_entry
        global credit_screen
        credit_screen = Toplevel()
        credit_screen.title("CREDIT")
        credit_screen.geometry("1000x600")
        Label(credit_screen, text="BANK ACCOUNT",bg="cadet blue", width="300", height="2", font=("Calibri", 13)).pack()
        select_screen=credit_screen
        det_print(select_screen)

        entry_frame=Frame(select_screen,width=600,height=300)
        entry_frame.pack(pady=50)

        ce_lable= Label(entry_frame, text="AMOUNT * ",font=("Calibri", 20))
        ce_lable.pack(pady=10)
        ce_entry = Entry(entry_frame, textvariable=cre_amount,font=("Calibri",20))
        ce_entry.pack(pady=5)
        btn_debit=Button(select_screen,text="CREDIT", height="2", width="15", font=("Calibri", 15),command=credit_bal).pack(pady=10)
        btn_back=Button(select_screen,text="GO BACK", height="2", width="15",bg="tan", font=("Calibri", 15),relief="ridge",bd=8,command=lambda:[credit_destroy(),logged_gui()]).pack(side=RIGHT,padx=20)

    
    def debit(self):
        global select_screen
        global account
        global d_amount
        global ac_entry
        global de_entry

        
        de_amount=IntVar(value="")
        account_no=IntVar(value="")
        
        logged_screeen_destroy()
       
        connector.commit()
        global debit_screen
        debit_screen = Toplevel()
        debit_screen.title("DEBIT")
        debit_screen.geometry("1000x600")
        Label(debit_screen, text="BANK ACCOUNT",bg="cadet blue", width="300", height="2", font=("Calibri", 13)).pack()
        select_screen=debit_screen
        det_print(select_screen)
        entry_frame=Frame(select_screen,width=600,height=300)
        entry_frame.pack(pady=50)

        ac_lable = Label(entry_frame, text="ACCOUNT.NO * ",font=("Calibri", 20))
        ac_lable.pack()
        ac_entry = Entry(entry_frame, textvariable=account_no,font=("Calibri",20))
        ac_entry.pack(pady=5)

        de_lable= Label(entry_frame, text="AMOUNT * ",font=("Calibri", 20))
        de_lable.pack(pady=10)
        de_entry = Entry(entry_frame, textvariable=de_amount,font=("Calibri",20))
        de_entry.pack(pady=5)

        btn_debit=Button(select_screen,text="DEBIT", height="2", width="15", font=("Calibri", 15),command=debit_bal).pack(pady=10)
        btn_back=Button(select_screen,text="GO BACK", height="2", width="15",bg="tan", font=("Calibri", 15),relief="ridge",bd=8,command=lambda:[debit_destroy(),logged_gui()]).pack(side=RIGHT,padx=20)
        #total_bal=("TOTAL_BALANCE:",balance)
        #Label(debit_screen, text=total_bal, width="300", height="2", font=("Calibri", 30)).pack(anchor=CENTER,padx=200,pady=100)

    def check_bal(self):
        global select_screen
        logged_screeen_destroy()
        balance=cur.execute('''select BALANCE from bank where USERID=?;''',(userid_var,))
        for i in balance:
            balance=i
        connector.commit()
        global check_bal_screen
        check_bal_screen = Toplevel()
        check_bal_screen.title("check balance")
        check_bal_screen.geometry("1000x600")
        Label(check_bal_screen, text="BANK ACCOUNT",bg="cadet blue", width="300", height="2", font=("Calibri", 13)).pack()
        select_screen=check_bal_screen
        det_print(select_screen)
        btn_back=Button(select_screen,text="GO BACK", height="2", width="15",bg="tan", font=("Calibri", 15),relief="ridge",bd=8,command=lambda:[check_bal_destroy(),logged_gui()]).pack(side=RIGHT,padx=20)
        total_bal=("TOTAL_BALANCE:",balance)
        Label(check_bal_screen, text=total_bal, width="300", height="2", font=("Calibri", 25)).pack(anchor=CENTER,padx=200,pady=100)
        #print("your bank balance is: ",balance[0])

    def new_user(self):
        
        name=username_entry.get()
        userid=userid_entry.get()
        acno=ac_entry.get()
        pin=pin_entry.get()
        check_pin=pin_re_entry.get()
        if pin==check_pin:
            balance=1000
            cur.execute('''insert into bank values(?,?,?,?,?);''',(name.upper(),int(userid),int(pin),int(acno),balance))
            connector.commit()
            time.sleep(1)
            register_destroy()
            reg_success()
            
            
        else:
            register_destroy()
            pin_not_match()
            
       
    def update_user(self):
        global select_screen
        logged_screeen_destroy()
        balance=cur.execute('''select BALANCE from bank where USERID=?;''',(userid_var,))
        for i in balance:
            balance=i
        connector.commit()
        global update_screen
        update_screen = Toplevel()
        update_screen.title("UPDATE")
        update_screen.geometry("1000x600")
        Label(update_screen, text="BANK ACCOUNT",bg="cadet blue", width="300", height="2", font=("Calibri", 13)).pack()
        select_screen=update_screen
        det_print(select_screen)

        global username_entry
        global pin_entry
        global pin_re_entry

        username = StringVar()
        pin_etr=IntVar(value="")
        re_pin=IntVar(value="")
        
        username_lable = Label(update_screen, text="username * ",font=("Calibri", 20))
        username_lable.pack(pady=10)
        username_entry = Entry(update_screen, textvariable=username,font=("Calibri", 15))
        username_entry.pack()

        pin_lable = Label(update_screen, text="PIN * ",font=("Calibri", 20))
        pin_lable.pack()
        pin_entry = Entry(update_screen, textvariable=pin_etr,show="*",font=("Calibri", 15))
        pin_entry.pack()

        pin_re_lable = Label(update_screen, text="RE PIN * ",font=("Calibri", 20))
        pin_re_lable.pack()
        pin_re_entry = Entry(update_screen, textvariable=re_pin,show="*",font=("Calibri", 15))
        pin_re_entry.pack()

        btn_update=Button(update_screen,text="UPDATE", height="2", width="15", font=("Calibri", 15),command=update_det).pack(pady=15)
        
        
        btn_back=Button(select_screen,text="GO BACK", height="2", width="15",bg="tan", font=("Calibri", 15),relief="ridge",bd=8,command=lambda:[update_destroy(),logged_gui()]).pack(side=RIGHT,padx=20)
        
        

        
   
    def delate_user(self):
        if userid_var==524769:
            global delete_screen
            global disp_list
            logged_screeen_destroy()
            delete_screen = Toplevel()
            delete_screen.title("delete")
            delete_screen.geometry("1000x600")
            Label(delete_screen, text="BANK ACCOUNT",bg="cadet blue", width="300", height="2", font=("Calibri", 13)).pack()
            select_screen=delete_screen
            userid=IntVar(value="")
            global del_userid_entry 
            userid_lable = Label(delete_screen, text="userid * ",font=("Calibri", 20))
            userid_lable.pack(pady=10)
            del_userid_entry = Entry(delete_screen, textvariable=userid,font=("Calibri", 15))
            del_userid_entry.pack(pady=5)

            btn_update=Button(delete_screen,text="DELETE", height="2", width="15", font=("Calibri", 15),command=del_ac).pack(pady=15)
            disp_list=Listbox(delete_screen,width=50,height=5,relief="ridge",fg="navy blue",font=("Calibri", 15))
            disp_list.pack(pady=15)

            btn_back=Button(delete_screen,text="GO BACK", height="2", width="15",bg="tan", font=("Calibri", 15),relief="ridge",bd=8,command=lambda:[del_screen_destroy(),logged_gui()]).pack(side=RIGHT,padx=20)

        else:
            mes=messagebox.askquestion("DELETE ACCOUNT","are you sure want to delete account")
            if mes=="yes":
                cur.execute('''delete from bank where USERID=?;''',(userid_var,))
                connector.commit()
                logged_screeen_destroy()
                messagebox.showinfo("INFO","YOUR ACCOUNT HAS BEEN DELETED.")

    def fetch_data(self):
        logged_screeen_destroy()
        fetch=cur.execute('''select * from bank where USERID=?;''',(userid_var,))
        for i in fetch:
            pass
        global profile_screen
        profile_screen = Tk()
        profile_screen.title("PROFILE")
        profile_screen.geometry("1000x600")
        Label(profile_screen, text="BANK ACCOUNT",bg="cadet blue", width="300", height="2", font=("Calibri", 13)).pack()

        btn_frame=Frame(profile_screen,width=900,height=300,relief="ridge",bd=10)
        btn_frame.pack(pady=50)
        select_screen=btn_frame
        det_print(btn_frame)
        pins=cur.execute('''select PIN from bank where USERID=?;''',(userid_var,))
        for k in pins:
            pin=k
        pin=("PIN:",pin)
        Label(btn_frame,text=pin,font=("Calibri", 15)).pack()

        balance=cur.execute('''select BALANCE from bank where USERID=?;''',(userid_var,))
        for i in balance:
            balance=i
        balance=("BALANCE:",balance)
        Label(btn_frame,text=balance,font=("Calibri", 15)).pack()

        dece="loan"
        get=cur.execute('''select AMOUNT from transactions where DECE=? and USERID=?;''',(dece,userid_var))
        t_amount=0
        for i in get:
            t_amount +=i[0]
        t_amount=("loan_AMOUNT:",t_amount)
        Label(btn_frame,text=t_amount,font=("Calibri", 15)).pack()
                
        btn_back=Button(profile_screen,text="GO BACK", height="2", width="15",bg="tan", font=("Calibri", 15),relief="ridge",bd=8,command=lambda:[profile_destroy(),logged_gui()]).pack(side=RIGHT,padx=20)
        
    def get_all(self):
        fetch_all=cur.execute('''select * from bank;''')
        for i in fetch_all:
            #print(i)
            pass
    def fetch_trans(self):
        logged_screeen_destroy()
        global fetch_screen
        fetch_screen = Tk()
        fetch_screen.title("transactions")
        fetch_screen.geometry("1000x600")
        Label(fetch_screen, text="BANK ACCOUNT",bg="cadet blue", width="300", height="2", font=("Calibri", 13)).pack()
        select_screen=fetch_screen
        det_print(fetch_screen)
        Label(fetch_screen,text="TRANSACTIONS SORT BY:",font=("Calibri", 15)).pack(pady=5)

        global sort
        get_data=StringVar()
        sort=ttk.Combobox(fetch_screen,width=30,height=10,textvariable=get_data,font=("Calibri", 15))
        sort["values"]=("loan","credit","debit")
        sort.pack(pady=5)
        btn_sort=Button(fetch_screen,text="SORT", height="2", width="15",bg="tan", font=("Calibri", 15),relief="ridge",bd=8,command=fetch_trans).pack(pady=5)

        global table
        table=ttk.Treeview(fetch_screen,selectmode="browse")
        table.pack(pady=5)
        scrlbar=ttk.Scrollbar(fetch_screen,orient="vertical",command=table.yview)
        scrlbar.pack(side="right",fill="x")
        table.configure(xscrollcommand=scrlbar.set)
        table["columns"]=("1","2","3","4","5","6")
        table["show"]="headings"
        table.column("1",width=200)
        table.column("2",width=80)
        table.column("3",width=150)
        table.column("4",width=70)
        table.column("5",width=100)
        table.column("6",width=80)
        
        table.heading("1",text="NAME")
        table.heading("2",text="USERID")
        table.heading("3",text="DATE")
        table.heading("4",text="DECE")
        table.heading("5",text="ACNO")
        table.heading("6",text="AMOUNT")

        data=cur.execute('''select * from transactions where USERID=?;''',(userid_var,))
        for i in data:
            NAME=i[0]
            USERID=i[1]
            DATE=i[2]
            DECE=i[3]
            ACNO=i[4]
            AMOUNT=i[5]
            table.insert("","end",values=(NAME,USERID,DATE,DECE,ACNO,AMOUNT))

        btn_back=Button(fetch_screen,text="GO BACK", height="2", width="15",bg="tan", font=("Calibri", 15),relief="ridge",bd=8,command=lambda:[fetch_destroy(),logged_gui()]).pack(side=RIGHT,padx=20)
        
        
    
b=bank()

def pin_error():
    messagebox.showwarning("WARNING","userid or password is inavalid.\nTRY AGAIN.")
def pin_not_match():
    messagebox.showwarning("WARNING","PIN IS NOT MATCHED.\nRE ENTER THE PIN.")

def reg_info():
    messagebox.showinfo("INFO","NAME: must be string.\nUSERID: must be 6 digit number.\nACCOUNT NO: must be start 25101000+ any 5 digits number.\nPIN: must be 4 digit number")
def reg_success():
    messagebox.showinfo("INFO","REGISTRATION SUCCESSSFUL.")

def logout():
    logged_screeen_destroy()
    logout=datetime.datetime.today().strftime('%H:%M:%S')
    cur.execute('''update LOGTAB set LOGOUT=? where LOGIN=?;''',(logout,login))
    connector.commit()
    messagebox.showinfo("INFO","LOGOUT SUCCESS.")

def debit_mes():
    messagebox.showinfo("INFO","AMMOUNT DEBITED SUCCESSFULLY.")

def debit_error():
    messagebox.showinfo("WARNING","INSUFFICIENT BALANCE.")
def update_mes():
    messagebox.showinfo("INFO","DETAILS UPDATED SUCCESSFULY.")
def cre_bal_error():
    messagebox.showwarning("WARNING","YOU HAVE EXCEEDED THE LIMIT 5000/-.")
def cre_mes():
    messagebox.showinfo("INFO","AMOUNT CREDITED TO YOUR SUCCESSFULY.")
def del_mes():
    messagebox.showinfo("INFO","ACCOUNT DELETED SUCCESSFULY.")
def del_user_error():
    messagebox.showwarning("WARNING","USERID NOT FOUND.")
def cre_error_mes():
    messagebox.showwarning("WARNING","AMOUNT IS GOING TO EXCEEDED.")    
def pay_mes():
    messagebox.showinfo("INFO","LOAN ACCOUNT PAID SUCCESSFULLY.")
def pay_error():
    messagebox.showwarning("WARNING","INSUFFICIENT BALANCE TO PAY LOAN.")


def det_print(select_screen):
    Label(select_screen,text=("USERID:",userid_var),font=("Calibri", 15)).pack()

    name_get=cur.execute('''select NAME from bank where USERID=?;''',(userid_var,))
    for i in name_get:
        name_get=i
    Label(select_screen,text=("NAME:",name_get),font=("Calibri", 15)).pack()

    acno_get=cur.execute('''select ACNO from bank where USERID=?;''',(userid_var,))
    for i in acno_get:
        acno_get=i
    Label(select_screen,text=("ACCOUNT_NO:",acno_get),font=("Calibri", 15)).pack()

def debit_bal():
    account=int(ac_entry.get())
    d_amount=int(de_entry.get())
    accounts=cur.execute('''select ACNO from bank;''')
    for j in accounts:
        if account==j[0]:
            balance=cur.execute('''select BALANCE from bank where USERID=?;''',(userid_var,))
            for i in balance:
                balance=i
            if d_amount<=balance[0]:
                balance=balance[0]-d_amount
                cur.execute('''update bank set BALANCE=? where USERID=?;''',(balance,userid_var,))
                date=datetime.datetime.today().strftime('%d-%m-%y(%H:%M:%S)')
                names=cur.execute('''select NAME from bank where USERID=?;''',(userid_var,))
                for i in names:
                    name=i[0]
                dece="debit"
                cur.execute('''insert into transactions values(?,?,?,?,?,?);''',(name,userid_var,date,dece,account,d_amount))
                connector.commit()
                crebalance=cur.execute('''select BALANCE from bank where ACNO=?;''',(account,))
                for i in crebalance:
                    crebalance=i
                    crebalance=crebalance[0]+d_amount
                    cur.execute('''update bank set BALANCE=? where ACNO=?;''',(crebalance,account,))
                    name=cur.execute('''select NAME from bank where ACNO=?;''',(account,))
                    for i in name:
                        name=i[0]
                    ruser=cur.execute('''select USERID from bank where ACNO=?;''',(account,))
                    for i in ruser:
                        ruser=i[0]
                    sac=cur.execute('''select ACNO from bank where USERID=?;''',(userid_var,))
                    for i in sac:
                        sac=i[0]
                        
                    cur.execute('''insert into transactions values(?,?,?,?,?,?);''',(name,ruser,date,"credit",sac,d_amount))
                    connector.commit()
                debit_mes()
            else:
                debit_error()

def credit_bal():
    cr_amount=int(ce_entry.get())
    limit=5000
    dece="loan"
    get=cur.execute('''select AMOUNT from transactions where DECE=? and USERID=?;''',(dece,userid_var))
    t_amount=0
    for i in get:
        t_amount +=i[0]
        
    if t_amount<=limit:
        bal=t_amount+cr_amount
        if bal<=5000:

            balance=cur.execute('''select BALANCE from bank where USERID=?;''',(userid_var,))
            for i in balance:
                balance=i
            balance=balance[0]+cr_amount
            cur.execute('''update bank set BALANCE=? where USERID=?;''',(balance,userid_var,))

            bank_balance=cur.execute('''select BALANCE from bank where USERID=?;''',(328754,))
            for i in bank_balance:
                bank_balance=i
            bank_balance=bank_balance[0]-cr_amount
            cur.execute('''update bank set BALANCE=? where USERID=?;''',(bank_balance,328754,))

            connector.commit()

            global date
            date=datetime.datetime.today().strftime('%d-%m-%y(%H:%M:%S)')
            names=cur.execute('''select NAME from bank where USERID=?;''',(userid_var,))
            for i in names:
                name=i[0]
            acno=cur.execute('''select ACNO from bank where USERID=?;''',(userid_var,))
            for i in acno:
                racno=i[0]
            cur.execute('''insert into transactions values(?,?,?,?,?,?);''',(name,userid_var,date,dece,racno,cr_amount))

            names=cur.execute('''select NAME from bank where USERID=?;''',(328754,))
            for i in names:
                name=i[0]
            acno=cur.execute('''select ACNO from bank where USERID=?;''',(328754,))
            for i in acno:
                racno=i[0]
            cur.execute('''insert into transactions values(?,?,?,?,?,?);''',(name,328754,date,"bank_loan",racno,cr_amount))
            connector.commit()
            cre_mes()
        else:
            cre_error_mes()
    else:
        cre_bal_error()

def update_det():
    name=username_entry.get()
    pin=pin_entry.get()
    check_pin=pin_re_entry.get()
    if pin==check_pin:
        cur.execute('''update bank set NAME=?,PIN=? where USERID=?;''',(name.upper(),int(pin),userid_var))
        connector.commit()
        time.sleep(1)
        update_mes()

def del_ac():
    del_userid=int(del_userid_entry.get())
    userids=cur.execute('''select USERID from bank;''')
    
    for j in userids:
        if del_userid==j[0]:
            cur.execute('''delete from bank where USERID=?;''',(del_userid,))
            connector.commit()
            disp_list.delete(0,1)
            disp_list.insert(1,"ACCOUNT DELETED SUCCESSFULLY")
        else:
            disp_list.delete(0,1)
            disp_list.insert(1,"USERID NOT FOUND.")

    
def fetch_trans():
    
    for i in table.get_children():
        table.delete(i)
    
    get=sort.get()
    data=cur.execute('''select * from transactions where USERID=? and DECE=?;''',(userid_var,get,))
    for i in data:
        NAME=i[0]
        USERID=i[1]
        DATE=i[2]
        DECE=i[3]
        ACNO=i[4]
        AMOUNT=i[5]
        table.insert("","end",values=(NAME,USERID,DATE,DECE,ACNO,AMOUNT))
        
def logged_gui():
    global logged_screen
    logged_screen = Toplevel()
    logged_screen.title("YOUR BANK ACCOUNT")
    logged_screen.geometry("1000x600")
    Label(logged_screen, text="BANK ACCOUNT",bg="cadet blue", width="300", height="2", font=("Calibri", 13)).pack()
    #fetch_name=cur.execute('''select NAME from bank where USERID=?;''',(bank.userid,))
    select_screen=logged_screen
    det_print(select_screen)

    #========================LOGGED GUI=================#
    btn_frame=Frame(logged_screen,bg="cadet blue",width=900,height=300,relief="ridge",bd=10)
    btn_frame.pack(pady=50)

    
    btn_check_bal=Button(btn_frame,text="check balance", height="2", bg="tan",width="15", font=("Calibri", 15),command=b.check_bal).pack(side=LEFT)
    btn_credit=Button(btn_frame,text="Loan", height="2", width="15",bg="tan", font=("Calibri", 15),command=b.credit).pack(side=LEFT,padx=5)
    btn_debit=Button(btn_frame,text="debit", height="2", width="15",bg="tan", font=("Calibri", 15),command=b.debit).pack(side=LEFT,padx=5)
    btn_update=Button(btn_frame,text="update", height="2", width="15",bg="tan", font=("Calibri", 15),command=b.update_user).pack(side=LEFT,padx=5)
    btn_delate=Button(btn_frame,text="delate", height="2", width="15", bg="tan",font=("Calibri", 15),command=b.delate_user).pack(side=LEFT,padx=5)
    btn_fetch_details=Button(btn_frame,text="Profile", height="2", width="15", bg="tan",font=("Calibri", 15),command=b.fetch_data).pack(side=LEFT,padx=5)
    btn_fetch_details=Button(logged_screen,text="fetch transactions", height="2", width="15", bd=5,bg="tan",font=("Calibri", 15),command=b.fetch_trans).pack(padx=5)

    ctrl_frame=Frame(logged_screen,bg="cadet blue",width=700,height=80,relief="ridge",bd=10)
    ctrl_frame.pack(anchor=SE,pady=50)
    btn_logout=Button(ctrl_frame,text="Log out", height="2", width="15",bg="orange",font=("Calibri", 15),command=logout).pack(side=LEFT)


    
# Designing window for registration
def register():
    
    global register_screen
    register_screen = Tk()
    register_screen.title("Register")
    register_screen.geometry("1000x600")
 
    global username
    global user_id
    global account
    global pin_etr
    global re_pin
    global username_entry
    global userid_entry
    global ac_entry
    global pin_entry
    global pin_re_entry

    username = StringVar()
    user_id=IntVar(value="")
    account=IntVar(value="")
    pin_etr=IntVar(value="")
    re_pin=IntVar(value="")
 
    Label(register_screen, text="REGISTER FOR YOUR BANK ACCOUNT",bg="cadet blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(register_screen, text="").pack()

    username_lable = Label(register_screen, text="name * ",font=("Calibri", 20))
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username,font=("Calibri", 15))
    username_entry.pack()

    userid_lable = Label(register_screen, text="userid * ",font=("Calibri", 20))
    userid_lable.pack()
    userid_entry = Entry(register_screen, textvariable=user_id,font=("Calibri", 15))
    userid_entry.pack()

    ac_lable = Label(register_screen, text="ACCOUNT.NO * ",font=("Calibri", 20))
    ac_lable.pack()
    ac_entry = Entry(register_screen, textvariable=account,font=("Calibri", 15))
    ac_entry.pack()

    pin_lable = Label(register_screen, text="PIN * ",font=("Calibri", 20))
    pin_lable.pack()
    pin_entry = Entry(register_screen, textvariable=pin_etr,show="*",font=("Calibri", 15))
    pin_entry.pack()

    pin_re_lable = Label(register_screen, text="RE PIN * ",font=("Calibri", 20))
    pin_re_lable.pack()
    pin_re_entry = Entry(register_screen, textvariable=re_pin,show="*",font=("Calibri", 15))
    pin_re_entry.pack()
    
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1,font=("Calibri", 20), bg="cadetblue",command=b.new_user).pack()
    Button(register_screen, text="back to home", width=12, height=1,font=("Calibri", 15),command=register_destroy).pack(pady=30)

 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel()
    login_screen.title("Login")
    login_screen.geometry("1000x600")
    Label(login_screen, text="LOGIN TO YOUR BANK ACCOUNT",bg="cadet blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(login_screen, text="").pack()
 
    global userid
    global pin
 
    userid= IntVar(value="")
    pin = IntVar(value="")
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="USERID * ",font=("Calibri", 20)).pack()
    username_login_entry = Entry(login_screen,textvariable=userid,font=("Calibri", 20))
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="PIN * ",font=("Calibri", 20)).pack()
    password_login_entry = Entry(login_screen, textvariable=pin, show= '*',font=("Calibri", 20))
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1,font=("Calibri", 20),bg="cadetblue",command=login_check).pack()
    Button(login_screen, text="back to home", width=12, height=1,font=("Calibri", 15),command=login_destroy).pack(pady=30)
    


    
def login_check():
    global userid_var
    global login
    
    userid_var=userid.get()
    userids=cur.execute('''select USERID from bank;''')
    all_data=cur.execute('''select * from bank;''')
    for i in userids:
        if userid_var in i:
            pin_var=pin.get()
            pins=cur.execute('''select PIN from bank where USERID=?;''',(userid_var,))
            for k in pins:
                pass
            if pin_var in k:
                names=cur.execute('''select NAME from bank where USERID=?;''',(userid_var,))
                for i in names:
                    name=i[0]
                
                date=datetime.datetime.today().strftime('%d-%m-%y')
                login=datetime.datetime.today().strftime('%H:%M:%S')
                logout=0

                cur.execute('''insert into LOGTAB values(?,?,?,?,?);''',(name,userid_var,date,login,logout))
                connector.commit()
                
                login_destroy()
                logged_gui()
            else:
                login_destroy()
                pin_error()
                
                
    
                   

def login_destroy():
    login_screen.destroy()

def register_destroy():
    register_screen.destroy()
def logged_screeen_destroy():
    logged_screen.destroy()
def check_bal_destroy():
    check_bal_screen.destroy()

def debit_destroy():
    debit_screen.destroy()
def update_destroy():
    update_screen.destroy()
def profile_destroy():
    profile_screen.destroy()
def credit_destroy():
    credit_screen.destroy()

def del_screen_destroy():
    delete_screen.destroy()
    logged_screen.destroy()
def fetch_destroy():
    fetch_screen.destroy()
    
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1000x600")
    main_screen.title("Account Login")
    Label(text="ASHOK BANK", bg="cadet blue", width="300", height="2", font=("Calibri", 30)).pack()
    Label(text="").pack()
    Label(text="HOME PAGE",font=("Calibri", 20)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30",font=("Calibri", 15), command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", font=("Calibri", 15),command=register).pack()
    Label(text="IF YOU HAVE AN ACCOUNT JUST LOGIN.OR YOU COLUD REGISTER. ", width="300", height="2", font=("Calibri", 13)).pack()
 
    main_screen.mainloop()

main_account_screen()


