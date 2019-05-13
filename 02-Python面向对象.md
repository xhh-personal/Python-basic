# Python面向对象

## 01- 面向对象和面向过程

都是开发程序的模式

+ 面向过程是 自己按照实现过程的步骤，完成功能的开发
+ 面对对象是 程序员找一个功能对象，功能对象里边提供功能方法，程序员只负责调度，不关心具体实现

## 02- 类和对象的介绍

+ 类：事或者物一个分类
+ 对象：具体到某一个事或者物

## 03- 类的定义

+ 需要用class关键字
+ 类中有 属性(特征) 方法(行为)

```python
# 定义学生类，这是旧式类
# Python2 中无父类
# Python3 中 旧式类 默认集成object
class Student:
    # 属性
    country = "China"
    # 方法
    def show(self):
        print("我是学生")
# 通过类创建对象
stu = Student()
stu.show()

print(Student.__bases__) # (<class 'object'>,)
```

新式类，即主动指定继承的父类

```python
class Student(object):
    country = "China"
    def show(self):
        pass
```

## 04- 给对象添加属性信息

Python对象创建后可以动态的添加属性……

```python
class Student(object):
    def show(self):
        print("Hello")
# 创建对象
stu = Student()
# 动态添加对象属性
stu.name = "zhangsan"
stu.age = 18

# 获取对象属性
print(stu.name, stu.age)

# 修改对象属性
stu.name = "wangwu"
print(stu.name, stu.age)
```

每次这样手动添加会比较复杂，用5.1方法可以解决

## 05- 魔法方法

+ 魔法方法：当需要完成某个功能操作的时候会自动调用某个方法
+ 表现形式：\_\_ 开始和结束

### 5.1 \_\_*init*\_\_ 

+ 作用：对象创建完成会调用此方法，给对象初始化，添加属性

```python
class Student(object):
    def __init__(self, name, age):
        # self 表示当前对象
        #
        self.name = name
        self.age = age
        print("__init__ called")
    def show_info(self):
        print(self.name, self.age)
# 创建对象
stu1 = Student("zhangsan", 18)
stu1.show_info()
stu2 = Student("lisi", 20)
stu2.show_info()
```

### 5.2 \_\_str\_\_

+ 作用：使用print打印对象的时候会自动调用
+ 需要返回字符串

```python
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        # 返回一个字符串信息
        return "我叫%s 年龄%d" % (self.name, self.age)
# 创建对象
stu1 = Student("zhangsan", 18)
print(stu1)
stu2 = Student("lisi", 20)
print(stu2)
```

### 5.3 \_\_del\_\_ 

+ 作用：当对象释放的时候会自动调用

+ 调用的时机：
  + 程序退出，程序中所使用的对象全部销毁
  + 当前对象的内存地址没有变量使用的时候会销毁
    + del 手动删除
    + 引用计数机制

```python
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 当对象引用计数为0的时候调用
    def __del__(self):
        print("object is killed:", self)
# 创建对象
stu1 = Student("zhangsan", 18)
print(stu1) # <__main__.Student object at 0x00000220AE3454E0>
stu2 = stu1
del stu1
del stu2
# object is killed: <__main__.Student object at 0x00000220AE3454E0>
```

### 5.4 \_\_new\_\_

+ 作用：当 创建对象的时候会调用

>创建对象会自动调用两个方法，先new表示对象创建完成再init对对象进行初始化

```python
class Student(object):
    # new方法里边的参数 是 需要兼容init方法 的参数,因此才会有*args, **kwargs
    # TypeError: __new__() takes 1 positional argument but 3 were given
    def __new__(cls, *args, **kwargs):
        print("创建对象")
        return object.__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("初始化对象")

stu = Student("zs", 20)
```



## 06- 继承

+ 子类继承父类，可以使用父类的属性和方法
+ 

### 6.1 单继承

+ 子类只继承一个父类

![1557370745487](C:\Users\73654\Documents\Study_Folder\Test\Python学习笔记\1557370696885.png)

![1557370786341](C:\Users\73654\Documents\Study_Folder\Test\Python学习笔记\2.png)

### 6.2 多继承

+ 相当于继承多个父类
+ Python方法的调用会遵循mro，类继承顺序，决定了方法调用时候的查找顺序
+ 调用类的mro方法可以查看类继承顺序

### 6.3 重写父类方法

+ 重写：子类继承父类，父类的方法满足不了子类的需要，可以对父类的方法进行重写
+ 子类调用方法的时候先从本类查找，如果没有再去父类，遵循mro的特点
+ 特点：
  + 继承关系
  + 方法名相同

### 6.4 调用父类的方法

#### 6.4.1 一般方法

+ 当前类里边没有父类的方法时

  + self.method()
  + 如果有则调用当前类的方法

+ 当前类复写了父类相同方法时

  + 父类类名.method(self)

    + 必须手动传递self

  + super(类名, self).method()

    + 根据指定类，在类继承链中获取下一个类
    + 类名，表示根据这个类 找 类继承链 中获取下一个类
    + self 表示获取self对象类型的类继承链
    + super不一定是直接继承的父类
      + 单继承理解成父类没问题
      + 多继承需要看 继承链
    + 用Super更加通用，但跟其他语言的super含义不一样

    > 在self继承链中，返回 类名的下一个类

#### 6.4.2 调用父类 \_\_*init*\_\_ 方法

如果子类提供了方法，需要父类的相同方法时，才需要调用super

+ <code>self.\_\_init\_\_(param)</code>  不可取
+ 父类类名.\_\_init\_\_(self, param)
+ <code>super(父类, self)._\_init\_\_(param)</code>
  + 参数可省略<code>super()._\_init\_\_(param)</code>

#### 6.4.3 重写父类中使用super

![1557372784039](C:\Users\73654\Documents\Study_Folder\Test\Python学习笔记\3)

### 07- 私有属性和私有方法

+ 在属性名和方法名**前面**加上'\_\_'  就是私有的
+ 私有属性外界无法访问，只能在本类中使用
+ 只能在\_\_*init*\_\_ 中添加
+ 在Python中 私有xx没有做到绝对私有，只是把xx进行了一个名字的伪装

```python
class Person(object):
    def __init__(self, name, age):
        # 公共属性
        self.name = name
        # 私有属性,只能在本类内部使用，在类外部不能使用
        # 只能在__init__中添加私有属性
        self.__age = age
    def show(self):
        print(self.name)
    def __money(self):
        print("100W")
person = Person("zhangsan", 20)
print(person.name)
# 私有属性外界访问不了
# print(person.__age)
# person.__money()

# 查看对象中的属性信息
print(person.__dict__)

# 本意是修改私有属性
# 这里不是修改了私有属性，而是动态添加了一个__age对象属性
# 提示:这里也不是添加的私有属性，只能在__init__中添加
person.__age = 22
print(person.__age)
print(person.__dict__)

# 不是绝对的私有, 以下操作 不是常规操作，不建议这样使用
print(person._Person__age) # 20
person._Person__money() # 100W
```

> 注：子类继承父类，不能直接使用父类的私有属性和私有方法

## 08- 类属性和实例属性

+ **类属性**是在 方法外 和 类内部 定义的属性
  + 类和对象都能访问
  + 只能通过类进行修改
  + 对象修改 仅仅是添加了一个对象属性，不是真正的修改
+ **实例属性**是在init方法里 定义的属性
  + 只能通过对象访问，修改

```python
class Person:
    # 类属性
    type = "黄种人"
    def __init__(self, name, age):
        # 实例(对象)属性
        self.name = name
        self.age = age
# ------- 类属性操作 -------
# 访问类属性
print(Person.type) # 黄种人
# 不能使用类访问 对象属性
# print(Person.age)
# AttributeError: type object 'Person' has no attribute 'age'

# 修改类属性
Person.type = "白种人"
print(Person.type)

# ------- 对象属性操作 -------
person = Person("zhangsan", 20)
print(person.name, person.age)
print(person.type)
```

> 总结：类属性的操作由类完成，对象属性的操作由实例完成，对象可以访问类属性，不能修改
>
> 同样，可以定义 私有类属性

## 09- 类方法和静态方法

```python
class Person(object):
    # 私有类属性
    __type = '黄种人'
    # 定义对象方法
    def show(self):
        print("我是人类_对象方法")

    # 定义类方法：cls表示当前类
    @classmethod
    def show_info(cls):
        print(cls)
        print("class method called")

    # 定义静态方法：与当前对象、当前类都没有关系。不会使用cls和self
    @staticmethod
    def show_msg():
        print("static method called")

    # 类方法可以修改类属性
    @classmethod
    def set_type(cls, type):
        cls.__type = type

    @classmethod
    def get_type(cls):
        return cls.__type
    # ------ 对象方法是最通用的方法，可以修改对象属性 和 类属性
    def instance_set_type(self, type):
        # 对象方法修改类属性，需要获取对象所对应的类
        self.__class__.__type = type

    def instance_get_type(self):
        return self.__class__.__type
p = Person()
p.show()
p.show_info()
p.show_msg()
p.set_type("白种人")
print(p.get_type())

p.instance_set_type("黑种人")
print(p.instance_get_type())
```

|      | 对象方法 | 类方法 | 静态方法 |
| ---- | -------- | ------ | -------- |
| 对象 | √        | √      | √        |
| 类   | 传入实例 | √      | √        |

|          | 对象属性 | 类属性            |
| -------- | -------- | ----------------- |
| 对象方法 | √        | obj.\_\_class\_\_ |
| 类方法   | ×        | √                 |
| 静态方法 | ×        | ×                 |

## 10- 多态

严格意义上讲，Python中并无多态，在其他面向对象语言中，多态要关心类型……

+ 关注的是 **同一个方法**，但是会出现不同的表现形式
+ Python中不需要关心类型

```python
class Text():
    def show(self):
        print("显示文字")

class Image():
    def show(self):
        print("显示图像")

class Video():
    def show(self):
        print("显示视频")

def show_data(data):
    # 多态：关心的是同一个方法，会出现不同的表现形式
    # Python中多态：只关心对象的方法，不关心对象的类型
    data.show()
    # 传入的对象必须都有show方法才行！

txt = Text()
img = Image()
video = Video()

show_data(txt)
show_data(img)
show_data(video)
```

## 11- 单例

+ 在APP中不管创建多少次对象，只有一个实例对象

在传统方式下，创建多个对象，他们的地址不一样

```python
class Student(object):
    def __new__(cls, *args, **kwargs):
        print("创建对象")
        return object.__new__(cls)

    def __init__(self):
        print("初始化对象")

stu1 = Student()
stu2 = Student()
# 两个对象的地址不一样
print(stu1, stu2)
```

单例要求，不管创建多少次对象，这些对象的内存地址都一样，需要在new方法中控制：

如果对象已经存在，就直接返回之前创建的对象；

如果要记录这个对象，必须是类属性

```python
class Student(object):

    # 私有类属性
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            print("创建对象")
            # 把创建的对象 给 类属性
            cls.__instance =  object.__new__(cls)
        return cls.__instance

    def __init__(self, name, age):
        print("初始化对象")
        self.name = name
        self.age = age

stu1 = Student("zs", 20)
print(stu1.__dict__) # {'name': 'zs', 'age': 20}
stu2 = Student('ss', 15)
print(stu1.__dict__) # {'name': 'ss', 'age': 15}
print(stu2.__dict__) # {'name': 'ss', 'age': 15}
# 两个对象的地址一样
print(stu1, stu2)
```

## 12- 面向对象高级编程

### 12.1 \_\_slots\_\_

+ 指明创建对象的时候不能再添加其他属性，只能是指定的属性
+ 好处：可以让对象的属性固定
+ 注意：加上后必须在init函数中加入相应初始化操作

```python
class Student(object):
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age

stu = Student("zhangsan", 18)
# stu.sex = '女'
# AttributeError: 'Student' object has no attribute 'sex'
print(stu.name, stu.age)
stu.name = 'lisi'
print(stu.name, stu.age)
```

### 12.2 @property

先观察下列代码：

```python
class Student(object):
    # __slots__ = ("name", "age")

    def __init__(self):
        self.__score = 100

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

stu = Student()
score = stu.get_score()
print(score) # 100

stu.set_score(99)
score = stu.get_score()
print(score) # 99
```

现在有一种需求，在设置值的时候不想通过函数的方式进行传值，而是像类似于下面的操作

<code>stu.set_score = 99</code>

可以进行如下操作来实现：

1.  在获取值的方法前加入 @property
2.  在设置值的方法前 @get_method.setter

这样操作后，被处理后的方法就变成了属性

此时不能用函数的方法进行设置和获取，会报错 <code>TypeError: 'int' object is not callable</code> 

```python
class Student(object):
    def __init__(self):
        self.__score = 100

    @property
    def get_score(self):
        return self.__score

    @get_score.setter
    def set_score(self, score):
        self.__score = score
stu = Student()
score = stu.get_score
print(score)

stu.set_score = 99
score = stu.get_score
print(score)
```

