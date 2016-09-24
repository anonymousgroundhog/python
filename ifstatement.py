#!/usr/bin/env python

#GET USER INPUT
var = raw_input("ENTER IN NAME: ")

#NEW VARIABLE WILL REPLACE WHITESPACES
newvar = var.replace(" ", "")

#EVALUATE INPUT
if(var == "Sean"):
	print "Sean is great"
elif (var == "Bob"):
	print "Bob, you are OK"
else:
	print "YOU STINK"

print "OUTPUT: ", newvar
