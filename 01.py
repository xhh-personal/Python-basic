my_str = 'hello'
print(my_str.index('e'))
print(my_str.find('h'))
# print(my_str.index('f'))
print(my_str.find('x'))
print(len(my_str))
print(my_str.count('l'))
print(my_str.replace('l','x'))
my_str = '百度,阿里,华为'
print(my_str.split(','))
my_url = "https://www.baidu.com"
print(my_url.startswith('https'))
print(my_url.endswith('com'))

my_str = 'aaabbcccc'
print(my_str.partition('bb'))