from tkinter import *
import os

window = Tk()
window.title("Shutdown App")
window.geometry("400x580")
window.resizable(False, False)


def restarttime():
    os.system("shutdown /r /t 30")


def restart():
    os.system("shutdown /r /t 1")


def shutdown():
    os.system("shutdown /s /t 1")


def logout():
    os.system("shutdown -l")


# icon
image_icon = PhotoImage(file="shutdown.png")
window.iconphoto(False, image_icon)

# first button
restart_time_button = PhotoImage(file="reset.png")
first_button = Button(window, image=restart_time_button, borderwidth=0, cursor="hand2", command=restarttime)
first_button.place(x=10, y=10)

# second button
close_button = PhotoImage(file="cancel.png")
second_button = Button(window, image=close_button, borderwidth=0, cursor="hand2", command=window.destroy)
second_button.place(x=200, y=10)

# third button
restart_button = PhotoImage(file="reload.png")
third_button = Button(window, image=restart_button, borderwidth=0, cursor="hand2", command=restart)
third_button.place(x=10, y=200)

# fourth button
shutdown_button = PhotoImage(file="shutdown.png")
fourth_button = Button(window, image=shutdown_button, borderwidth=0, cursor="hand2", command=shutdown)
fourth_button.place(x=200, y=200)

# fifth button
logout_button = PhotoImage(file="logout.png")
fifth_button = Button(window, image=logout_button, borderwidth=0, cursor="hand2", command=logout)
fifth_button.place(x=100, y=400)


window.mainloop()
