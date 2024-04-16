# for i in range(2,10):
#     for j in range(2,10):
#         print(f"{i}+{j}={i+j}",end=" ")
#     print()
#
# for i in range(2,10):
#     for j in range(2,10):
#         print(f"{i}-{j}={i-j}",end=" ")
#     print()

# for i in range(2,10):
#     for j in range(2,10):
#         print(f"{i}*{j}={i*j}",end=" ")
#     print()
#
# for i in range(2,10):
#     for j in range(2,10):
#         print(f"{i}/{j}={i/j}",end=" ")
#     print()

# minus = {}
# for i in range(2,10):
#     for j in range(2,10):
#         minus=(f"{i}-{j}={i-j}")
#
# print(minus)
#

addition_table = {}
#
# Заповнення таблиці додавання
for i in range(2, 10):
    for j in range(2, 10):
        addition_table[(i, j)] = i + j

# Виведення змінної з таблицею додавання
print(addition_table)
