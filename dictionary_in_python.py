# ============================================================
#          PYTHON DICTIONARIES — COMPREHENSIVE TUTORIAL
# ============================================================
# This file covers everything you need to know about Python Dictionaries:
#   1. Creating a Dictionary
#   2. Accessing Elements in a Dictionary
#   3. Modifying a Dictionary
#   4. Removing Elements from a Dictionary
#   5. Dictionary Operations
#   6. Built-in Functions and Methods
#   7. Dictionary vs Other Data Structures
#   8. Common Use Cases

print("=" * 60)
print("   PYTHON DICTIONARIES — COMPREHENSIVE TUTORIAL")
print("=" * 60)


# =============================================================
# SECTION 1: CREATING A DICTIONARY / WAYS TO CREATE IT
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 1: CREATING A DICTIONARY")
print("=" * 60)

# --- 1.1 Empty Dictionary ---
# An empty dictionary can be created in two ways:
empty_dict_1 = {}         # Using curly braces
empty_dict_2 = dict()     # Using the built-in dict() constructor

print("\n--- 1.1 Empty Dictionaries ---")
print("Using {}:     ", empty_dict_1)
print("Using dict(): ", empty_dict_2)

# --- 1.2 Dictionary with Key-Value Pairs ---
# A dictionary stores data as key: value pairs.
person = {"name": "Alice", "age": 30, "city": "New York"}
scores = {"math": 95, "science": 88, "english": 72}

print("\n--- 1.2 Dictionary with Key-Value Pairs ---")
print("Person: ", person)
print("Scores: ", scores)

# --- 1.3 Using dict() Constructor ---
# You can create a dictionary using keyword arguments with dict().
person2 = dict(name="Bob", age=25, city="London")
print("\n--- 1.3 Using dict() Constructor with Keyword Arguments ---")
print("Person2:", person2)

# Creating a dictionary from a list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
from_tuples = dict(pairs)
print("From list of tuples:", from_tuples)   # {'a': 1, 'b': 2, 'c': 3}

# Creating a dictionary using zip()
keys   = ["name", "age", "city"]
values = ["Charlie", 28, "Tokyo"]
from_zip = dict(zip(keys, values))
print("From zip():         ", from_zip)      # {'name': 'Charlie', 'age': 28, 'city': 'Tokyo'}

# --- 1.4 Nested Dictionaries ---
# A dictionary can contain other dictionaries as values.
students = {
    "student1": {"name": "Alice", "grade": "A"},
    "student2": {"name": "Bob",   "grade": "B"},
}
print("\n--- 1.4 Nested Dictionaries ---")
print("Students:", students)
print("student1 name:", students["student1"]["name"])   # Alice

# --- 1.5 Dictionary Comprehension ---
# A concise way to create dictionaries using a single-line expression.
squares = {x: x ** 2 for x in range(1, 6)}
even_squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}

print("\n--- 1.5 Dictionary Comprehension ---")
print("Squares 1-5:        ", squares)       # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("Even squares 1-10:  ", even_squares)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# --- 1.6 Using dict.fromkeys() ---
# Creates a dictionary with specified keys and an optional default value.
keys_list = ["a", "b", "c", "d"]
default_dict  = dict.fromkeys(keys_list)        # default value is None
value_dict    = dict.fromkeys(keys_list, 0)     # all keys set to 0

print("\n--- 1.6 Using dict.fromkeys() ---")
print("fromkeys (None default): ", default_dict)   # {'a': None, 'b': None, ...}
print("fromkeys (0 default):    ", value_dict)     # {'a': 0, 'b': 0, 'c': 0, 'd': 0}

# *** IMPORTANT NOTES — CREATING A DICTIONARY ***
# - Dictionary keys MUST be immutable: strings, numbers, tuples are valid keys.
# - Lists and dictionaries CANNOT be used as keys (they are mutable).
# - Duplicate keys are NOT allowed; the last value wins.
# - As of Python 3.7+, dictionaries maintain insertion order.
print("\n# NOTE: Keys must be immutable (str, int, tuple). Lists/dicts cannot be keys.")
print("# NOTE: Duplicate keys — the last value overwrites the earlier one.")
dup_key_dict = {"a": 1, "a": 2, "a": 3}
print("Duplicate keys — {'a':1,'a':2,'a':3} →", dup_key_dict)   # {'a': 3}

# Valid key types:
valid_keys = {
    "string_key": "value1",
    42:            "value2",
    (1, 2):        "value3",    # tuple is immutable → valid key
}
print("Valid key types:", valid_keys)

# Invalid key (uncomment to see TypeError):
# invalid = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'


# =============================================================
# SECTION 2: ACCESSING ELEMENTS IN A DICTIONARY
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 2: ACCESSING ELEMENTS IN A DICTIONARY")
print("=" * 60)

person = {"name": "Alice", "age": 30, "city": "New York", "hobby": "reading"}
print("\nDictionary:", person)

# --- 2.1 Accessing Values using Keys ---
# Use dict[key] to retrieve the value for a given key.
print("\n--- 2.1 Accessing Values using Keys ---")
print("person['name']:  ", person["name"])    # Alice
print("person['age']:   ", person["age"])     # 30
print("person['hobby']: ", person["hobby"])   # reading

# --- 2.2 Using get() Method (Safe Access) ---
# get(key) returns None if the key doesn't exist (no error).
# get(key, default) returns the default value if the key doesn't exist.
print("\n--- 2.2 Using get() Method ---")
print("get('name'):           ", person.get("name"))            # Alice
print("get('score'):          ", person.get("score"))           # None (key not present)
print("get('score', 0):       ", person.get("score", 0))        # 0   (default used)
print("get('age', 'Unknown'): ", person.get("age", "Unknown"))  # 30

# --- 2.3 Accessing All Keys ---
# keys() returns a view object of all keys in the dictionary.
print("\n--- 2.3 Accessing All Keys — keys() ---")
print("person.keys():  ", person.keys())    # dict_keys(['name', 'age', 'city', 'hobby'])
print("As list:        ", list(person.keys()))

# --- 2.4 Accessing All Values ---
# values() returns a view object of all values in the dictionary.
print("\n--- 2.4 Accessing All Values — values() ---")
print("person.values(): ", person.values())   # dict_values(['Alice', 30, 'New York', 'reading'])
print("As list:         ", list(person.values()))

# --- 2.5 Accessing All Key-Value Pairs ---
# items() returns a view object of (key, value) tuple pairs.
print("\n--- 2.5 Accessing All Key-Value Pairs — items() ---")
print("person.items(): ", person.items())
print("As list:        ", list(person.items()))

# --- 2.6 KeyError when Accessing Non-Existent Key ---
# Accessing a key that doesn't exist with [] raises KeyError.
print("\n--- 2.6 KeyError Example ---")
try:
    print(person["score"])    # This key doesn't exist in the dictionary
except KeyError as e:
    print("KeyError caught:", e)

# *** IMPORTANT NOTES — ACCESSING ***
# - dict[key] raises KeyError if the key doesn't exist.
# - get() is safer — returns None (or a default) instead of raising an error.
# - keys(), values(), items() return VIEW objects — they reflect changes to the dict.
# - Prefer get() when the key might not exist.
print("\n# NOTE: Use get() instead of [] when a key might be missing.")
print("# NOTE: keys(), values(), items() return live view objects, not copies.")


# =============================================================
# SECTION 3: MODIFYING A DICTIONARY
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 3: MODIFYING A DICTIONARY")
print("=" * 60)

info = {"name": "Alice", "age": 30}
print("\nOriginal:", info)

# --- 3.1 Adding New Key-Value Pairs ---
# Assign a value to a new key to add it to the dictionary.
info["city"] = "New York"
info["hobby"] = "reading"
print("\n--- 3.1 Adding New Key-Value Pairs ---")
print("After adding 'city' and 'hobby':", info)

# --- 3.2 Updating Existing Values ---
# Assigning to an existing key overwrites its value.
info["age"] = 31
print("\n--- 3.2 Updating Existing Values ---")
print("After updating 'age' to 31:", info)

# --- 3.3 Using update() Method ---
# update() merges another dictionary (or iterable of key-value pairs) into the current one.
info.update({"city": "Boston", "job": "Engineer"})
print("\n--- 3.3 Using update() Method ---")
print("After update({'city':'Boston','job':'Engineer'}):", info)

# update() with keyword arguments
info.update(age=32, points=75000)
print("After update(age=32, points=75000):", info)

# --- 3.4 Merge Operator | (Python 3.9+) ---
# The | operator creates a NEW merged dictionary without modifying the originals.
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 99, "c": 3}    # key "b" appears in both — dict2 value wins
merged = dict1 | dict2
print("\n--- 3.4 Merge Operator | (Python 3.9+) ---")
print("dict1:          ", dict1)    # unchanged
print("dict2:          ", dict2)    # unchanged
print("dict1 | dict2:  ", merged)   # {'a': 1, 'b': 99, 'c': 3}

# --- 3.5 Update Operator |= (Python 3.9+) ---
# The |= operator updates the dictionary IN PLACE (modifies the original).
dict3 = {"x": 10, "y": 20}
dict3 |= {"y": 99, "z": 30}
print("\n--- 3.5 Update Operator |= (Python 3.9+) ---")
print("After dict3 |= {'y':99,'z':30}:", dict3)   # {'x': 10, 'y': 99, 'z': 30}

# --- 3.6 Using setdefault() ---
# setdefault(key, default) sets the key to default ONLY if the key doesn't exist.
# If the key already exists, it leaves the value unchanged and returns it.
config = {"theme": "dark", "font_size": 14}
print("\n--- 3.6 Using setdefault() ---")
result1 = config.setdefault("theme", "light")       # key exists → no change
result2 = config.setdefault("language", "English")  # key missing → sets it
print("setdefault('theme','light'):      ", result1)  # dark (existing value)
print("setdefault('language','English'): ", result2)  # English (newly set)
print("Config after setdefault():        ", config)

# *** IMPORTANT NOTES — MODIFYING ***
# - dict[key] = value adds a new key or updates an existing one.
# - update() can accept a dict, a list of (key,value) tuples, or keyword args.
# - | creates a new dict; |= modifies in place (both Python 3.9+).
# - setdefault() is useful for initialising missing keys safely.
print("\n# NOTE: | creates a new dict; |= modifies in place (Python 3.9+).")
print("# NOTE: setdefault() only sets a value if the key does NOT already exist.")


# =============================================================
# SECTION 4: REMOVING ELEMENTS FROM A DICTIONARY
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 4: REMOVING ELEMENTS FROM A DICTIONARY")
print("=" * 60)

data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print("\nOriginal:", data)

# --- 4.1 pop(key) — Remove by Key and Return Value ---
# pop(key) removes the key and returns its value. Raises KeyError if not found.
removed_val = data.pop("b")
print("\n--- 4.1 pop(key) ---")
print("data.pop('b') returned:", removed_val)   # 2
print("Dictionary after pop:  ", data)

# --- 4.2 pop(key, default) — Remove with Default ---
# pop(key, default) returns the default value instead of raising KeyError.
safe_removed = data.pop("z", "Not Found")
print("\n--- 4.2 pop(key, default) ---")
print("data.pop('z', 'Not Found'):", safe_removed)   # Not Found
print("Dictionary unchanged:      ", data)

# --- 4.3 popitem() — Remove and Return Last Inserted Pair ---
# popitem() removes and returns the LAST inserted key-value pair as a tuple.
last_item = data.popitem()
print("\n--- 4.3 popitem() ---")
print("data.popitem() returned:", last_item)   # ('e', 5)
print("Dictionary after popitem:", data)

# --- 4.4 del dict[key] — Delete a Specific Key ---
# del removes a specific key-value pair. Raises KeyError if key doesn't exist.
del data["c"]
print("\n--- 4.4 del dict[key] ---")
print("After del data['c']:", data)

# --- 4.5 clear() — Remove All Elements ---
# clear() empties the dictionary, leaving it intact (not deleted).
clear_data = {"x": 10, "y": 20, "z": 30}
clear_data.clear()
print("\n--- 4.5 clear() ---")
print("After clear():", clear_data)   # {}

# --- 4.6 del dict — Delete the Entire Dictionary Variable ---
# del dict removes the variable entirely from memory.
temp_dict = {"key": "value"}
del temp_dict
print("\n--- 4.6 del dict ---")
try:
    print(temp_dict)    # NameError: name 'temp_dict' is not defined
except NameError as e:
    print("NameError after del temp_dict:", e)

# *** IMPORTANT NOTES — REMOVING ***
# - pop(key) raises KeyError if the key is not found (use default to avoid this).
# - popitem() raises KeyError if the dictionary is empty.
# - del dict[key] raises KeyError if the key doesn't exist.
# - clear() empties the dict but keeps the variable; del dict removes the variable.
print("\n# NOTE: pop() / del raise KeyError for missing keys.")
print("# NOTE: clear() empties the dict; del removes the variable entirely.")
try:
    {}.popitem()    # Empty dict → KeyError
except KeyError as e:
    print("KeyError from popitem() on empty dict:", e)


# =============================================================
# SECTION 5: DICTIONARY OPERATIONS
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 5: DICTIONARY OPERATIONS")
print("=" * 60)

inventory = {"apple": 10, "banana": 5, "cherry": 20}
print("\nDictionary:", inventory)

# --- 5.1 Membership Test (in / not in) ---
# 'in' and 'not in' check for KEY existence, NOT values.
print("\n--- 5.1 Membership Test (in / not in) — checks KEYS only ---")
print("'apple' in inventory:     ", "apple" in inventory)      # True
print("'grape' in inventory:     ", "grape" in inventory)      # False
print("'grape' not in inventory: ", "grape" not in inventory)  # True
print("10 in inventory:          ", 10 in inventory)           # False (10 is a value, not a key)

# --- 5.2 Comparison (== and !=) ---
# Two dictionaries are equal if they have identical key-value pairs (order doesn't matter).
print("\n--- 5.2 Comparison (== and !=) ---")
d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}    # Same pairs, different insertion order
d3 = {"a": 1, "b": 9}
print("d1 == d2:", d1 == d2)   # True  — order doesn't matter for equality
print("d1 == d3:", d1 == d3)   # False — value of 'b' differs
print("d1 != d3:", d1 != d3)   # True

# --- 5.3 Length (len()) ---
print("\n--- 5.3 Length with len() ---")
print("len(inventory):", len(inventory))   # 3

# --- 5.4 Iterating Through a Dictionary ---
print("\n--- 5.4 Iterating Through a Dictionary ---")

# Iterating over keys (default behaviour)
print("Keys:   ", end="")
for key in inventory:
    print(key, end="  ")
print()

# Iterating over values
print("Values: ", end="")
for value in inventory.values():
    print(value, end="  ")
print()

# Iterating over key-value pairs
print("Items:")
for key, value in inventory.items():
    print(f"  {key}: {value}")

# --- 5.5 Dictionary Unpacking (**) ---
# ** unpacks a dictionary into keyword arguments or merges dictionaries.
print("\n--- 5.5 Dictionary Unpacking (**) ---")
defaults = {"color": "blue", "size": "medium", "weight": 1.0}
overrides = {"color": "red", "weight": 2.5}
combined = {**defaults, **overrides}   # overrides takes precedence for duplicate keys
print("defaults:        ", defaults)
print("overrides:       ", overrides)
print("{**defaults, **overrides}:", combined)   # {'color': 'red', 'size': 'medium', 'weight': 2.5}

# Using ** to pass dict as function keyword arguments
def greet(name, age):
    return f"Hello, {name}! You are {age} years old."

params = {"name": "Alice", "age": 30}
print("greet(**params):", greet(**params))

# *** IMPORTANT NOTES — OPERATIONS ***
# - 'in' checks KEYS only; use 'in dict.values()' to check values.
# - Dictionary equality ignores insertion order (Python 3.7+).
# - {**d1, **d2} is a clean way to merge dicts (alternative to | in Python 3.9+).
print("\n# NOTE: 'in' checks keys only. Use 'in dict.values()' for value checks.")
print("# NOTE: Dict equality ignores order — {a:1,b:2} == {b:2,a:1} is True.")


# =============================================================
# SECTION 6: BUILT-IN FUNCTIONS AND METHODS
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 6: BUILT-IN FUNCTIONS AND METHODS")
print("=" * 60)

nums_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
print("\nDictionary:", nums_dict)

# --- 6.1 len(), sorted(), min(), max(), sum() ---
# These built-in functions operate on the KEYS by default.
print("\n--- 6.1 len(), sorted(), min(), max(), sum() ---")
print("len():         ", len(nums_dict))              # 5 (number of key-value pairs)
print("sorted():      ", sorted(nums_dict))           # sorted list of keys alphabetically
print("min() (keys):  ", min(nums_dict))              # 'five' (alphabetically smallest key)
print("max() (keys):  ", max(nums_dict))              # 'two'  (alphabetically largest key)

# To apply min/max/sum on values, pass dict.values():
print("min(values):   ", min(nums_dict.values()))     # 1
print("max(values):   ", max(nums_dict.values()))     # 5
print("sum(values):   ", sum(nums_dict.values()))     # 15

# sorted() with key parameter on values:
sorted_by_val = sorted(nums_dict.items(), key=lambda x: x[1])
print("sorted by value:", sorted_by_val)

# --- 6.2 copy() — Shallow Copy ---
# copy() returns a shallow copy of the dictionary (a new dict with the same references).
print("\n--- 6.2 copy() — Shallow Copy ---")
original = {"a": [1, 2, 3], "b": 4}
shallow  = original.copy()
shallow["b"] = 99           # modifying a primitive value does NOT affect original
shallow["a"].append(999)    # modifying a mutable value DOES affect original (shared reference)
print("original after shallow copy modification:", original)  # 'a' list is shared!
print("shallow:                                 ", shallow)

# --- 6.3 Difference Between copy() and = Assignment ---
print("\n--- 6.3 copy() vs = Assignment ---")
dict_a = {"x": 1, "y": 2}
dict_b = dict_a           # Both variables point to the SAME dictionary
dict_c = dict_a.copy()    # dict_c is a NEW, independent (shallow) copy

dict_b["x"] = 999         # Modifies the original via dict_b
print("dict_a after dict_b['x'] = 999:", dict_a)   # {'x': 999, 'y': 2} — also changed!
print("dict_c (copied before change): ", dict_c)   # {'x': 1, 'y': 2}  — unchanged

# --- 6.4 any() and all() ---
# any() and all() operate on KEYS by default (truthy/falsy check).
print("\n--- 6.4 any() and all() ---")
bool_dict = {0: "zero", 1: "one", 2: "two"}   # Key 0 is falsy
print("any({0:'zero',1:'one',2:'two'}):", any(bool_dict))   # True (keys 1 and 2 are truthy)
print("all({0:'zero',1:'one',2:'two'}):", all(bool_dict))   # False (key 0 is falsy)

status_dict = {"connected": True, "logged_in": True, "verified": True}
print("all(values):", all(status_dict.values()))   # True

# *** IMPORTANT NOTES — BUILT-IN FUNCTIONS ***
# - copy() does a SHALLOW copy; nested mutable objects are still shared.
# - Use copy.deepcopy() for a fully independent deep copy.
# - = does NOT copy a dict — it creates another reference to the same object.
# - any() / all() check keys by default; use .values() to check values.
print("\n# NOTE: copy() is shallow — use copy.deepcopy() for nested mutable objects.")
print("# NOTE: = assignment does NOT copy; both variables point to the same dict.")


# =============================================================
# SECTION 7: DICTIONARY vs OTHER DATA STRUCTURES
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 7: DICTIONARY vs OTHER DATA STRUCTURES")
print("=" * 60)

# --- 7.1 Dictionary vs List ---
print("\n--- 7.1 Dictionary vs List ---")
# List: ordered collection, accessed by integer index.
# Dict: key-value pairs, accessed by any immutable key.
shopping_list = ["apple", "banana", "cherry"]           # List
shopping_dict = {"apple": 10, "banana": 5, "cherry": 8} # Dict

print("List access by index:  shopping_list[0] →", shopping_list[0])
print("Dict access by key:    shopping_dict['apple'] →", shopping_dict["apple"])

# --- 7.2 Dictionary vs Set ---
print("\n--- 7.2 Dictionary vs Set ---")
# Set: unordered collection of UNIQUE elements, no key-value association.
# Dict: unordered collection of unique KEYS, each mapped to a value.
my_set  = {"apple", "banana", "cherry"}
my_dict = {"apple": 1, "banana": 2, "cherry": 3}
print("Set:  ", my_set)
print("Dict: ", my_dict)
# Both use {} syntax — but {} alone creates an empty DICT, not an empty set!
print("type({}):  ", type({}))          # <class 'dict'>
print("type({1}): ", type({1}))         # <class 'set'>

# --- 7.3 Dictionary vs Tuple ---
print("\n--- 7.3 Dictionary vs Tuple ---")
# Tuple: ordered, immutable sequence, accessed by index.
# Dict: mutable key-value store, accessed by key.
point_tuple = (10, 20)                   # Tuple: position by index
point_dict  = {"x": 10, "y": 20}        # Dict: position by name
print("Tuple access: point_tuple[0] →", point_tuple[0])
print("Dict access:  point_dict['x'] →", point_dict["x"])

# --- 7.4 Comparison Table (via comments) ---
# ┌──────────────┬──────────────┬────────────┬────────────┬───────────┐
# │ Feature      │ Dictionary   │ List       │ Set        │ Tuple     │
# ├──────────────┼──────────────┼────────────┼────────────┼───────────┤
# │ Ordered      │ Yes (3.7+)   │ Yes        │ No         │ Yes       │
# │ Mutable      │ Yes          │ Yes        │ Yes        │ No        │
# │ Duplicates   │ Keys: No     │ Yes        │ No         │ Yes       │
# │ Access by    │ Key          │ Index      │ -          │ Index     │
# │ Syntax       │ {k: v}       │ [x, y]     │ {x, y}     │ (x, y)    │
# └──────────────┴──────────────┴────────────┴────────────┴───────────┘
print("\n--- 7.4 When to Use a Dictionary ---")
print("Use a dict when you need to associate keys with values (like a lookup table).")
print("Use a list when you need an ordered sequence accessed by position.")
print("Use a set when you only need unique elements with no associated data.")
print("Use a tuple when you need an immutable ordered sequence.")


# =============================================================
# SECTION 8: COMMON USE CASES
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 8: COMMON USE CASES")
print("=" * 60)

# --- 8.1 Counting Occurrences (Word Frequency) ---
print("\n--- 8.1 Counting Occurrences (Word Frequency) ---")
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("Words:", words)
print("Word frequency:", word_count)   # {'apple': 3, 'banana': 2, 'cherry': 1}

# --- 8.2 Grouping Data ---
print("\n--- 8.2 Grouping Data ---")
people = [
    {"name": "Alice", "dept": "Engineering"},
    {"name": "Bob",   "dept": "Marketing"},
    {"name": "Carol", "dept": "Engineering"},
    {"name": "Dave",  "dept": "Marketing"},
    {"name": "Eve",   "dept": "Engineering"},
]
by_dept = {}
for person in people:
    dept = person["dept"]
    by_dept.setdefault(dept, []).append(person["name"])
print("Grouped by department:", by_dept)

# --- 8.3 Caching / Memoization ---
print("\n--- 8.3 Caching / Memoization ---")
cache = {}

def fibonacci(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    result = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = result
    return result

print("Fibonacci(10):", fibonacci(10))   # 55
print("Fibonacci(15):", fibonacci(15))   # 610
print("Cache contents:", cache)

# --- 8.4 JSON-like Data Structures ---
print("\n--- 8.4 JSON-like Data Structures ---")
user_profile = {
    "id": 101,
    "username": "alice123",
    "email": "alice@example.com",
    "preferences": {
        "theme": "dark",
        "notifications": True,
        "language": "en"
    },
    "scores": [95, 88, 72]
}
print("User profile:", user_profile)
print("Username:    ", user_profile["username"])
print("Theme:       ", user_profile["preferences"]["theme"])
print("First score: ", user_profile["scores"][0])

# --- 8.5 Default Values with collections.defaultdict ---
print("\n--- 8.5 Default Values with collections.defaultdict ---")
from collections import defaultdict

# defaultdict automatically creates a default value for missing keys.
dd_list   = defaultdict(list)    # default value is an empty list
dd_int    = defaultdict(int)     # default value is 0

dd_list["fruits"].append("apple")
dd_list["fruits"].append("banana")
dd_list["vegs"].append("carrot")
print("defaultdict(list):", dict(dd_list))   # {'fruits': ['apple', 'banana'], 'vegs': ['carrot']}

for word in ["hello", "world", "hello", "python", "world", "hello"]:
    dd_int[word] += 1
print("defaultdict(int) word count:", dict(dd_int))

# --- 8.6 Ordered Dictionaries Note ---
print("\n--- 8.6 Ordered Dictionaries (Python 3.7+) ---")
# Since Python 3.7, standard dicts maintain INSERTION ORDER.
ordered = {}
ordered["first"]  = 1
ordered["second"] = 2
ordered["third"]  = 3
print("Insertion order preserved:", ordered)   # {'first': 1, 'second': 2, 'third': 3}

# collections.OrderedDict was needed before Python 3.7;
# still useful when order-aware equality is required.
from collections import OrderedDict
od1 = OrderedDict([("a", 1), ("b", 2)])
od2 = OrderedDict([("b", 2), ("a", 1)])
print("OrderedDict od1 == od2:", od1 == od2)   # False (order matters for OrderedDict)
print("Regular dict  d1 == d2:", {"a":1,"b":2} == {"b":2,"a":1})   # True

# *** IMPORTANT NOTES — USE CASES ***
# - Use get() + default for safe counting/grouping without KeyError.
# - Use setdefault() to initialise missing list/dict values elegantly.
# - defaultdict saves boilerplate when all keys share the same default type.
# - Python 3.7+ dicts are ordered by insertion; OrderedDict is rarely needed now.
print("\n# NOTE: Python 3.7+ dicts maintain insertion order.")
print("# NOTE: Use defaultdict to avoid manual key initialisation.")


# =============================================================
#                   END OF TUTORIAL
# =============================================================

print("\n" + "=" * 60)
print("       END OF PYTHON DICTIONARIES TUTORIAL")
print("=" * 60)
print("Topics covered:")
print("  1. Creating a Dictionary")
print("  2. Accessing Elements in a Dictionary")
print("  3. Modifying a Dictionary")
print("  4. Removing Elements from a Dictionary")
print("  5. Dictionary Operations")
print("  6. Built-in Functions and Methods")
print("  7. Dictionary vs Other Data Structures")
print("  8. Common Use Cases")
print("=" * 60)
