import numpy as np

# data = np.random.rand(2, 3)
# print(data)
# print(data + data)
# print(data * 10)
# print(data.max())
# print(data.min())
# print(data.dtype)
# print(data.shape)
# print(data.size)

# data1 = np.array([[1, 2, 3], [4, 5, 6]])
# print(data1.max())
# print(data1.min())
# print(data1.dtype)
# print(data1.shape)
# print(data1.size)
# print(data1.ndim)
# print(data1.flags)
# print(data1.itemsize)
# print(np.zeros(5))
# print(np.arange(5))
# print(np.arange(5, 10))
# print(np.arange(5, 10, 2))
# print("创建等差数列:", np.linspace(1, 10, 5))
# print("创建底数为2的等比数列:", np.logspace(1, 10, 10, base=2))

# 切片
# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# print('我们的数组是：')
# print(x)
# print('\n')
# rows = np.array([[0, 0], [3, 3]])
# cols = np.array([[0, 2], [0, 2]])
# np.amin(cols, 1)
# y = x[rows, cols]
# print('这个数组的四个角元素是：')
# print(y)


# a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
# print('我们的数组是：')
# print(a)
# print('调用 amin() 函数：')
# print(np.amin(a, 1))
# print('再次调用 amin() 函数：')
# print(np.amin(a, 0))
# print('调用 amax() 函数：')
# print(np.amax(a))
# print('再次调用 amax() 函数：')
# print(np.amax(a, axis=0))

# b = np.array([[[3, 2], [5, 6], [9, 8]], [[0, 2], [2, 6], [6, 9]]])
# print(b.shape)
# print(np.amin(b, 0))  # [[0,2],[2,6],[6,8]]
# print(np.amin(b, 1))  # [[3,2],[0,2]]
# print(np.amin(b, 2))  # [[2,5,8],[0,2,6]]
# print(np.amax(b, 0))
# print(np.amax(b, 1))
# print(np.amax(b, 2))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a)
print(b)
c = np.meshgrid(a, b)
print(c)

print(2 if 2 >1 else 3)
