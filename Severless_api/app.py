import json
import requests
import random

# 定义一个名为 select 的函数，接受一个参数 a。
# 此函数基于给定的参数 a 从预定义的字典中选择一个对应的值。
# 如果参数 a 不在字典的键中，则随机选择一个键的值返回。
def select(a):
    dict = {'Anime': 'a', 'Comic': 'b', 'Game': 'c', 'Literature': 'd', 'Original': 'e', 'Internet': 'f', 'Other': 'g', 'Video': 'h', 'Poem': 'i', 'NCM': 'j', 'Philosophy': 'k', 'Funny': 'l'}
    if str(a) in dict.keys():
        return dict[str(a)]
    else:
        return dict[str(random.choice(list(dict.keys())))]

# 定义处理函数 handler，它处理事件触发时的逻辑。
def handler(event, context):
    # 将 event 参数从字符串反序列化为字典。
    my_event = json.loads(event)
    # 从 my_event 中提取 HTTP 请求的路径。
    path = my_event['requestContext']['http']['path']
    # 尝试获取查询参数中的 'category' 值，如果不存在则为 None。
    category_value = my_event.get('queryParameters', {}).get('category')

    # 如果请求路径为根路径 '/'，则执行以下逻辑。
    if path == '/':
        # 使用 select 函数根据 category_value 获取一个类别标识符。
        category = select(category_value)
        # 根据选定的类别构造请求 URL 并发送请求。
        url = requests.get("https://api.pwxiao.top/sentences/" + category + ".json")
        text = url.text

        # 将响应文本反序列化为 JSON。
        res = json.loads(text)

        try:
            # 尝试随机选择一个索引，用于从响应中选取一条数据。
            number = random.randint(0, (len(res) - 1))
        except:
            # 如果出现异常（如列表为空），则将索引设置为 6。
            number = 6

        # 根据选定的索引获取结果。
        result = res[number]

        # 构造并返回 HTTP 响应。
        return {
            'statusCode': 200,
            'body': json.dumps(result, ensure_ascii=False)
        }
    # 如果请求路径为 '/search/'，则执行搜索相关的逻辑。
    elif path == '/search/':
        # 尝试获取查询参数中的 's' 值，如果不存在则为 None。
        query = my_event.get('queryParameters', {}).get('s')
        key = 'hitokoto'
        # 向指定的 URL 发送请求，这里假设是搜索用的 URL。
        url = requests.get("https://api.pwxiao.top/sentences/i.json")
        text = url.text
        data = json.loads(text)

        # 在数据中搜索包含查询关键字的项。
        matches = [item for item in data if key in item and query in item[key]]
        # 构造并返回包含搜索结果的 HTTP 响应。
        return {
            'statusCode': 200,
            'body': json.dumps(matches, ensure_ascii=False)
        }
