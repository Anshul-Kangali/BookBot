import sys
from stats import word_count
from stats import char_count
from stats import char_dict_to_sorted_list

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 book_bot.py <path_to_book>")
    sys.exit(1)
  file = sys.argv[1]
  contents = get_book_text(file)
  num_words = word_count(contents)
  char_list = char_dict_to_sorted_list(char_count(contents))
  print_report(file, num_words, char_list)

def get_book_text(file: str) -> str:
  with open (file, "r") as f:
    contents = f.read()
  return contents

def print_report(file: str, word_count: int, char_list: list[tuple[str, int]]):
  print(
f'''\n========== BOOKBOT ==========
Analyzing book found at {file}...
---------- Word Count ----------
Found {word_count} total words
---------- Character Count ----------'''
  )
  for item in char_list:
    if not item[0].isalpha():
      continue
    print(f"{item[0]}: {item[1]}")
  print("========== END ==========")

main()
