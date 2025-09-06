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

if __name__ == "__main__":
    print(gauss_del(A,b))
