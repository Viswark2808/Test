list1= [x**2 for x in range(1, 11)]
print(list1)

print("--------------------------------")

arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)


for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr) 
