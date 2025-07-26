import json
import random

file_path = "pixwalls - fixed.json"

# Read JSON file
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Check if it's a list
if isinstance(data, list):
    random.shuffle(data)

# Write back the shuffled data
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
