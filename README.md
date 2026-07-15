# 📚 BookBot

BookBot is a command-line application that analyzes a text file and generates statistics about it.

> **Note:** This project was built as part of the Boot.dev Backend Developer course. The implementation was completed by following the guided project instructions while writing the code myself.

## Features

- Count total words
- Count character frequency
- Sort characters by frequency
- Ignore non-alphabetical characters in the report

## Technologies

- Python
- Modules
- Functions
- Dictionaries
- Lists
- File Handling

## How to Run

```bash
python book_bot.py books/frankenstein.txt
```

## Example Output

```text
========== BOOKBOT ==========
Analyzing book found at books/frankenstein.txt...
---------- Word Count ----------
Found 75767 total words
---------- Character Count ----------
e: 44538
t: 29493
a: 25894
...
========== END ==========
```

## Project Structure

```
book_bot.py
stats.py
```

## What I Learned

- Splitting code into modules
- Reading text files
- Command-line arguments
- Dictionaries
- Sorting
- Writing reusable functions
