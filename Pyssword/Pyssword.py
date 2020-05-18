#!/usr/bin/env python
# coding: utf-8

'''Pyssword - a password safe
 
 It is convenient to have your passwords stored in a single file for easy access.
 It is not so convenient to have them easily accessible for people other than you who may use your computer.  
 I created this simple Python password safe for my own personal use, so that you only need to remember one password (which I'll call key) from now on: the key to your Pyssword safe.
 It stores your encrypted passwords using a simple encryption algorithm that I made up, and let's you fetch the exact password you are looking for by writing the name of corresponding the website/service.  
 For example, if your password for your LinkedIn account is 'Ihatepasswords92', you can store it under the name 'LinkedIn', and retrieve it by feeding the program with your key and the string 'LinkedIn'.
 
 *Note*: your key will not me recorded anywhere, so make sure you remember it. Also, you could have more than one key for different passwords, but that would defeat the purpose of this program.
 
 ### Pre-requisites and instructions:
 You need to have a file named `storage.txt` in the same folder as the script `Pyssword.py`, which is created by exporting this notebook as a script.  
 Furthermore, the first time you run the script the `storage.txt` must contain the string "{}". 
'''

from math import sqrt
from getpass import getpass as input_no_echo #This enables inputs without showing what we are writing.
import json


## Encryption and decryption

def decrypt(encrypted, key):
    '''
    Decrypts encrypted using key, retrieving the original password encrypted with encrypt(password, key).
    Returns string with decrypted password.
    '''
    decrypted = ''
    for i in range(len(encrypted)): #We must undo what the encryption function does.
        char = encrypted[i]
        sqrt_unicode = int(sqrt(ord(char))) #Encryption squared the unicode, so we find its square root.
        char_decrypted = chr( sqrt_unicode - ord(key[i%len(key)]) ) #Subtracts what the encryption added.
        decrypted += char_decrypted #Update the encrypted string
    return decrypted


def encrypt(password, key):
    '''
    Encrypts password using key.
    Method: for each character in password, adds its unicode to the unicode (mod len(key)) of the character in the same position in key, and then squares the result.
    Returns string with encryption.
    '''
    encrypted = ''
    for i in range(len(password)):
        char = password[i]
        addition_unicode = ord(char) + ord(key[i%len(key)]) #The modulo operation makes it so that i cycles through key: it's OK to have len(key)<len(password). 
        char_encrypted = chr( addition_unicode**2 )
        encrypted += char_encrypted #Update the encrypted string
    return encrypted


## UI and processing inputs


def initialize_safe():
    global key
    key = input_no_echo('What is the key for your safe? (If this is your first time using Pyssword, write your new key (password for the safe) now, and stick with it in the future)')

def choose_mode():
    global mode
    print('Choose mode: \n s to save a new password. \n f to find password. \n l to list all passwords.\n d to delete a password.')
    mode = input()


def process():
    print('\n')
    if mode=='s': #Save a password.
        #Load password dictionary from JSON file.
        with open('storage.txt') as storage: #storage.txt must be JSON file. 
        #Just create a text file with the string '{}' in it if it's the first time using the safe.
            pass_dict = json.load(storage)  #Fills dictionary with the JSON data.
        #User inputs:
        password = input_no_echo('What password do you want to save?')
        service = input('What service/website is this password for?').lower() #All lower case.
        service = service.replace(' ','') #Remove spaces.
        #Encrypt password
        encrypted = encrypt(password, key)
        #Add new password to dictionary:
        pass_dict.update({service : encrypted})
        #Update JSON file:
        with open('storage.txt', 'w') as storage: #storage.txt must be JSON file. 
            json.dump(pass_dict, storage)

    elif mode=='f': #Find a password.
        #Load password dictionary from JSON file.
        with open('storage.txt') as storage: #storage.txt must be JSON file. 
        #Just create a text file with the string '{}' in it if it's the first time using the safe.
            pass_dict = json.load(storage)  #Fills dictionary with the JSON data.
        #User inputs:
        service = input('What service/website is the password for?').lower() #All lower case.
        service = service.replace(' ','') #Remove spaces.
        #Find and decrypt password.
        if service in pass_dict.keys():
            password = decrypt(pass_dict[service], key) #Decrypt encrypted password.
            print(password)
        else:
            print('Service not found.')

    elif mode=='l': #List all passwords.
        #Load password dictionary from JSON file.
        with open('storage.txt') as storage: #storage.txt must be JSON file. 
            pass_dict = json.load(storage)  #Fills dictionary with the JSON data.
        #Decrypt and print passwords (alphabetically on the services).
        passwords = []
        for service, encrypted in pass_dict.items():
            passwords.append((service, decrypt(encrypted, key)))
        sorted_pass = sorted(passwords, key = lambda tup: tup[0]) #Sorts alphabetically according to service.
        for service, password in sorted_pass:
            print('{}: {}'.format(service, password))

    elif mode=='d': #Delete a password.
        #Load password dictionary from JSON file.
        with open('storage.txt') as storage: #storage.txt must be JSON file. 
            pass_dict = json.load(storage)  #Fills dictionary with the JSON data.
        #User inputs:
        service = input('What service/website is the password that you want to delete for?').lower() #All lower case.
        service = service.replace(' ','') #Remove spaces.
        #Delete dictionary entry.
        if service in pass_dict.keys():
            del pass_dict[service]
        else:
            print('Service not found.')
        #Update JSON file:
        with open('storage.txt', 'w') as storage: #storage.txt must be JSON file. 
            json.dump(pass_dict, storage)

    else:
        print('Not a valid mode.')
    
    print('\n ======================================\n     Back to mode choosing    \n ======================================\n')


# ## The execution loop

initialize_safe()
while True:
    choose_mode()
    process()

