def missingNumber(n):
    sorted_list = sorted(n)

    for i in range(len(sorted_list)):
        if sorted_list[i] != i:
            return i

    return len(n)

n = list(map(int, input().split()))

result = missingNumber(n)

print(result)