my_dict = {'Дима': 2002, 'Катя': 2001, 'Настя': 2003}
print (my_dict)
print (my_dict ['Катя'])
print (my_dict.get('Антон'))
my_dict.update({'Эдуард': 2000, 'Глеб': 1999})
x = my_dict.pop('Дима')
print(x)
print (my_dict)

# 3
my_set = {1, 2, 'a', 'b', 1, 'c', 2}
print(my_set)
my_set.add(3)
my_set.add('d')
my_set.remove('a')
print(my_set)
