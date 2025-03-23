# Algoritmo Recursivo
def barajar_recursivo(X, Y, Z, i, j, k):
    if k == len(Z):
        return True
    if i < len(X) and X[i] == Z[k]:
        if barajar_recursivo(X, Y, Z, i + 1, j, k + 1):
            return True
    if j < len(Y) and Y[j] == Z[k]:
        if barajar_recursivo(X, Y, Z, i, j + 1, k + 1):
            return True
    return False

# Algoritmo Memoizado
def barajar_memoizado(X, Y, Z, i, j, k, memo):
    if k == len(Z):
        return True
    if (i, j, k) in memo:
        return memo[(i, j, k)]
    if i < len(X) and X[i] == Z[k]:
        if barajar_memoizado(X, Y, Z, i + 1, j, k + 1, memo):
            memo[(i, j, k)] = True
            return True
    if j < len(Y) and Y[j] == Z[k]:
        if barajar_memoizado(X, Y, Z, i, j + 1, k + 1, memo):
            memo[(i, j, k)] = True
            return True
    memo[(i, j, k)] = False
    return False

# Algoritmo Bottom-Up
def barajar_bottom_up(X, Y, Z):
    n, m = len(X), len(Y)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] and X[i - 1] == Z[i - 1]
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] and Y[j - 1] == Z[j - 1]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = (dp[i - 1][j] and X[i - 1] == Z[i + j - 1]) or (dp[i][j - 1] and Y[j - 1] == Z[i + j - 1])
    
    return dp[n][m]

# Ejemplo de uso:
X = ['A', 'B']
Y = ['C', 'D']
Z = ['A', 'C', 'B', 'D']

print(barajar_recursivo(X, Y, Z, 0, 0, 0))
memo = {}
print(barajar_memoizado(X, Y, Z, 0, 0, 0, memo))
print(barajar_bottom_up(X, Y, Z))
