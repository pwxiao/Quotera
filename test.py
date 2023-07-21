import json

def search():
    key = 'text'
    query = '天气'
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    matches = [item for item in data if key in item and query in item[key]]
    
    return matches


print(search())