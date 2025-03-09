def removeDuplicates(n):
    s = set(n)
    unique_numbers = list(s)
    return len(unique_numbers), unique_numbers
n = list(map(int, input().split()))
result, unique_numbers = removeDuplicates(n)
print(result, unique_numbers)