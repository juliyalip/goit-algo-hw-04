#  три алгоритми сортування: злиттям, вставками та Timsort 
import timeit 
import random 

sizes= [100, 1000, 5000]

# Cортування злиттям (merge sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    return merged

# Сортування вставками (insertion sort)
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def measure_time(sorted_func, arr):
    sorted_arr = lambda: sorted_func(arr.copy())
    return timeit.timeit(sorted_arr, number=1)* 1000


print(f"{'Розмір':<10}{'Cортування злиттям':<25}{'Сортування вставками':<25}{'Timsort':<25}")

for size in sizes:
    arr = random.sample(range(0, size), size)
    time_merge = measure_time(merge_sort, arr)
    time_insert = measure_time(insertion_sort, arr)
    time_timesort = measure_time(sorted, arr)
    print(f"{size:<10}{time_merge:<25}{time_insert:<25}{time_timesort:<25}")

# Висновки (Conclusions)
# Сортування вставками повільне на великих масивах 
# Merge sort, Timesort працюють швидше завдяки O(n log n)
# Timsort оптимізований під Python тому на практиці самий швидкий
 

