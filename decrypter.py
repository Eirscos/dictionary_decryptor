
import tkinter
def play():
    def closegame():
        login.destroy()
        menu()
    login = tkinter.Tk()
    login.title("guess the number")
    login.geometry("300x450")
    login.config(bg="white")
    welcome = tkinter.Label(login, text="login",bg="white")
    welcome.pack()
    usernametxt = tkinter.Label(login, text="username",bg="white")
    usernametxt.pack()
    username = tkinter.Entry(login)
    username.pack()
    passwordtxt = tkinter.Label(login, text="password",bg="white")
    passwordtxt.pack(side="left")
    password = tkinter.Entry(login,show="*")
    password.pack(side="right")
    back = tkinter.Button(login, text="back",command=closegame,bg="white")
    back.pack()
    login.mainloop()


def menu():
    def run_play():
        menu.destroy()
        play()
    menu = tkinter.Tk()
    menu.title("menu")
    menu.config(bg="white")
    menu.geometry("300x450")
    welcome = tkinter.Label(menu, text="please login to continue",bg="white")
    welcome.pack()
    play_button = tkinter.Button(menu, text="login", command=run_play, bg="white")
    play_button.pack()

    quit_button = tkinter.Button(menu, text="quit",command=menu.destroy,bg="white")
    quit_button.pack()
    menu.mainloop()
        
menu()
