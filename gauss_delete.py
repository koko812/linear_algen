A = [[1,-2],
    [2, 3]]
b = [[1],
    [3]]

def gauss_del(A, b):
    ex_A = [a+bb for a,bb in zip(A,b)]

    for col in range(len(A[0])):
        pivot = ex_A[col]
        for row in range(len(A)):
            if row==col:
                continue
            elif ex_A[row][col] != 0:
                print(pivot)
                print((ex_A[row][col]/pivot[col]))
                row -= pivot * (ex_A[row][col]/pivot[col])
    return ex_A 

if __name__ == "__main__":
    print(gauss_del(A,b))
