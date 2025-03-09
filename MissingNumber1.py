def missingNumber(n):
    
    total_sum = (len(n) * (len(n) + 1)) // 2
    actual_sum = sum(n)

    return total_sum - actual_sum

n = list(map(int, input().split()))

result = missingNumber(n)

print(result)