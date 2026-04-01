# ============================================================
#              PYTHON SETS — COMPREHENSIVE TUTORIAL
# ============================================================
# This file covers everything you need to know about Python Sets:
#   1. Creating a Set
#   2. Adding and Removing Elements
#   3. Set Operations (Mathematical)
#   4. Set Update Operations (In-place)
#   5. Set Comparison and Membership
#   6. Built-in Functions with Sets
#   7. Frozen Sets
#   8. Set vs Other Data Structures
#   9. Common Use Cases

print("=" * 60)
print("         PYTHON SETS — COMPREHENSIVE TUTORIAL")
print("=" * 60)


# =============================================================
# SECTION 1: CREATING A SET / WAYS TO CREATE A SET
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 1: CREATING A SET")
print("=" * 60)

# --- 1.1 Empty Set ---
# IMPORTANT: You CANNOT use {} to create an empty set — that creates an empty DICT!
# Use set() to create an empty set.
empty_set  = set()    # Correct way to create an empty set
empty_dict = {}       # This is an empty DICTIONARY, NOT a set!

print("\n--- 1.1 Empty Set (set() only — NOT {}) ---")
print("set():    ", empty_set,  "| type:", type(empty_set))   # set()  | <class 'set'>
print("{}:       ", empty_dict, "| type:", type(empty_dict))  # {}     | <class 'dict'>
# NOTE: Always use set() for an empty set. {} creates an empty dict!

# --- 1.2 Set with Values ---
# Use curly braces {} with values (NOT empty!) to create a set.
fruits_set  = {"apple", "banana", "cherry"}
numbers_set = {1, 2, 3, 4, 5}
mixed_set   = {1, "hello", 3.14, True}   # Mixed immutable types

print("\n--- 1.2 Set with Values ---")
print("Fruits:  ", fruits_set)
print("Numbers: ", numbers_set)
print("Mixed:   ", mixed_set)

# --- 1.3 Using set() Constructor with Iterables ---
# set() can convert any iterable into a set (duplicates are automatically removed).
from_list   = set([1, 2, 3, 2, 1, 4])       # Duplicates removed
from_string = set("hello")                  # Each character becomes an element
from_tuple  = set((10, 20, 30, 20, 10))     # Duplicates removed
from_range  = set(range(1, 6))              # {1, 2, 3, 4, 5}

print("\n--- 1.3 set() Constructor with Iterables ---")
print("From list [1,2,3,2,1,4]:   ", from_list)    # {1, 2, 3, 4}
print("From string 'hello':       ", from_string)  # {'h', 'e', 'l', 'o'}
print("From tuple (10,20,30,20):  ", from_tuple)   # {10, 20, 30}
print("From range(1,6):           ", from_range)   # {1, 2, 3, 4, 5}

# --- 1.4 Set Comprehension ---
# A concise way to create sets using a single-line expression.
squares_set     = {x ** 2 for x in range(1, 6)}
even_set        = {x for x in range(1, 11) if x % 2 == 0}
unique_lengths  = {len(word) for word in ["cat", "dog", "elephant", "ant", "bee"]}

print("\n--- 1.4 Set Comprehension ---")
print("Squares 1-5:       ", squares_set)       # {1, 4, 9, 16, 25}
print("Even numbers 1-10: ", even_set)          # {2, 4, 6, 8, 10}
print("Unique word lengths:", unique_lengths)   # {3, 8} (cat/dog/ant/bee=3, elephant=8)

# *** IMPORTANT NOTES — CREATING A SET ***
# - Sets contain ONLY UNIQUE elements — duplicates are automatically discarded.
# - Sets are UNORDERED — there is no indexing, slicing, or positional access.
# - Set elements MUST be immutable (strings, numbers, tuples are valid).
# - Lists and dictionaries CANNOT be elements of a set (they are mutable/unhashable).
# - {} creates an empty DICT; always use set() for an empty set.
print("\n# NOTE: {} creates an empty dict — use set() for an empty set.")
print("# NOTE: Sets are unordered and contain only unique elements.")
print("# NOTE: Elements must be immutable (str, int, tuple — NOT list or dict).")
# Invalid element (uncomment to see TypeError):
# bad_set = {[1, 2], 3}  # TypeError: unhashable type: 'list'


# =============================================================
# SECTION 2: ADDING AND REMOVING ELEMENTS
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 2: ADDING AND REMOVING ELEMENTS")
print("=" * 60)

colors = {"red", "green", "blue"}
print("\nOriginal set:", colors)

# --- 2.1 add() — Add a Single Element ---
# add(element) adds one element to the set.
# Adding an existing element has no effect (no duplicates).
colors.add("yellow")
colors.add("red")     # 'red' already exists — no change, no error
print("\n--- 2.1 add() ---")
print("After add('yellow') and add('red'):", colors)

# --- 2.2 update() — Add Multiple Elements from an Iterable ---
# update() adds all elements from an iterable (list, tuple, set, string).
colors.update(["purple", "orange"])
colors.update({"pink", "white"})   # can also accept another set
print("\n--- 2.2 update() ---")
print("After update(['purple','orange']) and update({'pink','white'}):", colors)

# --- 2.3 remove() — Remove an Element (Raises KeyError if Not Found) ---
# remove(element) removes the element; raises KeyError if it doesn't exist.
sample = {"a", "b", "c", "d"}
sample.remove("b")
print("\n--- 2.3 remove() ---")
print("After remove('b'):", sample)
try:
    sample.remove("z")   # 'z' doesn't exist
except KeyError as e:
    print("KeyError from remove('z'):", e)

# --- 2.4 discard() — Remove an Element (No Error if Not Found) ---
# discard(element) removes the element silently if it doesn't exist.
sample.discard("c")
sample.discard("z")   # 'z' doesn't exist — NO error, just silently ignored
print("\n--- 2.4 discard() ---")
print("After discard('c') and discard('z'):", sample)

# --- 2.5 pop() — Remove and Return an Arbitrary Element ---
# pop() removes and returns an arbitrary element (sets are unordered).
# Raises KeyError if the set is empty.
pop_set = {10, 20, 30, 40, 50}
popped = pop_set.pop()
print("\n--- 2.5 pop() ---")
print("Popped element (arbitrary):", popped)
print("Set after pop():           ", pop_set)

# --- 2.6 clear() — Remove All Elements ---
clear_set = {1, 2, 3, 4, 5}
clear_set.clear()
print("\n--- 2.6 clear() ---")
print("After clear():", clear_set)   # set()

# *** IMPORTANT NOTES — ADDING AND REMOVING ***
# - add() adds one element; update() adds multiple elements from any iterable.
# - remove() raises KeyError for missing elements; discard() does NOT.
# - pop() removes an ARBITRARY element (not necessarily the "last" one — sets are unordered).
# - clear() empties the set but keeps the variable.
print("\n# NOTE: remove() raises KeyError if element missing; discard() does not.")
print("# NOTE: pop() removes an arbitrary element — sets have no defined order.")


# =============================================================
# SECTION 3: SET OPERATIONS (MATHEMATICAL)
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 3: SET OPERATIONS (MATHEMATICAL)")
print("=" * 60)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("\nSet A:", A)
print("Set B:", B)

# --- 3.1 Union (| or union()) ---
# All elements from BOTH sets (duplicates removed).
# Visual: A ∪ B = everything in A or B or both
print("\n--- 3.1 Union (A | B or A.union(B)) ---")
print("A | B:       ", A | B)             # {1, 2, 3, 4, 5, 6, 7, 8}
print("A.union(B):  ", A.union(B))        # {1, 2, 3, 4, 5, 6, 7, 8}
# union() method can also accept other iterables (not just sets):
print("A.union([6,7,9]):", A.union([6, 7, 9]))   # {1, 2, 3, 4, 5, 6, 7, 9}

# --- 3.2 Intersection (& or intersection()) ---
# Only elements that appear in BOTH sets.
# Visual: A ∩ B = only what's shared between A and B
print("\n--- 3.2 Intersection (A & B or A.intersection(B)) ---")
print("A & B:               ", A & B)              # {4, 5}
print("A.intersection(B):   ", A.intersection(B))  # {4, 5}

# --- 3.3 Difference (- or difference()) ---
# Elements in the FIRST set but NOT in the second.
# Visual: A - B = elements only in A (not in B)
print("\n--- 3.3 Difference (A - B or A.difference(B)) ---")
print("A - B:              ", A - B)             # {1, 2, 3}  (in A, not in B)
print("B - A:              ", B - A)             # {6, 7, 8}  (in B, not in A)
print("A.difference(B):    ", A.difference(B))   # {1, 2, 3}

# --- 3.4 Symmetric Difference (^ or symmetric_difference()) ---
# Elements in EITHER set, but NOT in BOTH (opposite of intersection).
# Visual: A △ B = elements in A or B, but NOT in both
print("\n--- 3.4 Symmetric Difference (A ^ B or A.symmetric_difference(B)) ---")
print("A ^ B:                       ", A ^ B)                       # {1, 2, 3, 6, 7, 8}
print("A.symmetric_difference(B):   ", A.symmetric_difference(B))   # {1, 2, 3, 6, 7, 8}

# *** IMPORTANT NOTES — SET OPERATIONS ***
# - Operators (|, &, -, ^) only work with SET operands.
# - Methods (.union(), .intersection(), etc.) accept any iterable.
# - All operations return a NEW set; the originals are not modified.
print("\n# NOTE: Operators require set operands; methods accept any iterable.")
print("# NOTE: Set operations always return a NEW set — originals are unchanged.")
print("A after all operations:", A)   # unchanged


# =============================================================
# SECTION 4: SET UPDATE OPERATIONS (IN-PLACE)
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 4: SET UPDATE OPERATIONS (IN-PLACE)")
print("=" * 60)

# These operations modify the set IN PLACE (no new set is created).

# --- 4.1 update() / |= — Union Update ---
# Adds all elements from another set/iterable to the current set.
s1 = {1, 2, 3}
s1.update({3, 4, 5})          # same as s1 |= {3, 4, 5}
print("\n--- 4.1 update() / |= — Union Update ---")
print("After s1.update({3,4,5}):", s1)   # {1, 2, 3, 4, 5}

s2 = {10, 20, 30}
s2 |= {30, 40, 50}
print("After s2 |= {30,40,50}: ", s2)   # {10, 20, 30, 40, 50}

# --- 4.2 intersection_update() / &= — Intersection Update ---
# Keeps ONLY the elements that are in BOTH sets.
s3 = {1, 2, 3, 4, 5}
s3.intersection_update({3, 4, 5, 6, 7})   # same as s3 &= {3, 4, 5, 6, 7}
print("\n--- 4.2 intersection_update() / &= ---")
print("After intersection_update({3,4,5,6,7}):", s3)   # {3, 4, 5}

s4 = {1, 2, 3, 4, 5}
s4 &= {2, 4, 6}
print("After s4 &= {2,4,6}:                   ", s4)   # {2, 4}

# --- 4.3 difference_update() / -= — Difference Update ---
# Removes all elements found in the other set.
s5 = {1, 2, 3, 4, 5}
s5.difference_update({3, 4})   # same as s5 -= {3, 4}
print("\n--- 4.3 difference_update() / -= ---")
print("After difference_update({3,4}):", s5)   # {1, 2, 5}

s6 = {10, 20, 30, 40}
s6 -= {20, 40}
print("After s6 -= {20,40}:          ", s6)   # {10, 30}

# --- 4.4 symmetric_difference_update() / ^= — Symmetric Difference Update ---
# Keeps elements that are in EITHER set, but NOT in BOTH.
s7 = {1, 2, 3, 4}
s7.symmetric_difference_update({3, 4, 5, 6})   # same as s7 ^= {3, 4, 5, 6}
print("\n--- 4.4 symmetric_difference_update() / ^= ---")
print("After symmetric_difference_update({3,4,5,6}):", s7)   # {1, 2, 5, 6}

s8 = {1, 2, 3}
s8 ^= {2, 3, 4}
print("After s8 ^= {2,3,4}:                        ", s8)   # {1, 4}

# *** IMPORTANT NOTES — IN-PLACE OPERATIONS ***
# - In-place operators (|=, &=, -=, ^=) MODIFY the original set.
# - Non-in-place operators (|, &, -, ^) return a NEW set.
print("\n# NOTE: In-place operators (&=, |=, -=, ^=) modify the original set.")


# =============================================================
# SECTION 5: SET COMPARISON AND MEMBERSHIP
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 5: SET COMPARISON AND MEMBERSHIP")
print("=" * 60)

primes  = {2, 3, 5, 7, 11, 13}
evens   = {2, 4, 6, 8, 10}
small   = {2, 3, 5}

# --- 5.1 Membership Testing (in / not in) ---
print("\n--- 5.1 Membership Testing (in / not in) ---")
print("2 in primes:     ", 2 in primes)      # True
print("4 in primes:     ", 4 in primes)      # False
print("4 not in primes: ", 4 not in primes)  # True

# --- 5.2 Equality (== and !=) ---
# Two sets are equal if they contain exactly the same elements (order doesn't apply).
print("\n--- 5.2 Equality (== and !=) ---")
print("{1,2,3} == {3,2,1}:", {1, 2, 3} == {3, 2, 1})   # True — order doesn't matter
print("{1,2,3} != {1,2,4}:", {1, 2, 3} != {1, 2, 4})   # True

# --- 5.3 issubset() / <= — Is Subset ---
# A is a subset of B if ALL elements of A are also in B.
print("\n--- 5.3 issubset() / <= ---")
print("small.issubset(primes):  ", small.issubset(primes))   # True  (2,3,5 ⊆ primes)
print("small <= primes:         ", small <= primes)           # True
print("primes.issubset(small):  ", primes.issubset(small))   # False

# --- 5.4 issuperset() / >= — Is Superset ---
# A is a superset of B if ALL elements of B are also in A.
print("\n--- 5.4 issuperset() / >= ---")
print("primes.issuperset(small):", primes.issuperset(small))   # True
print("primes >= small:         ", primes >= small)            # True
print("small.issuperset(primes):", small.issuperset(primes))   # False

# --- 5.5 Proper Subset < and Proper Superset > ---
# A < B means A is a subset of B AND A != B (A is strictly smaller).
# A > B means A is a superset of B AND A != B (A is strictly larger).
print("\n--- 5.5 Proper Subset < and Proper Superset > ---")
print("small < primes:    ", small < primes)     # True  (small ⊂ primes, and not equal)
print("small < small:     ", small < small)      # False (equal sets are NOT proper subsets)
print("small <= small:    ", small <= small)     # True  (every set is a subset of itself)
print("primes > small:    ", primes > small)     # True

# --- 5.6 isdisjoint() — No Common Elements ---
# Returns True if the two sets have NO elements in common.
print("\n--- 5.6 isdisjoint() ---")
print("primes.isdisjoint(evens):    ", primes.isdisjoint(evens))    # False (2 is common)
print("{1,3,5}.isdisjoint({2,4,6}):", {1,3,5}.isdisjoint({2,4,6})) # True  (no common)

# *** IMPORTANT NOTES — COMPARISON AND MEMBERSHIP ***
# - Membership testing in a set is O(1) average time (very fast vs list's O(n)).
# - <= is subset (includes equal sets); < is PROPER subset (excludes equal sets).
# - >= is superset; > is PROPER superset.
# - isdisjoint() is more readable than checking intersection is empty.
print("\n# NOTE: Set membership testing (in) is O(1) — much faster than lists.")
print("# NOTE: <= means subset (can be equal); < means proper subset (not equal).")


# =============================================================
# SECTION 6: BUILT-IN FUNCTIONS WITH SETS
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 6: BUILT-IN FUNCTIONS WITH SETS")
print("=" * 60)

num_set = {3, 1, 4, 1, 5, 9, 2, 6}   # Note: duplicate 1 is automatically removed
print("\nSet:", num_set)

# --- 6.1 len() --- Number of Elements
print("\n--- 6.1 len() ---")
print("len(num_set):", len(num_set))   # 7 (not 8 — duplicate removed)

# --- 6.2 max() and min() ---
print("\n--- 6.2 max() and min() ---")
print("max(num_set):", max(num_set))   # 9
print("min(num_set):", min(num_set))   # 1

# --- 6.3 sum() ---
print("\n--- 6.3 sum() ---")
print("sum(num_set):", sum(num_set))   # 30  (3+1+4+5+9+2+6)

# --- 6.4 sorted() — Returns a Sorted List ---
# sorted() returns a NEW sorted LIST (sets cannot be sorted in-place — unordered).
print("\n--- 6.4 sorted() ---")
sorted_list = sorted(num_set)
print("sorted(num_set):              ", sorted_list)             # [1, 2, 3, 4, 5, 6, 9]
print("sorted(num_set, reverse=True):", sorted(num_set, reverse=True))  # [9, 6, 5, 4, 3, 2, 1]
print("Type of sorted() result:      ", type(sorted_list))       # <class 'list'>

# --- 6.5 any() and all() ---
# any() returns True if at least one element is truthy.
# all() returns True if ALL elements are truthy.
print("\n--- 6.5 any() and all() ---")
bool_set_1 = {0, 1, 2, 3}   # contains 0 (falsy)
bool_set_2 = {1, 2, 3, 4}   # all truthy
print("any({0,1,2,3}):", any(bool_set_1))   # True  (1, 2, 3 are truthy)
print("all({0,1,2,3}):", all(bool_set_1))   # False (0 is falsy)
print("any({1,2,3,4}):", any(bool_set_2))   # True
print("all({1,2,3,4}):", all(bool_set_2))   # True

# --- 6.6 enumerate() — Iterate with Index ---
# enumerate() assigns a counter to each element during iteration.
# Note: order is not guaranteed (sets are unordered).
print("\n--- 6.6 enumerate() ---")
lang_set = {"Python", "Java", "C++"}
print("enumerate() over set:")
for index, item in enumerate(lang_set):
    print(f"  Index {index}: {item}")

# *** IMPORTANT NOTES — BUILT-IN FUNCTIONS ***
# - sorted() returns a LIST, not a set (sets are unordered).
# - enumerate() works but the order may vary between runs (unordered set).
# - max(), min(), sum() work only if elements are comparable (same type).
print("\n# NOTE: sorted() on a set returns a LIST, not a set.")
print("# NOTE: Set order may vary — do not rely on iteration order.")


# =============================================================
# SECTION 7: FROZEN SETS
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 7: FROZEN SETS")
print("=" * 60)

# A frozenset is an IMMUTABLE version of a set.
# It supports all set operations EXCEPT add/remove/update (modification).

# --- 7.1 Creating a Frozenset ---
print("\n--- 7.1 Creating a Frozenset ---")
fs = frozenset({1, 2, 3, 4, 5})
fs_from_list   = frozenset([10, 20, 30, 20])  # Duplicates removed
fs_from_string = frozenset("hello")
empty_fs       = frozenset()

print("frozenset({1,2,3,4,5}):     ", fs)
print("frozenset([10,20,30,20]):   ", fs_from_list)
print("frozenset('hello'):         ", fs_from_string)
print("frozenset() (empty):        ", empty_fs)
print("Type:", type(fs))   # <class 'frozenset'>

# --- 7.2 Frozenset is Immutable ---
print("\n--- 7.2 Frozenset is Immutable ---")
try:
    fs.add(6)     # AttributeError: 'frozenset' object has no attribute 'add'
except AttributeError as e:
    print("AttributeError — cannot add to frozenset:", e)
try:
    fs.remove(1)  # AttributeError
except AttributeError as e:
    print("AttributeError — cannot remove from frozenset:", e)

# --- 7.3 Frozenset as Dictionary Key or Set Element ---
# Because frozenset is immutable (hashable), it can be used as a dict key or set element.
print("\n--- 7.3 Frozenset as Dictionary Key / Set Element ---")
fs_key_dict = {frozenset({1, 2}): "pair", frozenset({3, 4}): "another pair"}
print("Dict with frozenset keys:", fs_key_dict)

set_of_frozen = {frozenset({1, 2}), frozenset({3, 4}), frozenset({1, 2})}  # duplicate removed
print("Set of frozensets:       ", set_of_frozen)

# You CANNOT put a regular (mutable) set inside another set:
try:
    bad = {{1, 2}, {3, 4}}   # TypeError: unhashable type: 'set'
except TypeError as e:
    print("TypeError — cannot nest mutable sets:", e)

# --- 7.4 Frozenset Supports All Non-Modifying Set Operations ---
print("\n--- 7.4 Frozenset Supports All Read-Only Set Operations ---")
fa = frozenset({1, 2, 3, 4})
fb = frozenset({3, 4, 5, 6})

print("fa | fb:                  ", fa | fb)                    # union
print("fa & fb:                  ", fa & fb)                    # intersection
print("fa - fb:                  ", fa - fb)                    # difference
print("fa ^ fb:                  ", fa ^ fb)                    # symmetric difference
print("fa.issubset({1,2,3,4,5}): ", fa.issubset({1, 2, 3, 4, 5}))  # True
print("fa.isdisjoint({7,8,9}):   ", fa.isdisjoint({7, 8, 9}))      # True

# --- 7.5 When to Use frozenset vs set ---
# Use frozenset when:
#   - You need an immutable set (contents should not change).
#   - You need to use a collection of items as a dict key.
#   - You need to store a set inside another set.
# Use set when:
#   - You need to add or remove elements dynamically.
print("\n--- 7.5 When to Use frozenset vs set ---")
print("frozenset: use when immutability is needed (dict key, set element).")
print("set:       use when you need to add/remove elements dynamically.")

# *** IMPORTANT NOTES — FROZEN SETS ***
# - frozenset is immutable and hashable (can be used as dict key or set element).
# - Regular set is mutable and unhashable (CANNOT be used as dict key or set element).
# - frozenset supports union, intersection, difference, subset, etc. (read-only ops).
print("\n# NOTE: frozenset is immutable — use it when a set must be hashable.")
print("# NOTE: Regular sets are mutable and cannot be used as dict keys.")


# =============================================================
# SECTION 8: SET vs OTHER DATA STRUCTURES
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 8: SET vs OTHER DATA STRUCTURES")
print("=" * 60)

# --- 8.1 Set vs List ---
print("\n--- 8.1 Set vs List ---")
# List: ordered, allows duplicates, accessed by index, O(n) membership test.
# Set:  unordered, unique elements only, no indexing, O(1) membership test.
my_list = [1, 2, 2, 3, 3, 3, 4]
my_set  = {1, 2, 2, 3, 3, 3, 4}
print("List (preserves duplicates):", my_list)   # [1, 2, 2, 3, 3, 3, 4]
print("Set  (removes duplicates):  ", my_set)    # {1, 2, 3, 4}

import time

# Demonstrating performance difference for membership testing
big_list = list(range(1000000))
big_set  = set(range(1000000))

start = time.time(); _ = 999999 in big_list; list_time = time.time() - start
start = time.time(); _ = 999999 in big_set;  set_time  = time.time() - start
print(f"Membership test — List: {list_time:.6f}s | Set: {set_time:.6f}s (set is faster!)")

# --- 8.2 Set vs Tuple ---
print("\n--- 8.2 Set vs Tuple ---")
# Tuple: ordered, immutable, allows duplicates, accessed by index.
# Set:   unordered, mutable (add/remove), unique elements, no indexing.
my_tuple = (1, 2, 2, 3)
my_set2  = {1, 2, 2, 3}
print("Tuple:", my_tuple)   # (1, 2, 2, 3) — duplicates kept, order preserved
print("Set:  ", my_set2)    # {1, 2, 3}    — duplicates removed, unordered

# --- 8.3 Set vs Dictionary ---
print("\n--- 8.3 Set vs Dictionary ---")
# Dict: key-value pairs; Set: individual unique values (no associated data).
# Both use {} syntax, but dict has colons (key: value) and set has bare values.
my_dict  = {"a": 1, "b": 2, "c": 3}
my_set3  = {"a", "b", "c"}
print("Dict: ", my_dict)   # {'a': 1, 'b': 2, 'c': 3}
print("Set:  ", my_set3)   # {'a', 'b', 'c'}

# --- 8.4 Comparison Table (via comments) ---
# ┌─────────────────┬──────────┬────────────┬────────────┬───────────┐
# │ Feature         │ Set      │ List       │ Tuple      │ Dict      │
# ├─────────────────┼──────────┼────────────┼────────────┼───────────┤
# │ Ordered         │ No       │ Yes        │ Yes        │ Yes (3.7+)│
# │ Mutable         │ Yes      │ Yes        │ No         │ Yes       │
# │ Duplicates      │ No       │ Yes        │ Yes        │ Keys: No  │
# │ Access by Index │ No       │ Yes        │ Yes        │ By key    │
# │ Membership O()  │ O(1)     │ O(n)       │ O(n)       │ O(1)      │
# │ Syntax          │ {x, y}   │ [x, y]     │ (x, y)     │ {k: v}    │
# └─────────────────┴──────────┴────────────┴────────────┴───────────┘
print("\n--- 8.4 When to Use a Set ---")
print("Use a set when:")
print("  - You need only unique elements (no duplicates).")
print("  - You need fast O(1) membership testing.")
print("  - You need mathematical set operations (union, intersection, etc.).")
print("  - Order does NOT matter.")
print("  - You do NOT need to store key-value pairs.")

# *** IMPORTANT NOTES — SET vs OTHERS ***
# - Set membership test is O(1) (hash-based); list/tuple membership is O(n).
# - Sets automatically remove duplicates — useful for deduplication.
# - Use list when order matters or duplicates are needed.
# - Use tuple when the collection must be immutable.
# - Use dict when each element needs an associated value.
print("\n# NOTE: Sets have O(1) membership lookup — much faster than lists (O(n)).")


# =============================================================
# SECTION 9: COMMON USE CASES
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 9: COMMON USE CASES")
print("=" * 60)

# --- 9.1 Removing Duplicates from a List ---
print("\n--- 9.1 Removing Duplicates from a List ---")
data_with_dups = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique_data    = list(set(data_with_dups))   # convert to set then back to list
print("Original:          ", data_with_dups)
print("Unique elements:   ", unique_data)    # order may differ
# To preserve order while removing duplicates:
seen = set()
ordered_unique = [x for x in data_with_dups if not (x in seen or seen.add(x))]
print("Unique (ordered):  ", ordered_unique)   # order preserved

# --- 9.2 Finding Common Elements Between Collections ---
print("\n--- 9.2 Finding Common Elements Between Collections ---")
team_a = {"Alice", "Bob", "Charlie", "Dave"}
team_b = {"Bob", "Dave", "Eve", "Frank"}
common = team_a & team_b
only_a = team_a - team_b
only_b = team_b - team_a
print("Team A:           ", team_a)
print("Team B:           ", team_b)
print("In both teams:    ", common)   # {'Bob', 'Dave'}
print("Only in Team A:   ", only_a)   # {'Alice', 'Charlie'}
print("Only in Team B:   ", only_b)   # {'Eve', 'Frank'}

# --- 9.3 Membership Testing (Fast Lookups) ---
print("\n--- 9.3 Fast Membership Testing ---")
# Using a set for fast lookup instead of a list.
allowed_extensions = {".py", ".txt", ".md", ".json", ".csv"}
files_to_check     = ["report.pdf", "script.py", "data.csv", "image.png", "notes.txt"]

for filename in files_to_check:
    ext = "." + filename.rsplit(".", 1)[-1]
    status = "Allowed" if ext in allowed_extensions else "Blocked"
    print(f"  {filename}: {status}")

# --- 9.4 Finding Unique Elements ---
print("\n--- 9.4 Finding Unique Elements ---")
all_tags      = ["python", "coding", "python", "tutorial", "coding", "beginner", "python"]
unique_tags   = set(all_tags)
print("All tags:    ", all_tags)
print("Unique tags: ", unique_tags)

# --- 9.5 Data Validation (Checking Allowed Values) ---
print("\n--- 9.5 Data Validation (Checking Allowed Values) ---")
VALID_STATUSES = {"pending", "active", "inactive", "suspended", "deleted"}

def validate_status(status):
    if status in VALID_STATUSES:
        return f"'{status}' is a valid status."
    return f"'{status}' is INVALID! Allowed: {VALID_STATUSES}"

print(validate_status("active"))      # valid
print(validate_status("unknown"))     # invalid
print(validate_status("deleted"))     # valid

# *** IMPORTANT NOTES — USE CASES ***
# - Converting to set is the fastest way to deduplicate (but loses order).
# - Use a comprehension trick to deduplicate while preserving insertion order.
# - Sets are ideal as lookup tables for validation (O(1) vs O(n) for lists).
# - Set operations (union, intersection, difference) replace complex loops.
print("\n# NOTE: set() is the fastest way to deduplicate a list.")
print("# NOTE: Use sets as lookup tables for O(1) validation — faster than lists.")


# =============================================================
#                   END OF TUTORIAL
# =============================================================

print("\n" + "=" * 60)
print("         END OF PYTHON SETS TUTORIAL")
print("=" * 60)
print("Topics covered:")
print("  1. Creating a Set")
print("  2. Adding and Removing Elements")
print("  3. Set Operations (Mathematical)")
print("  4. Set Update Operations (In-place)")
print("  5. Set Comparison and Membership")
print("  6. Built-in Functions with Sets")
print("  7. Frozen Sets")
print("  8. Set vs Other Data Structures")
print("  9. Common Use Cases")
print("=" * 60)
