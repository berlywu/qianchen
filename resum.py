# 获取1-100中被6整除的数

# a_list = []
# for i in range(1,101):
#     if i % 6 == 0:
#        a_list.append(i)
# print(a_list[-3:])



# 取出字符串出现一次最前面的字符

a = "abeecaf"


list1 = []
for i in a:
    b = a.count(i)
    if b == 1:
        c = a.index(i)
        print(c)
        list1.append(c)
str = sorted(list1)
print(a[str[0]])

#
# a = [1,',', '2', '>', 'c']
#
# for i in a:
#     b = a.count(i)
#     print(b)