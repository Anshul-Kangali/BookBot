def word_count(text: str) -> str:
  word = text.split()
  return len(word)

def char_count(text: str) -> dict[str, int]:
  characters = {}
  for char in text:
    if char.lower() not in characters:
      characters[char.lower()] = 1
      continue
    characters[char.lower()] += 1
  return characters
  
def sort_on(count: tuple[str, int]):
  return count[1]
  
def char_dict_to_sorted_list(data: dict[str, int]) -> list[tuple[str, int]]:
  sort = []
  for key, value in data.items():
    sort.append((key, value))
  sorted_list = sorted(sort, reverse=True, key=sort_on)
  return sorted_list
