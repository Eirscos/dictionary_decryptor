import tkinter

def menu():
    menu = tkinter.Tk()
    menu.title("menu")
    menu.config(bg="white")
    play_button = tkinter.Button(menu, text="decrypt",bg="white")
    play_button.pack()
    instruction_button = tkinter.Button(menu, text="help",bg="white")
    instruction_button.pack()
    quit_button = tkinter.Button(menu, text="quit",command=menu.destroy,bg="white")
    quit_button.pack()
    menu.mainloop()






menu()
