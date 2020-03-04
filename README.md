# Pyssword - a password safe

It is convenient to have your passwords stored in a single file for easy access.
It is not so convenient to have them easily readable for other people.  
I created this simple Python password safe for my own personal use, so that you only need to remember one password (which I'll call key) from now on.  
It stores your encrypted passwords using a simple encryption algorithm that I made up, and let's you fetch the exact password you are looking for by writing the name of corresponding the website/service. 

For example, if your password for your LinkedIn account is 'Ihatepasswords92', you can store it under the name 'LinkedIn', and retrieve it by feeding the program with your key and the string 'LinkedIn'.

*Note*: your key will not me recorded anywhere, so make sure you remember it. Also, you could have more than one key for different passwords, but that would defeat the purpose of this program.

*Disclaimer*: Use this program at your own risk!

### Pre-requisites and instructions:
You need to have a file named `storage.txt` in the same folder as the script `Pyssword.py`, which is created by exporting the Pyssword.ipynb notebook as a script.  
Furthermore, the first time you run the script the `storage.txt` must contain the string "{}".   
This is already done for you if you just download the folder "Pyssword".

To use Pyssword, simply execute the Python script as usual writing `Python3 Pyssword.py` in the terminal, when in the correct folder.

# The encryption

The encryption is simple and is certainly not good enough for very sensitive information, but probably enough to store some passwords in your personal hard disk.

To encrypt a password, one first takes the unicode of the first character of the password (say "Ihatepasswords92"), adds the unicode of the first character of the key (say simply "key") and squares the result, and finally recovers the character corresponding to that unicode. This encrypts the first letter of the password. We keep doing this until we have encrypted the entire password, cycling through the key if necessary (*i.e.* if the password is longer than the key).

Here is the scheme of the encryption for the second letter of the passort "Ihatepasswords92" with the key "hey":

The decryption simply undoes this.

# UI

The UI is minimalistic. 
The program runs in the terminal, and we can choose wether we want to save, find or delete passwords by writing characters.


