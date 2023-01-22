import time
import tkinter as tk
import customtkinter
from tkinter import messagebox, Frame
from tkinter import StringVar
from PIL import ImageTk, Image   # PIL module for images

#atm menu instantiation
window = tk.Tk()
#hide menu window until login confirmed
window.withdraw()
#window title
window.title('ɮǟռӄʏʊȶ Virtual ATM')
#window size
window.geometry("700x500")
#code to disable maximize
window.resizable(0,0)
#window background color
window.configure(background="white")

#####################################################################
#Login Form
#toplevel window for Login
login_Form = tk.Toplevel()
login_Form.wm_geometry("700x500")
login_Form.resizable(0,0)
login_Form.configure(background="light slate gray")

frame = tk.Frame(login_Form, background='white')
frame.place(x=0, y=0, height=700, width=2500)

frame = tk.Frame(login_Form)
frame.place(x=0, y=0, height=500, width=350) 

image=Image.open('ATM(Group)/img/istockphoto-1183227867-612x612.jpg')
img=image.resize((400, 500), Image.ANTIALIAS)
my_img=ImageTk.PhotoImage(img)

add_help_icon = customtkinter.CTkImage(Image.open('ATM(Group)/img/info-circle-regular-24.png').resize((20,20), Image.ANTIALIAS))
add_exit_icon = customtkinter.CTkImage(Image.open('ATM(Group)/img/exit-regular-24.png').resize((20,20), Image.ANTIALIAS))

label = tk.Label(frame, image = my_img, bg="navy")
label.pack()

label = customtkinter.CTkLabel(login_Form, text="ɮǟռӄʏʊȶ", text_color='black', bg_color='white', font=('Arial', 40))
label.place(x=450, y=50)
label = customtkinter.CTkLabel(login_Form, text="Hey there! just a reminder, love is like a ATM MACHINE. \n Only WITHDRAWAL makes it empty DEPOSIT \n by showing that you care today.", text_color='grey', bg_color='white', font=('Arial', 10))
label.place(x=400, y=120)

name_user = customtkinter.CTkLabel(login_Form,text="Account Name", font=('Arial', 12),bg_color='white', text_color='grey').place(x=430, y=187)

pin = customtkinter.CTkLabel(login_Form,text="Enter Your Pin", font=('Arial', 12),bg_color='white', text_color='grey').place(x=430, y=270)

textbox = customtkinter.CTkEntry(login_Form,width=35,font=('Arial', 12), fg_color='white',bg_color='white', text_color='black', corner_radius=10, border_width=1)
textbox.place(x=410, y=220, height=45,width=220)
textbox.focus()

textbox1 = customtkinter.CTkEntry(login_Form,width=35,font=('Arial', 12),fg_color='white', text_color='black', bg_color='white', corner_radius=10, show="*", border_width=1)
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
  
help_button = customtkinter.CTkButton(master=login_Form,text=" ",command=about_app, image=add_help_icon,text_color='dark blue',corner_radius=10, bg_color='white', fg_color='white', hover_color='#2375c2')
help_button.place(x=650, y=10, height=30, width=50)

def register_button():
        messagebox.showinfo("Your acount has been created")

def register():
    register_form = tk.Toplevel(window)
    register_form.config(bg='white')
    register_form.geometry("700x500")
    register_form.title("Register Form")

    label = tk.Label(register_form, text="BANK REGISTER FORM", font=('Arial', 10), bg='white')
    label.pack(padx=10,pady=15)
    
    textbox = customtkinter.CTkEntry(register_form,width=35,font=('Arial', 12), fg_color='white',bg_color='white', text_color='black', corner_radius=10,placeholder_text='Account number', border_width=1)
    textbox.place(x=50, y=70, height=45,width=220)
    
    textbox = customtkinter.CTkEntry(register_form,width=35,font=('Arial', 12), fg_color='white',bg_color='white', text_color='black', corner_radius=10,placeholder_text='Phone number', border_width=1)
    textbox.place(x=50, y=140, height=45,width=220)
    
    textbox = customtkinter.CTkEntry(register_form,width=35,font=('Arial', 12), fg_color='white',bg_color='white', text_color='black', corner_radius=10,placeholder_text='Address', border_width=1)
    textbox.place(x=50, y=210, height=45,width=220)
    
    textbox = customtkinter.CTkEntry(register_form,width=35,font=('Arial', 12), fg_color='white',bg_color='white', text_color='black', corner_radius=10,placeholder_text='Create your Pin', border_width=1)
    textbox.place(x=50, y=280, height=45,width=220)
    
    btn4 = customtkinter.CTkButton(master=register_form, text="Register", command=register_button, text_color='white',corner_radius=10, bg_color='white', fg_color='dark blue')
    btn4.place(x=300, y=450, height=30, width=130)


register_button = customtkinter.CTkButton(master=login_Form, text="Register / Sign up", text_color='white',corner_radius=10, bg_color='white', fg_color='dark blue', command=register)
register_button.place(x=410, y=370, height=30, width=130)

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
           textbox.focus()
           sec_count -= 1
           print(sec_count)
    else:
        messagebox.showerror("Error", "Incorrect Password" + "\n   Attempts left: " + str(sec_count - 1))
        textbox.delete(0, tk.END)
        textbox.focus()
        sec_count -= 1
        print(sec_count)
	
    if sec_count == 0:
        messagebox.showerror("Error", "   Incorrect Password" + "\nTransaction Canceled")
        login_Form.destroy()
        window.deiconify()
  
#Login button 
btn2 = customtkinter.CTkButton(master=login_Form, text="Log in",text_color='white',corner_radius=10, bg_color='white', fg_color='dark blue', command=login_check)
btn2.place(x=560, y=370, height=30, width=70)

menubar = tk.Menu(window)
myMenu = tk.Menu(menubar, tearoff=0)

#display the menu bar
window.config(menu=menubar)

#ATM Visual Menu

#header labels and blank space separator
label = customtkinter.CTkLabel(window, text="ɮǟռӄʏʊȶ", fg_color='white', text_color='black')
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
	
balance = customtkinter.CTkButton(master=window,text="BALANCE",text_color='white',corner_radius=10, bg_color='white', fg_color='navy blue', command=check_balance)
balance.place(x=200, y=140, height=100, width=150)

#Deposit balance function on pop up window
def deposit_balance():

	toplevel = tk.Toplevel()
	toplevel.resizable(0,0)
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
	
	lbl_blank = tk.Label(toplevel, text=" ", bg="light slate gray")
	lbl_blank.pack()
	
	btn_cancel = tk.Button(toplevel, text="Cancel Transaction", command=toplevel.destroy)
	btn_cancel.pack(fill=tk.X)
	
deposit = customtkinter.CTkButton(master=window,text="DEPOSIT", text_color='white',corner_radius=10, bg_color='white', fg_color='navy blue', command=deposit_balance)
deposit.place(x=360, y=30, height=100, width=150)


#withDraw balance function on pop up window
def draw_balance():
	toplevel = tk.Toplevel()
	toplevel.resizable(0,0)
	toplevel.configure(background="light slate gray")
	#toplevel.wm_iconbitmap('lelu.ico')
	
	label1 = tk.Label(toplevel, text="Withdrawal Menu", font=("Helvetica", 20), bg="gray1", fg="white")
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
			messagebox.showinfo("Error", "Insufficient Funds" + "\nMax Balance Allowed: R" + str(initial_balance))
			ent_top_name.delete(0, tk.END)
			draw_balance()
			ent_top_name.focus()
			
		print(initial_balance)
		
		toplevel.destroy()
		
	btn_save = tk.Button(toplevel, text="Validate", command=save_draw)
	btn_save.pack()
	
	lbl_blank = tk.Label(toplevel, text=" ", bg="light slate gray")
	lbl_blank.pack()

	btn_cancel = tk.Button(toplevel, text="Cancel Transaction", command=toplevel.destroy)
	btn_cancel.pack(fill=tk.X)
	
withdraw = customtkinter.CTkButton(master=window,text="WITHDRAW", text_color='white',corner_radius=10, bg_color='white', fg_color='navy blue', command=draw_balance)
withdraw.place(x=200, y=30, height=100, width=150)

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
	
transcipt = customtkinter.CTkButton(master=window,text="TRANSACTION\n RECEIPT", text_color='white',corner_radius=10, bg_color='white', fg_color='navy blue', command=statement)
transcipt.place(x=360, y=140, height=100, width=150)

def log_out():     
        if messagebox.askyesno(title="Log out", message="Are you sure you want to exit?"):
            window.destroy()      

log_out = customtkinter.CTkButton(master=window,text="Exit", text_color='dark blue',corner_radius=10, bg_color='white', fg_color='white', command=log_out, image=add_exit_icon)
log_out.place(x=610, y=10, height=30, width=80)

window.mainloop()