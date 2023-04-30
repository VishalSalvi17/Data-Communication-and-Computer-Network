'''
Exp 5 Task1 
Group 3 
Prathamesh Bagekari 4
Akshat Bhat 5
Arka Haldi 15
'''
import numpy as np
import itertools as it
from PS2_rect import even_parity

a=np.array([[0,1,1,0,0,],
            [1,1,0,1,1,],
            [1,0,1,1,0,]
            ], ndmin=2)

b=np.array([[1,0,0,1,1,],
            [0,0,1,0,1,],
            [1,0,1,0,0,]
            ], ndmin=2)

c=np.array([[0,1,1,1,1,],
            [1,1,1,0,1,],
            [1,0,0,0,0,]
            ], ndmin=2)

test_codewords = [a,b,c]
# just for our reference, as given in the pdf

def rect_parity(codeword:np.ndarray,nrows:int,ncols:int):
    compressed_row = np.apply_along_axis(even_parity,1,codeword)[:-1] # row wise compression 
    compressed_col = np.apply_along_axis(even_parity,0,codeword)[:-1] # column wise compression 
    # finding index with 1
    i,j = -1,-1
    for t in range(nrows):
        if compressed_row[t]==1:
            i = t
    for t in range(ncols):
        if compressed_col[t]==1:
            j = t
    # print(compressed_row) i th row
    # print(compressed_col) jth column
    passed=True
    if np.sum(compressed_row) and np.sum(compressed_col) :
        print(f"detected error at {(i,j)} for codeword : \n{codeword}")
        codeword[i,j] = codeword[i,j]^1 # correction, bit flip
        passed = False
    else:
        print("passed...")
    return (codeword[:-1,:-1],passed)


# utility functions
def trial_test(array_of_codewords): # using a, b , c
    print('Testing all codewords...')
    for codeword in array_of_codewords:
        print('\nTesting codeword:')
        print(codeword)
        message_sequence,passed = rect_parity( codeword , nrows=2, ncols=4)
        if not passed:
            print("\n codeword failed, \n corrected codeword : \n",message_sequence,"\n")
    print(f'(14,8) rectangular parity code successfully tested for 1 bit error tests')
    return None


def test_correct_errors(array_of_codewords):
    # creates all codewords possible for (8,4)
    print('Testing all codewords...')
    nrows,ncols = array_of_codewords[0].shape # generic, to handle any shape 
    for codeword in array_of_codewords:
        message_sequence,passed = rect_parity( codeword , nrows-1, ncols-1)
        if not passed:
            print("Corrected message_sequence : \n",message_sequence,"\n")
    nrows-=1
    ncols-=1
    print(f'({nrows*ncols+nrows+ncols},{nrows*ncols}) rectangular parity code successfully tested for 1 bit error tests')


def codeword_generator(nrows=2,ncols=2):
    # n+1 is the size of the codeword
    # r is the number of rows of the rect dataword
    # c is the number of cols of the rect dataword
    codeword_length = nrows * ncols + nrows + ncols
    # completing the rectangle, we'll have n+1 = r*c + r + c + 1 = (r+1)*(c+1)
    PNumpyArr = []
    PList = list(it.product(range(2),repeat=codeword_length))
    for arr in PList :
        temp = list(arr)+[0]
        PNumpyArr.append(np.reshape(temp,(nrows+1,ncols+1)))
    return PNumpyArr


if __name__ == "__main__" :
    # keep the pivot zero, as it doesn't affect the result of either 
    # trial_test(test_codewords)
    test_correct_errors(codeword_generator())
    # generated_codewords=codeword_generator()
    # print(generated_codewords)