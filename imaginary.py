import math
from array import *

x = 0

c = -2 + 2j

y = pow(x,2) + c
listCoord = [[]]

# resolution = input('Enter a resolution: ')
# itterations = input('Enter itterations: ')

print("<=================>")
b = 0
f = open("coordinates.txt", "w")

while c.real <= 2 and c.imag >= -2:
    
        print(c)
        
        for it in range(20):
            
            y = pow(x,2) + c
            x = y
            if math.sqrt((pow(int(y.real),2)) + pow(int(y.imag),2))  >= 2:
                break
        
        # for i in range(400):
        #     for j in range(400):
        #         listCoord.insert(c.imag, c.real)
                
        if math.sqrt(pow( int(y.real),2 ) + pow( int(y.imag),2 )) < 2:
            f.write(f'{"{:.3f}".format(c.real)}:{"{:.3f}".format(c.imag)}\n') 
                   
        x = 0
        y = 0
        
        if math.trunc(c.real) < 2:
            c = c + 0.01

        if math.trunc(c.real) == 2:

            if math.trunc(c.imag) == -2:
                break
            
            elif c.imag > -2:
                c = c - 4 - 0.01j
                   
        b = b + 1
        print(f'b:{b} ==========')
        
# for x in listCoord:
#   print(x)         
            
        










# print("<===>")
# for i in range(10):
    
#     if pow(x,2)+c >= 2:
#         print("Above 2")
#         print(f'Result:{pow(x,2)+c}')
#         print(f'1st y: {y} x: {x}')
#         y = pow(x,2)+c
#         x = y
        
#         print(f'2nd Y:{y} x:{x}')
        
        
#     elif pow(x,2)+c < 2: 
#         print("Below 2")
#         print(f'Result:{pow(x,2)+c}')
#         print(f'1st y: {y} x: {x}')
#         y = pow(x,2)+c
#         x = y
        
#         print(f'2nd Y:{y} x:{x}')

