import math
from array import *

x = 0

c = -2 + 2j

y = pow(x,3) + 2*c

print("<=================>")
b = 0
f = open("coordinates.txt", "w")
num=0
while c.real <= 2 and c.imag >= -2:

        print(c)

        for it in range(1,100):

            if it%10==0:
                num = it/10
                i = open("iter"+str(num),"a")
                i.write(f'{"{:.3f}".format(c.real)}:{"{:.3f}".format(c.imag)}\n') 
                i.close()
                
            y = pow(x,2) + c
            x = y
            
            if math.sqrt((pow(int(y.real),2)) + pow(int(y.imag),2))  >= 2:
                break

        if math.sqrt(pow( int(y.real),2 ) + pow( int(y.imag),2 )) < 2:
            f.write(f'{"{:.3f}".format(c.real)}:{"{:.3f}".format(c.imag)}\n') 

        x = 0
        y = 0

        if math.trunc(c.real) < 2:
            c = c + 0.002

        if math.trunc(c.real) == 2:

            if math.trunc(c.imag) == -2:
                break

            elif c.imag > -2:
                c = c - 4 - 0.002j

        b = b + 1
        print(f'b:{b} ==========')