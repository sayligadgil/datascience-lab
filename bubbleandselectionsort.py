# A. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    a = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                # Swap elements
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# B. Selection Sort
def selection_sort(arr):
    n = len(arr)
    a = arr.copy()
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        # Swap elements
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

# --- User Input Section ---

# Get numbers separated by spaces from the user
user_input = input("Enter the numbers you want to sort (separated by spaces): ")

# Convert the string input into a list of integers
test_array = [int(x) for x in user_input.split()]

# --- Testing the sorting implementations ---
print("\n--- Results ---")
print("Original Array:", test_array)
print("Bubble Sorted:", bubble_sort(test_array))
print("Selection Sorted:", selection_sort(test_array))
