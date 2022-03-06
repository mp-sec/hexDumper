#!usr/bin/python3

import os
import sys
import binascii
from subprocess import call

userPath = input("Enter the absolute path to the file that is to be hex dumped: ")

if userPath == "": 
	print("No path was entered")
	sys.exit()

print(call(["hexdump", "-C", userPath]))

fileSize = os.path.getsize(userPath)
hexSize = hex(fileSize)
modifiedFS = str(fileSize) + " bytes"
print("Total length: ", modifiedFS, " (", hexSize, ")", sep="")

userInput = input("View raw hex dump? [Y/N]: ")

if userInput == "Y" or userInput == "y":
	with open(userPath, 'rb') as hexContent:
		hexDump = hexContent.read()
	print(binascii.hexlify(hexDump))
elif userInput == "N" or userInput == "n":
	print("Exiting program.")
else:
	print("Unacceptable entry made.\nProgram exiting.")
