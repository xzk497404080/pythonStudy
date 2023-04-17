#数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。
#输入描述：
# 先输入键值对的个数n（1 <= n <= 500）
# 接下来n行每行输入成对的index和value值，以空格隔开

# 输出描述：
# 输出合并后的键值对（多行）
n = int(input())
d = {}
for i in range(n):
    index, value = map(int, input().split())
    if index in d:
        d[index] += value
    else:
        d[index] = value
print(d.items())
# for k, v in sorted(d.items()):
#     print(k, v)



    
# len = input()
# dic = {}
# arr = []
# for i in range(int(len)):
#     kv = input()
#     k = int(kv.split(' ')[0])
#     v = int(kv.split(' ')[1])
#     if(dic.get(k)):
#         dic[k]+=v
#     else:
#         arr.append(k)
#         dic[k]=v
# # print(dic)
# arr.sort()
# # print(arr)
# for i in arr:
#     print(str(i)+' '+str(dic[i]))
    
