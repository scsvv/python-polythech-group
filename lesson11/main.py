import io
'''
read 
'''


name = list()

with open(r"file.txt", 'r') as outf:
    
    while True:
        line = outf.readline()
        if not line:
            break
        name.append(line)

print(name)