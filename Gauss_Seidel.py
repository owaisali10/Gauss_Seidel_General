import numpy as np

def doIteration(X0, A, B, tol):
    # Initializing
    X = X0
    
    #Lower Triangle Matrix
    L = np.tril(A, k=0)
    
    #Upper Triangle Matrix
    U = np.triu(A, k=1)
    
    #Inverse of Lower Triangle Matrix
    Linv = np.linalg.inv(L)
    
    T = -np.matmul(Linv,U)
    C = np.matmul(Linv,B)
    
    #General Solution X = TX +C
    condition, n = True, 0 
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

# To check if system is solvable using Gauss-Seidel iteration
def isDdm(A, size) :
    for i in range(size) :        
        sum = 0
        for j in range(size) :
            # Adding all elements
            sum = sum + abs(A[i][j])    
        # Substracting the diagonal
        sum = sum - abs(A[i][i])
        
        if (abs(A[i][i]) < sum) :
            return False
    return True                

# Getting user values
def takeInput():
    # Input Matrix size
    print("Number of unknowns?:", end=' ')
    m = int(input())
    # Example values:
    #a11, a12, b1 = 4, 1, 10
    #a21, a22, b2 = 2, 3, 14
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

def exactSolution(A, B):
    Xe = np.matmul(np.linalg.inv(A),B)
    return Xe

# Code begins
A, B, tol = takeInput()
print("Press 'Y' to continue 'N' to re-insert coefficients")
str = input()
X0 = []
if (str == "Y" or str == "y"):
    ddm = isDdm(A,len(B))
    if ddm == True:
        print("Initial guesses?")
        for i in range(len(B)):
            print(f"x{i+1}_initial:",end='')
            X0.append(float(input()))
        X, n = doIteration(X0, A, B, tol)
        print(f"Gauss-Seidel iteration with a tolerance of {tol} gives solution:")
        for i in range(len(B)):
            print(f"X{i}={X[i]},",end=' ')
        print(f" in {n} iterations")
        Xe = exactSolution(A, B)
        print("Compared to Exact Solution:")
        for i in range(len(B)):
            print(f"X{i}={Xe[i]},",end=' ')
    else:
        print("Not Strictly Diagonally Dominant. Cannot solve!")
        quit()
else:
    takeInput()
