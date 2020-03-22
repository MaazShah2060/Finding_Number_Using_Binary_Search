import time
import random
import os
y = int(input("Enter a number: "))
x = random.randrange(0,2)
rand_list = []
low = 0
index = -1
while(x<=100):
    index = index + 1
    rand_list.append(x)
    x = x+2
high = index
def search(arr,l,h,s):
    if (h%2!=0 and l<=h):
        mid = int((l + h)//2)
        if (arr[mid] == s):
            return mid
        elif(arr[mid] > s):
            return search(rand_list,l,mid-1,s)
        else:
            return search(rand_list,mid+1,h,s)
    elif(h%2==0 and l<=h):
        mid1 = int(((l+h) / 2))
        mid2=int(((l+h)+2)/2)
        if(arr[mid1] == s):
            return mid1
        elif(arr[mid2] == s):
            return mid2
        elif(arr[mid1] > s):
            return search(rand_list,l,mid1-1,s)
        else:
            return search(rand_list,mid2+1,h,s)
    else:
        return -1
b = search(rand_list,low,high,y)
if b != -1:
    print("Element is present at index: ", b)
else:
    print("Element not in array")
input("Press Enter to exit...")
