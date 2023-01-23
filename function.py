
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

def about_app(window):
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
  
#help_button = customtkinter.CTkButton(master=login_Form,text=" ",command=about_app, image=add_help_icon,text_color='dark blue',corner_radius=10, bg_color='white', fg_color='white', hover_color='#2375c2')
#help_button.place(x=650, y=10, height=30, width=50)
