ar=[1,2,6,10,5]
min_val=ar[0]
max_val=ar[0]
for i in ar:
    if i <min_val:
        min_val=i
for i in ar:
    if i> max_val:
        max_val=i
print(min_val)
print(max_val)
