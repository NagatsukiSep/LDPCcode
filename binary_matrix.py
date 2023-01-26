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

def unit_vec(n,pos):
    result = []
    for i in range(n):
        if i == pos:
            result.append([1])
        else:
            result.append([0])
    return transpose(result)

def rank(H):
    check_binary(H)
    echelon(H)
    rank = 0
    for i in range(len(H)):
        for j in range(len(H[0])):
            if H[i][j] == 1:
                rank += 1
                break
    return rank

def generator(H):
    check_binary(H)
    _rank = rank(H)
    full_ranked = partial_matrix(echelon(H),0,len(H[0])-1,0,_rank-1)
    count = 0
    tmp = None
    for i in range(len(full_ranked[0])):
        if partial_matrix(full_ranked,i,i,0,len(full_ranked)-1) == transpose(unit_vec(len(full_ranked),count)):
            count += 1
        else:
            if tmp == None:
                tmp = partial_matrix(full_ranked,i,i,0,len(full_ranked)-1)
            else:
                tmp = concatenate_row(tmp,partial_matrix(full_ranked,i,i,0,len(full_ranked)-1))
    G = None
    ele_count = 0
    tmp_count = 0
    for i in range(len(full_ranked[0])):
        if partial_matrix(full_ranked,i,i,0,len(full_ranked)-1) == transpose(unit_vec(len(full_ranked),ele_count)):
            if G == None:
                G = partial_matrix(transpose(tmp),ele_count,ele_count,0,len(transpose(tmp))-1)
            else:
                G = concatenate_row(G,partial_matrix(transpose(tmp),ele_count,ele_count,0,len(transpose(tmp))-1))
            ele_count += 1
        else:
            if G == None:
                G = transpose(unit_vec(len(transpose(tmp)),tmp_count))
            else:
                G = concatenate_row(G,transpose(unit_vec(len(transpose(tmp)),tmp_count)))
            tmp_count += 1
    return G



def random_matrix(n,m):
    seed = random.randint(0,100000)
    random.seed(seed)
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.randrange(0,2))
        result.append(row)
    if(check_valid(result)):
        print("seed: " + str(seed))
        return result
    else:
        return random_matrix(n,m)

def check_valid(H):
    for i in range(len(H[0])):
        tmp = 0
        for j in range(len(H)):
            tmp = H[j][i] or tmp
        if tmp == 0:
            return False
    return True

def random_matrix_seed(n,m,seed):
    random.seed(seed)
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.randrange(0,2))
        result.append(row)
    return result

def display(H):
    if H == None:
        print("None")
        return
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
hoge = random_matrix(4,7)
# hoge = random_matrix_seed(4,7,49078)
display(hoge)
print()
print(rank(hoge))
display(echelon(hoge))
print()
display(generator(hoge))
print()
display(dot(generator(hoge),transpose(echelon(hoge))))
# display(transpose(unit_vec(4,0)))