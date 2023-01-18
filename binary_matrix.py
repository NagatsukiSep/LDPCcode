import random

def dot(m1, m2):
    check_binary(m1)
    check_binary(m2)
    if(len(m1[0]) != len(m2)):
        raise ValueError("m1 and m2 are not compatible")
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m2[0])):
            sum = 0
            for k in range(len(m2)):
                sum ^= m1[i][k] & m2[k][j]
            row.append(sum)
        result.append(row)
    return result

def identity(n):
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            if(i == j):
                row.append(1)
            else:
                row.append(0)
        result.append(row)
    return result

def transpose(m1):
    check_binary(m1)
    result = []
    for i in range(len(m1[0])):
        row = []
        for j in range(len(m1)):
            row.append(m1[j][i])
        result.append(row)
    return result

def concatenate_row(m1,m2):
    check_binary(m1)
    check_binary(m2)
    if(len(m1) != len(m2)):
        raise ValueError("m1 and m2 are not compatible")
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j])
        for j in range(len(m2[0])):
            row.append(m2[i][j])
        result.append(row)
    return result

def concatenate_column(m1,m2):
    check_binary(m1)
    check_binary(m2)
    if(len(m1[0]) != len(m2[0])):
        raise ValueError("m1 and m2 are not compatible")
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j])
        result.append(row)
    for i in range(len(m2)):
        row = []
        for j in range(len(m2[0])):
            row.append(m2[i][j])
        result.append(row)
    return result

def get_var_name(var):
    for k,v in globals().items():
        if id(v) == id(var):
            name=k
    return name

def check_binary(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if(m[i][j] != 0 and m[i][j] != 1):
                raise ValueError(get_var_name(m) + " is not a binary matrix")

def partial_matrix(m, r_start, r_end, c_start, c_end):
    check_binary(m)
    result = []
    for i in range(c_start, c_end+1):
        row = []
        for j in range(r_start, r_end+1):
            row.append(m[i][j])
        result.append(row)
    return result
    

def generator(H):
    check_binary(H)
    G = concatenate_row(identity(len(H[0])-len(H)),transpose(partial_matrix(H,0,len(H[0])-len(H)-1,0,len(H)-1)))
    return G

def echelon(H):
    check_binary(H)
    r = 0
    c = 0
    while r < len(H) and c < len(H[0]):
        if H[r][c] == 0:
            for j in range(r+1,len(H)):
                if H[j][c] == 1:
                    for k in range(len(H[0])):
                        H[r][k]^=H[j][k]
                    break
        if H[r][c] == 1:
            for j in range(len(H)):
                if j != r and H[j][c] == 1:
                    for k in range(len(H[0])):
                        H[j][k] ^= H[r][k]
            r +=1
        c +=1
    return H

def random_matrix(n,m):
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.randrange(0,2))
        result.append(row)
    return result

def display(H):
    for i in range(len(H)):
        for j in range(len(H[0])):
            print(H[i][j], end="")
        print("\n", end="")

# def encode(x,H):
#     check_binary(x)
#     check_binary(H)
#     G = generator_matrix(7,4)
#     return dot(G,x)

a = [[1,0,1],[0,1,0]]
b = [[1,0],[1,0],[1,0]]
c = [[1,0,1],[1,0,1],[1,0,0]]
d = [[0,1,1,0,0,0,0,1,1,0,0,1,0],[],[]]
# print(dot(a,b))
# print(identity(3))
# print(transpose(a))
# print(transpose(c))
# print(concatenate_row(a,identity(len(a))))
# print(concatenate_column(a,identity(3)))
# print(partial_matrix(c,0,2,1,2))
display(echelon(random_matrix(4,7)))