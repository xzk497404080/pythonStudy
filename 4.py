# 输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；
# •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
line = input()
print(len(line) % 8 != 0)
if len(line) % 8 != 0:
    line = line + '0' * (8 - len(line) % 8)
for i in range(0, len(line), 8):
    print(line[i:i+8])