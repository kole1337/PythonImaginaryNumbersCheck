import math
from array import *
from pyde.de import DiffEvol

graph_numb  = open("10-10i.txt", "w")

def fractalSolution(): 
    imag_num = 0 + 0j
    
    for i in range(100):
        
        imag_num = imag_num + 1 + 1j
        
        
        
        graph_numb.write(f'{imag_num.real}:{imag_num.imag}\n')
        print(f'{imag_num.real}:{imag_num.imag}')
    
fractalSolution()    