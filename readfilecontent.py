#!/usr/bin/env python

#THIS IS A COMMENT

print "FILE READ"
print "--------------------------------------------------------"

with open('data.txt', 'r') as myfile:
#MANIPULATE AND REMOVE NEW LINE
    data=myfile.read().replace('\n', ' ')

print "Data output: ", data
print "---------------------------------------------------------"
