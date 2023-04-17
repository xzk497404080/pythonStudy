import math
num = input()
#从小到大输出num的所有质因子
result = ''
def getPrime(num):
    k = math.sqrt(int(num))
    # print('---',num)
    for i in range(2,int(k)+1):
        # print(i)
        if num % i == 0:
            # result = result + str(i) + ' '
            print(i,end=' ')
            getPrime(num//i)
            return
    print(num)
        # else:
        #     print(num,end=' ')
getPrime(int(num))
# print(result)
