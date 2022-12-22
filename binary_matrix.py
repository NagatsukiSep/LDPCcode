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

a = [[1,0,1],[0,1,0]]
b = [[1,0],[1,0],[1,0]]
c = [[1,0,1],[0,1,0],[1,3,1]]
# print(dot(a,b))
# print(identity(3))
# print(transpose(a))
# print(transpose(c))