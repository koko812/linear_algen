import math

#A = [[3,2], [0,1]]
#A = [[4,1,0], [1,3,1], [0,1,2]]
A = [[4,1,0], [0,3,1], [0,0,2]]
v = [[2], [1], [1]]
u = [[3], [5]]

def matmul(A, v):
    if len(A[0]) != len(v):
        print("invalid input")
        return 0 

    ret = [[sum([aa * vv[0] for aa, vv in zip(a,v)])] for a in A]
    return ret

def vecmul(u,v):
    ret = sum([uu[0] * vv[0] for uu, vv in zip(u,v)])
    return ret

def norm(v):
    return math.sqrt(sum([vv[0]**2 for vv in v]))

def power_method(A,v):
    print(f"A = {A}")
    print(f"v  = {v}")
    v_norm = norm(v)
    v = normalized_n_v = [[vv[0]/v_norm] for vv in v]
    for i in range(10):
        n_v = matmul(A,v)
        n_v_norm = norm(n_v)
        normalized_n_v = [[n_vv[0]/n_v_norm] for n_vv in n_v]
        print(normalized_n_v)
        print(vecmul(normalized_n_v, matmul(A, normalized_n_v)))
        v = normalized_n_v


if __name__ == "__main__":
    print(matmul(A,v))
    print("vecmul", vecmul(u,v))
    power_method(A,v)