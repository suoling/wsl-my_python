# for i in range(100):
#     print(i)

# range() 函数可创建一个整数列表，一般用在 for 循环中。
# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
for_list = ['a', 'b']
for a in for_list:
    print(a)


data = [6, 3, 7, 9, 1, 3, 5]
# data.sort()
data2 = sorted(data)


# sort 与 sorted 区别：
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，
# 而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。


print(data)
print(data2)
