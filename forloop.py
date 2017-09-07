#for loop

l = [1,2,3,4,5]
for  num in l:
    if num % 2 == 0:
        print("even number ->"+str(num))
    else:
        print("odd number ->"+str(num))

y = [1,1,1,2,3,3,2,4,5,4,5]
x = set(y)
list_sum = 0
for num1 in x:
    list_sum = list_sum + num1

print(list_sum)
print('\n')

# looping tuples
l2= [(1,2),(4,5),(9,10)]
for tup in l2:
    print(tup)
    for x in tup:
        print(x)

print('\n')
for (t1,t2) in l2:
    print(t2)
print('\n')

d = {'a':1,'b':2,'c':3}
for (k1,k2) in d.items():
    print(k2)

print('\n')
#range and xrange
for num in range(1,6):
    print(num)
print('\n')
print(type(range(1,6)))





