x = []
num = int(input("enter number of elements in the list: "))

for i in range(num):
    element = input("enter a number: ")
    x.append(element)
x.sort()
print(x[len(x)-1])