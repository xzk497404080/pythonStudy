# 明明生成了N个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。
# 第一行先输入随机整数的个数 N 。 接下来的 N 行每行输入一个整数，代表明明生成的随机数。 
n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
nums = list(set(nums))
nums.sort()
for num in nums:
    print(num)
#     num = int(input())
#     nums[num]=num
# print(nums)
#     nums.append(int(input()))
# nums = list(set(nums))
# nums.sort()
# for num in nums:
#     print(num)