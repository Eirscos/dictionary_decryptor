import tkinter

def menu():
    menu = tkinter.Tk()
    menu.title("menu")
    menu.config(bg="white")
    welcome_msg = tkinter.Label(menu, text='welcome to the ultimate decrypter',bg="white")
    welcome_msg.pack()
    play_button = tkinter.Button(menu, text="decrypt",bg="white")
    play_button.pack()
    quit_button = tkinter.Button(menu, text="quit",command=menu.destroy,bg="white")
    quit_button.pack()
    menu.mainloop()






menu()
