no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    items = ""
    result = 0
    n = int(input())
    if n == 2:
        print("NO")
    else:
        count = n // 2
        for i in range(1,count+1):
            items += str(2*i) + " "
            result += (2*i)
        i = 1
        while count > 1:
            items += str(i) + " "
            result -= i
            i += 2
            count -= 1

        if result % 2 != 0:
            items += str(result) + " "
            print("YES")
            print(items.strip())
        else:
            print("NO")
