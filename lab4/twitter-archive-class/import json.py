import json
import pandas as pd

def load_ytd(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strip the JavaScript assignment prefix (e.g., 'window.YTD.tweets.part0 = ')
    json_str = content[content.find('='):].lstrip('=').strip()
    
    data = json.loads(json_str)
    return data