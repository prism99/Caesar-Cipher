#!/usr/bin/python

"""
Caesar Cipher's by Kyle Bilak kbilak@email.uscb.edu
April 18 2019 
"""
encrypted_text = raw_input("Enter your message to decrypt: ")
 
unencrypted_message = ""
for i in encrypted_text:
    x = ord(i) # take letters unicode value 
    x = x - 1  # subtract one to that value
    x2 = chr(x) # convert int number back to letter
    unencrypted_message = unencrypted_message + x2
print("Decrypted message: " + unencrypted_message ) # output the encrypted user input
