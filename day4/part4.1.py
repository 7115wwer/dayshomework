import hashlib
a = open('input.txt', 'r'). read()
file = open('output1.txt', 'w+')
for i in range (10000000000000000000000) :
    b = a + str(i)
    c = hashlib.md5(b.encode('utf-8')).hexdigest()
    if c.startswith ('00000') :
        break
file.write(str(i))
file.close ()