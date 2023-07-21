import json
import requests

def search():
    query = "白"
    key = 'hitokoto'
    url = requests.get("https://api.pwxiao.top/sentences/i.json")
    text = url.text
    data = json.loads(text)
        
    matches = [item for item in data if key in item and query in item[key]]
    matches = json.dumps(matches,ensure_ascii=False)
    
    return matches


print(search())