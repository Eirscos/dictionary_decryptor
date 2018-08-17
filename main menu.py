
import tkinter
from tkinter import messagebox
usernames=["bob","john"]
passwords=["123","password"]



def login():
    def checkpw():
        username = entry_username.get()
        password = entry_password.get()
        if username in usernames:
            user=usernames.index(username)
            if passwords[user]==password:
                print("correct")
            else:
                entry_password.delete(0,"end")
                messagebox.showerror("Error", "the username or password is incorrect")
        else:
            entry_password.delete(0,"end")
            messagebox.showerror("Error", "the username or password is incorrect")
            

    def back():
        login.destroy()
        menu()
    login = tkinter.Tk()
    login.title("menu")
    login.config(bg="white")
    login.geometry("300x200")
    label_username = tkinter.Label(login, bg="white", text="Username",font=("TkDefaultFont",20))
    label_password = tkinter.Label(login, bg="white", text="Password",font=("TkDefaultFont",20))

    entry_username = tkinter.Entry(login, width=10, bg="white",font=("TkTextFont",20))
    entry_password = tkinter.Entry(login, width=10, bg="white", show="*",font=("TkTextFont",20))

    label_username.grid(row=0, sticky="E")
    label_password.grid(row=1, sticky="E")
    entry_username.grid(row=0, column=1)
    entry_password.grid(row=1, column=1)


    logbtn = tkinter.Button(login, bg="white", text="Login", command=checkpw,width=10,font=("TkDefaultFont",20))
    logbtn.grid(columnspan=2)
    backbtn = tkinter.Button(login, bg="white", text="Back", command=back,width=10,font=("TkDefaultFont",20))
    backbtn.grid(columnspan=2)

    

def menu():
    def run_play():
        menu.destroy()
        login()
    menu = tkinter.Tk()
    menu.title("menu")
    menu.config(bg="white")
    menu.geometry("300x165")
    welcome = tkinter.Label(menu, text="please login to continue",bg="white",font=("TkDefaultFont",20))
    welcome.pack()
    play_button = tkinter.Button(menu, text="login", command=run_play, bg="white",font=("TkDefaultFont",20))
    play_button.pack()

    quit_button = tkinter.Button(menu, text="quit",command=menu.destroy,bg="white",font=("TkDefaultFont",20))
    quit_button.pack()
    menu.mainloop()
        
menu()
