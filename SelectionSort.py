
ar=[1000,45,78,32]
n=len(ar)
for i in range(n-1):
    min_val=i
    for j in range(i+1,n):
        if ar[j]< ar[min_val]:
            min_val=j
    ar[i],ar[min_val]=ar[min_val],ar[i]
print("sorted_arrays",ar)
