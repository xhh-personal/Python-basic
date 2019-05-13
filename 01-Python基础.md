#  Python基础语法

## 01-第一个Python程序

```python
print("hello world")
```

## 02-变量的定义

> 格式：变量名 = 数据

```python
score = 100
name = "张三"
pi = 3.14
print(score)
# 在Python中不需要指定数据类型，会根据数据自动推导出数据类型
is_ok = True
# 通过type查看变量类型
print(type(score))
print(type(name))
print(type(pi))
print(type(is_ok))

# 判断是否是指定数据类型
isinstance(obj, type)
```

> 常用数据类型：int str float bool list tuple dict set

## 03-变量的命名规则

### 基本规则

>字母、数字、下划线组成，但不能以数字开头

### 变量命名方式

* 驼峰命名法

    ```python
    # 小驼峰
    myName = "李四"
    # 大驼峰
    MyName = "王五"
    ```

* 下划线命名法 **（推荐使用）**

    ```python
    my_name = "赵六"
    ```

## 04-关键字

关键字在Python中具有特殊功能标识符，关键字不能作为变量名使用

```python
import keyword
kw = keyword.kwlist
print(kw)
'''
 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
'''
```

## 05-注释

对代码的解释和说明，可以提供代码的可读性

### 单行注释

以#开头

### 多行注释

用三个双引号 or 三个单引号 包围起来  
快捷键：Ctrl + /

```python
# 单行注释
'''
多行注释1
多行注释1
'''
"""
多行注释2
多行注释2
"""
```

## 06-数据类型转换

+ int()
    - float -> int 取整数部分
+ float()

+ str()

+ evel() 获取字符串 __原始数据__
    - evel('abc') 会报错 NameError: name 'abc' is not defined.

```python
num1 = 10
my_str = "10"
# 把字符串转成 int 类型
num2 = int(my_str)
print(type(num2))
# 目前类型统一可以进行计算
result = num1 + num2
print(result)

my_float_str = "3.14"
num3 = float(my_float_str)
print(num3)
print(type(num3))

# int类型和float类型计算 会把int转成float
result = num1 + num3
print(result)

num4 = 4.55
# 注意：只取整数部分
num5 = int(num4)
print(num5)

print(type(str(num4)))

# eval: 获取字符串原始数据
# my_str = "5.15"
'''
my_str = "abc"
NameError: name 'abc' is not defined
'''
my_str = '[1,3,5]'
value = eval(my_str)
print((value))
print(type(value))
```

## 07-输出和输入

### 7.1输出

print函数定义如下：

```python
def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
    """
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    """
    pass
```

+ <code>*args</code> 表示不定长的参数
+ seq = ' ' 默认用空格符间隔，可以修改
+ end='\n 同理

测试代码：

```python
print('hello world')
my_str1 = 'hello'
my_str2 = 'world'
# 输出多个参数之间 默认使用 空格进行分割
print(my_str1, my_str2)
# 修改输出的分隔符
print(my_str1, my_str2, sep ='&')
# 修改为不换行
print("hello", end='')
print('你好')
print("哈哈\n嘻嘻")
```

### 7.2 输入

input函数定义如下：

```python
def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
    """
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    """
    pass
```

 <code>input()</code> 返回的数据类型都是str
> 注：Python2中使用 <code>raw_print</code>

## 08-if判断

### if-else结构

```python
age = int(input('请输入您的年龄：'))
if age >= 18:
    print('adult')
else:
    print('not adult')
```

### if-elif-else结构

```python
age = int(input('请输入您的年龄：'))
if 15 <= age <= 17:
    print('1')
elif age > 17 and age <= 40:
    print('2')
elif age > 40 and age < 80:
    print('3')
else:
    print('unknown')
```

### 可以判断的类型

+ bool类型
+ 数字类型——非0即真
+ 容器类型——有数据即真，无数据为假
+ None空值
  + None --> 条件不成立
  + not None --> 条件成立

## 09-比较运算符

+ == , >= , > , < , <= , !=
+ 运算结果返回bool类型

## 10-逻辑运算符

+ and , or , not

```python
score = 90
if score >= 90 and score <= 100:
    print('优秀')
num1 = 1
if num1 == 1 or num1 == 2:
    print('Nice')
if not 1 == 2:
    print('条件成立')
```

## 11-字符串常见操作

+ 根据子串查找下标
    - <code>str.find()</code> 如果没有找到就返回-1
    - <code>str.index()</code>如果没有找到抛出异常

+ 统计字符串个数
    - <code>len(str)</code>
    - <code>str.count(substr)</code>
+ 替换指定数据
    - <code>str.replace(old,new[,count])</code>
+ 分割数据
    - <code>str.split()</code>
+ 判断是否以指定数据开头
    - <code>str.startswith()</code>
+ 把字符串以指定子串分割成三部分
    - <code>str.partition(sep)</code>
+ 根据指定字符串拼接数据
    - <code>flag_str.join()</code>
    - 注：前提是最终的数据是字符串<code>"123" ['1','2']</code>等
+ 去除空格
    - <code>str.strip()</code> 去除两边空格
    - <code>str.lstrip()</code> 去除左边空格
    - <code>str.rstrip()</code> 去除右边空格
+ 去除指定数据
    - <code>str.strip(sub)</code> 去除两边
    - <code>str.lstrip(sub)</code> 去除左边
    - <code>str.rstrip(sub)</code> 去除右边

```python
my_str = 'hello'
print(my_str.index('e')) # 1
print(my_str.find('h')) # 0
# print(my_str.index('f')) # Error
print(my_str.find('x')) # -1
print(len(my_str)) # 5
print(my_str.count('l')) # 2
print(my_str.replace('l','x')) # hexxo

my_str = '百度,阿里,华为'
print(my_str.split(',')) # ['百度', '阿里', '华为']

my_url = "https://www.baidu.com"
print(my_url.startswith('https')) # True
print(my_url.endswith('com')) # True

my_str = 'aaabbcccc'
print(my_str.partition('bb')) # ('aaa', 'bb', 'cccc')

print('-'.join('abc')) # a-b-c
print('-'.join(['1', '2', '3'])) # 1-2-3
print('-'.join(('1', '2', '3')))

print(' hello '.strip())
print(' hello '.lstrip())

print('abcdcba'.strip('a'))     # bcdcb
print('abcdcba'.lstrip('a'))    # bcdcba
```

## 13-列表与元组

### 13.1 列表（有序）

+ 定义：以中括号表现形式的数据集合
+ 列表中可以放入任意类型的数据

+ 下标：一个编号，根据编号找到数据
    + 正数下标：默认从0开始，表示第1个元素
    + 负数下标：-1表示 倒数 第1个元素

+ 访问元素可以直接用<code>varname[index]</code>

```python
my_list = [1, 1.22, "abc", True]
print(my_list, type(my_list)) # [1, 1.22, 'abc', True] <class 'list'>
# 根据下标获取列表数据
print(my_list[0]) # 1
print(my_list[-2]) # abc
```

+ 添加操作
    - <code>append()</code> 
        - 向列表中追加一个指定数据
    - <code>insert(index, object)</code>
        - 在index位置插入指定数据
    - <code>extend(list)</code>




    ```python
    # 1.1 向列表中追加一个指定数据
    my_list.append(1)
    my_list.append("大家好")
    print(my_list) # [1, '大家好']
    
    # 1.2 插入指定数据
    my_list.insert(1, 'abc')
    print(my_list) # [1, 'abc', '大家好']
    
    my_list1 = ["西瓜", "草莓", "芒果"]
    # my_list.append(my_list1)
    # print(my_list)
    
    # 1.3 extend 扩展一组数据
    my_list.extend(my_list1) # [1, 'abc', '大家好', '西瓜', '草莓', '芒果']
    print(my_list)
    ```

+ 修改操作
  
    + 访问下标直接改
+ 删除操作
    + <code>remove(obj)</code> 删除指定数据
    + <code>del list[index]</code>
        - 用del关键字删除指定下标的元素
        - 如果不合法则抛出异常
    + <code>pop()</code>
        - 默认删除最后一个元素
        - 同时返回被删除的元素

    ```python
    # 修改数据
    my_list = [1, 'abc', '大家好', '西瓜', '草莓', '芒果']
    my_list[0] = '葡萄'
    my_list[-1] = '桃子'
    print(my_list)

    # 删除数据
    my_list = ['葡萄', 'abc', '大家好', '西瓜', '草莓', '桃子']
    my_list.remove('abc')
    print(my_list)
    del my_list[-1]
    print(my_list)
    print(my_list.pop(), my_list)
    ```

+ 查询操作
    - <code>object in list</code>
    - <code>object not in list</code>
        - 返回<code>True/False</code>
    - <code>list.index(obj)</code> 根据数据查询指定下标
        - 返回索引值
        - 不存在则抛出异常
    - <code>list.count(obj)</code> 根据指定数据获取 数据 在列表中的个数

    ```python
    # 查找
    my_list = ['大家好', '葡萄', '葡萄', '西瓜', '草莓']
    print("西瓜" in my_list)
    print("相加" not in my_list)
    print(my_list.index("葡萄")) # 1
    # print(my_list.index("111"))
    print(my_list.count("葡萄")) # 2
    print(my_list.count("11")) # 0
    ```

### 13.2 元组

+ 定义： 以小括号表现形式的数据集合
  
    - 坑点：如果仅仅有1个元素需要在其后加逗号<code>(5,)</code>不然括号会被忽略
+ 注意：
    - 元组可以存放任意数据
    - 元组指定下标获取数据，不能对元组进行数据的修改
    - 如果元组数据为列表，可对列表操作进行数据修改
+ 查询操作同列表

    ```python
    my_tuple = (1, 4, 'abc', True, 1.2)
    print(my_tuple)
    print(my_tuple[2], my_tuple[-1])
    # del my_tuple[2]
    # my_tuple[0] = 2

    my_tuple = (1, [3, 5])
    # 直接根据下标修改元组中的数据。不支持
    # my_tuple[1] = [2, 4]
    # 取到元素再修改
    my_tuple[1][0] = 2
    print(my_tuple) # (1, [2, 5])
    ```

## 14- 字典（无序）

+ 定义：以大括号表现形式的键值对数据的集合，比如<code>{'name':'zhangsan', 'age':18}</code>

+ 注意：
    - key 一般都是字符串，只能是不可变类型(数字、字符串、元组)，不能使用可变类型：[],{}
    - 通过key获取对应value，key在字典里边唯一
- 字典是无序的，定义的数据顺序和输出顺序 不一致
  
+ 取值操作
    - <code>dict[key]</code>
        - 如果key不存在则抛出异常
    - <code>dict.get(key, default)</code>
        - 如果key不存在，默认返回 <code><class 'NoneType'></code> None , 也可设置默认返回的值

    ```python
    my_dict = {'name':'zhangsan', 'age':18}
    print(my_dict, type(my_dict))
    print(my_dict['name'])
    print(my_dict.get('age'))
    # my_dict['sex']
    print(my_dict.get('sex', "男"))
    ```

+ 添加/删除操作

  ```python
  # 定义空字典
  my_dict = {}
  # 添加键值对，key不在字典里则添加
  my_dict['name'] = 'zhangsan'
  my_dict['age'] = 18
  my_dict['sex'] = 'Male'
  my_dict['address'] = 'Beijing'
  print(my_dict)
  # 修改键值对，key存在就是修改
  my_dict['address'] = 'Shanghai'
  print(my_dict)
  ```

+ 删除操作

  - <code>del dict[key]</code>

  - <code>dict.popitem()</code> 随机删除键值对，返回key和value的元组

  - <code>dict.pop(key)</code> 删除指定key的键值对，返回key和value

	```python
  my_dict = {'name': 'zhangsan', 'sex': 'Male', 'address': 'Shanghai'}
  # 随机删除键值对，返回<class 'tuple'> key和value
  value = my_dict.popitem()
  print(value, type(value))
  ```

+ 查操作
  - <code>key in dict</code>
  - <code>key in dict.keys()</code>
  - <code>value in dict.values()</code>
  
  ```python
  my_dict = {'name': 'zhangsan', 'age': 18, 'sex': 'Male', 'address': 'Shanghai'}
  print(my_dict.keys(), type(my_dict.keys()))
  # dict_keys(['name', 'age', 'sex', 'address']) <class 'dict_keys'>
  print(my_dict.values(), type(my_dict.values()))
  # dict_values(['zhangsan', 18, 'Male', 'Shanghai']) <class 'dict_values'>
  ```
  
## 15-循环(for、while)

+ 定义：根据条件循环执行某种操作

+ 基本用法：

  ```python
  num = 1
  while num <= 5:
      print(num)
      num += 1
  print('--------------')
  
  # for循环一般结合range使用
  # range(起始,结束,步长)
  # range(1,5) 实际上是[1,5) 不包含5,步长=1
  for value in range(1, 100, 10):
      print(value)
  print('--------------')
  
  # range(5) 起始=0,结束=5,步长=1
  for value in range(5):
      print(value)
  ```

+ 跟else结合

  ```python
  num = 5
  while num >= 1:
      print(num)
      num -= 1
  else:
      print("循环执行结束")
  
  for value in range(3):
      if value == 2 :
          print('ok')
      print(value)
  else:
      print('循环结束')
  ```

+ continue和break

  + 不能单独使用，只能在循环语句中使用
  + break的时候，else语句也不执行，强行退出循环体

+ else和break实例(注意else所在位置，不能往后缩进)

  ```python
  name = input("请输入你的姓名：")
  for value in ["张三", "李四"]:
      if value == name:
          print(value)
          break
  else:
      print("没有找到这个人")
  ```

+ for的应用——获取容器类型(字符串、列表、元组、字典、set)中每一个数据

  - 遍历字符串、列表、元组

  ```python
  # 仅获取value(set可用)
  my_str = "abc"
  for val in my_str:
      print(val)
  
  my_list = ["apple", "pear", "banana"]
  for val in my_list:
      print(val)
  print("------------")
  
  # 同时获取index value
  my_list = enumerate(["apple", "pear", "banana"])
  print(my_list)
  for val in my_list:
      # 此时每个val为元组
      print(val[0], val[1])
  print("------------")
  
  my_list = enumerate(["apple", "pear", "banana"])
  # index, val获取的是 元组中的每一个值，就是拆包
  for index, val in my_list:
      print(index, val)
  ```

  + 遍历 字典

  ```python
  my_dict = {'name': 'zhangsan', 'age': 18, 'sex': 'Male', 'address': 'Shanghai'}
  # 遍历 key
  for key in my_dict:
      print(key)
  print('----------')
  
  # 遍历 value
  for value in my_dict.values():
      print(value)
  print('----------')
  
  # 同时取到key value
  # for key, value in my_dict:  # 错误写法
  #     print(key, value)
  print(my_dict.items()) # 每一项组成的元组的列表
  print('----------')
  for key, value in my_dict.items():
      print(key, value)
  ```

  

## 16-集合

+ 定义：以大括号表现形式的数据集合，集合里边不能有重复数据，集合也是无序
+ 注意：
  + 不能根据下标获取和修改数据，可以添加和删除
  + 定义空的集合不能使用<code>{}</code> 会识别为dict，正确操作：<code>my_set = set()</code>

+ 常见操作：

  - <code>add(obj)</code> 添加数据
  - <code>remove(obj)</code> / <code>discard(obj)</code> 删除数据
    - remove不存在会抛出异常
    - discard不存在会忽略，不会崩溃

  ```python
  my_set = {1, 4, 'abc', 'hello'}
  print(my_set, type(my_set))
  my_set.add(5)
  print(my_set)
  
  # my_set.remove('abcd')
  print(my_set.discard('abcd')) # None
  print(my_set.discard(5)) # None
  ```

+ 集合可以对容器类型数据去重
  
  - <code>set(list)</code>

## 补充- 元组、列表、集合互相转换

+ set()
+ tuple()
+ list()

> 直接调用相关的 函数 即可转换。注意转为set的时候自动去重

## 17- 拆包

+ 通俗理解：把容器类型（字符串、列表、元组、字典、集合）中每一个数据使用不同的变量进行保存

```python
my_str = "abc"
var1, var2, var3 = my_str
print(var1, var2, var3)

my_dict = {'name': 'zhangsan', 'age': 18, 'sex': 'Male', 'address': 'Shanghai'}
# key1, key2 = my_dict
# 变量个数要和容器的个数一致
key1, key2, key3, key4 = my_dict
```

## 18- 函数

### 18.1 函数的介绍

+ 通俗理解：某一个功能的代码实现
+ 目的：代码复用，降低代码冗余

### 18.2 函数的定义和调用

```python
# 定义函数,不自动调用
def fun():
    print("helloWorld")
    print("helloWorld")
# 调用函数
fun()

# 定义含参数的 函数
def show(name, age):
    print("My name is %s, %d years old." % (name, age))
show('Amy', 100)
```

### 18.3 函数的四种类型

+ 无参数、无返回值
+ 有参数、无返回值
+ 无参数、有返回值
+ 有参数、有返回值

```python
def fun3():
    return "类型3函数"
print(fun3())

def fun4(name, age):
    return "My name is %s, %d years old." % (name, age)
print(fun4('xiaohuihui', 20))
```

### 18.4 函数的调用顺序

+ 函数的定义不会执行其中代码
+ 函数调用的时候先去给函数传参，当函数体中代码执行完返回到调用的地方，继续执行

形参、实参略

### 18.5 局部变量、全局变量

+ 局部变量定义：函数内定义的变量叫 局部变量，只能在函数内使用，不能在函数外使用
+ 全局变量定义：在函数外定义的变量 叫 全局变量，可以在不同函数内使用，共享数据

```python
# 全局变量
score = 100
def show():
    # 局部变量
    score = 99
    print("分数:", score) # 99
def show1():
    print("全局变量：", score) # 100
# print(score)
```

```python
score = 100
def show():
    # 若要修改全局变量则用 global varname 先声明一下再操作
    # global score = 99 写法错
    global score
    score = 99
    print("分数:", score)
def show1():
    print("全局变量：", score)
# print(score)
show()
show1()
```

### 18.6 缺省参数

+ 定义：在函数定义的时候参数就有值，这样的参数叫做缺省参数
+ 注意事项：
  + 必选参数放到前面，默认参数在后
  + 默认参数必须指向不变对象
  + 默认参数只在定义时候计算一次
  + 默认参数一直指向同一个对象

```python
def calc(num1, num2 = 2):
    return  num1 + num2
print(calc(2)) # 2+2=4
print(calc(2,10)) # 2+10=12
```

### 18.7 调用函数传参方式

+ 位置参数方式传参,必须按照 函数参数顺序 传参
+ 关键字参数方式传参,可以不按照 顺序

```python
def show(name, age):
    print(name, age)

# positional argument
# 使用位置参数方式传参,必须按照 函数参数顺序 传参
show('zhangsan', 10)

# keyword argument
# 使用关键字参数方式传参,可以不按照 顺序
show(age=20, name='lisi')

# 前面使用位置参数,后边可以使用关键字
# 前面使用关键字传参，后边必须关键字！

# show(name='111',18) 报错！
```

### 18.8 函数的不定长参数(*)

+ 定义：调用函数的时候 不确定传入多少个参数，可能是0个或多个函数

#### 18.8.1 不定长位置参数

```python
def sum(*args):
    # args 把传入的位置参数封装到一个元组
    print(args,type(args))
    result = 0
    for v in args:
        result += v

    return result
sum() # () <class 'tuple'>
sum(1, 4, 5) # (1, 4, 5) <class 'tuple'>

# sum(args=(1,2,3))
# sum(a=1,b=2)
```

+ 习惯上使用*args
+ args ==> 传入的位置参数封装的一个元组
+ 调用函数的时候只能 使用__位置传参方式__
+ 形参当实参

    ```python
def show_msg(*args):
        print(args)
    
    def show(*args):
        # 对元组进行拆包
        show_msg(*args)
    show(1, 2)
    ```



#### 18.8.2 不定长关键字参数

```python
# 2. 不定长关键字参数
def show_msg(**kwargs):
    print(kwargs, type(kwargs))
    for k, v in kwargs.items():
        print(k, v)

# 不能使用位置参数给不定长关键字函数传参
# show_msg(1,2)
show_msg(a=1, b=2) # {'a': 1, 'b': 2} <class 'dict'>
```

+ 习惯上用<code>**kwargs</code>

+ kwargs ==> 传入的关键字参数 封装的 一个字典

+ 形参当实参

    ```python
    def show_msg(**kwargs):
        print(kwargs)
        # for k, v in kwargs.items():
        #     print(k, v)

    def show(**kwargs):
        # show_msg(a = kwargs) # {'a': {'a': 1, 'b': 2}}
        # show_msg(a=1, b=2)
        # print(**kwargs) 报错
        # 对字典进行拆包
        show_msg(**kwargs)
    show(a=1, b=2)
    ```
    
+ 禁止位置参数传参——*后边的必须用关键字参数，前边的无限制

    ```python
    def show(*, name, age):
        print(name, age)
    # show("xhh", 22)
    # TypeError: show() takes 0 positional arguments but 2 were given
    show(name='xhh', age=22)
    
    def show(sex, *, name, age):
        print(name, age)
    
    ```

    

#### 18.8.3 函数参数的高级使用

以下代码为正确的：

```python
# name,age 为必选参数
# args为不定长位置参数
# kwargs 为不定长关键字参数
def show(name, age, *args, **kwargs):
    print(name, age, args, kwargs)

# 不能使用下面的方式调用，因为前边使用关键字后面不能使用位置参数
# show(name='李四', age=18, 10, 20, c=1, b=2)

# 使用 位置方式 给 必选参数 传参
show('李四', 18, 10, 20, 30, c=1, b=2, d='random')
# 李四 18 (10, 20, 30) {'c': 1, 'b': 2, 'd': 'random'}
```

```python
def show(*args, name, age, **kwargs):
    print(name, age, args, kwargs)

show(1, 2, 3, 4, name='xiaohuihui', age=18, aa=1, bb=3)
# xiaohuihui 18 (1, 2, 3, 4) {'aa': 1, 'bb': 3}
```

以下代码会有语法错误：

```python
# **kwargs必须放到所有参数的最后边
def show(**kwargs, name, age, *args):
    print(name, age, args, kwargs)

def show(name, age,**kwargs, *args):
    print(name, age, args, kwargs)
```

跟缺省参数的结合：

```python
# 设置了缺省参数，但是没效果
def show(name, age = 18, *args, **kwargs):
    print(name, age, args, kwargs)
show('zhangsan', 'haha', 'xixi', a=10)
# zhangsan haha ('xixi',) {'a': 10}

# 如果要使用默认参数，需要放到*args后边
def show(name, *args, age = 18, **kwargs):
    print(name, age, args, kwargs)
show('zhangsan', 'haha', 'xixi', a=10)
# zhangsan 18 ('haha', 'xixi') {'a': 10}
show('zhangsan', 'haha', 'xixi', age= 10, a=10)
# zhangsan 10 ('haha', 'xixi') {'a': 10}
```

### 18.9 函数的注意事项

+ 函数名不能相同，无重载，如果定义了第二个函数名和第一个函数名相同，那么第一个函数不能使用
+ 变量名 和 函数名 不能相同

```python
def show():
    print("不带参数的show")
show()
def show(msg):
    print(msg)
show("带参数的show")
show = 10
# show()  TypeError: 'int' object is not callable
```

### 18.10 函数嵌套

#### 18.10.1 定义

在函数里边再定义一个函数

```python
def show():
    def test():
        print("在我show函数内部定义")
    # test() 没有这个调用则无法执行
show()
# test()
```

### 18.11 递归函数

+ 定义：函数里边再调用函数本身
+ 特点：传递、回归
+ 注意：
  + 不能无限次递归调用
  + 必须设置结束递归的条件及返回值

```python
import sys
def gc(num):
    # 当计算1! 时不需要往下传递，需要返回结果
    # 必须要设置结束递归的条件
    if num == 1:
        return 1
    else:
        return num * gc(num - 1)
# 获取默认的递归次数
print(sys.getrecursionlimit()) # 1000
print(gc(6)) # 720
# print(gc(1000)) 因超出次数无法调用

# 设置递归次数
sys.setrecursionlimit(1100)
print(gc(1000))
```

### 18.12 匿名函数*

+ 定义：顾名思义就是函数没有名字，使用lambda关键字定义的函数就是匿名函数
+ 注意事项：
  + 只适合做一下简单的操作，返回值不需要加return
  + 一般使用变量保持匿名函数

```python
# 只适合做一下简单的操作，返回值不需要加return
result = (lambda x, y: x + y)(1, 2)
print(result) # 3
# 使用变量保持匿名函数
mult = lambda x, y:x * y
print(mult(2,5)) # 10
def fun():
    return 1
print(type(fun)) # <class 'function'>
print(type(mult)) # <class 'function'>

# 判断是否是奇数
def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True
print(is_odd(3)) # True

# 匿名函数的应用场景——简化代码
new_is_odd = lambda num: False if num % 2 == 0 else True
print(new_is_odd(4)) # False

# 对字典列表排序的时候 可以 使用匿名函数
my_list = [{"name": 'zs', "age": 20}, {"name": 'zs', "age": 18}]

# item: 表示列中的每一项字典数据
# item:["age"] 根据字典中age对应的value值进行排序
my_list.sort(key=lambda item: item["age"], reverse = False)
print(my_list)

# 匿名函数也是函数,上述lambda匿名函数可转化为下面的函数
def get_value(item):
    return item["age"]
```

### 18.13 内置函数

+ 内置函数就是 python 自己定义的函数，可以直接使用，无须导入包
  + len,max,min,sorted,open,lower
  + <code>id()</code> 获取10进制内存地址
  + <code>hex(id()) </code>获取十六进制内存地址
  + <code>dir(object)</code> 返回对象的属性/方法列表
  + <code>isinstance(obj, class)</code>  判断obj是不是class类型

```python
# len() 统计容器类型 元素个数
print(len("abc"))
print(len(["aa", "bc"]))
print(len((1, 2)))
# max() 统计容器类型数据中的最大值
print(max("538"))
print(max([5,6,0]))
# sorted 排序
new_list = sorted([8, 6, 7])
print(new_list) # [6, 7, 8]

# del() 可以删除变量
del(new_list)
# print(new_list)
```

### 18.14 函数的文档说明

三方公司 查看自己公司 接口方法或者函数的时候需要使用

```python
def add(num1, num2):
    '''
    计算数字之和
    :param num1:第一个数字
    :param num2:第二个数字
    :return:返回 和
    '''
    return num1 + num2

value = add(1, 2)
help(add)
'''
add(num1, num2)
    计算数字之和
    :param num1:第一个数字
    :param num2:第二个数字
    :return:返回 和

'''
help(len)
'''
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

'''
```

### 18.15 偏函数

+ 通俗理解：指明函数的参数偏爱某个值，这样的函数叫做偏函数
+ 引子

```python
# 需求：num3不想传递
def show(num1, num2, num3 = 1):
    return num1 + num2 + num3

print(show(1, 2)) # 4

# 但有些时候还需要用到其他值，但不想传
# 定义一个偏函数
def show2(num1, num2, num3 = 2):
    return show(num1, num2, num3)
print(show2(1, 2)) # 5
# 注意定义有些复杂，相当于重新定义了一次函数，但也算偏函数
```

+ <code>functools包的使用</code>

```python
import functools
def show(num1, num2, num3 = 1):
    return num1 + num2 + num3

# 指明函数的参数设置为某个值
show2 = functools.partial(show, num3 = 2) # 返回的函数就是偏函数
print(show2(1, 2)) # 5

# 指明内置函数的参数偏爱某个值，生成一个偏函数
# int()默认按照 10进制 进行转
print(int("123")) # 123

new_func = functools.partial(int, base = 2)
print(new_func('11')) # 3
```

### 18.16 返回函数

+ 返回函数：在函数里边返回一个函数

```python
# 函数的嵌套
def show():
    def inner():
        print('hahaha')
    # 返回了一个函数
    return inner
# 获得返回的函数
new_func = show()
# 执行返回的函数
new_func() # hahaha
```

```python
# 此函数可作为18.17高阶函数中 函数返回一个函数 的例子
def calc(opt):
    if opt == '+':
        return lambda num1,num2 : num1+num2
    if opt == '-':
        return lambda num1,num2 : num1-num2
new_func = calc('-')
print(new_func(1,2)) # -1
```

### 18.17 高阶函数

+ 高阶函数：一个函数的参数 接受 另外一个函数 或者 返回一个函数
+ 针对的是 把函数 作为参数或者返回值

```python
# 定义一个普通函数
def add(num1, num2):
    return num1 + num2

# 高阶函数——将函数作为参数接收
def calc_num(num1, num2, func):
    return func(num1, num2)

print(calc_num(4,5,add)) # 9

# 高阶函数——返回一个函数例子见 返回函数一节
```

```python
# 高阶函数 - 综合两种情况
def test(func):
    func()
    return lambda :print("lambda called")

def show_msg():
    print("show_msg called")

new_func = test(show_msg) # show_msg called
new_func() # lambda called

# 一步到位
test(show_msg)()
'''
show_msg called
lambda called
'''
```

### 18.18 闭包

+ 闭包：在函数嵌套的情况下，内部函数使用了外部函数的参数或者变量，并把这个内部函数返回，返回的函数称为闭包
+ 条件：
  + 函数嵌套情况下
  + 内部函数使用外部函数的参数/变量
  + 返回这个内部函数

```python
def show(msg):
    num = 10
    def inner():
        print(num, msg)
    return inner

new_func = show("哈哈")
print(new_func) # <function show.<locals>.inner at 0x00000116C077BBF8>
new_func() # 10 哈哈
```

+ 应用场景：可以根据参数生成不同的返回函数(闭包)

  ```python
  def hello(msg, count):
      return lambda msg, count: msg*count
  new_func1 = hello("A", 2)
  print(new_func1()) # AA
  print(new_func1()) # AA
  new_func2 = hello("B", 2)
  print(new_func2()) # BB
  print(new_func2()) # BB
  ```

### 18.19 装饰器**

#### 18.19.1 引例

+ 装饰器： 本质上就是一个函数
+ 作用：给原函数的功能上进行拓展
+ 好处：不改变原函数的定义及调用的操作

```python
def show():
    print("AAAA")

show() # AAAA

# 装饰器--> 通过闭包完成
def decorator(new_func):
    def inner():
        print('-' * 10)
        new_func()
    return inner
# 原有的show环境并没有被清除 --> 不改变原函数的定义
show = decorator(show)
show()
'''
----------
AAAA
'''
```

#### 18.19.2 使用语法糖@

+ 在使用@的时候装饰器的代码就会执行

```python
# 装饰器--> 通过闭包完成
def decorator(new_func):
    print("decorator called")
    def inner():
        print('-' * 10)
        new_func()
    return inner
@decorator # show = decorator(show)
def show():
    print("AAAA")
show()
'''
----------
AAAA
'''

'''
decorator: <function decorator at 0x000002ABE7DDAE18>
new_func: <function show at 0x000002ABE7DDAF28>
inner: <function decorator.<locals>.inner at 0x000002ABE7F61048>
show: <function decorator.<locals>.inner at 0x000002ABE7F61048>

show, 00-hello_py.py:10
inner, 00-hello_py.py:6
<module>, 00-hello_py.py:11
execfile, _pydev_execfile.py:18
run, pydevd.py:1135
main, pydevd.py:1735
<module>, pydevd.py:1741
'''
```

#### 18.19.3 设计装饰器

根据装饰器内的函数特点可分为以下几类：

+ 不带参数，无返回值(见18.19.2)

+ 带参数，无返回值 —— 在inner加入参数并调用

  ```python
  # 装饰器--> 通过闭包完成
  def decorator(func):
      def inner(num1, num2):
          print("计算结果如下：")
          func(num1, num2)
      return inner
  @decorator # show = decorator(show)
  def add(num1, num2):
      print(num1 + num2)
  add(1, 2)
  '''
  计算结果如下：
  3
  '''
  ```

+ ​	带参数，有返回值

  ```python
  # 装饰器--> 通过闭包完成
  def decorator(func):
      print("decorator called")
      def inner(num1, num2):
          print("计算结果如下：")
          return func(num1, num2)
      return inner
  @decorator # show = decorator(show)
  def add(num1, num2):
      return num1 + num2
  @decorator
  def msg(num1, num2):
      print(num1, num2)
  
  print(add(1, 2))
  '''
  计算结果如下：
  3
  '''
  print(msg('hello','111'))
  '''
  计算结果如下：
  hello 111
  None
  '''
  ```

  亦可装饰无返回值的函数，只不过返回了None

  > 亦可装饰内置函数，但只能采用手动赋值的形式，不能用语法糖，另外参数和返回值需要处理妥当

#### 18.19.4 通用装饰器

上述装饰器存在如下问题：

+ 被装饰的函数 和 装饰器里边的函数 参数需要一致

可用不定长参数解决这一问题

```python
def decorator(func):
    print("decorator called")
    def inner(*args, **kwargs):
        # 装饰代码
        return func(*args, **kwargs)
    return inner
```

#### 18.19.5 带参数的装饰器

先观察下面这段代码：

```python
def decorator1(func):
    def inner():
        print("A"* 10)
        func()
    return inner
def decorator2(func):
    def inner():
        print("B"* 10)
        func()
    return inner
def decorator3(func):
    def inner():
        print("C"* 10)
        func()
    return inner

@decorator3
def show():
    print(1111)

show()
```

当出现需要根据不同参数生成不同装饰器时，这种做法显然不妥

可定义带参数的装饰器，如下：

```python
def get_decorator(char):
    def decorator(func):
        def inner():
            print(char * 10)
            func()
        return inner
    return decorator

@get_decorator('S')
def show():
    print(1111)

show()
```

#### 18.19.6 函数使用多个装饰器

```python
def decorator1(func):
    def inner():
        print('-' * 30)
        func()
    return inner
def decorator2(func):
    def inner():
        print('*' * 30)
        func()
    return inner
@decorator1 # show = decorator1(decorator2.inner) => decorator1.inner
@decorator2 # show = decorator2(show) -> decorator2.inner
def show():
    print('AAAA')

show()
'''
------------------------------
******************************
AAAA
'''
```



## 19.切片*

+ 定义：根据下标的范围获取一部分数据，比如：列表、字符串可以使用切片
+ 使用格式：element[start, end, step]
  + start为起始下标，默认为0
  + end为结束下标，不包含
  + step为步长，默认是1

+ 使用技巧
  + 前n个[0:3] 简化为 [:3]
  + 后n个[-n:]
  + 全部[:]
  + 倒置[::-1]

```python
my_str = "hello"
print(my_str[1:4]) # ell

# 取前3位
print(my_str[0:3]) # hel
print(my_str[:3]) # hel

# 取后3位
print(my_str[2:5]) # llo
# 冒号后跟-1 —— 最后1个数据取不到
print(my_str[-3:-1]) # ll
print(my_str[-3:0]) # 空串,0表示第1个数据，在-3的前边
# 冒号后面不知道——表示可以去到最后1个数据
print(my_str[-3:]) # llo

# 快速获取整个字符串
# result = my_str[0:5]
result = my_str[:]
print(result) # hello

# 步长是负数 表示 从后往前取值
print(my_str[-2:-5:-1]) # lle
print(my_str[3:0:-1]) # lle
print(my_str[::-1]) # olleh

# 间隔的取
print(my_str[::2]) # hlo
```

## 20- 列表生成式(列表推导式)

+ 通俗理解：使用for循环快速创建一个列表，最终获取一个列表
+ 目的：快速创建一个列表
+ 语法格式：<code>[表达式 for val in xxx]</code> 

```python
my_list = []
for i in range(1, 6):
    my_list.append(i)
print(my_list)

# 列表推导式目的：快速创建一个列表
print([val for val in range(1, 6)])
# [1, 2, 3, 4, 5]
print([val*2 for val in range(1, 6)])
# [2, 4, 6, 8, 10]
print([len(val) for val in ["aaa", "cd"]])
# [3, 2]
print([val+"hello" for val in ["aaa", "cd"]])
# ['aaahello', 'cdhello']

# 双for
print([(x, y) for x in range(1, 3) for y in range(4, 6)])
# [(1, 4), (1, 5), (2, 4), (2, 5)]

# 加入if判断
print([val for val in range(1, 11) if val % 2 == 0])
# [2, 4, 6, 8, 10]
```

## 21- 引用

+ 通俗理解：程序中的数据在内存中的地址，简称内存地址

```python
a = 10
b = a
print("a保存的数据的内存地址：", hex(id(a))) # 0x7fffa6bae470
print("b保存的数据的内存地址：", hex(id(b))) # 0x7fffa6bae470
print(a, b) # 10 10
a = 20
print("a保存的数据的内存地址：", hex(id(a))) # 0x7fffa6bae5b0
print("b保存的数据的内存地址：", hex(id(b))) # 0x7fffa6bae470
print(a, b) # 20 10
```

## 22- 可变类型和不可变类型

+ 可变类型：可在在原有数据基础上对数据进行修改(增删改)，修改后内存地址不变
  + 举例：列表、集合、字典
  + (自注)这里不变的是变量本身的存放的地址，该地址 指向的内存空间 仍然是地址

```python
my_list = [1, 5, 6]
# 查看内存地址
print(str(my_list) + " <-- " + hex(id(my_list)))
for val in my_list:
    print("%d <-- " % val +hex(id(val)))

my_list[0] = 2
my_list.append(7)
print(str(my_list) + " <-- " + hex(id(my_list)))
for val in my_list:
    print("%d <-- " % val +hex(id(val)))

del my_list[1]
print(str(my_list) + " <-- " + hex(id(my_list)))
for val in my_list:
    print("%d <-- " % val +hex(id(val)))
```

```python
[1, 5, 6] <-- 0x1fc05156288
1 <-- 0x7fffbc0fe350
5 <-- 0x7fffbc0fe3d0
6 <-- 0x7fffbc0fe3f0
[2, 5, 6, 7] <-- 0x1fc05156288
2 <-- 0x7fffbc0fe370
5 <-- 0x7fffbc0fe3d0
6 <-- 0x7fffbc0fe3f0
7 <-- 0x7fffbc0fe410
[2, 6, 7] <-- 0x1fc05156288
2 <-- 0x7fffbc0fe370
6 <-- 0x7fffbc0fe3f0
7 <-- 0x7fffbc0fe410
```

+ 不可变类型：不能在原有数据基础上对数据进行修改，当然直接赋值一个新值，那么内存地址会发生改变（实际上改的是内存地址）
  + 字符串，数字，元组

```python
my_str = "hello"
print(hex(id(my_str)) + " --> " + my_str)
# my_str[0] = 'a' 不能修改数据！

# 重新赋值后，变量的内存地址发生改变，指向新的元素的地址空间
my_str = "world"
print(hex(id(my_str)) + " --> " + my_str)

my_num = 5
print(hex(id(my_num)) + " --> " + str(my_num))
# my_num[0] = 1
my_num = 6
print(hex(id(my_num)) + " --> " + str(my_num))

my_tuple = (4, 6)
print(hex(id(my_tuple)) + " --> " + str(my_tuple))
for val in my_tuple:
    print(hex(id(val)) + " --> " + str(val))
# my_tuple[0] = 5
my_tuple = (5, 6)
print(hex(id(my_tuple)) + " --> " + str(my_tuple))
for val in my_tuple:
    print(hex(id(val)) + " --> " + str(val))
```

```python
0x1831f259538 --> hello
0x1831f312848 --> world
0x7fffbc3ce3d0 --> 5
0x7fffbc3ce3f0 --> 6
0x1831f311988 --> (4, 6)
0x7fffbc3ce3b0 --> 4
0x7fffbc3ce3f0 --> 6
0x1831f3e6708 --> (5, 6)
0x7fffbc3ce3d0 --> 5
0x7fffbc3ce3f0 --> 6
```

> 个人总结：基本类型对象int, float, bool 等变量直接存放 对象的地址，地址处存放对象本身
>
> 例如数字5，本身的地址并不发生变化
>
> 集合类型变量存放的地址处，是若干对象的地址？（不严谨）并非对象本身
>
> 元组、字符串不能修改，变化后变量地址变化，地址中的 对象地址部分发生变化
>
> 列表、字典、集合 变化后 变量地址不变，变化的是地址中的 对象地址

| 地址内容 | 数据发生变化                   | 实质                                         |
| -------- | ------------------------------ | -------------------------------------------- |
| 不可变   | 重新赋值      变量地址发生变化 | 变量指向 新对象(集合) 的存放的地址           |
| 可变     | 增删改后      变量地址不变     | 集合地址不变，但集合中指向对象的地址发生变化 |

## 23- global的使用 - 拓展

### 23.1 global与不可变类型

```python
# 定义不可变类型全局变量
g_num = 10
print("函数外g_num:", hex(id(g_num)), "-->", g_num)
def modify():
    # 声明要修改全局变量, 表示要修改全局变量的内存地址
    global g_num
    g_num = 1
    print("函数内g_num:", hex(id(g_num)), "-->", g_num)

modify()
print(g_num)
```

### 23.2 global与可变类型

+ 不加global

```python
# 定义可变类型的全局变量
g_list = [3, 5]
print("函数外g_list:", hex(id(g_list)), "-->", g_list)
def modify():
    # 在原有数据基础上 添加了一个数据
    # 如果只是修改数据，这里不需要加上global,加上也不会有问题
    # global g_list 加上也不会受到影响
    g_list.append(4)
    print("函数内g_list:", hex(id(g_list)), "-->", g_list)
modify()
print(g_list)
```

输出结果如下：

```python
函数外g_list: 0x22b58286288 --> [3, 5]
函数内g_list: 0x22b58286288 --> [3, 5, 4]
[3, 5, 4]
```

分析：内存地址不发生变化的情况下，不用加

```python
# 定义可变类型的全局变量
g_list = [3, 5]
print("函数外g_list:", hex(id(g_list)), "-->", g_list)
def modify():
    g_list = [1, 2]
    print("函数内g_list:", hex(id(g_list)), "-->", g_list)
modify()
print(g_list)
```

输出结果如下：

```python
函数外g_list: 0x1f5daf96288 --> [3, 5]
函数内g_list: 0x1f5db1960c8 --> [1, 2]
[3, 5]
```



+ 加global

```python
# 定义可变类型的全局变量
g_list = [3, 5]
print("函数外g_list:", hex(id(g_list)), "-->", g_list)
def modify():
    global g_list
    g_list = [1, 2]
    print("函数内g_list:", hex(id(g_list)), "-->", g_list)
modify()
print(g_list)
```

运行结果如下：

```python
函数外g_list: 0x272c88b6288 --> [3, 5]
函数内g_list: 0x272ca5a1588 --> [1, 2]
[1, 2]
```

> 要在函数内 修改 全局变量 内存地址，必须加上global关键字
>
> 对于可变类型，只修改数据，可以不加global

## 24- 公共运算符的操作

### 24.1 +运算符 拼接

+ 可以完成列表、元组、字符串的拼接

```python
print("hello"+"world") # helloworld
print([1, 3]+[4, 5]) # [1, 3, 4, 5]
print((1, 3)+(4, 5)) # (1, 3, 4, 5)
```

### 24.2 *运算符 复制

+ 可以完成列表、元组、字符串的复制

```python
print('-'*15) # ---------------
print('ab'*5) # ababababab
print([1, 2] * 3) # [1, 2, 1, 2, 1, 2]
print((4, 5) * 3) # (4, 5, 4, 5, 4, 5)
```

## 25- 文件

### 25.1 文件的介绍

可以做到数据的永久存储，文件以硬盘为载体

### 25.2 文件读写操作

+ <code>open()</code> 打开文件
  + 文件访问模式
    + r 只读，文件不存在会抛出异常
    + w 只写
      + 文件不存在则会创建文件并打开
      + 如果文件存在，先把原有数据清空
    + a 追加写入
    + rb 二进制方式读取文件数据
    + wb 二进制方式写入文件数据
    + ab 二进制方式追加写入文件数据
    + r+ , w+ , a+ 支持读写，但要看前面的主模式
      + r+  写入数据时候不会先清空数据，会从开头开始覆盖
    + rb+ , wb+ , ab+ 支持二进制方式读写模式
  + 设定编码 encoding="utf-8"
    + Windows下默认编码为GBK / cp936
    + Linux、MacOS下默认编码为UTF-8
    + **二进制模式不需要指定编码模式**

> python2中不支持中文，需要指定编码格式
>
> python3支持中文，使用utf-8编码

+ <code>write()</code> 支持写入的方式打开文件后，写入文件
  + 多次写入数据不会覆盖前面的数据
  + 编码格式采用指定的编码

+ <code>read()</code> 读取文件
  + 如果打开文件时候指定的编码 与 文件编码 不一致会抛出异常 UnicodeDecodeError: 'gbk' codec can't decode byte 0xad in position 2: illegal multibyte sequence(Python3.7)

```python
# 打开文件使用open函数
# ------- r模式 -------
file = open("1.txt", "r", encoding="utf-8") # 默认r模式
content = file.read()
print(content) # 中文world
file.close()
# ------- w模式 -------
# file = open("1.txt", "w", encoding="utf-8")
# file.write("中文")
# file.write("world")
# file.close()
# a模式略

file = open("1.txt", 'rb',)
content = file.read()
print(content) # b'\xe4\xb8\xad\xe6\x96\x87world'
file.close()
```

### 25.3 文件的不同读取操作

+ <code>read()</code> 从文件指针处开始 读取，读取后文件指针改变

+ read(1) 表示从文件指针处开始读取1个长度数据，可能是一个汉字，也可能是一个字母
  - rb模式的话是指定读取的字节数，读取后需要解码decode

+ <code>tell()</code> 查看文件指针的位置
+ <code>seek()</code> 设置文件指针的位置
+ `readline()`  读取一行数据
  + 当遇到'\n'(也会读到)表示读取数据结束
+ <code>readlines()</code>
  + 把每行的数据放到一个列表中

 ### 25.4 文件拷贝

+ 小文件拷贝

  ```python
  # 1.打开原文件读取数据
  # rb模式：比较通用的模式，可以兼容不同类型的文件
  src_file = open("3.txt", "rb")
  # 读取文件中的全部数据
  file_data = src_file.read()
  # 2.打开目标文件准备写入数据
  # 拓展：可以指定拷贝后的文件路径
  # dst_file = open("C:\\Users\\73654\\Desktop\\dst.txt", "wb")
  dst_file = open("C:/Users/73654/Desktop/dst.txt", "wb")
  dst_file.write(file_data)
  src_file.close()
  dst_file.close()
  # 实测：500MB的文件照读不误
  ```

  

+ 大文件拷贝

  ```python
  src_file = open("big.txt", "rb")
  dst_file = open("big_copy.txt", "wb")
  # 循环读取文件中的数据
  while True:
      file_data = src_file.read(1024)
      if file_data:
          # 表示有数据
          dst_file.write(file_data)
      else:
          print("数据读取完成:",file_data) # b''
          break
  src_file.close()
  dst_file.close()
  ```

### 25.5 文件和文件夹的相关操作

引入os模块，os有如下函数

+ <code>rename(src, dst)</code> 重命名
  + 文件路径必须存在
+ <code>renames(src, dst)</code> 重命名
  + 文件路径不存在则创建

+ <code>mkdir()</code> 创建文件夹
+ <code>getcwd()</code> 获取当前目录
+ <code>chdir()</code> 更改当前路径change dir
+ <code>listdir(path)</code> 返回当前文件目录列表
+ <code>remove(file_path)</code> 删除文件
+ <code>rmdir()</code> 删除文件夹，只能删除空的
  + 若要删非空的，需要引入 文件操作高级模块 shutil
  + <code>shutil.rmtree()</code>
+ <code>path.abspath(path)</code> 获取绝对路径
+ <code>path.basename(abs_path)</code> 根据绝对路径获取 文件名
+ <code>path.splitext(abs_path)</code> 根据绝对路径获取 (文件名, 后缀)，可通过拆包获取

> 划重点：listdir, chdir, rename, rmtree