# LockBoxCipher
 This project is developed to help you safely store your passwords in your local PC.
 You have an unic Key, which is not saved anywhere in your local PC, and all your passwords will be saved in such a
 manner that you will need your key to access them (Read 'Key' section for more details). so you don't need to worry 
 about physical access to your PC.
 Your password contains your key + your own master password. these two will be stored using hash, even if someone gets
 access to your passwords database, he won't be able to convert the passwords to the real ones without having your main
 key.  It has a graphical user interface, so you can easily work with your password manager.


## Key
As mentioned, you will have an unic key (containing 20 digits) which you can use to safely store and browse your 
passwords. You have to first create your password and your key from create section in main window. Afterward, hash of it will be saved in 
```data/main_password.json```.

### How to be sure about safety?
The key itself is used to encode and decode the passwords, and it will not be saved anywhere. And No one will be able to
decode your password without that code. Even if someone changes the hash in ```data/main_password.json``` and create his
own key and password and key, your password will not be shown to them correctly.

### Important!
If you forget or lose your key, you won't be able to restore your passwords!

