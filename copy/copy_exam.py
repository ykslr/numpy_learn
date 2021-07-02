import numpy as np

# 创建一个一维数组，数据从0-11，共12个元素
a = np.arange(12)
print(a)

# 完全不复制的情况，a和b只是同一个东西的不同名字
b = a
b.shape = 3, 4    # 通过b修改对象属性，a同样发生了变化
print(a.shape)

b[0, 0] = 100     # 通过b修改数据，a同样发生了变化
print(a)

# 浅拷贝的情况
# 浅拷贝会复制对象属性，但数据内容还是指向原来的地方
# 也就是说更改对象属性，不会影响彼此
# 但是更改数据会影响彼此
c = a.view()      # 使用view方法创建一个查看相同数据的新数据对象
print(c)
c.shape = 2, 6    # 更改c对象的属性不会影响a对象
print(a.shape)
c[0, 1] = 101     # 更改c的数据，a同样发生变化
print(a)

# 深拷贝的情况
# 深拷贝是完全拷贝，会复制对象属性和数据
# 也就是说更改对象属性和数据都不会影响彼此
d = a.copy()      # 使用copy方法进行深拷贝
print(d)
d.shape = 2, 6    # 更改d对象的属性不会影响a对象
print(a.shape)
d[0, 2] = 102     # 更改d的数据不会影响a的数据
print("\na is \n", a)

print("\nd is \n", d)
