#!/usr/bin/python

"""
Caesar Cipher's by Kyle Bilak kbilak@email.uscb.edu
April 18 2019 
"""
unencrypted_message = raw_input("Enter your message to encrypt: ")
 
encrypted_message = ""
for i in unencrypted_message:
    x = ord(i) # take letters unicode value 
    x = x + 1  # add one to that value
    x2 = chr(x) # convert int number back to letter
    encrypted_message = encrypted_message + x2
print("Encrypted message: " + encrypted_message ) # output the encrypted user input
