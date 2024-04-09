from tkinter import *
from rich.console import Console
import sys
from tkinter import Tk, Button, Frame
import re
from tkinter import *
from time import sleep
from bitcoin import *
import subprocess
import threading
import tkinter as tk
from bitcoinaddress import Wallet

#3HnpWD48knNGdRD4n6xFE3c4dJrUhYgj7A

window = Tk()
window.title("Private key Checker")
window.geometry("900x600")
window.iconbitmap('logo.ico')
window.configure(bg='black')
window.resizable(0, 0)

#Btc WAllet Checker--------------------------------------------------------------------------------------------------------
def button_function():
    hash160 = hashkey1.get()
    print (hash160)
    
def main():
    hwal = Entry2.get()
    print(hwal)
    
    
def btc1():
    print("")
    print("Final Attack")
    print("---------------------------------------------------------")
    hash160 = hashkey1.get()
    hwal = Entry2.get()
    btc_amnt = btck.get()
    print(hash160)
    print(hwal)
    print(btc_amnt)


#btcsentdefine
#def flashc():
    #hkey = hashkey1.get()
    #hwal = Entry2.get()
    #btc_amnt = btck.get()
    
def Take_input():
    hash160 = hashkey1.get()
    Output.insert(END, hash160 + "\n")
    hwal = Entry2.get()
    Output.insert(END, hwal + "\n")
    btc_amnt = btck.get()
    Output.insert(END, btc_amnt + "\n")
  
def new_oputput():
    hash160 = hashkey1.get()
    wallet = Wallet(hash160)
    Output.delete("1.0","end")
    Output.insert(END, str(Wallet(hash160)) + "\n")
    
        
#windowcode--------------------------------------------------------------------------------------------------------
abc = PhotoImage(file='logo1.png')
label17 = Label(window, image=abc,bg = "black")
label17.grid(row = 0, column = 0, sticky = E)

l = Label(window, text = "DEVELOPED BY LUCIFER",bg = "black",foreground="white")
l.config(font =("Courier", 14))
l.grid(row = 0, column = 1, sticky = E)

button4 = Button(window, text = "Cancel",bg = "black",foreground="white", command = window.destroy)
button4.grid(row = 0, column = 5)

hash_key = Label(window, text = "Enter Private Key",bg = "black",foreground="white")
hash_key.config(font =("Courier", 14))
hash_key.grid(row = 2, column = 1, sticky = E)

hashkey1 = Entry(window, width=60)
hashkey1.grid(row = 2, column = 2, pady = 1,padx = 5)

#button1 = Button(window, text = " Set ",bg = "black",foreground="white", command=button_function)
#button1.grid(row = 3, column = 4)


#Wallet_address = Label(window, text = "Wallet Address",bg = "black",foreground="white")
#Wallet_address.config(font =("Courier", 14))
#Wallet_address.grid(row = 4, column = 1, sticky = E)

#Entry2 = Entry(window)
#Entry2.grid(row = 4, column = 2, pady = 4)


#button2 = Button(window, text = "Check",bg = "black",foreground="white", command=main)
#button2.grid(row = 4, column = 3)

#Value1 = Label(window, text = "Btc Amount",bg = "black",foreground="white")
#Value1.config(font =("Courier", 14))
#Value1.grid(row = 7, column = 2)

#btck = Entry(window)
#btck.insert(END, '1.00')
#btck.grid(row = 8, column = 2, pady = 2)

button3 = Button(window, text = "Send Now",bg = "black",foreground="white", command=new_oputput)
button3.grid(row = 2, column = 5)

Output = Text(window, height = 20, 
              width = 60, 
              bg = "black",foreground="white")
Output.grid(row = 9, column = 2,pady = 10)

#console cmd--------------------------------------------------------------------------------------------------------

#new code here--------------------------------------------------------------------------------------------------------



window.mainloop()
