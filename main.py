# in the name of GOD

"""
 This project is developed to help you safely store your passwords in your local PC.
 You have an unic Key, which is not saved anywhere in your local PC, and all your passwords will be saved in such a
 manner that you will need your key to access them. (Read 'Key' section in README.md for more details) so you don't need to worry about physical access to your PC.
 Your password contains your key + your own master password. these two will be stored using hash, even if someone gets
 access to your passwords database, he won't be able to convert the passwords to the real ones without having your main
 key.

 It has a graphical user interface, so you can easily work with your password manager.

 GitHub Repo: https://github.com/hayatisaeed/LockBoxCipher
"""

from tkinter import *


def onclick():
    pass


main_window = Tk()
main_window.title("LockBoxCipher v1.0")
main_window.geometry("500x500")

password_label = Label(main_window, text="Please Enter Your Master Key + password (no space between)")
password_entry = Entry(main_window)

password_label.pack()
password_entry.pack()
