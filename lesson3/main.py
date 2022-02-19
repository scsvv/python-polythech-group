a = 1
b = 1
c = 0
while c < 100:
    c = a + b
    if c > 100:
        break
    print(c)
    a = b 
    b = c

print("------------------------------------")
a = 1
b = 1
c = 0
for i in range(15):
    c = a + b
    print(c)
    a = b 
    b = c
