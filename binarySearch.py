l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

arr = list(map(int, input("Enter a list (leave empty for default) : ").split()))
key = int(input("Enter the element to be searched : "))
if (len(arr) < 1):
    arr = l

def binarySearch(arr, key):
    high = len(arr) - 1
    low = 0 
    while (low <= high):
        mid = (high+low)//2
        if (key < arr[mid]):
            high = mid - 1
            mid = (high+low)//2
        elif (key > arr[mid]):
            low = mid + 1
            mid = (high+low)//2
        else :
            return(mid)

result = binarySearch(arr,key)
if (result == None):
    print("Element not found in list.")
    exit()
print ("Element found.")

