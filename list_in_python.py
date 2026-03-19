# ============================================================
#             PYTHON LISTS — COMPREHENSIVE TUTORIAL
# ============================================================
# This file covers everything you need to know about Python Lists:
#   1. Creating a List
#   2. Indexing in a List
#   3. List Slicing
#   4. Operations in a List
#   5. Built-in Functions and Methods

print("=" * 60)
print("       PYTHON LISTS — COMPREHENSIVE TUTORIAL")
print("=" * 60)


# =============================================================
# SECTION 1: CREATING A LIST / WAYS TO CREATE A LIST
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 1: CREATING A LIST")
print("=" * 60)

# --- 1.1 Empty List ---
# An empty list can be created in two ways:
empty_list_1 = []           # Using square brackets
empty_list_2 = list()       # Using the built-in list() constructor

print("\n--- 1.1 Empty Lists ---")
print("Using []:     ", empty_list_1)
print("Using list(): ", empty_list_2)

# --- 1.2 List with Values ---
# Lists can hold elements of any type.
integers_list = [1, 2, 3, 4, 5]
strings_list  = ["apple", "banana", "cherry"]
mixed_list    = [42, "hello", 3.14, True, None]  # Mixed types in one list

print("\n--- 1.2 List with Values ---")
print("Integers:  ", integers_list)
print("Strings:   ", strings_list)
print("Mixed:     ", mixed_list)

# --- 1.3 Nested Lists ---
# A list can contain other lists as elements (nested/2D lists).
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\n--- 1.3 Nested Lists ---")
print("Nested list:", nested_list)
print("Access inner element [1][2]:", nested_list[1][2])  # → 6

# --- 1.4 Using list() Constructor with Iterables ---
# The list() constructor can convert any iterable into a list.
from_string = list("hello")           # Each character becomes an element
from_range  = list(range(1, 6))       # Range 1 to 5
from_tuple  = list((10, 20, 30))      # Tuple to list

print("\n--- 1.4 list() Constructor with Iterables ---")
print("From string:  ", from_string)   # ['h', 'e', 'l', 'l', 'o']
print("From range:   ", from_range)    # [1, 2, 3, 4, 5]
print("From tuple:   ", from_tuple)    # [10, 20, 30]

# --- 1.5 List Comprehension ---
# A concise way to create lists using a single-line expression.
squares       = [x ** 2 for x in range(1, 6)]          # Squares of 1–5
even_numbers  = [x for x in range(1, 11) if x % 2 == 0]  # Even numbers 1–10

print("\n--- 1.5 List Comprehension ---")
print("Squares 1-5:       ", squares)       # [1, 4, 9, 16, 25]
print("Even numbers 1-10: ", even_numbers)  # [2, 4, 6, 8, 10]

# *** IMPORTANT NOTES — CREATING A LIST ***
# - Lists are ordered (elements maintain insertion order).
# - Lists are mutable — you CAN change their content after creation.
# - A list can hold duplicate values.
# - A list can be empty.
print("\n# NOTE: Lists are ordered, mutable, and allow duplicates.")


# =============================================================
# SECTION 2: INDEXING IN A LIST
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 2: INDEXING IN A LIST")
print("=" * 60)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#  Index:    0         1         2        3          4      (positive)
#  Index:   -5        -4        -3       -2         -1      (negative)

print("\nList:", fruits)

# --- 2.1 Positive Indexing ---
# Indexing starts at 0 from the LEFT side.
print("\n--- 2.1 Positive Indexing ---")
print("Index 0 (first):  ", fruits[0])   # apple
print("Index 1:          ", fruits[1])   # banana
print("Index 2:          ", fruits[2])   # cherry
print("Index 4 (last):   ", fruits[4])   # elderberry

# --- 2.2 Negative Indexing ---
# Negative indexes count from the RIGHT side; -1 is the last element.
print("\n--- 2.2 Negative Indexing ---")
print("Index -1 (last):       ", fruits[-1])  # elderberry
print("Index -2 (second last):", fruits[-2])  # date
print("Index -5 (first):      ", fruits[-5])  # apple

# --- 2.3 IndexError ---
# Accessing an index that doesn't exist raises an IndexError.
print("\n--- 2.3 IndexError Example ---")
try:
    print(fruits[10])   # This index doesn't exist
except IndexError as e:
    print("IndexError caught:", e)

# *** IMPORTANT NOTES — INDEXING ***
# - Positive index starts at 0 (NOT 1).
# - Negative index starts at -1 for the last element.
# - Accessing an out-of-range index raises IndexError.
print("\n# NOTE: Index starts at 0; negative index starts at -1.")


# =============================================================
# SECTION 3: LIST SLICING
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 3: LIST SLICING")
print("=" * 60)

# Syntax: list[start : stop : step]
#   start — index to begin slice (inclusive, default 0)
#   stop  — index to end slice   (exclusive, default end of list)
#   step  — step/interval        (default 1)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nList:", numbers)

# --- 3.1 Basic Slice with start and stop ---
print("\n--- 3.1 Slice with start and stop ---")
print("numbers[2:6]:  ", numbers[2:6])   # [2, 3, 4, 5]  (index 2 to 5)
print("numbers[0:4]:  ", numbers[0:4])   # [0, 1, 2, 3]

# --- 3.2 Slicing with step ---
print("\n--- 3.2 Slice with step ---")
print("numbers[0:9:2]:", numbers[0:9:2])  # [0, 2, 4, 6, 8]  (every 2nd)
print("numbers[1:8:3]:", numbers[1:8:3])  # [1, 4, 7]        (every 3rd)

# --- 3.3 Negative Slicing ---
# You can use negative indexes in slices as well.
print("\n--- 3.3 Negative Slicing ---")
print("numbers[-4:-1]: ", numbers[-4:-1])  # [6, 7, 8]
print("numbers[-5:]:   ", numbers[-5:])    # [5, 6, 7, 8, 9]

# --- 3.4 Reversing a List using Slicing ---
# Using step = -1 gives the list in reverse order.
print("\n--- 3.4 Reversing with [::-1] ---")
print("numbers[::-1]: ", numbers[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# --- 3.5 Omitting start / stop / step ---
print("\n--- 3.5 Omitting start / stop / step ---")
print("numbers[:]:    ", numbers[:])       # entire list (copy)
print("numbers[:5]:   ", numbers[:5])      # first 5 elements  [0,1,2,3,4]
print("numbers[5:]:   ", numbers[5:])      # from index 5 onward [5,6,7,8,9]
print("numbers[::2]:  ", numbers[::2])     # every 2nd element [0,2,4,6,8]

# *** IMPORTANT NOTES — SLICING ***
# - Slicing NEVER raises an IndexError, even if start/stop are out of range.
# - Slicing returns a NEW list (the original is unchanged).
# - list[:] creates a shallow copy of the list.
print("\n# NOTE: Slicing returns a new list and never raises IndexError.")
safe_slice = numbers[0:100]   # No error even though index 100 doesn't exist
print("numbers[0:100]:", safe_slice)       # returns the full list safely


# =============================================================
# SECTION 4: OPERATIONS IN THE LIST
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 4: OPERATIONS IN THE LIST")
print("=" * 60)

list_a = [1, 2, 3]
list_b = [4, 5, 6]

# --- 4.1 Concatenation (+) ---
# Joins two or more lists into a new list.
print("\n--- 4.1 Concatenation (+) ---")
combined = list_a + list_b
print("list_a + list_b:        ", combined)           # [1, 2, 3, 4, 5, 6]
print("[0] + list_a + ['end']: ", [0] + list_a + ["end"])  # [0, 1, 2, 3, 'end']
# NOTE: + creates a NEW list; the originals are unchanged.
print("list_a unchanged:       ", list_a)

# --- 4.2 Repetition (*) ---
# Repeats the list a given number of times.
print("\n--- 4.2 Repetition (*) ---")
repeated = list_a * 3
print("list_a * 3:  ", repeated)   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print("[0] * 5:     ", [0] * 5)    # [0, 0, 0, 0, 0]

# --- 4.3 Comparison (== and !=) ---
# Compares two lists element by element.
print("\n--- 4.3 Comparison (== and !=) ---")
print("[1,2,3] == [1,2,3]: ", [1, 2, 3] == [1, 2, 3])  # True
print("[1,2,3] == [3,2,1]: ", [1, 2, 3] == [3, 2, 1])  # False (order matters)
print("[1,2,3] != [1,2,4]: ", [1, 2, 3] != [1, 2, 4])  # True
# NOTE: Two lists are equal only if they have the same elements in the same order.

# --- 4.4 Membership (in) ---
# Checks if an element exists in the list.
print("\n--- 4.4 Membership (in) ---")
colors = ["red", "green", "blue"]
print("'red' in colors:    ", "red" in colors)     # True
print("'yellow' in colors: ", "yellow" in colors)  # False

# --- 4.5 Non-membership (not in) ---
# Checks if an element does NOT exist in the list.
print("\n--- 4.5 Non-membership (not in) ---")
print("'red' not in colors:    ", "red" not in colors)     # False
print("'yellow' not in colors: ", "yellow" not in colors)  # True

# *** IMPORTANT NOTES — OPERATIONS ***
# - + creates a NEW list; use extend() to add elements in place.
# - * with 0 gives an empty list: [1,2] * 0 → []
# - Comparison checks ORDER and VALUES; [1,2] != [2,1].
# - 'in' and 'not in' scan the entire list (O(n) time).
print("\n# NOTE: + and * return new lists; == checks order and values.")


# =============================================================
# SECTION 5: BUILT-IN FUNCTIONS AND METHODS IN LIST
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 5: BUILT-IN FUNCTIONS AND METHODS")
print("=" * 60)

# -------------------------------------------------------
# 5.1 Built-in Functions
# -------------------------------------------------------

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("\n--- 5.1 Built-in Functions ---")
print("List:", nums)

# len() — returns the number of elements in the list
print("len(nums):    ", len(nums))       # 9

# sum() — returns the total of all numeric elements
print("sum(nums):    ", sum(nums))       # 36

# sorted() — returns a NEW sorted list; the ORIGINAL is unchanged
sorted_nums = sorted(nums)
print("sorted(nums): ", sorted_nums)    # [1, 1, 2, 3, 4, 5, 5, 6, 9]
print("Original:     ", nums)           # unchanged

# sorted() with reverse=True — descending order
print("sorted(nums, reverse=True):", sorted(nums, reverse=True))

# *** NOTE: sorted() returns a new list; sort() modifies in place (see 5.6).

# -------------------------------------------------------
# 5.2 Adding Elements
# -------------------------------------------------------

my_list = [10, 20, 30]
print("\n--- 5.2 Adding Elements ---")
print("Original:", my_list)

# append() — adds a SINGLE element at the END of the list
my_list.append(40)
print("After append(40):      ", my_list)   # [10, 20, 30, 40]

# insert(index, value) — inserts an element at a SPECIFIC position
my_list.insert(1, 15)    # insert 15 at index 1
print("After insert(1, 15):   ", my_list)   # [10, 15, 20, 30, 40]

# extend(iterable) — adds ALL elements of an iterable to the list
my_list.extend([50, 60])
print("After extend([50,60]): ", my_list)   # [10, 15, 20, 30, 40, 50, 60]

# NOTE: append([50,60]) would add the list as a SINGLE element,
#       whereas extend([50,60]) adds each element individually.

# -------------------------------------------------------
# 5.3 Removing Elements
# -------------------------------------------------------

remove_list = [10, 20, 30, 20, 40, 50]
print("\n--- 5.3 Removing Elements ---")
print("Original:", remove_list)

# remove(value) — removes the FIRST occurrence of the specified value
remove_list.remove(20)
print("After remove(20):       ", remove_list)  # [10, 30, 20, 40, 50]

# pop(index) — removes and RETURNS the element at the given index
#              defaults to the LAST element if no index is given
popped_last  = remove_list.pop()     # removes last element
popped_index = remove_list.pop(1)    # removes element at index 1
print("Popped last element:    ", popped_last)   # 50
print("Popped index 1:         ", popped_index)  # 30
print("After pop() and pop(1): ", remove_list)   # [10, 20, 40]

# del — deletes an element by index, or a slice, or the entire list variable
del_list = [100, 200, 300, 400, 500]
del del_list[1]                       # delete index 1
print("After del del_list[1]:  ", del_list)  # [100, 300, 400, 500]
del del_list[1:3]                     # delete slice (index 1 & 2)
print("After del del_list[1:3]:", del_list)  # [100, 500]

# clear() — removes ALL elements, leaving an empty list
clear_list = [1, 2, 3, 4, 5]
clear_list.clear()
print("After clear():          ", clear_list)    # []

# *** IMPORTANT NOTES — REMOVING ***
# - remove() raises ValueError if the value is not found.
# - pop() raises IndexError if the index is out of range.
# - del deletes the element or even the variable; clear() empties the list.
print("\n# NOTE: remove() → ValueError; pop() → IndexError if out of range.")
try:
    [1, 2, 3].remove(99)
except ValueError as e:
    print("ValueError from remove():", e)

# -------------------------------------------------------
# 5.4 Sorting and Reversing
# -------------------------------------------------------

sort_list = [5, 2, 8, 1, 9, 3]
print("\n--- 5.4 Sorting and Reversing ---")
print("Original:", sort_list)

# sort() — sorts the list IN PLACE (modifies the original list)
sort_list.sort()
print("After sort():           ", sort_list)   # [1, 2, 3, 5, 8, 9]

# sort(reverse=True) — sort in descending order
sort_list.sort(reverse=True)
print("After sort(reverse=True):", sort_list)  # [9, 8, 5, 3, 2, 1]

# reverse() — reverses the list IN PLACE (modifies the original list)
rev_list = [10, 20, 30, 40, 50]
rev_list.reverse()
print("After reverse():        ", rev_list)    # [50, 40, 30, 20, 10]

# *** IMPORTANT NOTES — SORT vs SORTED ***
# - sort()   → modifies the original list, returns None.
# - sorted() → returns a NEW sorted list, original is unchanged.
print("\n# NOTE: sort() modifies in place; sorted() returns a new list.")

# -------------------------------------------------------
# 5.5 Searching and Counting
# -------------------------------------------------------

search_list = ["cat", "dog", "bird", "dog", "fish", "dog"]
print("\n--- 5.5 Searching and Counting ---")
print("List:", search_list)

# count(value) — counts the number of times a value appears
print("count('dog'):  ", search_list.count("dog"))   # 3
print("count('cat'):  ", search_list.count("cat"))   # 1
print("count('lion'): ", search_list.count("lion"))  # 0 (not found → no error)

# index(value) — returns the index of the FIRST occurrence of the value
print("index('dog'):  ", search_list.index("dog"))   # 1
print("index('bird'): ", search_list.index("bird"))  # 2

# *** IMPORTANT NOTES — SEARCHING ***
# - count() returns 0 if the element is not found (no error).
# - index() raises ValueError if the element is not found.
print("\n# NOTE: count() returns 0 if not found; index() raises ValueError.")
try:
    search_list.index("lion")
except ValueError as e:
    print("ValueError from index():", e)


# =============================================================
#                   END OF TUTORIAL
# =============================================================

print("\n" + "=" * 60)
print("       END OF PYTHON LISTS TUTORIAL")
print("=" * 60)
print("Topics covered:")
print("  1. Creating a List")
print("  2. Indexing in a List")
print("  3. List Slicing")
print("  4. Operations in a List")
print("  5. Built-in Functions and Methods")
print("=" * 60)
