def fatorial(n):
    if n < 1:
        return 1
    return n * fatorial(n - 1)

num = int(input())
print(fatorial(num))