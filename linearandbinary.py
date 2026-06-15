# C. Linear Search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# D. Binary Search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# --- User Input Section ---

# 1. Get the array from the user (separated by spaces)
user_array_input = input("Enter numbers separated by spaces: ")

# Convert the string input into a list of integers
# .split() breaks "11 12 22" into ['11', '12', '22']
# int(x) converts each string into an integer
search_list = [int(x) for x in user_array_input.split()]

# 2. Get the target value from the user
target = int(input("Enter the target number to search for: "))

# --- CRITICAL STEP FOR BINARY SEARCH ---
# Binary search ONLY works on sorted arrays. 
# We sort the list here just in case the user entered it out of order.
search_list.sort()

# --- Testing the searching implementations ---
print("\n--- Results ---")
print("Sorted Array:", search_list, "| Target:", target)
print("Linear Search Index:", linear_search(search_list, target))
print("Binary Search Index:", binary_search(search_list, target))
