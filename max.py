x = []
num = int(input("enter number of elements in the list: "))

for i in range(num):
    element = input("enter a number: ")
    x.append(element)
maximum_value = x[0]
for i in range(1, len(x)):
    if x[i] > maximum_value:
        maximum_value = x[i]
print(maximum_value)
