def find_max_key(dictionary):
    return max(dictionary, key=dictionary.get) if dictionary else None

# Test function
dictionary = {'a': 10, 'b': 20, 'c': 15, 'd': 30, 'e': 25}
result = find_max_key(dictionary)
print(f"Key co gia tri lon nhat la: {result}")

