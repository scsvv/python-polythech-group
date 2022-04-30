x = 1/0

'''
try: 
    x = 1/0
except ArithmeticError:
    print(f"Handle error: {ArithmeticError}")
'''

a = input()
b = input()

try: 
    z = int(a) + int(b)
    print("try")
except:
    print("Bad news")
    z = 0 
finally:
    print("finally")

print(z)
