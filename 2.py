# 接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。不区分大小写
# 例如输入：Hello World! H
line = input()
c = input()
print(line.lower().count(c.lower()))