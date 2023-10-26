#!/usr/bin/env python3
from binascii import hexlify
from binascii import unhexlify
from password import Password

crypted="PASSWORD"
password=Password.decrypt(crypted)
password=Password.decrypt(unhexlify(crypted))
print (password)
