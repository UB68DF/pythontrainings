#list comprehension

list = []
for letter in 'word':
    list.append(letter)
print(list)
print('\n')

list = [letter for  letter in 'word']
print(list)
print('\n')

list1 = [x**3 for x in range(1,11)]
print(list1)

print('\n')
list2 = [number for number in range(1,11) if number%2 == 1]
print(list2)

celsius = [-10,-5,0, 10, 20,40,50,60,70,100]
farenhiet = [((number*9/5.0) + 32) for number in celsius]
print(farenhiet)




