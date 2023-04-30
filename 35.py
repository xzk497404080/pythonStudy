# 描述
# 蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。

# 例如，当输入5时，应该输出的三角形为：

# 1 3 6 10 15
# 2 5 9 14
# 4 8 13
# 7 12
# 11


# 输入描述：
# 输入正整数N（N不大于100）

# 输出描述：
# 输出一个N行的蛇形矩阵。

n = input()
n = int(n)
a = []
for i in range(n):
    a.append([])
    for j in range(i,n):
        a[i].append(0)
print(a)
for i in range(n):
    for j in range(i,n):
        if i == 0:
            a[i][j] = j+1
        else:
            a[i][j] = a[i-1][j]+j+1-i
print(a)
