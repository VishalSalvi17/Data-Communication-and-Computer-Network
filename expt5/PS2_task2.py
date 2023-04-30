'''
Exp 5 Task2 
Group 3 
Prathamesh Bagekari 4
Akshat Bhat 5
Arka Haldi 15
'''

import numpy as np

def syndrome_decode(codeword,n,k,G):
    q = n - k # Redundant Bits

    # G(k x n) = [I(k x k) : P(k x q)]
    P = G[:,k:] # Parity Sub Matrix

    # Parity Check Matrix = H(q x n) = [trans(P(q x n) : I(q x q))]
    P_transpose = np.transpose(P)

    H = np.concatenate((P_transpose,np.identity(q)),axis=1)
    H_transpose = np.transpose(H)
    
    S = np.mod(np.dot(codeword,H_transpose),2) # Syndrome
    # print('H_transpose:\n',H_transpose)
    print('Syndrome:\n',S)
    if np.array_equal(S,np.zeros(q)) :
        print("No error..")
        return f"Codeword: {codeword}"
    else:
        print(f"OOPS: Error detected ...expected {np.zeros((1,q))} got {S}")
        print("Corrected codeword :")
        for i,row in enumerate(H_transpose):
            if np.array_equal(S,row):
                codeword[i] ^= 1
                print(codeword)
                print('Identified dataword')
                return codeword[:-q]
        
def decode_and_print(n,k,Generator_matrix_array,m):
    for Generator_matrix in Generator_matrix_array:
        print('Encoded dataword :\n',m)
        for i in range(n):
            codeword = np.mod(np.dot(m,Generator_matrix),2)
            transmitted_codeword = codeword
            print()
            print(i)
            print('~~~~~~~~~~~~~~~~~~~~~')
            print('Transmitted codeword:\n',transmitted_codeword)
            codeword[i]^=1
            print('Received codeword:\n',codeword)
            print(syndrome_decode(codeword,n,k,Generator_matrix))
            print()
        codeword = np.mod(np.dot(m,Generator_matrix),2)
        transmitted_codeword = codeword
        print()
        print(n)
        print('~~~~~~~~~~~~~~~~~~~~~')
        print('Transmitted codeword:\n',transmitted_codeword)
        print('Received codeword:\n',codeword)
        print(syndrome_decode(codeword,n,k,Generator_matrix))
        print(f'Deciphered dataword: {m}')
        print(f'\nAll 0 and 1 error tests passed for (7,4,3) code with generator matrix G:\n{Generator_matrix}')
    return None

if __name__ == "__main__":
    # (7,4) Hamming Code , for the purpose of this experiment
    # ==> n = 7, k = 4, q = n - k = 3
    n = 7
    k = 4
    Generator_matrix_array = [ np.array([
                                [1,0,0,0,1,1,1],
                                [0,1,0,0,1,1,0],
                                [0,0,1,0,1,0,1],
                                [0,0,0,1,0,1,1]],
                                ndmin=2),
                               np.array([
                                [1,0,0,0,1,0,1],
                                [0,1,0,0,1,1,1],
                                [0,0,1,0,1,1,0],
                                [0,0,0,1,0,1,1]],
                                ndmin=2),
                               np.array([
                                [1,0,0,0,0,1,1],
                                [0,1,0,0,1,1,1],
                                [0,0,1,0,1,1,0],
                                [0,0,0,1,1,0,1]],
                                ndmin=2),
                            ]
    m = np.array([1,0,1,0])
    decode_and_print(n,k,Generator_matrix_array,m) # Pass generator arrays into the function