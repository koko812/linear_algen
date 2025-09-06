import random

A = [[1,1,1],
    [2,-1,1],
    [1,2,-1]]
b = [[6],
    [3],
    [2]]

def gauss_del(A, b):
    ex_A = [a+bb for a,bb in zip(A,b)]

    for col in range(len(A[0])):
        pivot = ex_A[col]
        pivot_num = pivot[col]

        for row in range(len(A)):
            if row==col:
                continue
            elif ex_A[row][col] != 0:
                target = ex_A[row]
                ratio = target[col]/pivot[col]
                ex_A[row] = [t - p * ratio for t, p in zip(target, pivot)]

        ex_A[col] = [p / pivot_num for p in pivot]
            
    return ex_A 


def make_equation(dim=None, A=None, x=None):
    if dim is None:
        dim = len(x)
    if A is None:
        print(f"dim = {dim}")
        A = [[random.randint(-5,5) for i in range(dim)] for i in range(dim)]
    if x is None:
        x = [random.randint(1, 8) for i in range(dim)]

    #print(A,x)
    b = [[sum([aa*xx for aa, xx in zip(a, x)])] for a in A]
    print(f"A = {A}")
    print(f"b = {b}")
    print(f"x = {x}")
    return A,b,x
    

if __name__ == "__main__":
    A,b,_ =make_equation(x=[1,2])
    #print(A)
    #print(b)
    print(f"answer = {gauss_del(A,b)}")
