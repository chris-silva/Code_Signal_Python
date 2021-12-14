def constructShell(n):
    return [[0 for i in range(j % n + 1)] for j in range((n*2-1) // 2)] + [[0 for i in range(n)]] + [[0 for i in range((n*2-1) // 2 - j)] for j in range((n*2-1) // 2)]


print(constructShell(3))
