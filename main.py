def fibonacci(index):
    a = 0
    b = 1
    tmp = 0

    for x in range(index):
        tmp = a + b
        a = b
        b = tmp
    return tmp


fibonacci(10)
