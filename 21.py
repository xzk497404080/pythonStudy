# 描述
# 现在有一种密码变换算法。
# 九键手机键盘上的数字与字母的对应： 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0，把密码中出现的小写字母都变成九键键盘对应的数字，如：a 变成 2，x 变成 9.
# 而密码中出现的大写字母则变成小写之后往后移一位，如：X ，先变成小写，再往后移一位，变成了 y ，例外：Z 往后移是 a 。
# 数字和其它的符号都不做变换。

 
# 1≤n≤100 
# 输入描述：
# 输入一组密码，长度不超过100个字符。

# 输出描述：
# 输出密码变换后的字符串  
dic = {
    'a':2,
    'b':2,
    'c':2,
    'd':3,
    'e':3,
    'f':3,  
    'g':4,
    'h':4,
    'i':4,
    'j':5,
    'k':5,
    'l':5,
    'm':6,
    'n':6,
    'o':6,
    'p':7,
    'q':7,
    'r':7,
    's':7,
    't':8,
    'u':8,
    'v':8,
    'w':9,
    'x':9,
    'y':9,
    'z':9,
}
# 字母
letter = 'abcdefghijklmnopqrstuvwxyz'
# 大写字母
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

s = input()
for i in s:
    if i in letter:
        print(dic[i],end='')
    elif i in upper:
        if(i=='Z'):
            print('a',end='')
        else:

            print(letter[letter.index(i.lower())+1],end='')
    else:
        print(i,end='')
