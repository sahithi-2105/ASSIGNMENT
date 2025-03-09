def removeDuplicates(n):  

    if len(n) <= 1:
        return len(n)
    i = 0  
    for j in range(1, len(n)):
        if n[i] != n[j]:
            i += 1
            n[i] = n[j]  

    return i + 1,n[:i+1] 

n = list(map(int, input().split()))  
result,unique_numbers= removeDuplicates(n) 
print(result,unique_numbers)   