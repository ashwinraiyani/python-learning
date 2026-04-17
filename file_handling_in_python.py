# ============================================================
#         PYTHON FILE HANDLING — COMPREHENSIVE TUTORIAL
# ============================================================
# This file covers everything you need to know about File Handling
# in Python for Text files and CSV files:
#   1. Text File — Opening and Closing Files
#   2. Text File — Writing Data
#   3. Text File — Reading Data
#   4. Text File — Close Operation
#   5. CSV File — Introduction
#   6. CSV File — Writing Data
#   7. CSV File — Reading Data
#   8. Important Notes & Best Practices

import os
import csv

print("=" * 60)
print("   PYTHON FILE HANDLING — COMPREHENSIVE TUTORIAL")
print("=" * 60)


# =============================================================
# SECTION 1: TEXT FILE — OPENING AND CLOSING FILES
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 1: TEXT FILE — OPENING AND CLOSING FILES")
print("=" * 60)

# --- 1.1 Opening a File using open() ---
# The built-in open() function is used to open files.
# Syntax: open(filename, mode)
# Common modes:
#   'r'  — Read (default). File must exist. Cursor at start.
#   'w'  — Write. Creates file if it doesn't exist; OVERWRITES if it does.
#   'a'  — Append. Creates file if needed; adds content at the END.
#   'r+' — Read + Write. File must exist. Does NOT truncate the file.
#   'x'  — Exclusive creation. Fails if file already exists.

print("\n--- 1.1 open() File Modes ---")
print("Mode 'r'  : Read only  (file must exist)")
print("Mode 'w'  : Write only (creates/overwrites)")
print("Mode 'a'  : Append     (creates/adds at end)")
print("Mode 'r+' : Read+Write (file must exist)")
print("Mode 'x'  : Create new (fails if file exists)")

# --- 1.2 Using the 'with' Statement (Context Manager) ---
# The 'with' statement automatically closes the file when the block ends.
# This is the RECOMMENDED way to work with files.
# Syntax: with open(filename, mode) as file_object:

print("\n--- 1.2 Using 'with' Statement (Recommended) ---")
# Write a sample file so we can demonstrate reading
with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python File Handling is easy.\n")
    file.write("This is line 3.\n")
print("Created 'sample.txt' using 'with' statement.")
print("File is automatically closed after 'with' block.")

# --- 1.3 Closing a File Manually using close() ---
# If you don't use 'with', you MUST call close() manually.
print("\n--- 1.3 Manual open() and close() ---")
file = open("sample.txt", "r")      # Open in read mode
content = file.read()               # Read entire content
file.close()                        # MUST close manually
print("File read and closed manually.")
print("First 30 characters:", content[:30])

# *** IMPORTANT NOTES — OPENING AND CLOSING FILES ***
# - Always use 'with' to avoid forgetting to close the file.
# - 'w' mode OVERWRITES the file completely — existing data is lost!
# - 'a' mode only ADDS to the file — existing data is preserved.
# - Not closing a file can cause data loss (buffer not flushed)
#   or resource leaks (file handle not released).
print("\n# NOTE: Always use 'with' statement to avoid resource leaks.")
print("# NOTE: 'w' overwrites; 'a' appends — choose carefully!")


# =============================================================
# SECTION 2: TEXT FILE — WRITING DATA
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 2: TEXT FILE — WRITING DATA")
print("=" * 60)

# --- 2.1 write(s) — Write a Single String ---
# write() writes exactly the string you give it.
# It does NOT add a newline automatically.
print("\n--- 2.1 write() — Single String ---")
with open("sample.txt", "w") as file:
    chars_written = file.write("First line")   # Returns number of chars written
    print("Characters written:", chars_written)

with open("sample.txt", "r") as file:
    print("File content:", repr(file.read()))  # No newline at end!
# NOTE: "First line" has no '\n', so no newline is added.

# --- 2.2 Writing Multiple Lines with \n ---
# You must add '\n' explicitly to create line breaks.
print("\n--- 2.2 Writing Multiple Lines using \\n ---")
with open("sample.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")

with open("sample.txt", "r") as file:
    print("File content after writing 3 lines:")
    print(file.read())

# --- 2.3 'w' Mode (Create/Overwrite) vs 'a' Mode (Append) ---
# 'w' mode: starts fresh every time — previous content is GONE.
# 'a' mode: keeps existing content and ADDS new content at the end.
print("\n--- 2.3 'w' Mode vs 'a' Mode ---")

# Write initial content
with open("sample.txt", "w") as file:
    file.write("Original Line\n")

# Overwrite with 'w' — original content is lost
with open("sample.txt", "w") as file:
    file.write("Overwritten Line\n")

with open("sample.txt", "r") as file:
    print("After 'w' mode (overwrites):", file.read().strip())

# Append with 'a' — original content is preserved
with open("sample.txt", "a") as file:
    file.write("Appended Line\n")

with open("sample.txt", "r") as file:
    print("After 'a' mode (appends):")
    print(file.read())

# --- 2.4 writelines() — Write a List of Strings ---
# writelines() writes each string in the list to the file.
# Like write(), it does NOT add newlines automatically.
print("\n--- 2.4 writelines() — Write a List of Strings ---")
lines_to_write = ["Apple\n", "Banana\n", "Cherry\n"]
with open("sample.txt", "w") as file:
    file.writelines(lines_to_write)

with open("sample.txt", "r") as file:
    print("File content after writelines():")
    print(file.read())

# *** IMPORTANT NOTES — WRITING DATA ***
# - write() returns the NUMBER of characters written.
# - write() does NOT add '\n' automatically — add it yourself.
# - 'w' mode TRUNCATES (empties) the file before writing.
# - writelines() writes all strings in a list; no newlines are added.
# - write() vs writelines(): write() takes one string;
#   writelines() takes a list of strings.
print("# NOTE: write() returns char count; does NOT add newline automatically.")
print("# NOTE: writelines() writes a list of strings — still no auto-newlines.")


# =============================================================
# SECTION 3: TEXT FILE — READING DATA
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 3: TEXT FILE — READING DATA")
print("=" * 60)

# First, create a fresh sample file for reading demonstrations
with open("sample.txt", "w") as file:
    file.write("Line 1: Hello\n")
    file.write("Line 2: Python\n")
    file.write("Line 3: File Handling\n")
    file.write("Line 4: Is Fun\n")
    file.write("Line 5: End\n")

print("(Prepared sample.txt with 5 lines for reading demos)")

# --- 3.1 read() — Read Entire File as a Single String ---
print("\n--- 3.1 read() — Read Entire File ---")
with open("sample.txt", "r") as file:
    content = file.read()
print("Entire file content:")
print(content)

# --- 3.2 read(n) — Read First n Characters ---
print("\n--- 3.2 read(n) — Read First n Characters ---")
with open("sample.txt", "r") as file:
    first_10 = file.read(10)   # Read only first 10 characters
    next_5   = file.read(5)    # Read next 5 characters from current cursor
print("First 10 characters:", repr(first_10))
print("Next  5  characters:", repr(next_5))
# NOTE: The cursor moves forward with each read() call.

# --- 3.3 readline() — Read a Single Line ---
# readline() reads one line at a time, including the trailing '\n'.
# Each call moves the cursor to the next line.
print("\n--- 3.3 readline() — Read One Line at a Time ---")
with open("sample.txt", "r") as file:
    line1 = file.readline()   # Reads "Line 1: Hello\n"
    line2 = file.readline()   # Reads "Line 2: Python\n"
    line3 = file.readline()   # Reads "Line 3: File Handling\n"
print("readline() call 1:", repr(line1))
print("readline() call 2:", repr(line2))
print("readline() call 3:", repr(line3))

# --- 3.4 readlines() — Read All Lines into a List ---
# readlines() returns a list where each element is a line (with '\n').
print("\n--- 3.4 readlines() — Read All Lines as a List ---")
with open("sample.txt", "r") as file:
    all_lines = file.readlines()
print("readlines() returns a list:")
for i, line in enumerate(all_lines):
    print(f"  all_lines[{i}]: {repr(line)}")

# --- 3.5 Iterating Over File Object Line by Line ---
# The most memory-efficient way to read large files.
# Python's file object is iterable — each iteration yields one line.
print("\n--- 3.5 Iterating Over File Object (for line in file) ---")
with open("sample.txt", "r") as file:
    for line in file:
        print("  Line:", line.strip())   # strip() removes the trailing '\n'

# --- 3.6 seek() and tell() — Managing the File Cursor ---
# tell()  — returns the current cursor position (in bytes)
# seek(n) — moves the cursor to position n (0 = beginning)
print("\n--- 3.6 seek() and tell() — Cursor Management ---")
with open("sample.txt", "r") as file:
    print("Initial cursor position:", file.tell())   # 0

    file.read(10)
    print("After read(10), cursor at:", file.tell())  # 10

    file.seek(0)   # Reset cursor to the beginning
    print("After seek(0), cursor at:", file.tell())   # 0

    first_line = file.readline()
    print("First line after seek(0):", first_line.strip())

# *** IMPORTANT NOTES — READING DATA ***
# - After reading, the cursor moves forward. Use seek(0) to re-read.
# - read()      → entire file as one string. Good for small files.
# - readline()  → one line at a time. Good for sequential processing.
# - readlines() → all lines as a list. Easy but loads everything into memory.
# - for line in file → most memory-efficient for large files.
# - Use strip() to remove trailing '\n' from each line.
# - readline() returns an empty string '' when the end of file is reached.
print("\n# NOTE: seek(0) resets cursor to start of file for re-reading.")
print("# NOTE: Use 'for line in file' for large files — memory efficient.")
print("# NOTE: Use strip() to remove trailing '\\n' from readline() output.")


# =============================================================
# SECTION 4: TEXT FILE — CLOSE OPERATION
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 4: TEXT FILE — CLOSE OPERATION")
print("=" * 60)

# --- 4.1 close() — Manually Close a File ---
# After you're done with a file, close() releases the OS file handle.
# It also flushes any buffered (unwritten) data to disk.
print("\n--- 4.1 close() — Manual Close ---")
file = open("sample.txt", "r")
print("Is file closed before close():", file.closed)   # False
file.read()
file.close()
print("Is file closed after  close():", file.closed)   # True

# --- 4.2 file.closed Attribute ---
# The .closed attribute returns True if the file is closed, False otherwise.
print("\n--- 4.2 file.closed Attribute ---")
file = open("sample.txt", "r")
print("file.closed (open)  :", file.closed)    # False
file.close()
print("file.closed (closed):", file.closed)    # True

# --- 4.3 'with' Statement — Automatic Close ---
# The 'with' statement is a context manager.
# It GUARANTEES the file is closed when the block exits,
# even if an exception occurs inside the block.
print("\n--- 4.3 'with' Statement — Auto-Close ---")
with open("sample.txt", "r") as file:
    data = file.read(5)
    print("Inside 'with', file.closed:", file.closed)    # False
# File is automatically closed here
print("Outside 'with', file.closed:", file.closed)   # True

# --- 4.4 What Happens if You Don't Close a File ---
# - On writes: data may stay in the buffer and NOT be written to disk.
# - The OS may limit how many files can be open at once.
# - In long-running programs, unclosed files = memory/resource leak.
print("\n--- 4.4 Why Closing is Important ---")
print("1. Flushes write buffer — ensures data is actually saved to disk.")
print("2. Releases OS file handle — prevents resource exhaustion.")
print("3. Allows other processes to access the file (especially on Windows).")

# *** IMPORTANT NOTES — CLOSE OPERATION ***
# - BEST PRACTICE: Always use 'with' — it closes automatically.
# - After close(), any attempt to read/write raises a ValueError.
# - close() is idempotent: calling it multiple times is safe.
print("\n# NOTE: Best practice — always use 'with' statement.")
print("# NOTE: Accessing a closed file raises ValueError.")
try:
    closed_file = open("sample.txt", "r")
    closed_file.close()
    closed_file.read()   # This will raise ValueError
except ValueError as e:
    print("ValueError when reading closed file:", e)


# =============================================================
# SECTION 5: CSV FILE — INTRODUCTION
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 5: CSV FILE — INTRODUCTION")
print("=" * 60)

# --- 5.1 What is a CSV File? ---
# CSV = Comma-Separated Values
# A plain-text file where each line is a row of data, and
# values in each row are separated by a delimiter (usually a comma).
# Example CSV content:
#   Name,Age,City
#   Alice,30,New York
#   Bob,25,London
print("\n--- 5.1 What is a CSV File? ---")
print("CSV = Comma-Separated Values")
print("Each row is a line; values are separated by commas (or another delimiter).")
print("Example:  Name,Age,City")
print("          Alice,30,New York")

# --- 5.2 Importing the csv Module ---
# Python's built-in 'csv' module handles reading and writing CSV files.
# No installation required — it's part of the standard library.
print("\n--- 5.2 Importing the csv Module ---")
print("'import csv' is already done at the top of this file.")
print("csv module version / location:", csv.__file__ if hasattr(csv, "__file__") else "built-in")

# --- 5.3 Opening a CSV File for Writing ---
# Always use newline='' when opening CSV files to prevent extra blank rows.
# This is especially important on Windows (where '\r\n' is the line ending).
print("\n--- 5.3 Opening a CSV File ---")
print("For writing: open('sample.csv', 'w', newline='')")
print("For reading: open('sample.csv', 'r', newline='')")
print("For appending: open('sample.csv', 'a', newline='')")

# --- 5.4 csv.writer and csv.reader Objects ---
# csv.writer(file) — creates a writer object to write rows to a CSV file.
# csv.reader(file) — creates a reader object to read rows from a CSV file.
print("\n--- 5.4 csv.writer and csv.reader Objects ---")
print("csv.writer(file)  — used to write data to a CSV file.")
print("csv.reader(file)  — used to read data from a CSV file.")

# *** IMPORTANT NOTES — CSV INTRODUCTION ***
# - Always use newline='' in open() for CSV — avoids extra blank rows.
# - The csv module handles commas inside quoted fields correctly.
# - CSV files can use different delimiters (e.g., ';', '\t') — use
#   the 'delimiter' parameter: csv.writer(file, delimiter=';')
print("\n# NOTE: Always use newline='' when opening CSV files.")
print("# NOTE: csv module handles quoted fields with commas correctly.")


# =============================================================
# SECTION 6: CSV FILE — WRITING DATA
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 6: CSV FILE — WRITING DATA")
print("=" * 60)

# --- 6.1 writerow() — Write a Single Row ---
# writerow(row) writes one row (a list or tuple) to the CSV file.
# It automatically separates values with commas and adds a line ending.
print("\n--- 6.1 writerow() — Write a Single Row ---")
with open("sample.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name", "Age", "City"])      # Header row
    writer.writerow(["Alice", 30, "New York"])    # First data row
    writer.writerow(["Bob", 25, "London"])        # Second data row
    writer.writerow(["Charlie", 35, "Paris"])     # Third data row

print("Wrote 4 rows (1 header + 3 data) to 'sample.csv' using writerow().")

# Verify by reading raw file
with open("sample.csv", "r") as csv_file:
    print("Raw CSV content after writerow():")
    print(csv_file.read())

# --- 6.2 writerows() — Write Multiple Rows at Once ---
# writerows(rows) writes ALL rows from a list of lists in one call.
# This is more concise when you already have all data in a list.
print("\n--- 6.2 writerows() — Write Multiple Rows at Once ---")
header = ["Product", "Price", "Stock"]
data_rows = [
    ["Laptop",  999.99, 50],
    ["Phone",   499.99, 120],
    ["Tablet",  299.99, 75],
    ["Monitor", 199.99, 30],
]

with open("sample.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)       # Write header first (one row)
    writer.writerows(data_rows)   # Write all data rows at once

print("Wrote header + 4 data rows to 'sample.csv' using writerows().")

# Verify by reading raw file
with open("sample.csv", "r") as csv_file:
    print("Raw CSV content after writerows():")
    print(csv_file.read())

# --- 6.3 Difference Between writerow() and writerows() ---
print("\n--- 6.3 writerow() vs writerows() ---")
print("writerow(row)   → writes ONE row at a time (a single list/tuple).")
print("writerows(rows) → writes ALL rows at once (a list of lists/tuples).")
print("Example:")
print("  writer.writerow(['Alice', 30])          # one row")
print("  writer.writerows([['Bob', 25],          # multiple rows")
print("                    ['Charlie', 35]])")

# --- 6.4 Writing with a Custom Delimiter ---
# The default delimiter is ','. You can use ';', '\t', '|', etc.
print("\n--- 6.4 Writing with Custom Delimiter ---")
with open("sample_tab.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter="\t")   # Tab-separated
    writer.writerow(["Name", "Score"])
    writer.writerow(["Alice", 95])
    writer.writerow(["Bob", 87])

with open("sample_tab.csv", "r") as csv_file:
    print("Tab-separated CSV content:")
    print(csv_file.read())

# *** IMPORTANT NOTES — CSV WRITING ***
# - writerow()  → ONE row at a time (pass a list/tuple).
# - writerows() → ALL rows at once (pass a list of lists/tuples).
# - ALWAYS use newline='' in open() for CSV files.
# - writerow() automatically converts values (int, float) to strings.
# - The header row is just another row — write it first manually.
print("# NOTE: writerow() writes ONE row; writerows() writes ALL rows.")
print("# NOTE: Always use newline='' in open() to prevent blank rows.")


# =============================================================
# SECTION 7: CSV FILE — READING DATA
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 7: CSV FILE — READING DATA")
print("=" * 60)

# First, prepare sample.csv with known data for reading
with open("sample.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerows([
        ["Alice",   30, "New York"],
        ["Bob",     25, "London"],
        ["Charlie", 35, "Paris"],
        ["Diana",   28, "Tokyo"],
    ])

# --- 7.1 csv.reader — Reading Rows from a CSV File ---
# csv.reader returns an iterable; each iteration gives one row as a list.
# All values are returned as STRINGS, even numbers.
print("\n--- 7.1 csv.reader — Reading All Rows ---")
with open("sample.csv", "r", newline="") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print("  Row:", row)   # Each row is a list of strings

# --- 7.2 Separating Header from Data Rows ---
# Use next(reader) to read the header row separately from data rows.
print("\n--- 7.2 Separating Header from Data Rows ---")
with open("sample.csv", "r", newline="") as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)          # Read header row separately
    print("Header:", header)
    print("Data rows:")
    for row in reader:
        # Values are strings — convert types as needed
        name = row[0]
        age  = int(row[1])         # Convert string to int
        city = row[2]
        print(f"  Name: {name:<10} | Age: {age:>3} | City: {city}")

# --- 7.3 Reading with a Custom Delimiter ---
print("\n--- 7.3 Reading with Custom Delimiter ---")
with open("sample_tab.csv", "r", newline="") as csv_file:
    reader = csv.reader(csv_file, delimiter="\t")
    print("Tab-separated CSV rows:")
    for row in reader:
        print("  Row:", row)

# *** IMPORTANT NOTES — CSV READING ***
# - Each row is returned as a LIST of strings (not integers/floats).
# - Use int(), float() etc. to convert values to the right type.
# - Use next(reader) to skip/consume the header row.
# - csv.reader handles quoted fields with commas inside correctly.
# - If the CSV uses ';' or '\t' as delimiter, specify delimiter= in csv.reader.
print("\n# NOTE: csv.reader returns all values as STRINGS — convert as needed.")
print("# NOTE: Use next(reader) to skip the header row.")


# =============================================================
# SECTION 8: IMPORTANT NOTES & BEST PRACTICES
# =============================================================

print("\n" + "=" * 60)
print("  SECTION 8: IMPORTANT NOTES & BEST PRACTICES")
print("=" * 60)

# --- 8.1 Summary of File Modes ---
print("\n--- 8.1 File Modes Summary ---")
print("Mode | Description                             | File must exist?")
print("-----|----------------------------------------|------------------")
print(" 'r' | Read only (default)                    | YES (FileNotFoundError)")
print(" 'w' | Write (creates new or OVERWRITES)      | NO  (creates if missing)")
print(" 'a' | Append (adds to end)                   | NO  (creates if missing)")
print("'r+' | Read + Write (no truncate)             | YES (FileNotFoundError)")
print(" 'x' | Exclusive create (fails if exists)     | NO  (FileExistsError)")

# --- 8.2 Text Mode vs Binary Mode ---
print("\n--- 8.2 Text Mode vs Binary Mode ---")
print("Text mode  ('r', 'w', 'a')    — default; handles string data.")
print("Binary mode ('rb', 'wb', 'ab') — for images, audio, video, etc.")
print("Example: open('photo.jpg', 'rb')   # read binary")
print("         open('output.bin', 'wb')  # write binary")

# --- 8.3 Always Use 'with' Statement ---
print("\n--- 8.3 Always Use 'with' Statement ---")
print("Recommended:")
print("  with open('file.txt', 'r') as f:")
print("      data = f.read()")
print("")
print("Avoid (error-prone):")
print("  f = open('file.txt', 'r')")
print("  data = f.read()")
print("  f.close()   # easily forgotten; skipped on exception!")

# --- 8.4 Handling FileNotFoundError with try-except ---
# If you open a file in 'r' mode and it doesn't exist, Python raises FileNotFoundError.
print("\n--- 8.4 Handling FileNotFoundError ---")
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print("FileNotFoundError caught:", e)
except PermissionError as e:
    print("PermissionError caught:", e)

# --- 8.5 CSV: Importance of newline='' ---
print("\n--- 8.5 CSV: newline='' Is Important ---")
print("On Windows, the default line ending is '\\r\\n'.")
print("Without newline='', csv.writer adds an extra blank row after each row.")
print("Always open CSV files like this:")
print("  with open('file.csv', 'w', newline='') as f:")
print("      writer = csv.writer(f)")

# --- 8.6 write() vs writelines() ---
print("\n--- 8.6 write() vs writelines() ---")
print("write(s)          → writes a single string; returns char count.")
print("writelines(lines) → writes a list of strings; returns None.")
print("Neither adds newlines automatically — add '\\n' yourself.")

# --- 8.7 File Cursor: seek() and tell() ---
print("\n--- 8.7 File Cursor: seek() and tell() ---")
with open("sample.txt", "r") as file:
    print("tell() at start:", file.tell())
    file.read(5)
    print("tell() after read(5):", file.tell())
    file.seek(0)
    print("tell() after seek(0):", file.tell())
    file.seek(0, 2)   # seek to END of file (offset 0 from end)
    print("tell() after seek(0, 2) [end of file]:", file.tell())

# seek(offset, whence):
#   whence=0 (default) — from the beginning of file
#   whence=1           — from the current cursor position
#   whence=2           — from the end of file

# *** FINAL BEST PRACTICES SUMMARY ***
print("\n--- Final Best Practices Summary ---")
print("1.  Use 'with' statement — auto-closes file, even on exceptions.")
print("2.  Use 'r' mode to read — safe, won't modify the file.")
print("3.  Be careful with 'w' mode — it OVERWRITES all existing content.")
print("4.  Use 'a' mode to add lines to an existing file.")
print("5.  Always add '\\n' manually in write() for line breaks.")
print("6.  Use strip() to remove trailing '\\n' when reading lines.")
print("7.  Use seek(0) to reset cursor and re-read from the beginning.")
print("8.  CSV: always use newline='' in open() to prevent blank rows.")
print("9.  CSV: all values from csv.reader are STRINGS — convert as needed.")
print("10. Wrap file opens in try-except to handle FileNotFoundError.")


# =============================================================
# CLEANUP: Remove Sample Files Created During This Tutorial
# =============================================================

print("\n" + "=" * 60)
print("  CLEANUP: Removing Sample Files")
print("=" * 60)

# Removing the sample files created during this tutorial.
# This is optional — comment out these lines if you want to inspect the files.
for filename in ["sample.txt", "sample.csv", "sample_tab.csv"]:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Removed: {filename}")

print("Cleanup complete.")


# =============================================================
#                   END OF TUTORIAL
# =============================================================

print("\n" + "=" * 60)
print("   END OF PYTHON FILE HANDLING TUTORIAL")
print("=" * 60)
print("Topics covered:")
print("  1. Text File — Opening and Closing Files")
print("  2. Text File — Writing Data")
print("  3. Text File — Reading Data")
print("  4. Text File — Close Operation")
print("  5. CSV File — Introduction")
print("  6. CSV File — Writing Data")
print("  7. CSV File — Reading Data")
print("  8. Important Notes & Best Practices")
print("=" * 60)
