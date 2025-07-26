import json
import random
import re

file_path = "pixwalls - fixed.json"

# Allowed image extensions
valid_extensions = [".jpg", ".jpeg", ".png", ".webp"]

# Load the JSON
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Shuffle the items
if isinstance(data, list):
    random.shuffle(data)

# Fix corrupted extensions in 'thumbUrl' and 'url'
def sanitize_url(url):
    # Match .jpg, .jpeg, .png, .webp possibly followed by garbage (e.g. ".jpgg")
    return re.sub(r'(\.jpe?g|\.png|\.webp)[a-zA-Z0-9]*$', r'\1', url)

for item in data:
    if "thumbUrl" in item:
        item["thumbUrl"] = sanitize_url(item["thumbUrl"])
    if "url" in item:
        item["url"] = sanitize_url(item["url"])

# Write back safely
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
