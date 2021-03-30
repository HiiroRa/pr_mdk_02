def h(n, start, finich):
    if n == 1:
        print(1, start, finich)
    else:
        tmp = 6 - start - finich
        h(n - 1, start, tmp)
        print(n, start, finich)
        h(n - 1, tmp, finich)
n =int(input())
h(n, 1, 3)