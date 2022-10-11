from winreg import REG_NOTIFY_CHANGE_SECURITY


count = 0

def binarySearch(arr, left, right, val):
 
    while left <= right:
 
        mid = (left+ right) // 2       # // means floor division
        
        # alternate way to avoid overflow in some languages
        # mid = left + (right - left) // 2          
 
        #counting how many comparisons have been made
        global count
        count += 1
        
        # Check if val is the middle one
        if arr[mid] == val:
            return mid
 
        # If val is greater, consider only the upper half
        elif arr[mid] < val:
            left = mid +1
 
        # If val is smaller, ignore only the lower half
        else:
            right = mid -1
  
    #reaching here means value not found, return -1 to indicate not found
    return -1
 
 
# Main program
#arr =  [1,10,35,62,70,81,90,93,95,100]
arr = [1, 2, 3, 4, 10, 20, 25, 30, 40, 45, 55, 60, 75, 80, 99, 100]
#arr = [1, 2, 3, 4, 10, 20, 25, 30, 40, 45, 55, 60, 75, 80, 99, 100, 101, 102, 105, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230]

print(arr)

to_find = int(input('Input a number to search for: '))

result = binarySearch(arr, 0, len(arr)-1, to_find)
 
if result != -1:
    print(f'Value {to_find} found at index {result}')
else:
    print('Value not found')

print(f'Comparision count: {count}')
