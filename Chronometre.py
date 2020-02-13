from tkinter import *
import tkinter


class Chrono(tkinter.Label):

    def __init__(self, form):
        tkinter.Label.__init__(self, form, text='Starting')
        self.label = Label(self, text="", width=10)
        self.label.pack()
        self.remaining = 0
        self.countdown(1800)

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="time's up!")
        else:
            self.label.configure(text="{:d} s".format(self.remaining))
            self.label.config(fg="gold", bg="gray17")
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)


class Form:
    def __init__(self, master):
        self.master = master
        self.label_time = Label(self.master, text='TIME REMAINING', fg="gold", bg="gray17", font=('bahnschrift', 12,))
        self.label_time = Chrono(self.master)
        self.label_time.pack()


root = Tk()
main = Form(root)
root.mainloop()