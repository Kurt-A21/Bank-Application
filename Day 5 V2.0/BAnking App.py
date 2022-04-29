from functools import update_wrapper
import tkinter as tk
from tkinter import Button, Entry, Label, PhotoImage, StringVar, Toplevel, font
from tkinter.constants import N, W
from typing import AsyncGenerator
from PIL import ImageTk, Image
import os


def show_frame(frame):
    frame.tkraise()

window = tk.Tk()
window.iconbitmap("Images/bank icon1.ico")
window.title("Bank Application")
window.state("normal")
window.geometry("400x400")

window.rowconfigure(0, weight = 1)
window.columnconfigure(0, weight = 1)

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)



for frame in (frame1, frame2, frame3):
  frame.grid(row = 0, column= 0, sticky="nsew")

global login_name

def login_session():
      all_accounts = os.listdir()
      global login_name
      login_name = temp_username.get()
      login_password = temp_login_password.get()
     
      for name in all_accounts:
            if name == login_name:
                  file = open(name, "r")
                  file_data = file.read()
                  file_data = file_data.split("\n")
                  password = file_data[1]
                  #Account Dashboard
                  if login_password == password:
                        frame1.destroy()
                        open(openWindow())
                        return
                  else: 
                        login_notify.config(fg="red", bg= "white", text="Password is incorrect*")
                        return            
      login_notify.config(fg="red", bg="white", text="Account does not exist*")
      


      
#Deposit amount
def deposit():
      #Vars
      global amount 
      global deposit_notif
      global current_balance_label
      global updated_balance
      amount = StringVar()
      
      file = open(login_name, "r")
      file_data = file.read()
      user_details = file_data.split("\n")
      details_balance = user_details[4]
      
      #Deposit window   
      credit = Toplevel(window)
      credit.title("Credit Amount")
      credit.iconbitmap("Images/bank icon1.ico")
      credit.config(bg="#5BFBE5")
      credit.geometry("320x200") 
      #Labels
      Label(credit, text="Deposit", font="arial, 14", bg="#5BFBE5").grid(row=0, sticky=W, pady=15)
      current_balance_label = tk.Label(credit, text="Cureent Balance :R"+details_balance, font="arial, 11", bg="#5BFBE5")
      current_balance_label.grid(row=1, sticky=W)
      Label(credit, text="Amount : ", bg="#5BFBE5", font="arial,12").grid(row=2, sticky=W, pady=5)
      deposit_notif = Label(credit, font="arial, 12",bg="#5BFBE5")
      deposit_notif.grid(row=4, sticky=W, pady=5)
      #Entry
      Entry(credit, width=15, textvariable=amount).grid(row=2, column = 1, pady=5, sticky=W)
      #Button
      Button(credit, text="Confirm", font="arial, 9", command=finish_deposit).grid(row=3, sticky=W)
      
def finish_deposit():
      if amount.get()=="":
            deposit_notif.config(text="Amount is required *", fg="red")
            return
      if float(amount.get()) <= 0:
            deposit_notif.config(text="A positive amount is needed *", fg="red")    
            return
      
      file = open(login_name, 'r+')
      file_data = file.read()
      user_details = file_data.split("\n")
      current_balance = user_details[4]
      updated_balance = current_balance
      updated_balance = float(current_balance) + float(amount.get())
      file_data = file_data.replace(current_balance, str(updated_balance))
      file.seek(0)
      file.truncate()
      file.write(file_data)
      file.close()
      
      current_balance_label.config(text="Current Balance : R" +str(updated_balance), fg="purple")
      deposit_notif.config(text="Deposit successfully", fg="purple")

      
#Debit amount
def withdrawel():
      debit = Toplevel(window)
      debit.title("Debit Amount")
      debit.iconbitmap("Images/bank icon1.ico")
      debit.config(bg="#5BFBE5")
      debit.geometry("320x200")
      
      #Vars
      global withdraw_amount 
      global withdraw_notif
      global current_balance_label
      withdraw_amount = StringVar()
      
      file = open(login_name, "r")
      file_data = file.read()
      user_details = file_data.split("\n")
      details_balance = user_details[4]
      
      #Labels
      Label(debit, text="Deposit", font="arial, 14", bg="#5BFBE5").grid(row=0, sticky=W, pady=15)
      current_balance_label = tk.Label(debit, text="Cureent Balance :R"+details_balance, font="arial, 11", bg="#5BFBE5")
      current_balance_label.grid(row=1, sticky=W)
      Label(debit, text="Amount : ", bg="#5BFBE5", font="arial,12").grid(row=2, sticky=W, pady=5)
      withdraw_notif = Label(debit, font="arial, 12",bg="#5BFBE5")
      withdraw_notif.grid(row=4, sticky=W, pady=5)
      #Entry
      Entry(debit, width=15, textvariable=withdraw_amount).grid(row=2, column = 1, pady=5, sticky=W)
      #Button
      Button(debit, text="Confirm", font="arial, 9", command=finish_withdraw).grid(row=3, sticky=W)
      
      
def finish_withdraw():
      if withdraw_amount.get()=="":
            deposit_notif.config(text="Amount is required *", fg="red")
            return
      if float(withdraw_amount.get()) <= 0:
            deposit_notif.config(text="A positive amount is needed *", fg="red")    
            return
      
      file = open(login_name, 'r+')
      file_data = file.read()
      user_details = file_data.split("\n")
      current_balance = user_details[4]
      
      if float(withdraw_amount.get()) > float(current_balance):
            withdraw_notif.config(text="Insufficient funds", fg="red") 
            return
      
      updated_balance = current_balance
      updated_balance = float(current_balance) - float(amount.get())
      file_data = file_data.replace(current_balance, str(updated_balance))
      file.seek(0)
      file.truncate()
      file.write(file_data)
      file.close()
      
      current_balance_label.config(text="Current Balance : R" +str(updated_balance), fg="purple")
      withdraw_notif.config(text="Withdraw successfully", fg="purple")
      
def personal_details():
      file = open(login_name, 'r')
      file_data = file.read()
      user_details = file_data.split("\n")
      details_name = user_details[0]
      details_age = user_details[2]
      details_gender = user_details[3]
      details_acc_bal = user_details[4]
      
      per_details = Toplevel(window)
      per_details.title("Personal details")
      per_details.iconbitmap("Images/bank icon1.ico")
      per_details.config(bg="#5BFBE5")
      per_details.geometry("180x160")
      
      #Labels
      title = tk.Label(per_details, bg="#5BFBE5", text="Personal Details\n", font="arial, 14").grid(row=0, sticky= W)
      
      d_name = tk.Label(per_details, bg="#5BFBE5", text="Name : "+details_name, font="arial, 11").grid(row=2, sticky= W)
      
      d_age = tk.Label(per_details, bg="#5BFBE5", text="Age : "+details_age, font='arial, 11').grid(row=3, sticky= W)
      
      d_gender = tk.Label(per_details, bg="#5BFBE5", text="Gender : "+details_gender, font="arial,11").grid(row=4, sticky= W)

#=============================frame1 code

bg=PhotoImage(file="Images/bg wallpaper1.png")
my_wallpaper = tk.Label(frame1, image=bg)
my_wallpaper.place(x=0, y=0, relheight=1, relwidth=1)
 
#==========Vars
global temp_username
global temp_login_password
global login_notify
global frame1_title
global frame2_title

temp_username = StringVar()
temp_login_password = StringVar()
login_notify = StringVar()

frame1_title = tk.LabelFrame(frame1, text="Welcome To", font="arial, 18", padx=30, pady=20)
frame1_title.config(bg="white")
frame1_title.pack(padx=25, pady= 20 )

my_img  = ImageTk.PhotoImage(Image.open("Images/logo.png"))
my_label = tk.Label(frame1_title, image = my_img).pack()

#============Lable and Entry
user_name = tk.Label(frame1_title, text="Username:", bg="white")
user_name.pack()
user_name1 = tk.Entry(frame1_title, textvariable= temp_username,  bg="#5BFBE5")
user_name1.pack()

password = tk.Label(frame1_title, text="Password:", bg="white")
password.pack()
password1 = tk.Entry(frame1_title, bg="#5BFBE5", textvariable= temp_login_password, show="*")
password1.pack()

login_btn = tk.Button(frame1_title, text="Login", command = login_session,  font="arial, 10")
login_btn.pack()

login_notify = tk.Label(frame1_title, font="arial, 12")
login_notify.pack()



msg = tk.Label(frame1_title, text="\nIf you want to create account click on Register\n", font="bold, 10", bg="white")
msg.pack()


#============================Register Window
def finsih_reg():
     name3 = temp_name.get()
     password = temp_passsword.get()
     age = temp_age.get()
     gender = temp_gender.get()
     
     all_accounts = os.listdir()
     print(all_accounts)
     
     if name3 == "" or password == "" or age == "" or gender == "":
           notif.config(bg="#5BFBE5", fg = "red", text= "All fields are required *")
           return
    
     for name_check in all_accounts:
                 if name3 == name_check:
                      notif.config(bg="#5BFBE5", fg="red", font="arial, 11", text="Account has already exist")
                      return
                 else:
                     new_file = open(name3, "w")
                     new_file.write(name3+"\n")
                     new_file.write(password+"\n")
                     new_file.write(age+"\n")
                     new_file.write(gender+"\n")
                     new_file.write("0")
                     new_file.close()
                     notif.config(bg="#5BFBE5", fg="purple", font="arial.11", text="Account have been created")
                     
        
def open2nd():
  #Global Vars    
  global temp_name
  global temp_passsword
  global temp_age
  global temp_gender
  global notif

  
  #Vars
  temp_name = StringVar()
  temp_passsword = StringVar()
  temp_age = StringVar()
  temp_gender = StringVar()

  
  reg = Toplevel(window)
  reg.title("Register")
  reg.iconbitmap("Images/bank icon1.ico")
  reg.config(bg="#5BFBE5")
  label = tk.Label(reg, text="Register\n",  font="arial, 18", fg="black", bg="#5BFBE5")
  label.pack(padx=55, pady=24)

  name2 = tk.Label(reg, text="Name", bg="#5BFBE5", font="arial, 12").pack()
  name1 = tk.Entry(reg, bg="white", textvariable = temp_name).pack()

  age2 = tk.Label(reg, text="Age", bg="#5BFBE5", font="arial, 12").pack()
  age1 = tk.Entry(reg, bg="white", textvariable = temp_age).pack()
  
  gender2 = tk.Label(reg, text="Gender", bg="#5BFBE5", font="arial, 12").pack()
  gender1 = tk.Entry(reg, bg="white", textvariable = temp_gender).pack()

  pass_w2 = tk.Label(reg, text="Password", bg="#5BFBE5", font="arial, 12").pack() 
  pass_w1 = tk.Entry(reg, bg="white", textvariable = temp_passsword, show="*").pack()
  
  con_firm = tk.Button(reg, text="Confirm",  font="arial, 12", command = finsih_reg).pack(pady=10, padx=20)
  
  notif = tk.Label(reg, font="arial, 11")
  notif.pack()
  
  
reg_btn = tk.Button(frame1_title, text="Register", command = open2nd)
reg_btn.pack()

      
           
#=============================frame2code
def openWindow():
            bg1=PhotoImage(file="Images/bg wallpaper1.png")
            my_wallpaper = tk.Label(frame3, image=bg1)
            my_wallpaper.place(x=0, y=0, relheight=1, relwidth=1)

            file = open(login_name, 'r')
            file_data = file.read()
            user_details = file_data.split("\n")
            details_name = user_details[0]
            details_acc_bal = user_details[4]


                  
            frame2_title = tk.LabelFrame(frame3, text="Hi there "+details_name , font="arial, 18")
            frame2_title.config(bg="white")
            frame2_title.pack(padx=35, pady= 30 )

            c_bal = Label(frame2_title, bg="white", text="Current Balance : R"+details_acc_bal, font="arial,12").pack(pady=20)
            credit_amount1 = tk.Button(frame2_title, text="Deposit Amount", command = deposit).pack(pady=15)
            debit_amount2 = tk.Button(frame2_title, text="Withdraw Amount", command= withdrawel).pack(pady = 15)
            p_details = tk.Button(frame2_title, text = "Personal Details", command = personal_details).pack(pady = 15)
            prevbtn = tk.Button(frame2_title, text= "Exit", command= window.destroy).pack(pady=15)
            
            
            qrevbtn = tk.Button(openWindow, text= "Exit")
            qrevbtn.pack()


      
show_frame(frame1)

window.mainloop()