

def fuc(num: int):
    e = 1
    for i in range(1, num + 1):
        e *= i
    return e

print(fuc(3))
