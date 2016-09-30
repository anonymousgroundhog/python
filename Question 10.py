from math import pow
from fractions import gcd

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m


def Question11 (a,b):
    
    if gcd(a,b) == 1:
       print "Worked" #NEED TO DETERMINE HOW TO FIND X AND Y VALUES-----------------------CHECK INTO CODE
    else:
        print "No solution possible because gcd != 1"
    return 