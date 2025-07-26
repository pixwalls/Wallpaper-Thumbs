import json
import random
import re

file_path = "pixwalls_shuffle.json"
valid_exts = [".jpg", ".jpeg", ".png", ".webp"]

# Regex pattern to clean trailing garbage from extensions
pattern = re.compile(r'(\.jpe?g|\.png|\.webp)[a-zA-Z0-9]*$', re.IGNORECASE)

def sanitize_url(url):
    match = pattern.search(url)
    if match:
        return url[:match.end()]
    return url  # Return as-is if no extension match

# Load data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Shuffle list
if isinstance(data, list):
    random.shuffle(data)

# Fix corrupted thumbUrl and url entries
for item in data:
    if 'thumbUrl' in item:
        item['thumbUrl'] = sanitize_url(item['thumbUrl'])
    if 'url' in item:
        item['url'] = sanitize_url(item['url'])

# Save the fixed file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
