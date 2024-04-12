import requests
import json
import os

def crawl_data():
    # 从网站爬取数据的代码，这里使用一个示例URL
    url = 'https://v1.hitokoto.cn/?c=b'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from the website.")
        return None

def update_json(data):
    # 从现有的 JSON 文件中加载数据
    data_json_path = os.environ.get('DATA_JSON_PATH')
    with open(data_json_path, 'r',encoding="utf-8") as f:
        existing_data = json.load(f)

    # 更新 JSON 数据
    print(data)
    existing_data.append(data)

    # 将更新后的数据写回 JSON 文件
    with open(data_json_path, 'w',encoding="utf-8") as f:
        try:
            json.dump(existing_data, f, indent=4,ensure_ascii=False)
            print("Data successfully updated in data.json.")
        except Exception as e:
            print("Error occurred while updating data.json:", e)

def main():
    data = crawl_data()
    if data:
        update_json(data)
        print("Data updated successfully.")
    else:
        print("Data update failed.")

if __name__ == "__main__":
    main()
