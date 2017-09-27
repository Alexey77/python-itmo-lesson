#pep8

print ('Hello')
ame = input ('Name - ')
print ('Hello', name, '!')

"""
Скалярные типа данных
в один момент может хранить только 1-о значение

bool
int
float
str




# int
i1 = 777
i2 = 0x59 # шестнадцатеричная
i3 = 0b1010101001 # двоичная
i4 = 0o255 #восмеричная

#float
f1 = 1.23
f2 = 12e-3 # 12 * 10^-3
f3 = 12e3 # 12 * 10^3
# bytes - байтовая строка
s5 = b'Bytes string'
"""
#str
s1 = 'Some string'
s2 = "Some string"
s3 = r'Raw strin' # сырtые строки
s4 = u'Hello' #unicode

s6 = """
многострочная
строка
"""

# Структурированные (сложные)
# tuple, list, set, dict, object

# Кортежи - tuple
t1 = (1,)
t2 = (True, 1, 1.2, 'string', (1, 2, 3))

# Списки list
l1 = [[1], [2], 3, False]

# Множества - set
set1 = {1, 2, 3}
set2 = set () #пустое множество

'''
Элементы в множестве не повторяются
остаются только уникальные данные
'''

# Словари - dict
d = {
    'id':1,

}

# Специальные типы:
a = None
