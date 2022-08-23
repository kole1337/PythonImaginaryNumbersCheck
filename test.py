c = 0
import math
c = 2.0000000001 + -2j

if c.real < 2:
    c = c + 0.1
    print("c.real != 2:")
         
            
if math.trunc(c.real) == 2:
    print("c.real == 2")
            
    if c.imag == -2:
        print("c.imag == -2:")
    elif c.imag > -2:
        c = c - 4 - 0.1j
        print("c.imag != -2:")