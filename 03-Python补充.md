# Python补充知识

## 一、异常

### 1.1 异常简介

当使用Python解释器去执行代码的时候，遇到了错误，在控制台输出错误信息，这个错误信息就是异常

+ 代码遇到异常会终止执行  
```python
name = 'zhangsan'
name + 10
```

![1557402111833](C:\Users\73654\Documents\Study_Folder\Test\Python学习笔记\4.png)

+ 多数异常类 都 继承自 Exception 类
+ 


### 1.2 异常捕获

异常捕获通过try实现：

对于下面这段代码：

```python
num1 = input("请输入第一个数字：")
num2 = input("请输入第二个数字：")

result = int(num1) + int(num2)
print(result)
```

如果不去捕获异常，输入字母时会出现如下结果：

![1557402366247](C:\Users\73654\Documents\Study_Folder\Test\Python学习笔记\5.png)

ValueError继承自 Exception

添加异常捕获机制：

```python
try:
    # 把可能出现异常的代码放到try语句里
    num1 = input("请输入第一个数字：")
    num2 = input("请输入第二个数字：")

    result = int(num1) + int(num2)
    print(result)
except Exception as e: # e表示异常对象
    # 捕获到的异常会在except里边进行处理
    print(e)
```

输入不合法数据时出现如下结果：

![1557406548527](C:\Users\73654\Documents\Study_Folder\Test\Python学习笔记\6.png)

当然可以捕获多种类型异常：

```python
try:
    name = 'zs'
    del name
    # 在try里边如果执行代码遇到了异常，不会再try里边的后续代码，会执行except代码
    print(name)
    result = 1 / 0
# 可以同时捕获多种类型异常
except (NameError, ZeroDivisionError) as e:
    print(e)
```

else和finally的使用

```python
try:
    result = 1 / 0
# 可以同时捕获多种类型异常
except (NameError, ZeroDivisionError) as e:
    print(e)
else:
    print("没有异常 --> 会执行else")
finally:
    print("无论有没有异常 都会 执行finally语句")
```

> 总结：
>
> try语句块： 放可能出现异常的代码，一旦遇到异常不再执行后续语句，然后去对应except
>
> except语句块：捕获到的异常处理（可以捕获多种类型异常），一般情况指定Exception即可
>
> else语句块：没有异常时候，try执行完毕后执行此语句块
>
> finally语句块：不论有无异常，最后都会执行此语句块

### 1.3 自定义异常

+ 自定义异常类继承自Exception
+ 示例代码如下：

```python
# 自定义异常类
class CustomException(Exception):
    def __init__(self, content):
        self.content = content
    
    # 表示抛出异常时 异常描述信息
    def __str__(self):
        return "我是自定义异常，因为数据不是a，异常数据为%s" % self.content

content = input("请输入数据")
if content != "a":
    raise CustomException(content)
```

输出结果：

![1557660228911](C:\Users\73654\Documents\Study_Folder\Test\Python学习笔记\7)

### 1.4 手动抛出异常

在需要的地方用 raise 关键词 可以手动抛出异常，1.3 示例展示了 抛出自定义异常，当然也可以抛出系统异常。

不传入参数时候：<code>raise NameError()</code>

![1557660902673](C:\Users\73654\Documents\Study_Folder\Test\Python学习笔记\8)

如果传入了参数： <code>raise NameError("异常信息")</code>：

![1557660961891](C:\Users\73654\Documents\Study_Folder\Test\Python学习笔记\9)

如果系统自己抛出异常，异常信息由系统指定：

```python
a = 1
del a
print(a)
```

![1557661102439](C:\Users\73654\Documents\Study_Folder\Test\Python学习笔记\10)

> 注意：raise 只能抛出异常类型

## 二、模块

### 2.1 模块的介绍

+ 通俗理解模块就是一个.py文件，模块是管理功能代码的
+ 模块里 可以定义类、定义函数、定义全局变量，也可以执行对应的功能代码操作

### 2.2 内置模块

+ Python自己内部的模块，比如time, random
+ 用import导入后即可使用

```python
import time
import random
print("haha")
# 产生1~5之间的随机整数
result = random.randint(1, 5)
print(result)
# 休眠1s
time.sleep(1)
```

### 2.3 自定义模块

+ 理解：和变量名的定义 很类似，都是由 字母、数字、下划线组成，但不能以数字开头，否则无法导入。
+ 命名规则和变量名的一样，统一使用下划线命名法
+ 最好不能跟系统模块名字重复。否则导入该系统模块时就默认导入了 自定义模块

```python
# first_module.py 文件

# 定义全局变量
g_num = 10

def show():
    print("There is a function")

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_msg(self):
        print(self.name, self.age)
```

```python
import first_module

# 使用模块中的代码
print(first_module.g_num) # 10
first_module.show() # There is a function
stu = first_module.Student("李四", 20)
stu.show_msg() # 李四 20
```

### 2.4 主模块

+ 含义：执行的这个模块就是主模块

+ 查看模块名可以用

  ```python
  print(__name)
  # __main__ 表示主模块
  # 否则输出当前模块名
  ```

+ 

被导入模块有输出的情况下，导入时会输出

```python
# second_module.py 文件

g_score = 100

def show_info():
    print("show_info")

def sum_num(num1, num2):
    return num1 + num2

print(__name__)
# 测试 sum_num有没有问题
print("second:", sum_num(1, 3))
```

```python
import second_module
print(__name__)
print("当前模块:", second_module.sum_num(3, 2))
```

输出结果：

```
second_module
second: 4
__main__
当前模块: 5
```

**为了避免在 非 主模块测试的代码 影响 主模块，可以加入if判断**

```python
# 修改后的second_module.py 文件
g_score = 100

def show_info():
    print("show_info")

def sum_num(num1, num2):
    return num1 + num2

print(__name__)
if __name__ == '__main__':
    # 测试 sum_num有没有问题
    print("second:", sum_num(1, 3))
```

运行主模块后：

```python
second_module
__main__
当前模块: 5
```

可以发现"second: 4"不在执行

### 2.5 模块的导入方式

见3.2

### 2.6 模块导入的注意点

1. 自定义模块名不要跟系统的模块名重名
2. 导入的功能代码不要在当前模块定义，否则使用不了导入模块的功能代码

```python
form first_module import show

def show():
    print("aaa")

show() # aaa
```

推荐如下导入模块方式

```python
import first_module

def show():
    print("aaa")

show() # aaa
first_module.show() # There is a function 
```

### 2.7 模块搜索的顺序

+ <code>sys.path</code> 

```
['C:\\Users\\73654\\PycharmProjects\\day01', 'C:\\Users\\73654\\PycharmProjects\\day01', 'C:\\Program Files\\JetBrains\\PyCharm 2019.1.1\\helpers\\pycharm_display', 'C:\\Users\\73654\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip', 'C:\\Users\\73654\\AppData\\Local\\Programs\\Python\\Python37\\DLLs', 'C:\\Users\\73654\\AppData\\Local\\Programs\\Python\\Python37\\lib', 'C:\\Users\\73654\\AppData\\Local\\Programs\\Python\\Python37', 'C:\\Users\\73654\\PycharmProjects\\day01\\venv', 'C:\\Users\\73654\\PycharmProjects\\day01\\venv\\lib\\site-packages', 'C:\\Users\\73654\\AppData\\Roaming\\Python\\Python37\\site-packages', 'C:\\Users\\73654\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages', 'C:\\Users\\73654\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\win32', 'C:\\Users\\73654\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\win32\\lib', 'C:\\Users\\73654\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\Pythonwin', 'C:\\Program Files\\JetBrains\\PyCharm 2019.1.1\\helpers\\pycharm_matplotlib_backend']
```

以上是在Pycharm中输出结果

## 三、包

### 3.1 包的介绍

+ 通俗理解：包就是一个文件夹，只不过文件夹中有一个\_\_*init*\_\_.py文件
+ 包是管理模块的，模块是管理功能代码的

### 3.2 包的导入

| 导入模块方式                          | 导入包方式                                 | 类型     | 限定                                                     |
| ------------------------------------- | ------------------------------------------ | -------- | -------------------------------------------------------- |
| import 模块名 [as 别名]               | **import 包名.模块名 [as 别名]**           | 模块     |                                                          |
| from 模块名 import 功能代码 [as 别名] | form 包名.模块名 import 功能代码 [as 别名] | 功能代码 | 需要保证当前模块没有导入模块的功能代码                   |
| from 模块名 import *                  |                                            | 功能代码 | 可用\_\_all\_\_限定导入的功能代码                        |
|                                       | **from 包名 import 模块名 [as 别名]**      | 模块     |                                                          |
|                                       | from 包名 import *                         | 模块     | 必须在\_\_init\_\_.py用\_\_all\_\_限定可导入的模块       |
|                                       | import 包名                                |          | 直接导入包，不会导入对应的模块，需要在init文件中自己导入 |

## 四、pip的使用

从网上下载并安装 第三方 的 包

pip 默认针对Python2

pip3 是针对Python3

常用命令：

+ <code>pip3 list</code> 查看当前安装了哪些包
+ <code>pip3 uninstall xx</code> 删除xx包
+ <code>pip3 install xx</code> 安装xx包

辅助参数：

-i 指定源，国内的pip源如下：

阿里云 <http://mirrors.aliyun.com/pypi/simple/>

中国科技大学 [https://pypi.mirrors.ustc.edu.cn/simple/ ](https://pypi.mirrors.ustc.edu.cn/simple/ )

豆瓣(douban) <http://pypi.douban.com/simple/>

清华大学 <https://pypi.tuna.tsinghua.edu.cn/simple/>

中国科学技术大学 <http://pypi.mirrors.ustc.edu.cn/simple/>

## 五、IO包

### 5.1 StringIO

把数据临时写入到内容，不想存到文件的时候可用

```python
# 把字符串数据写入到内存
import io
# StringIO的操作 与 文件的写入和读取 很类似
str_io = io.StringIO()

# 向内存写入字符串数据
str_io.write("hello")
str_io.write("world")
# str_io.write("哈哈".encode("utf-8"))
# TypeError: string argument expected, got 'bytes'

# 获取数据
content = str_io.getvalue()
print(content)

# 设置文件指针的位置 到 文件开头
str_io.seek(0)
# 默认全部读取出来
result = str_io.read()
print(result)
```

### 5.2 ByteIO

```python
from io import BytesIO

byte_io = BytesIO()

# 向内存写入数据
byte_io.write("哈哈".encode("utf-8"))
# 读取数据，获取写入到内存中的全部数据
data = byte_io.getvalue()
print(data)

content = data.decode("utf-8")
print(content)
```

输出结果

```
b'\xe5\x93\x88\xe5\x93\x88'
哈哈
```

## 六、序列化与反序列化pickle

pickle 对于任何对象都通用，不论是json还是 普通的自定义对象

pickle 序列化后得到的是二进制数据，需要注意文件的访问模式

### 6.1 序列化

+ 把内存中的数据保存到本地，可以做到持久化存储

```python
import pickle

my_list = [{"name": "李四", "age": 20}, {"name": "王五", "age": 21}]
file = open("my_list.serialize", "wb")
pickle.dump(my_list, file)
file.close()
```

得到的数据如下：

```
�]q(}q(XnameqX李四qXageqKu}q(hX王五qhKue.
```

### 6.2 反序列化

把文件中的数据读取出来，得到保存的 Python对象

```python
import pickle

file = open("my_list.serialize", "rb")
my_list = pickle.load(file)

print(my_list)
file.close()
```

输出结果：

```
[{'name': '李四', 'age': 20}, {'name': '王五', 'age': 21}]
```

## 七、json序列化与反序列化

+ 只能支持部分数据类型，不通用。
+ 支持 列表、字典、int类型，自定义类型不可以
+ 以字符串的形式存储，而不是二进制数据

### 7.1 序列化

```python
import json
my_list = [{"name": "李四", "age": 20}, {"name": "王五", "age": 21}]
file = open("my_list.txt", "w", encoding="utf-8")
json.dump(my_list, file)
file.close()
```

文件中的数据如下：

```
[{"name": "\u674e\u56db", "age": 20}, {"name": "\u738b\u4e94", "age": 21}]
```

### 7.2 反序列化

```python
import json
file = open("my_list.txt", "r", encoding="utf-8")
my_list = json.load(file)
print(my_list)
file.close()
```

输出结果：

```
[{'name': '李四', 'age': 20}, {'name': '王五', 'age': 21}]
```

### 7.3 序列化对象的本质

+ 序列化对象的本质是 把 对象的属性进行保存
+ 用json没办法把对象序列化，只能序列化对象的\_\_dict\_\_

```python
import json


class Student(object):
    def __init__(self):
        self.name = "李四"
        self.age = 10


file = open("stu.txt", "w", encoding="utf-8")
stu = Student()
print(stu.__dict__)
json.dump(stu.__dict__, file)
file.close()
```

```python
[{"name": "\u674e\u56db", "age": 20}, {"name": "\u738b\u4e94", "age": 21}]
```

## 八、可迭代对象

### 8.1 可迭代对象简介

+ 可迭代对象 是 使用for循环遍历取值的对象
+ for循环可以直接遍历取值的对象：列表、元组、字典、字符串、集合、range

### 8.2 判断是否是可迭代对象

- 可以导入 <code>collections</code>包中 <code>Iterable</code>模块

  利用 <code>isinstance()</code> 方法判断是否是**指定类型**<code>Iterable</code>

```python
from collections.abc import Iterable
print(isinstance([1, 2], Iterable))  # True
```

> 注意：如果是from collections import Iterable会出现如下警告(Python 3.7.3rc1)
>
> DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated, and in 3.8 it will stop working
>   from collections import Iterable

+ 可迭代对象 都有一个 \_\_iter\_\_方法

  ```python
  result = dir([1, 2])
  print(result)
  ```

  ```
  ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
  ```

## 九、迭代器

### 9.1 迭代器简介

+ 迭代器：在类中有\_\_iter\_\_和\_\_next\_\_的方法 创建的对象 就是迭代器
+ 作用：记录数据的位置，并根据这个位置获取下一个值（取值）
+ 惰性取值，不会先把所有值生成好

### 9.2 自定义迭代器

自定义迭代器 类 如下：

```python
class MyIterator(object):
    def __init__(self):
        self.my_list = [4, 5, 19]
        self.current_index = 0

    def __iter__(self):
        # 返回迭代器对象
        return  self

    def __next__(self):
        if self.current_index < len(self.my_list):
            # 获取迭代器中的下一个值
            result = self.my_list[self.current_index]
            self.current_index += 1
            return result
        else:
            # 跑出停止迭代异常
            raise StopIteration("停止迭代！")
```

### 9.3 迭代器的遍历(迭代)

+ 手动next方式

  ```python
  # 创建迭代器
  my_iterator = MyIterator()
  # 使用next函数获取迭代器中的下一个值
  result = next(my_iterator)
  print(result) # 4
  
  result = next(my_iterator)
  print(result) # 5
  
  result = next(my_iterator)
  print(result) # 19
  """
  继续迭代会抛出异常……
  """
  ```

+ for循环 内部 会自动处理 停止迭代异常

  ```python
  # 创建迭代器
  my_iterator = MyIterator()
  # 使用next函数获取迭代器中的下一个值
  result = next(my_iterator)
  print(result) # 4
  
  for val in my_iterator:
      print(val) 
  """
  5
  19
  """
  ```

## 十、生成器

### 10.1 生成器简介

生成器是一个特殊的迭代器，根据一定的算法去生成数据。因此可用next函数和for循环取值

生成器和迭代器有一个共同的特点：节省内存

以往是 一次性 把所有数据都准备好，而它们则是 根据需要每次生成一个值

> 值只能 往后取，不能往前

### 10.2 生成器创建方式

#### 10.2.1 使用生成器表达式

跟列表生成器很类似，把[] 换成()即可

```python
result = [x for x in range(4)]
print(result) # [0, 1, 2, 3]
result = (x for x in range(4))
print(result) # <generator object <genexpr> at 0x7f3792369318>
```

#### 10.2.2 使用yield创建生成器

先看一段实例代码：

```python
def show_num():
    for i in range(5):
        return i

value = show_num()
print(value)
```

执行return的时候函数就结束了，只能返回0

把return改成yield就是生成器了

```python
def show_num():
    for i in range(5):
        yield i


g = show_num()
print(g)
for val in g:
    print(val)
```

输出结果：

```
0
1
2
3
4
```

+ yield特点：
  + 代码遇到yield会暂停，然后把结果返回出去
  + 下次启动生成器在暂停的位置继续往下执行
  + 可以返回多次值

```python
def show_num():
    for i in range(5):
        print("1111")
        yield i
        print("2222")

g = show_num()
print(next(g))
```

```
1111
0
```

```python
def show_num():
    for i in range(5):
        print("1111")
        yield i
        print("2222")

g = show_num()
print(next(g))
print(next(g))
```

```
1111
0
2222
1111
1
```



### 10.3 生成器遍历

同迭代器(next和for)

## 十一、线程

### 11.1 线程是什么

之前所学的代码无法完成多任务，没办法两个函数“同时"执行，以前的代码都只有一条线程，只能按照调用的先后顺序依次执行

+ 线程：执行代码的分支，默认程序只有一个线程
+ 线程执行是无序的，由CPU调度决定

```python
import time

def AA():
    for i in range(10):
        print(i, "aa")
        time.sleep(0.2)
def BB():
    for i in range(10):
        print(i, "bb")
        time.sleep(0.2)

if __name__ == '__main__':
    AA()
    BB()
```

上述代码会先执行AA()，执行完毕后才会去执行BB()

### 11.2 多线程的代码实现

+ 引入<code>threading</code> 模块
+ <code>Thread()</code>函数创建子线程，参数说明：
  + <code>target</code> 参数接收 目标函数
  + <code>daemon</code> 为True时，守护主线程
  + <code>args</code> 以元组形式给 目标函数传参
  + <code>kwargs</code> 以字典形式给 目标函数传参

+ <code>ThreadObject.start()</code> 启动线程，线程对应函数的代码才会执行

```python
import time
import threading

def AA(count):
    for i in range(count):
        print(i, "aa")
        time.sleep(0.2)

def BB(count):
    for i in range(count):
        print(i, "bb")
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子线程，执行对应的代码，target表示目标函数
    sub_thread1 = threading.Thread(target=AA, kwargs={"count": 3})
    sub_thread1.start()
    sub_thread2 = threading.Thread(target=BB, args=(3,))
    sub_thread2.start()
```

示例输出（多线程输出结果不确定）：

```py
0 aa
0 bb
1 aa
1 bb
2 bb
2 aa
```

### 11.3 守护线程

+ 默认情况下，主线程会等待所有的子线程执行完成以后再退出

  + 如果是子线程中有死循环，主线程不会退出

  ```python
  import time
  import threading
  
  def AA(count):
      print("AA:", threading.current_thread())
      for i in range(count):
          print(i, "aa")
          time.sleep(0.2)
  
  if __name__ == '__main__':
      print("main:", threading.current_thread())
      t1 = threading.Thread(target=AA, kwargs={"count": 3})
      t1.start()
  
      print("over")
  ```

  ```
  main: <_MainThread(MainThread, started 140719848908608)>
  AA: <Thread(Thread-1, started 140719843464960)>
  0 aa
  over
  1 aa
  2 aa
  ```

+ 设置守护线程

  + 主线程退出的时候，子线程直接销毁，不再执行对应的代码

  ```python
  t1 = threading.Thread(target=AA, kwargs={"count": 3})
  t1.setDaemon(True)
  t1.start()
  
  time.sleep(1)
  print("over")
  ```

  ```
  0 aa
  1 aa
  2 aa
  over
  ```

  除了用setDaemon(True) 的方式外，还可以

  在创建线程的时候，传入Daemon参数达到守护线程的目的

### 11.4 互斥锁

先观察下面的代码：

```python
import threading
g_num = 0
def AA():
    global g_num
    for i in range(1000000):
        g_num += 1
    print("AA:", g_num)

def BB():
    global g_num
    for i in range(1000000):
        g_num += 1
    print("BB:", g_num)

if __name__ == '__main__':
    # 创建两个线程
    first_thread = threading.Thread(target=AA)
    second_thread = threading.Thread(target=BB)
    
    first_thread.start()
    second_thread.start()
```

输出结果不确定

```
BB: 1385465
AA: 1545123
```

```
AA: 1550914
BB: 1565660
```

……

两个线程同时对 同一个全局变量 操作 出现了资源竞争问题，可以用互斥锁解决

```python
import threading
g_num = 0
# 创建互斥锁
lock = threading.Lock()

def AA():
    # 上锁
    lock.acquire()
    global g_num
    for i in range(1000000):
        g_num += 1
    print("AA:", g_num)
    # 释放锁
    lock.release()

def BB():
    # 上锁
    lock.acquire()
    global g_num
    for i in range(1000000):
        g_num += 1
    print("BB:", g_num)
    # 释放锁
    lock.release()

if __name__ == '__main__':
    # 创建两个线程
    first_thread = threading.Thread(target=AA)
    second_thread = threading.Thread(target=BB)

    first_thread.start()
    second_thread.start()
```

输出结果：

```
AA: 1000000
BB: 2000000
```

> 注：视频在此位置有 跳跃，一段视频消失了……

> GIL 全局解释器锁：CPython内置
>
> Python的多线程不是真正意义上的多线程，没办法让两个线程"同时"执行，Python解释器会让某一线程先执行（上锁），其他线程等待一小段时间（释放锁）

## 十二、进程

### 12.1 进程是什么

+ 进程：每次创建一个进程，操作系统会给这个进程分配对应的运行资源，一个进程里面默认有一个线程
+ 真正干活的是线程，进程只提供资源
+ 使用进程也可以完成多任务

### 12.2 进程的代码实现

大体上跟 线程 类似

```python
import multiprocessing
import time

def show():
    for i in range(5):
        print("show")
        time.sleep(0.1)

def show1():
    for i in range(5):
        print("show1")
        time.sleep(0.1)

if __name__ == '__main__':
    # 创建子进程
    first = multiprocessing.Process(target=show)
    second = multiprocessing.Process(target=show1)

    # 启动进程执行任务
    first.start()
    second.start()
```

### 12.3 在主进程终止子进程

+ 默认情况下，主进程会等到子进程执行完成后再退出（同线程）

1.  让子进程终止，销毁子进程

   ```python
   sub_process.terminate()
   ```

2. 设置守护进程（同线程）

### 12.4 共享全局变量问题

进程之间是相互独立的，只是变量名相同而已，不会共享全局变量的数据

子进程会对主进程的资源进行拷贝

```python
import multiprocessing
my_list = []
def add_data():
    for i in range(3):
        my_list.append(i)
    
    print("add_data:", my_list)

def read_data():
    print("read:", my_list)

if __name__ == '__main__':
    # 创建两个子进程
    add_process = multiprocessing.Process(target=add_data)
    read_process = multiprocessing.Process(target=read_data)
    
    # 启动进程执行任务
    add_process.start()
    # 进程等待，主进程等待子进程执行完，再让后边的代码执行
    add_process.join()
    read_process.start()
```

```
add_data: [0, 1, 2]
read: []
```

### 12.5 进程之间的通信方式

#### 12.5.1 消息队列

+ 消息队列的 添加和获取数据
  + <code>Queue()</code> 创建空队列，容量默认为任意多个，可以指定

```python
import multiprocessing

# 创建消息队列
queue = multiprocessing.Queue(3)

# 往队列添加数据
queue.put(1)
queue.put(2)
queue.put(3)

# 从队列中获取数据
print(queue.get())
```

+ 用消息队列实现在 进程之间共享数据
  + 创建一个队列
  + 以参数的形式传到各个进程

```python
import multiprocessing

def add_data(queue):
    for i in range(3):
        print("add:", i)
        queue.put(i)

def read_data(queue):
    while True:
        if queue.empty():
            break
        value = queue.get()
        print("get:", value)

if __name__ == '__main__':
    queue = multiprocessing.Queue(3)
    # 创建两个子进程
    add_process = multiprocessing.Process(target=add_data, args=(queue,))
    read_process = multiprocessing.Process(target=read_data, args=(queue,))

    # 启动进程执行任务
    add_process.start()
    # 进程等待，主进程等待子进程执行完，再让后边的代码执行
    add_process.join()
    read_process.start()
```

 #### 12.5.2 管道





> 多任务：使用线程和进程
>
> 从资源角度来说，线程更加节省资源，进程消耗资源较多
>
> 从代码稳定性来说，多进程比多线程稳定性要强，因为一个进程挂掉不会影响其他进程



































