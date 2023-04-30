'''
Exp 5 Task1 
Group 3 
Prathamesh Bagekari 4
Akshat Bhat 5
Arka Haldi 15
'''

def even_parity(seq):
    element = 0
    for data in seq:
        element = element^data
    return element