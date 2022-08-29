#!/usr/bin/env python3

import os
#import win32.client as win32

#ask info
ae_name = input("Whats is AE's name?  ")
ae_phone = input("Whats is AE's phone?  ")
ae_email = input("Whats is AE's email?  ")
ae_title = input("Whats is AE's title?  ")

#change working directory
os.chdir("C:\\Users\\Signatures")

#insert info into signature
signature = """
  <  HTML CODE
  >"""


with open(ae_name+" Signature.html", "w") as file:
    file.write(signature)
    
