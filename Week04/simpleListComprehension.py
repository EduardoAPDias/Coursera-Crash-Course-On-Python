print("List comprehension result:")

print([x*2 for x in range(1,11)])

print("Long form code result:")

my_list = []
for x in range(1,11):
    my_list.append(x*2)
print(my_list)

