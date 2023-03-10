import time
import tkinter as tk
import customtkinter
from PIL import ImageTk, Image   # PIL module for images
import mysql.connector as mysql
from tkinter import messagebox

#atm menu instantiation
window = tk.Tk()
#hide menu window until login confirmed
window.withdraw()
#window title
window.title('ɮǟռӄʏʊȶ Virtual ATM')
#window size
window.geometry("700x250")
#code to disable maximize
window.resizable(0,0)
#window background color
window.configure(background="#2C3333")

#####################################################################
#Login Form
#toplevel window for Login
login_Form = tk.Toplevel()	
login_Form.wm_geometry("700x500")
login_Form.resizable(0,0)

frame = tk.Frame(login_Form, background='#2C3333')
frame.place(x=0, y=0, height=700, width=2500)

frame = tk.Frame(login_Form)
frame.place(x=0, y=0, height=500, width=350) 

image=Image.open('ATM(Group)/img/istockphoto-1183227867-612x612.jpg')
img=image.resize((400, 500), Image.ANTIALIAS)
my_img=ImageTk.PhotoImage(img)


add_login_icon = customtkinter.CTkImage(Image.open('ATM(Group)/img/user-circle-solid-24.png').resize((20,20), Image.ANTIALIAS))
add_register_icon = customtkinter.CTkImage(Image.open('ATM(Group)/img/user-plus-solid-24.png').resize((20,20), Image.ANTIALIAS))
add_help_icon = customtkinter.CTkImage(Image.open('ATM(Group)/img/info-circle-regular-24.png').resize((20,20), Image.ANTIALIAS))
add_exit_icon = customtkinter.CTkImage(Image.open('ATM(Group)/img/exit-regular-24.png').resize((20,20), Image.ANTIALIAS))
add_balance_icon = customtkinter.CTkImage(Image.open('ATM(Group)/img/wallet-solid-24(1).png').resize((20,20), Image.ANTIALIAS))
add_receipt_icon = customtkinter.CTkImage(Image.open('ATM(Group)/img/receipt-solid-24(1).png').resize((20,20), Image.ANTIALIAS))
add_deposit_icon = customtkinter.CTkImage(Image.open('ATM(Group)/img/layer-plus-solid-24.png').resize((20,20), Image.ANTIALIAS))
add_withdraw_icon = customtkinter.CTkImage(Image.open('ATM(Group)/img/peso.png').resize((20,20), Image.ANTIALIAS))


label = tk.Label(frame, image = my_img, bg="#2C3333")
label.pack()

label = customtkinter.CTkLabel(master=login_Form, text="ɮǟռӄʏʊȶ", text_color='#E7F6F2', bg_color='#2C3333', font=('Arial', 40))
label.place(x=450, y=70)

name_user = customtkinter.CTkLabel(login_Form,text="Account Name", font=('Arial', 12),bg_color='#2C3333', text_color='#E7F6F2').place(x=430, y=187)
pin = customtkinter.CTkLabel(login_Form,text="Enter Your Pin", font=('Arial', 12),bg_color='#2C3333', text_color='#E7F6F2').place(x=430, y=270)

textbox = customtkinter.CTkEntry(login_Form,width=35,font=('Arial', 12), fg_color='#2C3333',bg_color='#2C3333', text_color='#E7F6F2', corner_radius=10, border_width=1)
textbox.place(x=410, y=220, height=45,width=220)
textbox.focus()

textbox1 = customtkinter.CTkEntry(login_Form,width=35,font=('Arial', 12),fg_color='#2C3333', text_color='#E7F6F2', bg_color='#2C3333', corner_radius=10, show="*", border_width=1)
textbox1.place(x=410, y=300, height=45,width=220)
textbox.focus()

def about_app():
    de_window = tk.Toplevel(window)
    de_window.config(bg='white')
    de_window.geometry("500x500")
    de_window.title("Guide")
    
    frame = tk.Frame(de_window, bg="white")
    frame.place(x=0, y=150, height=150, width=500) 
    
    label = customtkinter.CTkLabel(de_window, text="If you don't have an Account, You can\n create in the Register/Sign up Tab. ",font=('Ubuntu mono', 20), text_color= 'black')
    label.place(x=10, y=10, height=100, width=480)

    label1 = customtkinter.CTkLabel(de_window, text="Steps for creating an Account.", font=('Ubuntu mono', 17), text_color= 'blue')
    label1.place(x=10, y=125, height=50, width= 280)

    label2 = customtkinter.CTkLabel(de_window, text="1. Create a Account Number.", font=('Ubuntu mono', 13),  text_color= 'black')
    label2.place(x=10, y=190, height=50, width= 220)

    label3 = customtkinter.CTkLabel(de_window, text="2. Enter your Phone Number.", font=('Ubuntu mono', 13),  text_color= 'black')  
    label3.place(x=10, y=250, height=50, width= 220)

    label4 = customtkinter.CTkLabel(de_window, text="3. Enter your Adress.", font=('Ubuntu mono', 13),  text_color= 'black')
    label4.place(x=10, y=310, height=50, width= 175)

    label5 = customtkinter.CTkLabel(de_window, text="4. Create your own Pin.", font=('Ubuntu mono', 13),  text_color= 'black')
    label5.place(x=10, y=370, height=50, width= 185)

    label6 = customtkinter.CTkLabel(de_window, text="5. Press the Regiser Button to successfully create your Account.", font=('Ubuntu mono', 13),  text_color= 'black')
    label6.place(x=10, y=430, height=50, width= 425)
  
help_button = customtkinter.CTkButton(master=login_Form,text=" ",command=about_app, image=add_help_icon,corner_radius=5, bg_color='#2C3333', fg_color='#E7F6F2', hover_color='#A5C9CA')
help_button.place(x=660, y=10, height=30, width=50)

def register():
	register_form = tk.Toplevel(window)
	register_form.config(bg='white')
	register_form.geometry("700x500")
	register_form.title("Register Form")

	label = tk.Label(register_form, text="BANK REGISTER FORM", font=('Arial', 10), bg='white')
	label.pack(padx=10,pady=15)

	accNumber = customtkinter.CTkEntry(register_form,width=35,font=('Arial', 12), fg_color='white',bg_color='white', text_color='black', corner_radius=10,placeholder_text='Account number', border_width=1)
	accNumber.place(x=50, y=70, height=45,width=220)

	phoneNumber = customtkinter.CTkEntry(register_form,width=35,font=('Arial', 12), fg_color='white',bg_color='white', text_color='black', corner_radius=10,placeholder_text='Phone number', border_width=1)
	phoneNumber.place(x=50, y=140, height=45,width=220)

	address = customtkinter.CTkEntry(register_form,width=35,font=('Arial', 12), fg_color='white',bg_color='white', text_color='black', corner_radius=10,placeholder_text='Address', border_width=1)
	address.place(x=50, y=210, height=45,width=220)

	pin4 = customtkinter.CTkEntry(register_form,width=35,font=('Arial', 12), fg_color='white',bg_color='white', text_color='black', corner_radius=10,placeholder_text='Create your Pin', border_width=1)
	pin4.place(x=50, y=280, height=45,width=220)
 
	def register_button():
		if(accNumber.get()=="" or phoneNumber.get()=="" or address.get()=="" or pin4.get()==""):
			messagebox.showinfo('status',"All Fields are Required")
		else:
			con = mysql.connect(host='localhost', database='atm', user='root', password='')
			cursor = con.cursor()
			cursor.execute("INSERT INTO data_table (account, number, address, pin) VALUES ('"+ accNumber.get() +"','"+ phoneNumber.get() \
			+"', '"+ address.get() +"', '"+ pin4.get() +"' )")
			cursor.execute("commit")
			messagebox.showinfo('Status',"Registration successful!")
			con.close()
	btn4 = customtkinter.CTkButton(master=register_form, text="Register", command=register_button, text_color='white',corner_radius=10, bg_color='white', fg_color='dark blue')
	btn4.place(x=300, y=450, height=30, width=130)

register= customtkinter.CTkButton(master=login_Form, text="Register", text_color='#2C3333',corner_radius=5, bg_color='#2C3333', fg_color='#E7F6F2', command=register, image=add_register_icon, compound='left')
register.place(x=410, y=390, height=30, width=130)


#security counter variable
sec_count = 3
#Login function
def login_check():
    
    var_pin = textbox.get()
    var_pin1 = textbox1.get()
    
    pin = "admin"
    pin1 = 12345
	
    global sec_count
	
    if var_pin1.isdigit():
       var_pin1 = int(var_pin1)
		
       if var_pin1 == pin1 and var_pin == pin:
           messagebox.showinfo("Successful", "Login Successful")
           login_Form.destroy()
			#show Menu window after login confirmation
           window.deiconify()
			
       else:
           messagebox.showerror("Error", "Incorrect Password" + "\n   Attempts left: " + str(sec_count - 1))
           textbox.delete(0, tk.END)
           textbox1.delete(0, tk.END)      
           textbox.focus()
           sec_count -= 1
           print(sec_count)
    else:
        messagebox.showerror("Error", "Incorrect Password" + "\n   Attempts left: " + str(sec_count - 1))
        textbox.delete(0, tk.END)
        textbox1.delete(0, tk.END)      
        textbox.focus()
        sec_count -= 1
        print(sec_count)
	
    if sec_count == 0:
        messagebox.showerror("Error", "   Incorrect Password" + "\nTransaction Canceled")
        login_Form.destroy()
  
#Login button 
btn2 = customtkinter.CTkButton(master=login_Form, text="Log in",text_color='#2C3333',corner_radius=5, bg_color='#2C3333', fg_color='#E7F6F2', command=login_check, image=add_login_icon, compound='left')
btn2.place(x=550, y=390, height=30, width=80)


#ATM Visual Menu
#header labels and blank space separator
label = customtkinter.CTkLabel(window, text="ɮǟռӄʏʊȶ", fg_color='#2C3333', text_color='#E7F6F2', bg_color='#2C3333')
label.place(x=10, y=10)

#ATM Initial values and Buttons Menu
initial_balance = 10000

deposit_statement = ""

withdrawal_statement = ""

time_statement = ""

statement_list = []

#Checking balance function on pop up window
def check_balance():
	messagebox.showinfo("Balance", "Amount Available: " + str(initial_balance))
	
balance = customtkinter.CTkButton(master=window,text="BALANCE",text_color='#395B64',corner_radius=10, bg_color='#2C3333',  fg_color="#E7F6F2",command=check_balance,hover_color='#A5C9CA', image=add_balance_icon, compound='left')
balance.place(x=50, y=170, height=50, width=280)

#Deposit balance function on pop up window
def deposit_balance():

	toplevel = tk.Toplevel()
	toplevel.configure(background="white")
	
	label1 = tk.Label(toplevel, text="Deposit Menu", font=("Helvetica", 20), bg="gray1", fg="white")
	label1.pack()
	
	lbl_top_name = tk.Label(toplevel, text="Enter Amount To Deposit: ", bg="light slate gray")
	lbl_top_name.pack()
	
	ent_top_name = tk.Entry(toplevel)
	ent_top_name.pack()
	ent_top_name.focus()
	
	def save_deposit():
		var_save = ent_top_name.get()
		
		global initial_balance
		global deposit_statement
		global statement_list
		
		if var_save.isdigit():
			var_save = int(var_save)
			initial_balance = var_save + initial_balance
			
			#deposit time and date
			time_deposit = time.strftime('%H:%M:%S')
			date_deposit = time.strftime('%Y-%m-%d')

			deposit_statement = "Deposit of " + str(var_save) + " made at " + str(time_deposit) + " on date: " + str(date_deposit)
		
			statement_list.append(deposit_statement)
		
			print(" ")
			print(deposit_statement)
			print(" ")
			print(initial_balance)
			toplevel.destroy()
			
		else:
			messagebox.showinfo("Error", "Invalid Entry")
			ent_top_name.delete(0, tk.END)
			ent_top_name.focus()
			
	btn_save = tk.Button(toplevel, text="Validate", command=save_deposit)
	btn_save.pack()
	
	btn_cancel = tk.Button(toplevel, text="Cancel Transaction", command=toplevel.destroy)
	btn_cancel.pack(fill=tk.X)
	
deposit = customtkinter.CTkButton(master=window,text="DEPOSIT", text_color='#395B64',corner_radius=10, bg_color='#2C3333', fg_color="#E7F6F2", command=deposit_balance, hover_color='#A5C9CA', image=add_deposit_icon, compound='left')
deposit.place(x=360, y=80, height=50, width=280)

#withDraw balance function on pop up window
def draw_balance1():
	toplevel = tk.Toplevel()
	toplevel.resizable(0,0)
	toplevel.configure(background="light slate gray")
	
	label1 = customtkinter.CTkLabel(toplevel, text="Withdrawal Menu", font=("Helvetica", 20))
	label1.pack()
	
	lbl_top_name = tk.Label(toplevel, text="Enter Amount To Withdraw: ", bg="light slate gray")
	lbl_top_name.pack()
	
	ent_top_name = tk.Entry(toplevel)
	ent_top_name.pack()
	ent_top_name.focus()
	
	def save_draw():
		var_draw = ent_top_name.get()
		var_draw = int(var_draw)
		
		global initial_balance
		global withdrawal_statement
		global statement_list
		
		if initial_balance >= var_draw:
			initial_balance = initial_balance - var_draw
			
			#withdrawal time and date
			time_draw = time.strftime('%H:%M:%S')
			date_draw = time.strftime('%Y-%m-%d')

			withdrawal_statement = "Withdrawal of " + str(var_draw) + " made at " + str(time_draw) + " on date: " + str(date_draw)
			
			statement_list.append(withdrawal_statement)
		else:
			messagebox.showinfo("Error", "Insufficient Funds" + "\nMax Balance Allowed: " + str(initial_balance))
			ent_top_name.delete(0, tk.END)
			draw_balance1()
			ent_top_name.focus()
			
		print(initial_balance)
		
		toplevel.destroy()
		
	btn_save = tk.Button(toplevel, text="Validate", command=save_draw)
	btn_save.pack()
	
	lbl_blank = tk.Label(toplevel, text=" ", bg="light slate gray")
	lbl_blank.pack()

	btn_cancel = tk.Button(toplevel, text="Cancel Transaction", command=toplevel.destroy)
	btn_cancel.pack(fill=tk.X)
	
def draw_balance():
	toplevel = tk.Toplevel()
	toplevel.geometry("485x420")
	toplevel.configure(background="#2C3333")
	
	label1 = customtkinter.CTkLabel(toplevel, text="Withdrawal Menu", font=("Helvetica", 20), text_color='#E7F6F2')
	label1.pack()
	
	ent_top_name = tk.Entry(toplevel)
	ent_top_name.focus()
	
	def destroy_window():
		toplevel.destroy()
 
	def amount_button(num):
		current = ent_top_name.get()
		ent_top_name.delete(0, tk.END)
		ent_top_name.insert(0, str(current) + str(num))
		return
 
	def save_draw():
		var_draw = ent_top_name.get()
		var_draw = int(var_draw)
		
		global initial_balance
		global withdrawal_statement
		global statement_list
		
		if initial_balance >= var_draw:
			initial_balance = initial_balance - var_draw
			
			#withdrawal time and date
			time_draw = time.strftime('%H:%M:%S')
			date_draw = time.strftime('%Y-%m-%d')

			withdrawal_statement = "Withdrawal of " + str(var_draw) + " made at " + str(time_draw) + " on date: " + str(date_draw)
			
			statement_list.append(withdrawal_statement)
		else:
			messagebox.showinfo("Error", "Insufficient Funds" + "\nMax Balance Allowed:" + str(initial_balance))
			ent_top_name.delete(0, tk.END)
			draw_balance()
			ent_top_name.focus()
			
		print(initial_balance)
		toplevel.destroy()
 
	btn_500 = customtkinter.CTkButton(master=toplevel, text="500", command=lambda: [amount_button(500), save_draw()])
	btn_500.place(x=30, y=50, height=50, width=205)
	
	btn_1000 = customtkinter.CTkButton(master=toplevel, text="1,000", command=lambda: [amount_button(1000), save_draw()])
	btn_1000.place(x=240, y=50, height=50, width=205)
	
	btn_2000 = customtkinter.CTkButton(master=toplevel, text="2,000", command=lambda: [amount_button(2000), save_draw()])
	btn_2000.place(x=30, y=110, height=50, width=205)
 
	btn_3000 = customtkinter.CTkButton(master=toplevel, text="3,000", command=lambda: [amount_button(3000), save_draw()])
	btn_3000.place(x=240, y=110, height=50, width=205)
	
	btn_5000 = customtkinter.CTkButton(master=toplevel, text="5,000", command=lambda: [amount_button(5000), save_draw()])
	btn_5000.place(x=30, y=170, height=50, width=205)
 
	btn_6000 = customtkinter.CTkButton(master=toplevel, text="6,000", command=lambda: [amount_button(6000), save_draw()])
	btn_6000.place(x=240, y=170, height=50, width=205)
	
	btn_8000 = customtkinter.CTkButton(master=toplevel, text="8,000", command=lambda: [amount_button(8000), save_draw()])
	btn_8000.place(x=30, y=230, height=50, width=205)
 
	btn_10000 = customtkinter.CTkButton(master=toplevel, text="10,000", command=lambda: [amount_button(10000), save_draw()])
	btn_10000.place(x=240, y=230, height=50, width=205)
	
	btn_otherAmount = customtkinter.CTkButton(master=toplevel, text="Enter other amount", command=lambda: [draw_balance1(), destroy_window()])
	btn_otherAmount.place(x=30, y=290, height=50, width=415)

	btn_cancel = customtkinter.CTkButton(master=toplevel, text="Cancel Transaction", command=toplevel.destroy)
	btn_cancel.place(x=30, y=350, height=50, width=415)
 
withdraw = customtkinter.CTkButton(master=window,text="WITHDRAW", text_color='#395B64',corner_radius=10, bg_color='#2C3333',  fg_color="#E7F6F2",command=draw_balance, hover_color='#A5C9CA', image=add_withdraw_icon, compound='left')
withdraw.place(x=50, y=80, height=50, width=280)

#Print statement function on pop up window
def statement():
	
	global statement_list
	global time_statement
	global initial_balance
	
	time1 = time.strftime('%H:%M:%S')
	date1 = time.strftime('%Y-%m-%d')
	
	time_statement = "Statement printed at " + str(time1) + " on date: " + str(date1)
	blank_space = " "
	account_balance = "Account Balance: " + str(initial_balance)
	
	statement_list.append(blank_space)
	statement_list.append(account_balance)
	statement_list.append(blank_space)
	statement_list.append(time_statement)
	statement_list.append(blank_space)

	toplevel = tk.Toplevel()
	toplevel.wm_geometry("700x500")
	toplevel.configure(background="beige")
	
	label1 = tk.Label(toplevel, text="Statement Menu", font=("Helvetica", 20), bg="gray1", fg="white")
	label1.pack(fill=tk.X)
	
	lbl_top_name = tk.Label(toplevel, text="Statement Summary: ")
	lbl_top_name.pack(side=tk.TOP)
	
	Scrolls = tk.Scrollbar(toplevel)
	Scrolls.pack(side=tk.RIGHT,fill=tk.Y)

	listboxPrintStatement = tk.Listbox(toplevel, height=12, yscrollcommand=Scrolls.set)
	listboxPrintStatement.pack(fill=tk.X)

	for item in statement_list:
		listboxPrintStatement.insert(tk.END, item)

	Scrolls.configure(command=listboxPrintStatement.yview)
	
	btn_close = tk.Button(toplevel, text="Close Statement", command=toplevel.destroy)
	btn_close.pack()
	
transcipt = customtkinter.CTkButton(master=window,text="TRANSACTION RECEIPT", text_color='#395B64',corner_radius=10, bg_color='#2C3333',  fg_color="#E7F6F2",command=statement, hover_color='#A5C9CA', image=add_receipt_icon, compound='left')
transcipt.place(x=360, y=170, height=50, width=280)

def log_out():     
        if messagebox.askyesno(title="Log out", message="Are you sure you want to exit?"):
            window.destroy()      

exit_button = customtkinter.CTkButton(master=window,text="Card Remove", text_color='#395B64',corner_radius=10, bg_color='#2C3333',fg_color='#E7F6F2', command=log_out, image=add_exit_icon, hover_color='#A5C9CA')
exit_button.place(x=550, y=10, height=30, width=130)

window.mainloop()