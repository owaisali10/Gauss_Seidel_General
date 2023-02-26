import numpy as np

def iterate(X0, A, B, tol):
    X = X0
    L = np.tril(A, k=0)
    U = np.triu(A, k=1)
    Linv = np.linalg.inv(L)
    T = -np.matmul(Linv,U)
    C = np.matmul(Linv,B)

    condition, n = True, 0 
    #a1, b1, c1 = 4, 1, 10
    #a2, b2, c2 = 2, 3, 14
    while condition:
       Xn = np.matmul(T,X) + C
       n = n+1
       for i in range(len(B)):
            if abs(X[i] - Xn[i]) <= tol:
                condition = False
            else:
                condition = True
                break
       X = Xn
            
    return X, n

def isDDM(A, size) :
    for i in range(size) :        
        sum = 0
        for j in range(size) :
            sum = sum + abs(A[i][j])    
        sum = sum - abs(A[i][i])
        
        if (abs(A[i][i]) < sum) :
            return False
    return True                

def take_input():
    # Input Matrix size
    print("Number of unknowns?:", end=' ')
    m = int(input())
    A, B, a = [], [], []
    for i in range(m):
        for j in range(m):
            print (f"a{i+1}{j+1}:", end=''),
            a.append(float(input()))
        A.insert(i,a)
        a = []
        print(f"b{i+1}:", end='')
        B.append(float(input()))
    print("What's your tolerance?: 1e-",end='')
    tol = 10**(-int(input()))
    print("Is this your system of equations?:")
    print(f"{A}[X] =  {B}")
    return A, B, tol

# Code begins
A, B, tol = take_input()
print("Press 'Y' to continue 'N' to re-insert coefficients")
str = input()
X0 = []
if (str == "Y" or str == "y"):
    ddm = isDDM(A,len(B))
    if ddm == True:
        print("Initial guesses?")
        for i in range(len(B)):
            print(f"x{i+1}_initial:",end='')
            X0.append(float(input()))
        X, n = iterate(X0, A, B, tol)
        for i in range(len(B)):
            print(f"X{i}={X[i]},",end=' ')
        print(f" in {n} iterations")
    else:
        print("Not Strictly Diagonally Dominant. Cannot solve!")
        quit()
else:
    take_input()




