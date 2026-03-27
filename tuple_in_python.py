# ============================================================
#            PYTHON TUPLES — COMPREHENSIVE TUTORIAL
# ============================================================
# This file covers everything you need to know about Python Tuples:
#   1. Creating a Tuple
#   2. Indexing in a Tuple
#   3. Tuple Slicing
#   4. Operations on Tuples
#   5. Immutability of Tuples
#   6. Built-in Functions and Methods
#   7. Tuple vs List — Key Differences
#   8. Common Use Cases of Tuples

print("=" * 60)
print("      PYTHON TUPLES — COMPREHENSIVE TUTORIAL")
print("=" * 60)


# =============================================================
# SECTION 1: CREATING A TUPLE / WAYS TO CREATE A TUPLE
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 1: CREATING A TUPLE")
print("=" * 60)

# --- 1.1 Empty Tuple ---
# An empty tuple can be created in two ways:
empty_tuple_1 = ()          # Using parentheses
empty_tuple_2 = tuple()     # Using the built-in tuple() constructor

print("\n--- 1.1 Empty Tuples ---")
print("Using ():      ", empty_tuple_1)
print("Using tuple(): ", empty_tuple_2)

# --- 1.2 Single-Element Tuple (THE GOTCHA!) ---
# A trailing comma is REQUIRED to make a single-element tuple.
# Without the comma, Python treats the parentheses as grouping, not a tuple.
not_a_tuple  = (5)     # This is just the integer 5 — NOT a tuple!
is_a_tuple   = (5,)    # This IS a tuple — notice the trailing comma.
also_a_tuple = 5,      # Parentheses are optional; the comma makes it a tuple.

print("\n--- 1.2 Single-Element Tuple (Watch the comma!) ---")
print("(5)  → type:", type(not_a_tuple),  "| value:", not_a_tuple)   # <class 'int'>
print("(5,) → type:", type(is_a_tuple),   "| value:", is_a_tuple)    # <class 'tuple'>
print("5,   → type:", type(also_a_tuple), "| value:", also_a_tuple)  # <class 'tuple'>
# NOTE: (5) is NOT a tuple. Always add a trailing comma for a single-element tuple!

# --- 1.3 Tuple with Multiple Values ---
# Tuples can hold elements of any type.
integers_tuple = (1, 2, 3, 4, 5)
strings_tuple  = ("apple", "banana", "cherry")
mixed_tuple    = (42, "hello", 3.14, True, None)  # Mixed types in one tuple

print("\n--- 1.3 Tuple with Multiple Values ---")
print("Integers: ", integers_tuple)
print("Strings:  ", strings_tuple)
print("Mixed:    ", mixed_tuple)

# --- 1.4 Nested Tuples ---
# A tuple can contain other tuples as elements (nested tuples).
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("\n--- 1.4 Nested Tuples ---")
print("Nested tuple:", nested_tuple)
print("Access inner element [1][2]:", nested_tuple[1][2])  # → 6

# --- 1.5 Using tuple() Constructor with Iterables ---
# The tuple() constructor can convert any iterable into a tuple.
from_string = tuple("hello")          # Each character becomes an element
from_list   = tuple([10, 20, 30])     # List to tuple
from_range  = tuple(range(1, 6))      # Range 1 to 5

print("\n--- 1.5 tuple() Constructor with Iterables ---")
print("From string: ", from_string)   # ('h', 'e', 'l', 'l', 'o')
print("From list:   ", from_list)     # (10, 20, 30)
print("From range:  ", from_range)    # (1, 2, 3, 4, 5)

# --- 1.6 Tuple Packing and Unpacking ---
# Packing: assigning multiple values to one tuple variable (no parentheses needed).
packed = 10, 20, 30       # Packing three values into a tuple
print("\n--- 1.6 Tuple Packing and Unpacking ---")
print("Packed tuple:", packed)        # (10, 20, 30)

# Unpacking: extracting tuple values into individual variables.
a, b, c = packed
print("Unpacked — a:", a, "| b:", b, "| c:", c)   # 10  20  30

# Extended unpacking with * — collect remaining elements into a list.
first, *rest = (1, 2, 3, 4, 5)
print("first:", first, "| rest:", rest)            # 1   [2, 3, 4, 5]

# --- 1.7 Tuple Comprehension? (Generator Expression) ---
# Note: Using () with a comprehension does NOT create a tuple — it creates
# a generator object. Use tuple() around the expression to get a tuple.
gen_obj   = (x ** 2 for x in range(1, 6))   # This is a GENERATOR, not a tuple
tup_comp  = tuple(x ** 2 for x in range(1, 6))  # This IS a tuple

print("\n--- 1.7 Tuple Comprehension? (It's actually a Generator) ---")
print("(x**2 for x ...) type:", type(gen_obj))    # <class 'generator'>
print("tuple(x**2 for x ...): ", tup_comp)        # (1, 4, 9, 16, 25)

# *** IMPORTANT NOTES — CREATING A TUPLE ***
# - Tuples are ordered (elements maintain insertion order).
# - Tuples are IMMUTABLE — you CANNOT change their content after creation.
# - A tuple can hold duplicate values.
# - A single-element tuple MUST have a trailing comma: (5,) not (5).
# - () with a comprehension gives a generator, NOT a tuple — wrap with tuple().
print("\n# NOTE: Tuples are ordered, immutable, and allow duplicates.")
print("# NOTE: Single-element tuple needs a trailing comma — (5,) not (5).")


# =============================================================
# SECTION 2: INDEXING IN A TUPLE
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 2: INDEXING IN A TUPLE")
print("=" * 60)

fruits = ("apple", "banana", "cherry", "date", "elderberry")
#  Index:    0         1         2        3          4       (positive)
#  Index:   -5        -4        -3       -2         -1       (negative)

print("\nTuple:", fruits)

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
# - Indexing works exactly the same as with lists.
print("\n# NOTE: Index starts at 0; negative index starts at -1.")


# =============================================================
# SECTION 3: TUPLE SLICING
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 3: TUPLE SLICING")
print("=" * 60)

# Syntax: tuple[start : stop : step]
#   start — index to begin slice (inclusive, default 0)
#   stop  — index to end slice   (exclusive, default end of tuple)
#   step  — step/interval        (default 1)

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print("\nTuple:", numbers)

# --- 3.1 Basic Slice with start and stop ---
print("\n--- 3.1 Slice with start and stop ---")
print("numbers[2:6]:  ", numbers[2:6])   # (2, 3, 4, 5)  — index 2 to 5
print("numbers[0:4]:  ", numbers[0:4])   # (0, 1, 2, 3)

# --- 3.2 Slicing with step ---
print("\n--- 3.2 Slice with step ---")
print("numbers[0:9:2]:", numbers[0:9:2])  # (0, 2, 4, 6, 8) — every 2nd element
print("numbers[1:8:3]:", numbers[1:8:3])  # (1, 4, 7)        — every 3rd element

# --- 3.3 Negative Slicing ---
# You can use negative indexes in slices as well.
print("\n--- 3.3 Negative Slicing ---")
print("numbers[-4:-1]: ", numbers[-4:-1])  # (6, 7, 8)
print("numbers[-5:]:   ", numbers[-5:])    # (5, 6, 7, 8, 9)

# --- 3.4 Reversing a Tuple using Slicing ---
# Using step = -1 gives the tuple in reverse order.
print("\n--- 3.4 Reversing with [::-1] ---")
print("numbers[::-1]: ", numbers[::-1])    # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

# --- 3.5 Omitting start / stop / step ---
print("\n--- 3.5 Omitting start / stop / step ---")
print("numbers[:]:    ", numbers[:])       # entire tuple (copy)
print("numbers[:5]:   ", numbers[:5])      # first 5 elements  (0,1,2,3,4)
print("numbers[5:]:   ", numbers[5:])      # from index 5 onward (5,6,7,8,9)
print("numbers[::2]:  ", numbers[::2])     # every 2nd element (0,2,4,6,8)

# *** IMPORTANT NOTES — SLICING ***
# - Slicing NEVER raises an IndexError, even if start/stop are out of range.
# - Slicing returns a NEW tuple (the original is unchanged).
# - tuple[:] creates a shallow copy of the tuple.
# - Slicing a tuple always returns a tuple (not a list).
print("\n# NOTE: Slicing returns a new tuple and never raises IndexError.")
safe_slice = numbers[0:100]   # No error even though index 100 doesn't exist
print("numbers[0:100]:", safe_slice)        # returns the full tuple safely


# =============================================================
# SECTION 4: OPERATIONS ON TUPLES
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 4: OPERATIONS ON TUPLES")
print("=" * 60)

tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)

# --- 4.1 Concatenation (+) ---
# Joins two or more tuples into a new tuple.
print("\n--- 4.1 Concatenation (+) ---")
combined = tuple_a + tuple_b
print("tuple_a + tuple_b:         ", combined)               # (1, 2, 3, 4, 5, 6)
print("(0,) + tuple_a + ('end',): ", (0,) + tuple_a + ("end",))  # (0, 1, 2, 3, 'end')
# NOTE: + creates a NEW tuple; the originals are unchanged.
print("tuple_a unchanged:         ", tuple_a)

# --- 4.2 Repetition (*) ---
# Repeats the tuple a given number of times.
print("\n--- 4.2 Repetition (*) ---")
repeated = tuple_a * 3
print("tuple_a * 3: ", repeated)    # (1, 2, 3, 1, 2, 3, 1, 2, 3)
print("(0,) * 5:    ", (0,) * 5)   # (0, 0, 0, 0, 0)
print("tuple_a * 0: ", tuple_a * 0) # () — empty tuple

# --- 4.3 Comparison (== and !=) ---
# Compares two tuples element by element.
print("\n--- 4.3 Comparison (== and !=) ---")
print("(1,2,3) == (1,2,3): ", (1, 2, 3) == (1, 2, 3))  # True
print("(1,2,3) == (3,2,1): ", (1, 2, 3) == (3, 2, 1))  # False (order matters)
print("(1,2,3) != (1,2,4): ", (1, 2, 3) != (1, 2, 4))  # True
# NOTE: Two tuples are equal only if they have the same elements in the same order.

# --- 4.4 Membership (in) ---
# Checks if an element exists in the tuple.
print("\n--- 4.4 Membership (in) ---")
colors = ("red", "green", "blue")
print("'red' in colors:    ", "red" in colors)     # True
print("'yellow' in colors: ", "yellow" in colors)  # False

# --- 4.5 Non-membership (not in) ---
# Checks if an element does NOT exist in the tuple.
print("\n--- 4.5 Non-membership (not in) ---")
print("'red' not in colors:    ", "red" not in colors)     # False
print("'yellow' not in colors: ", "yellow" not in colors)  # True

# *** IMPORTANT NOTES — OPERATIONS ***
# - + creates a NEW tuple; you cannot add elements to an existing tuple.
# - * with 0 gives an empty tuple: (1,2) * 0 → ()
# - Comparison checks ORDER and VALUES; (1,2) != (2,1).
# - 'in' and 'not in' scan the entire tuple (O(n) time).
print("\n# NOTE: + and * return new tuples; == checks order and values.")


# =============================================================
# SECTION 5: IMMUTABILITY OF TUPLES
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 5: IMMUTABILITY OF TUPLES")
print("=" * 60)

immutable = (10, 20, 30, 40, 50)
print("\nTuple:", immutable)

# --- 5.1 Tuples Cannot Be Modified ---
# Attempting to change an element raises a TypeError.
print("\n--- 5.1 TypeError on Item Assignment ---")
try:
    immutable[0] = 99     # This will raise a TypeError
except TypeError as e:
    print("TypeError caught:", e)

# --- 5.2 Workaround: Convert to List, Modify, Convert Back ---
# If you truly need to modify a tuple, convert it to a list first.
print("\n--- 5.2 Workaround — Convert to List and Back ---")
temp_list = list(immutable)  # Step 1: convert tuple → list
temp_list[0] = 99            # Step 2: modify the list
modified = tuple(temp_list)  # Step 3: convert list → tuple
print("Original tuple:", immutable)   # (10, 20, 30, 40, 50) — unchanged
print("Modified tuple:", modified)    # (99, 20, 30, 40, 50)

# --- 5.3 Mutable Objects Inside a Tuple CAN Be Modified ---
# A tuple's references are fixed, but if an element is mutable (like a list),
# the contents of that mutable element CAN still be changed.
print("\n--- 5.3 Mutable Objects Inside a Tuple ---")
tuple_with_list = (1, 2, [30, 40, 50])
print("Before:", tuple_with_list)           # (1, 2, [30, 40, 50])
tuple_with_list[2].append(60)              # Modifying the list INSIDE the tuple
tuple_with_list[2][0] = 99                 # Changing an element inside that list
print("After:  ", tuple_with_list)          # (1, 2, [99, 40, 50, 60])
# NOTE: The tuple itself didn't change (still 3 elements at same positions),
#       but the list it points to was mutated.

# --- 5.4 Why Immutability Matters ---
# Tuples are HASHABLE (when all elements are hashable), which means:
#   - They can be used as dictionary keys.
#   - They can be stored in sets.
#   - They are safer — you don't accidentally modify your data.
print("\n--- 5.4 Why Immutability Matters ---")
coord = (10, 20)
location_map = {coord: "City Center"}     # Tuple as a dict key ✓
print("Dict with tuple key:", location_map)
print("Lookup by key:      ", location_map[(10, 20)])

# Lists CANNOT be used as dictionary keys (they are unhashable):
try:
    bad_key = {[10, 20]: "City Center"}   # This will raise a TypeError
except TypeError as e:
    print("TypeError with list key:", e)

# *** IMPORTANT NOTES — IMMUTABILITY ***
# - Tuples are IMMUTABLE — you cannot add, remove, or change elements.
# - Trying to modify a tuple raises TypeError.
# - Workaround: convert tuple → list → modify → convert back to tuple.
# - Mutable objects (lists) INSIDE a tuple can still be mutated.
# - Immutability makes tuples hashable → usable as dict keys and set members.
print("\n# NOTE: Tuples are immutable; mutable contents inside can still change.")


# =============================================================
# SECTION 6: BUILT-IN FUNCTIONS AND METHODS FOR TUPLES
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 6: BUILT-IN FUNCTIONS AND METHODS")
print("=" * 60)

# -------------------------------------------------------
# 6.1 Built-in Functions
# -------------------------------------------------------

nums = (3, 1, 4, 1, 5, 9, 2, 6, 5)
print("\n--- 6.1 Built-in Functions ---")
print("Tuple:", nums)

# len() — returns the number of elements in the tuple
print("len(nums):    ", len(nums))        # 9

# sum() — returns the total of all numeric elements
print("sum(nums):    ", sum(nums))        # 36

# max() — returns the largest element
print("max(nums):    ", max(nums))        # 9

# min() — returns the smallest element
print("min(nums):    ", min(nums))        # 1

# sorted() — returns a NEW *list* (NOT a tuple!) in sorted order
sorted_nums = sorted(nums)
print("sorted(nums):            ", sorted_nums)   # [1, 1, 2, 3, 4, 5, 5, 6, 9]
print("type(sorted(nums)):      ", type(sorted_nums))   # <class 'list'>
print("Original tuple unchanged:", nums)

# sorted() with reverse=True — descending order
print("sorted(nums, reverse=True):", sorted(nums, reverse=True))

# tuple() — converts other iterables to a tuple
print("tuple([1,2,3]):   ", tuple([1, 2, 3]))    # (1, 2, 3)
print("tuple('abc'):     ", tuple("abc"))         # ('a', 'b', 'c')
print("tuple(range(5)):  ", tuple(range(5)))      # (0, 1, 2, 3, 4)

# *** NOTE: sorted() returns a list, not a tuple. Wrap with tuple() if needed.
print("tuple(sorted(nums)):", tuple(sorted(nums)))  # (1, 1, 2, 3, 4, 5, 5, 6, 9)

# -------------------------------------------------------
# 6.2 Tuple Methods (only 2!)
# -------------------------------------------------------
# Tuples have ONLY TWO built-in methods because they are immutable.
# No add/remove/sort methods exist — the data cannot be changed.

search_tuple = ("cat", "dog", "bird", "dog", "fish", "dog")
print("\n--- 6.2 Tuple Methods (count & index) ---")
print("Tuple:", search_tuple)

# count(value) — counts how many times a value appears in the tuple
print("count('dog'):  ", search_tuple.count("dog"))   # 3
print("count('cat'):  ", search_tuple.count("cat"))   # 1
print("count('lion'): ", search_tuple.count("lion"))  # 0 (not found → no error)

# index(value) — returns the index of the FIRST occurrence of the value
print("index('dog'):  ", search_tuple.index("dog"))   # 1
print("index('bird'): ", search_tuple.index("bird"))  # 2

# index() raises ValueError if the element is not found
print("\n# NOTE: index() raises ValueError if element not found.")
try:
    search_tuple.index("lion")
except ValueError as e:
    print("ValueError from index():", e)

# *** IMPORTANT NOTES — BUILT-IN FUNCTIONS AND METHODS ***
# - Tuples have ONLY 2 methods: count() and index() — because they are immutable.
# - sorted() returns a LIST, not a tuple — wrap with tuple() to get a tuple.
# - count() returns 0 if the element is not found (no error).
# - index() raises ValueError if the element is not found.
print("\n# NOTE: Tuples have only 2 methods: count() and index().")


# =============================================================
# SECTION 7: TUPLE vs LIST — KEY DIFFERENCES
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 7: TUPLE vs LIST — KEY DIFFERENCES")
print("=" * 60)

# --- 7.1 Mutability ---
# List  → MUTABLE   (you can add, remove, or change elements)
# Tuple → IMMUTABLE (you cannot change elements after creation)
print("\n--- 7.1 Mutability ---")
my_list  = [1, 2, 3]
my_tuple = (1, 2, 3)
my_list[0] = 99          # ✓ Works fine
print("List  after modification:", my_list)
try:
    my_tuple[0] = 99     # ✗ Raises TypeError
except TypeError as e:
    print("Tuple modification error:", e)

# --- 7.2 Syntax ---
# List  → square brackets   [ ]
# Tuple → parentheses       ( )  or just commas
print("\n--- 7.2 Syntax ---")
print("List  syntax: [1, 2, 3] →", [1, 2, 3])
print("Tuple syntax: (1, 2, 3) →", (1, 2, 3))

# --- 7.3 Performance ---
# Tuples are generally FASTER to create and use LESS MEMORY than lists.
# This is because tuples are immutable (Python can optimize them internally).
import sys
list_example  = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)
print("\n--- 7.3 Performance (Memory) ---")
print("Memory — list: ", sys.getsizeof(list_example),  "bytes")
print("Memory — tuple:", sys.getsizeof(tuple_example), "bytes")
# NOTE: Tuple typically uses less memory than an equivalent list.

# --- 7.4 Use Cases ---
# List  → use when data changes (shopping cart, user input, dynamic collections)
# Tuple → use when data is fixed (coordinates, RGB colours, database rows)
print("\n--- 7.4 Use Cases ---")
print("List  → dynamic data: shopping cart, collected results, growing datasets")
print("Tuple → fixed data:   (latitude, longitude), RGB(255,0,0), DB record row")

# --- 7.5 Tuples as Dictionary Keys ---
# Tuples are hashable (when all elements are hashable) → can be dict keys.
# Lists are unhashable → CANNOT be dict keys.
print("\n--- 7.5 Tuples as Dictionary Keys ---")
grid_map = {(0, 0): "origin", (1, 0): "right", (0, 1): "up"}
print("Dict with tuple keys:", grid_map)
print("Lookup (1, 0):       ", grid_map[(1, 0)])

# --- Quick Comparison Table (as comments) ---
# +------------------+------------------+------------------+
# | Feature          | List             | Tuple            |
# +------------------+------------------+------------------+
# | Mutable          | Yes              | No               |
# | Syntax           | [1, 2, 3]        | (1, 2, 3)        |
# | Methods          | Many (20+)       | Only 2           |
# | Performance      | Slower           | Faster           |
# | Memory           | More             | Less             |
# | Dict key         | No (unhashable)  | Yes (hashable)   |
# | Use case         | Dynamic data     | Fixed data       |
# +------------------+------------------+------------------+
print("\n# Comparison: List=mutable/slow/many-methods; Tuple=immutable/fast/2-methods.")


# =============================================================
# SECTION 8: COMMON USE CASES OF TUPLES
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 8: COMMON USE CASES OF TUPLES")
print("=" * 60)

# --- 8.1 Returning Multiple Values from a Function ---
# Python functions can return multiple values as a tuple (implicitly).
print("\n--- 8.1 Returning Multiple Values from a Function ---")

def min_max(numbers):
    """Returns the (minimum, maximum) of a sequence as a tuple."""
    return min(numbers), max(numbers)   # Python packs these into a tuple

result = min_max([4, 7, 1, 9, 2])
print("min_max([4,7,1,9,2]) →", result)           # (1, 9)
low, high = min_max([4, 7, 1, 9, 2])              # Unpack directly
print("Unpacked — low:", low, "| high:", high)    # 1   9

# --- 8.2 Swapping Variables ---
# Tuples make variable swapping a one-liner in Python (no temp variable needed).
print("\n--- 8.2 Swapping Variables ---")
x, y = 100, 200
print("Before swap: x =", x, "| y =", y)   # 100  200
x, y = y, x                                # Swap using tuple unpacking
print("After swap:  x =", x, "| y =", y)   # 200  100

# --- 8.3 Tuples as Dictionary Keys ---
# Because tuples are hashable, they work as dictionary keys.
# This is useful for multi-dimensional indexing or composite keys.
print("\n--- 8.3 Tuples as Dictionary Keys ---")
city_population = {
    ("New York", "US"):  8_336_817,
    ("Mumbai",   "IN"):  20_667_656,
    ("Tokyo",    "JP"):  13_960_000,
}
print("Population of Mumbai:", city_population[("Mumbai", "IN")])

# --- 8.4 Unpacking in Loops ---
# When iterating over a list of tuples, you can unpack each tuple directly.
print("\n--- 8.4 Unpacking in Loops ---")
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"  x = {x}, y = {y}")

# Another example — student records:
students = [("Alice", 90), ("Bob", 85), ("Charlie", 92)]
print("Student scores:")
for name, score in students:
    print(f"  {name}: {score}")

# --- 8.5 Named Tuples (collections.namedtuple) ---
# Named tuples let you access elements by name instead of index,
# making code more readable while keeping tuple benefits (immutable, fast).
print("\n--- 8.5 Named Tuples (collections.namedtuple) ---")
from collections import namedtuple

# Define a named tuple type called 'Point' with fields 'x' and 'y'
Point = namedtuple("Point", ["x", "y"])
p = Point(x=3, y=7)
print("Point:   ", p)         # Point(x=3, y=7)
print("p.x:     ", p.x)       # 3  — access by name
print("p.y:     ", p.y)       # 7
print("p[0]:    ", p[0])       # 3  — still works by index too
print("type(p): ", type(p))   # <class '__main__.Point'>

# Another example — an Employee record:
Employee = namedtuple("Employee", ["name", "age", "department"])
emp = Employee("Alice", 30, "Engineering")
print("Employee:", emp)
print("Name:", emp.name, "| Dept:", emp.department)

# *** IMPORTANT NOTES — USE CASES ***
# - Functions can return multiple values as a tuple; unpack on the calling side.
# - x, y = y, x  is the Pythonic one-liner for swapping variables.
# - Tuples are ideal composite dict keys: (row, col), (city, country).
# - Unpack tuples directly in for-loop: for x, y in pairs.
# - namedtuple adds field names to tuples, improving readability with no overhead.
print("\n# NOTE: Tuples shine for multi-return, swapping, dict keys, loop unpacking.")


# =============================================================
#                   END OF TUTORIAL
# =============================================================

print("\n" + "=" * 60)
print("       END OF PYTHON TUPLES TUTORIAL")
print("=" * 60)
print("Topics covered:")
print("  1. Creating a Tuple")
print("  2. Indexing in a Tuple")
print("  3. Tuple Slicing")
print("  4. Operations on Tuples")
print("  5. Immutability of Tuples")
print("  6. Built-in Functions and Methods")
print("  7. Tuple vs List — Key Differences")
print("  8. Common Use Cases of Tuples")
print("=" * 60)
