#################List（列表）##################
"""
列表是写在方括号([])之间、用逗号分隔开的元素列表。
列表截取的语法格式：变量[头下标:尾下标]
索引值以 0 为开始值，-1 为从末尾的开始位置。
加号（+）是列表连接运算符，星号（*）是重复操作。
"""
'''
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表
'''
'''
list = ['zhangsan','lisi','wangwu','lier',888,999,'010','san','si','wu']
print('原始list为',list)
del list[1:3]
print ('删除过后的list:',list)
'''
# append方法，在末尾加入
print('##########append方法的用法###########')
test = []
print('列表为空')
test.append(111)
test.append('zhangsan')
test.append('lisi')
print('现在的列表为', test)

# insert方法，在任意位置加入
print('##########insert方法的用法###########')
test.insert(0, 888)  # 在首位0处加入888
print(test)

# pop方法，把末尾的字符跳出来
print('##########pop方法的用法###########')
test0 = [12, 22, 35, 4, 56, 68, '70']
pt = test0.pop()  # 把末尾的字符跳出来，放到poptest中去
print(test0)
print('末尾删除过的字符为:', pt + '.')

# pop（）方法，把任意位置的字符字符跳出去，需要指定索引位置
print('##########pop方法的用法,任意位置的字符###########')
test1 = [1, 2, 3, 4, 5]
pop2test = test1.pop(0)  # 把末尾的字符跳出来，放到pop2test中去
print('删除了第一个字符', pop2test)

# remove方法，根据具体值删除内容（只知道要删除的元素的值）
print('##########remove方法的用法1###########')
test2 = ['aa', 'bb', 'cc', 'dd']
print('原来的内容为:', test2)
test2.remove('bb')
print('删除后的内容为;', test2)

# remove方法，赋值变量删除
print('##########remove方法的用法2###########')
test3 = [11, 22, 33, 44, 55, 65, 75, 85, 95]
print(test3)
by = 22  # 定义不要的变量
test3.remove(by)
print(test3)
print('我不要了', by, '哈哈哈')

# sort方法，对列表永久排序
print('##########sort方法的用法###########')
cars = sorted(['aa', 'ee', 'bb', 'cc', 'dd'])
print(cars)
cars.sort(reverse=True)  # 相反的顺序排序
print(cars)

# sorted方法，对列表临时排序，不改变原来的排序
print('##########sorted方法的用法###########')
car2 = ['aa', 'ee', 'bb', 'cc', 'dd', 'uu']
print('原始的list', car2)
print('临时排序后', sorted(car2))
print('再次显示原始的list', car2)
