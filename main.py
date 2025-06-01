from customtkinter import *
from PIL import ImageTk, Image, ImageFilter
from tkinter import ttk
import mysql.connector

set_appearance_mode("light")

img1= CTkImage(Image.open("Air_icon.png"), size=(35,35))
img= CTkImage(Image.open("Air_icon.png"), size=(55,55))
img2= CTkImage(Image.open("light_b.png"), size=(25,25))
root = CTk()
root.geometry("2000x2000")
root.configure(fg_color="#FFFFFF")

fram = None
l4=CTkLabel(master=fram)

count= 1

db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='66165Nisch&18503',
    database='air'
)
cursor = db_connection.cursor()

def login():
    global fram
    fram = CTkFrame(master=root, width= 200, height=800, fg_color="#FFFFFF")
    fram.pack(padx=10, pady=100, fill= BOTH, expand= True)

    l1=CTkLabel(master=fram, image=img1,text="  Welcome to Stark Airlines", font=("Bell MT", 19), compound=LEFT).pack(padx=10, pady=30)

    l2=CTkEntry(master=fram, placeholder_text="Username", font=("Bell MT", 19), width = 180)
    l2.pack(padx=10, pady=10 )

    l3=CTkEntry(master=fram, placeholder_text="Password", font=("Bell MT", 19), width = 180)
    l3.pack(padx=10, pady=20)
    l3.configure(show="*")

    b=  CTkButton(master=fram, text="Login", font=("Bell MT", 19), command=lambda :conf(l2,l3)).pack(padx=10, pady=10)

def conf(x,y):
    global count
    global l4
    # if count >1:
    #     l4.pack_forget()
    # count+=1
    # if x.get()=="Sanjeev" and y.get()== "Sah":
    #     admin()
    # elif x.get()=="Guest" and y.get()== "Guest":
    #     Current_flight_N()
    # else:
    #     l4=CTkLabel(master=fram, text="Invalid Username or Password")
    #     l4.pack(padx=10, pady=10)
    admin()
    

def admin():
    fram.pack_forget()
    global fra
    fra= CTkFrame(root, width= 200, height=800, fg_color="#FFFFFF")
    fra.pack()
    
    g= CTkFrame(master=fra)
    g.pack(pady=1, anchor=E)

    bt1 = CTkButton(master=g, text="", image=img2, font=("Lucida Calligraphy Italic", 19), width=1, command=back)
    bt1.pack(side=RIGHT, padx=1)
    
    L1=CTkLabel(master=fra, image=img,text=" Stark Airlines", font=("Lucida Calligraphy Italic", 30), compound=LEFT).pack(padx=10, pady=10)

    b1=  CTkButton(master=fra, text="Current Flight", font=("Bell MT", 19), command= Current_flight_A).pack(padx=40, pady=20, anchor=W)
    b2=  CTkButton(master=fra, text="Flight Details", font=("Bell MT", 19), command=Flight_Details).pack(padx=40, pady=10, anchor=W)
    b7=  CTkButton(master=fra, text="Reservation Options", font=("Bell MT", 19), command=Reservation).pack(padx=40, pady=10, anchor=W)
    l=CTkLabel(master=fra, text="Customer :", font=("Bell MT, B", 22)).pack(padx=40, pady=20, side= LEFT)
    b3=  CTkButton(master=fra, text="Add", font=("Bell MT", 19), command=customer_add).pack(padx=10, pady=10, side = LEFT)
    b4=  CTkButton(master=fra, text="View", font=("Bell MT", 19), command=customer_view).pack(padx=10, pady=10, side = LEFT)
    b5=  CTkButton(master=fra, text="Update", font=("Bell MT", 19), command=customer_update).pack(padx=10, pady=10, side = LEFT)
    b6=  CTkButton(master=fra, text="Delete", font=("Bell MT", 19), command=customer_delete).pack(padx=10, pady=10, side = LEFT)

def Current_flight_A():
    fra.pack_forget()
    global f
    f = CTkFrame(master=root)
    f.pack()

    g= CTkFrame(master=f)
    g.pack(pady=1, anchor=E)

    bt1 = CTkButton(master=g, text="", image=img2, font=("Lucida Calligraphy Italic", 19), width=1, command=back_1)
    bt1.pack(side=RIGHT, padx=1)

    b1=  CTkLabel(master=f, text="Current Flights :", font=("Lucida Calligraphy Italic", 30)).pack(padx=20, pady=20, anchor=W, side=TOP)
    f1 = CTkFrame(master=f)
    f1.pack()
    f2 = CTkFrame(master=f)
    f2.pack()
    f3 = CTkFrame(master=f)
    f3.pack()
    b1=  CTkLabel(master=f1, text="Morning (9 AM):", font=("Lucida Calligraphy Italic", 30)).pack(padx=20, pady=20, anchor=W)
    scrollbar = ttk.Scrollbar(master=f1, orient="vertical")
    scrollbar.pack(side="right",fill="y")
    global tree
    tree = ttk.Treeview(f1, columns=("customer_name","phone_no","age","route","reservation_type"), show="headings", yscrollcommand=scrollbar.set)
    tree.heading("customer_name", text="Customer Name")
    tree.heading("phone_no", text="Phone Number")
    tree.heading("age", text="Age")
    tree.heading("route", text="Route")
    tree.heading("reservation_type", text="Reservation Type")
    tree.pack(fill="both",expand=True)
    currentflightm_sql()

    b1=  CTkLabel(master=f2, text="Day (12:30 PM): ", font=("Lucida Calligraphy Italic", 30)).pack(padx=20, pady=20, anchor=W)
    scrol = ttk.Scrollbar(master=f2, orient="vertical")
    scrol.pack(side="right",fill="y")
    tree = ttk.Treeview(f2, columns=("customer_name","phone_no","age","route","reservation_type"), show="headings", yscrollcommand=scrol.set)
    tree.heading("customer_name", text="Customer Name")
    tree.heading("phone_no", text="Phone Number")
    tree.heading("age", text="Age")
    tree.heading("route", text="Route")
    tree.heading("reservation_type", text="Reservation Type")
    tree.pack(fill="both",expand=True)
    currentflightd_sql()


    b1=  CTkLabel(master=f3, text="Evening (16:15 PM):", font=("Lucida Calligraphy Italic", 30)).pack(padx=20, pady=20, anchor=W)
    scro = ttk.Scrollbar(master=f3, orient="vertical")
    scro.pack(side="right",fill="y")
    tree = ttk.Treeview(f3, columns=("customer_name","phone_no","age","route","reservation_type"), show="headings", yscrollcommand=scro.set)
    tree.heading("customer_name", text="Customer Name")
    tree.heading("phone_no", text="Phone Number")
    tree.heading("age", text="Age")
    tree.heading("route", text="Route")
    tree.heading("reservation_type", text="Reservation Type")
    tree.pack(fill="both",expand=True)
    currentflighte_sql()

def Current_flight_N():
    fram.pack_forget()
    global f
    f = CTkFrame(master=root)
    f.pack()

    g= CTkFrame(master=f)
    g.pack(pady=1, anchor=E)

    bt1 = CTkButton(master=g, text="", image=img2, font=("Lucida Calligraphy Italic", 19), width=1, command=back_1N)
    bt1.pack(side=RIGHT, padx=1)

    b1=  CTkLabel(master=f, text="Current Flights :", font=("Lucida Calligraphy Italic", 30)).pack(padx=20, pady=20, anchor=W, side=TOP)
    f1 = CTkFrame(master=f)
    f1.pack()
    f2 = CTkFrame(master=f)
    f2.pack()
    f3 = CTkFrame(master=f)
    f3.pack()
    b1=  CTkLabel(master=f1, text="Morning (9 AM):", font=("Lucida Calligraphy Italic", 30)).pack(padx=20, pady=20, anchor=W)
    scrollbar = ttk.Scrollbar(master=f1, orient="vertical")
    scrollbar.pack(side="right",fill="y")
    global tree
    tree = ttk.Treeview(f1, columns=("customer_name","phone_no","age","route","reservation_type"), show="headings", yscrollcommand=scrollbar.set)
    tree.heading("customer_name", text="Customer Name")
    tree.heading("phone_no", text="Phone Number")
    tree.heading("age", text="Age")
    tree.heading("route", text="Route")
    tree.heading("reservation_type", text="Reservation Type")
    tree.pack(fill="both",expand=True)
    currentflightm_sql()
    
    
    b1=  CTkLabel(master=f2, text="Day (12:30 PM): ", font=("Lucida Calligraphy Italic", 30)).pack(padx=20, pady=20, anchor=W)
    scrol = ttk.Scrollbar(master=f2, orient="vertical")
    scrol.pack(side="right",fill="y")
    tree = ttk.Treeview(f2, columns=("customer_name","phone_no","age","route","reservation_type"), show="headings", yscrollcommand=scrol.set)
    tree.heading("customer_name", text="Customer Name")
    tree.heading("phone_no", text="Phone Number")
    tree.heading("age", text="Age")
    tree.heading("route", text="Route")
    tree.heading("reservation_type", text="Reservation Type")
    tree.pack(fill="both",expand=True)
    currentflightd_sql()


    b1=  CTkLabel(master=f3, text="Evening (16:15 PM):", font=("Lucida Calligraphy Italic", 30)).pack(padx=20, pady=20, anchor=W)
    scro = ttk.Scrollbar(master=f3, orient="vertical")
    scro.pack(side="right",fill="y")
    tree = ttk.Treeview(f3, columns=("customer_name","phone_no","age","route","reservation_type"), show="headings", yscrollcommand=scro.set)
    tree.heading("customer_name", text="Customer Name")
    tree.heading("phone_no", text="Phone Number")
    tree.heading("age", text="Age")
    tree.heading("route", text="Route")
    tree.heading("reservation_type", text="Reservation Type")
    tree.pack(fill="both",expand=True)
    currentflighte_sql()

def currentflightm_sql():
    cursor.execute("select customer_name,phone_no,age,route,reservation_type from customer,flight,reserve where customer.flight_id=flight.flight_id and customer.reserve_id=reserve.reserve_id and flight.flight_time='09:00:00' and flight.flight_day='Sunday';")
    data = cursor.fetchall()

    for row in data:
        tree.insert("", "end", values=row)

def currentflightd_sql():
    cursor.execute("select customer_name,phone_no,age,route,reservation_type from customer,flight,reserve where customer.flight_id=flight.flight_id and customer.reserve_id=reserve.reserve_id and flight.flight_time='12:30:00' and flight.flight_day='Sunday';")
    data = cursor.fetchall()

    for row in data:
        tree.insert("", "end", values=row)

def currentflighte_sql():
    cursor.execute("select customer_name,phone_no,age,route,reservation_type from customer,flight,reserve where customer.flight_id=flight.flight_id and customer.reserve_id=reserve.reserve_id and flight.flight_time='16:15:00' and flight.flight_day='Sunday';")
    data = cursor.fetchall()

    for row in data:
        tree.insert("", "end", values=row)

def Flight_Details():
    fra.pack_forget()
    global  f1
    f1 = CTkFrame(master=root)
    f1.pack(fill=BOTH, expand=True)
    g= CTkFrame(master=f1)
    g.pack(pady=1, anchor=E)

    bt1 = CTkButton(master=g, text="", image=img2, font=("Lucida Calligraphy Italic", 19), width=1, command=back_2)
    bt1.pack(side=RIGHT, padx=1)

    b1=  CTkLabel(master=f1, text="Flight Details :", font=("Lucida Calligraphy Italic", 30)).pack(padx=20, pady=20, anchor=W)
    scrollbar = ttk.Scrollbar(master=f1, orient="vertical")
    scrollbar.pack(side="right",fill="y")
    global tree
    tree = ttk.Treeview(f1, columns=("flight_id","flight_time","flight_day","route"), show="headings", yscrollcommand=scrollbar.set)
    tree.heading("flight_time", text="Flight Time")
    tree.heading("flight_id", text="Flight ID")
    tree.heading("flight_day", text="Flight Day")
    tree.heading("route", text="Route")
    tree.pack(fill="both",expand=True)
    flight_sql()

def flight_sql():
    cursor.execute("SELECT * FROM flight")
    data = cursor.fetchall()

    for row in data:
        tree.insert("", "end", values=row)

def Reservation():
    fra.pack_forget()
    global f2
    f2 = CTkFrame(master=root)
    f2.pack()

    g= CTkFrame(master=f2)
    g.pack(pady=1, anchor=E)

    bt1 = CTkButton(master=g, text="", image=img2, font=("Lucida Calligraphy Italic", 19), width=1, command=back_3)
    bt1.pack(side=RIGHT, padx=1)

    b1=  CTkLabel(master=f2, text="Reservation Options :", font=("Lucida Calligraphy Italic", 30)).pack(padx=20, pady=20, anchor=W)
    scrollbar = ttk.Scrollbar(master=f2, orient="vertical")
    scrollbar.pack(side="right",fill="y")
    global tree
    tree = ttk.Treeview(f2, columns=("reservation_id","reservation_type","price","seat_assignment"), show="headings", yscrollcommand=scrollbar.set)
    tree.heading("reservation_type", text="Class")
    tree.heading("reservation_id", text="Reservation ID")
    tree.heading("price", text="Price")
    tree.heading("seat_assignment", text="Seat Assignment")
    tree.pack(fill="both",expand=True)
    reservation_sql()

def reservation_sql():
    cursor.execute("SELECT * FROM reserve")
    data = cursor.fetchall()

    for row in data:
        tree.insert("", "end", values=row)

def customer_add():
    fra.pack_forget()
    global f3, e2, e3, e4, e5, e6, e7
    f3=CTkFrame(master=root,fg_color="#FFFFFF")
    f3.pack()
    g= CTkFrame(master=f3)
    g.pack(pady=1, anchor=E)

    bt1 = CTkButton(master=g, text="", image=img2, font=("Lucida Calligraphy Italic", 19), width=1, command=back_4)
    bt1.pack(side=RIGHT, padx=1)

    l1=CTkLabel(master=f3,text="Add Customer Details",font=("Lucida Calligraphy Italic", 22)).pack(padx=10,pady=10)
    f3a=CTkFrame(master=f3,fg_color="#FFFFFF")
    f3a.pack(padx=10)
    f3b=CTkFrame(master=f3,fg_color="#FFFFFF")
    f3b.pack(padx=10)
    f3c=CTkFrame(master=f3,fg_color="#FFFFFF")
    f3c.pack(padx=10)
    f3d=CTkFrame(master=f3,fg_color="#FFFFFF")
    f3d.pack(padx=10)
    f3e=CTkFrame(master=f3,fg_color="#FFFFFF")
    f3e.pack(padx=10)
    f3f=CTkFrame(master=f3,fg_color="#FFFFFF")
    f3f.pack(padx=10)
    l2=CTkLabel(master=f3a,text="Customer ID",font=("Bell MT", 18)).pack(padx=10,pady=10, side =LEFT)
    e2=CTkEntry(master=f3a, font=("Bell MT", 18))
    e2.pack(padx=10,pady=10)
    l3=CTkLabel(master=f3b,text="Customer Name",font=("Bell MT", 18)).pack(padx=10,pady=10, side =LEFT)
    e3=CTkEntry(master=f3b, font=("Bell MT", 18))
    e3.pack(padx=10,pady=10)
    l4=CTkLabel(master=f3c,text="Age",font=("Bell MT", 18)).pack(padx=10,pady=10, side =LEFT)
    e4=CTkEntry(master=f3c, font=("Bell MT", 18))
    e4.pack(padx=10,pady=10)
    l5=CTkLabel(master=f3d,text="Phone Number",font=("Bell MT", 18)).pack(padx=10,pady=10, side =LEFT)
    e5=CTkEntry(master=f3d, font=("Bell MT", 18))
    e5.pack(padx=10,pady=10)
    l6=CTkLabel(master=f3e,text="Flight ID",font=("Bell MT", 18)).pack(padx=10,pady=10, side =LEFT)
    e6=CTkEntry(master=f3e, font=("Bell MT", 18))
    e6.pack(padx=10,pady=10)
    l7=CTkLabel(master=f3f,text="Reserve ID",font=("Bell MT", 18)).pack(padx=10,pady=10, side =LEFT)
    e7=CTkEntry(master=f3f, font=("Bell MT", 18))
    e7.pack(padx=10,pady=10)
    b1=CTkButton(master=f3,text="ADD",font=("Bell MT",20), command=cust_add).pack(padx=10,pady=10)

    scrollbar = ttk.Scrollbar(master=f3, orient="vertical")
    scrollbar.pack(side="right",fill="y")
    global tree
    tree = ttk.Treeview(f3, columns=("customer_id","customer_name","age","phone_no","flight_id","reserve_id"), show="headings", yscrollcommand=scrollbar.set)
    tree.heading("customer_id", text="Customer ID")
    tree.heading("customer_name", text="Customer Name")
    tree.heading("age", text="Age")
    tree.heading("phone_no", text="Phone Number")
    tree.heading("flight_id", text="Flight ID")
    tree.heading("reserve_id", text="Reserve ID")
    tree.pack(fill="both",expand=True, pady=30)
    customer_sql()

def cust_add():
    cursor.execute("Insert into customer (customer_id, customer_name , age, phone_no, flight_id, reserve_id) values (%s, %s, %s, %s,%s, %s)", (e2.get(), e3.get(),e4.get(), e5.get(),e6.get(), e7.get()))
    db_connection.commit()
    tree.delete(*tree.get_children())
    customer_sql()
    
def customer_view():
    fra.pack_forget()
    global f4
    f4=CTkFrame(master=root,fg_color="#FFFFFF")
    f4.pack(fill= Y, expand=True)
    g= CTkFrame(master=f4)
    g.pack(pady=1, anchor=E)

    bt1 = CTkButton(master=g, text="", image=img2, font=("Lucida Calligraphy Italic", 19), width=1, command=back_5)
    bt1.pack(side=RIGHT, padx=1)
    l1=CTkLabel(master=f4,text="Customer Details",font=("Lucida Calligraphy Italic", 19)).pack(padx=10,pady=10)
    scrollbar = ttk.Scrollbar(master=f4, orient="vertical")
    scrollbar.pack(side="right",fill="y")
    global tree
    tree = ttk.Treeview(f4, columns=("customer_id","customer_name","age","phone_no","flight_id","reserve_id"), show="headings", yscrollcommand=scrollbar.set)
    tree.heading("customer_id", text="Customer ID")
    tree.heading("customer_name", text="Customer Name")
    tree.heading("age", text="Age")
    tree.heading("phone_no", text="Phone Number")
    tree.heading("flight_id", text="Flight ID")
    tree.heading("reserve_id", text="Reserve ID")
    tree.pack(fill="both",expand=True)
    customer_sql()

def customer_sql():
    cursor.execute("SELECT * FROM customer")
    data = cursor.fetchall()

    for row in data:
        tree.insert("", "end", values=row)

def customer_update():
    fra.pack_forget()
    global f5, e3, e4, e5, e6, e7
    f5=CTkFrame(master=root,fg_color="#FFFFFF")
    f5.pack(fill=BOTH, expand=True)
    g= CTkFrame(master=f5)
    g.pack(pady=1, anchor=E)
    bt1 = CTkButton(master=g, text="", image=img2, font=("Lucida Calligraphy Italic", 19), width=1, command=back_6)
    bt1.pack(side=RIGHT, padx=1)
    l1=CTkLabel(master=f5,text="Update Customer Details",font=("Lucida Calligraphy Italic", 19)).pack(padx=10,pady=10)
    
    scrollbar = ttk.Scrollbar(master=f5, orient="vertical")
    scrollbar.pack(side="right",fill="y")
    global tree
    tree = ttk.Treeview(f5, columns=("customer_id","customer_name","age","phone_no","flight_id","reserve_id"), show="headings", yscrollcommand=scrollbar.set)
    tree.heading("customer_id", text="Customer ID")
    tree.heading("customer_name", text="Customer Name")
    tree.heading("age", text="Age")
    tree.heading("phone_no", text="Phone Number")
    tree.heading("flight_id", text="Flight ID")
    tree.heading("reserve_id", text="Reserve ID")
    tree.pack(fill="both",expand=True)
    customer_sql()

    e3 = CTkEntry(master= f5, placeholder_text="Customer Name", font=("Lucida Calligraphy Italic", 19), width=190)
    e3.pack(padx=10,pady=10, side = LEFT, expand=True)
    e4 = CTkEntry(master= f5, placeholder_text="Age", font=("Lucida Calligraphy Italic", 19))
    e4.pack(padx=10,pady=10, side = LEFT, expand=True)
    e5 = CTkEntry(master= f5, placeholder_text="Phone number", font=("Lucida Calligraphy Italic", 19))
    e5.pack(padx=10,pady=10, side = LEFT, expand=True)
    e6 = CTkEntry(master= f5, placeholder_text="Flight ID", font=("Lucida Calligraphy Italic", 19))
    e6.pack(padx=10,pady=10, side = LEFT, expand=True)
    e7 = CTkEntry(master= f5, placeholder_text="Reserve ID", font=("Lucida Calligraphy Italic", 19))
    e7.pack(padx=10,pady=10, side = LEFT, expand=True)

    b= CTkButton(master= f5, text= "Update",  font=("Lucida Calligraphy Italic", 19), command= cust_update).pack(padx=10, pady=10, side = BOTTOM, expand=True)

def cust_update():
    selected_item = tree.selection()
    item = tree.item(selected_item)
    row_data = item['values']
    customer_id = row_data[0]
    cursor.execute("UPDATE customer SET customer_name=%s, age=%s , phone_no=%s, flight_id=%s, reserve_id=%s WHERE customer_id=%s",(e3.get(),e4.get(), e5.get(),e6.get(), e7.get(), customer_id))
    db_connection.commit()
    tree.delete(*tree.get_children())
    customer_sql()


def customer_delete():
    fra.pack_forget()
    global f6
    f6=CTkFrame(master=root,fg_color="#FFFFFF")
    f6.pack(fill= BOTH, expand=True)
    g= CTkFrame(master=f6)
    g.pack(pady=1, anchor=E)
    bt1 = CTkButton(master=g, text="", image=img2, font=("Lucida Calligraphy Italic", 19), width=1, command=back_7)
    bt1.pack(side=RIGHT, padx=1)
    l1=CTkLabel(master=f6,text="Delete Customer Details",font=("Lucida Calligraphy Italic", 19)).pack(padx=10,pady=10)
    scrollbar = ttk.Scrollbar(master=f6, orient="vertical")
    scrollbar.pack(side="right",fill="y")
    global tree
    tree = ttk.Treeview(f6, columns=("customer_id","customer_name","age","phone_no","flight_id","reserve_id"), show="headings", yscrollcommand=scrollbar.set)
    tree.heading("customer_id", text="Customer ID")
    tree.heading("customer_name", text="Customer Name")
    tree.heading("age", text="Age")
    tree.heading("phone_no", text="Phone Number")
    tree.heading("flight_id", text="Flight ID")
    tree.heading("reserve_id", text="Reserve ID")
    tree.pack(fill="both",expand=True)
    customer_sql()
    b= CTkButton(master= f6, text="Delete", font=("Lucida Calligraphy Italic", 19), command = cust_delete).pack(padx=10, pady=30)

def cust_delete():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        row_data = item['values']
        primary_key = row_data[0]
        cursor.execute("DELETE FROM customer WHERE customer_id=%s", (primary_key,))
        db_connection.commit()
        tree.delete(selected_item)
        tree.delete(*tree.get_children())
        customer_sql()

def back():
    fra.pack_forget()
    login()

def back_1():
    f.pack_forget()
    admin()

def back_1N():
    f.pack_forget()
    login()

def back_2():
    f1.pack_forget()
    admin()

def back_3():
    f2.pack_forget()
    admin()
    
def back_4():
    f3.pack_forget()
    admin()
    
def back_5():
    f4.pack_forget()
    admin()

def back_6():
    f5.pack_forget()
    admin()

def back_7():
    f6.pack_forget()
    admin()

login()

root.mainloop()