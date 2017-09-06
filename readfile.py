f = open('a.txt')
f.seek(0)
readText = f.read()
# Readline keeps entire file in memory and is not suitable for large files
readLines = f.readline()
print(readText)
print('\n')
print(readText)
print('\n')
for line in open('a.txt'):
    print (line + "printed..")

