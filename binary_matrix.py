def dot(m1, m2):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if(m1[i][j] != 0 and m1[i][j] != 1):
                raise ValueError("m1 is not a binary matrix")
    for i in range(len(m2)):
        for j in range(len(m2[0])):
            if(m2[i][j] != 0 and m2[i][j] != 1):
                raise ValueError("m2 is not a binary matrix")
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
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if(m1[i][j] != 0 and m1[i][j] != 1):
                raise ValueError("m1 is not a binary matrix")
    result = []
    for i in range(len(m1[0])):
        row = []
        for j in range(len(m1)):
            row.append(m1[j][i])
        result.append(row)
    return result


a = [[1,0,1],[0,1,0]]
b = [[1,0],[1,0],[1,0]]
# print(dot(a,b))
# print(identity(3))
# print(transpose(a))