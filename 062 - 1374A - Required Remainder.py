no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    x, y, n = map(int, input().split())
    if (n - (n%x) + y) <= n:
        print(n - (n%x) + y)
    else:
        print(n - (n%x) - (x-y))
