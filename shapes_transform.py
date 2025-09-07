from matplotlib import pyplot as plt
import math

v1 = [[1], [1]]
v2 = [[1], [-1]]
v3 = [[-1], [-1]]
v4 = [[-1], [1]]
shape = [v1,v2,v3,v4]

A = [[2,1], [1,1]]
ini_v = [[5],[-4]]

def matmul(A, v):
    if len(A[0]) != len(v):
        print("invalid input")
        return 0 

    ret = [[sum([aa * vv[0] for aa, vv in zip(a,v)])] for a in A]
    return ret

def _to_coodinate(shape):
    c_x, c_y = zip(*shape)
    c_x = [xx for x in  c_x for xx in x]
    c_y = [xx for x in  c_y for xx in x]
    c_x.append(c_x[0])
    c_y.append(c_y[0])
    return c_x, c_y

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
    for i in range(1000):
        n_v = matmul(A,v)
        n_v_norm = norm(n_v)
        normalized_n_v = [[n_vv[0]/n_v_norm] for n_vv in n_v]
        #print(normalized_n_v)
        #print(vecmul(normalized_n_v, matmul(A, normalized_n_v)))
        v = normalized_n_v
    print(f"eigen_vector: {normalized_n_v}")
    print(f"eigen_value: {vecmul(normalized_n_v, matmul(A, normalized_n_v))}")

if __name__ == "__main__":
    print(shape)
    shape_d = [matmul(A,v) for v in shape]
    power_method(A, ini_v)
    print(shape_d)
    o_x, o_y = _to_coodinate(shape)
    d_x, d_y = _to_coodinate(shape_d)
    plt.plot(o_x, o_y)
    plt.plot(d_x, d_y)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid()
    plt.savefig("plt.png")