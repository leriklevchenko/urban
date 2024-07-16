immutable_var = (1, 2, 3, 4, True)
print(immutable_var)
# immutable_var [0] = 3
# print(immutable_var)
# нельзя заменить изменения кортежа т.к. он является неизменяемым списком

mutable_list = ([1, 2, 3, 4],5,True)
mutable_list [0][2] = 6
print(mutable_list)
