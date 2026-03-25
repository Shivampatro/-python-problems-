def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

while True:
    ch = input()
    if ch == '5':
        break
    a = float(input())
    b = float(input())
    if ch == '1':
        print(add(a, b))
    elif ch == '2':
        print(sub(a, b))
    elif ch == '3':
        print(mul(a, b))
    elif ch == '4':
        print(div(a, b))