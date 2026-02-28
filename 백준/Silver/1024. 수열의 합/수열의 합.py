N, L = map(int, input().split())

result = None
# 백준 1024 조건: 수열 길이는 L 이상, 100 이하
for k in range(L, 101):  # k: L ~ 100
    num = N - k * (k - 1) // 2
    if num < 0:
        break
    if num % k == 0:
        a = num // k
        if a < 0:
            continue
        result = list(range(a, a + k))
        break

if result is None:
    print(-1)
else:
    print(*result)