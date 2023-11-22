from flask import Flask , request
import requests , json , random




@app.route('/',methods=["GET"])
def return_class():
   headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; V2203A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110005 MMWEBSDK/20230701 MMWEBID/7078 MicroMessenger/8.0.40.2420(0x28002858) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64',
    'Referer': 'https://www.example.com',
    'Cookie': 'PHPSESSID=ajrghtq0nm1ivf9baqjd64ihpp'
    }


    # 发送GET请求
    response = requests.get('http://alpro.xiaovei.cn:80/api/kebiao/getList', headers=headers)

    # 检查响应状态码
    if response.status_code == 200:
        # 处理响应数据
        data = response.text


    res = json.loads(data)

    course_list = res["data"]

    tables = []
    # 遍历课程列表
    for course in course_list:
        # 获取课程信息
        
        course_name = course["course_name"]
        teacher = course["teacher"]
        address = course["address"]
        start_week = course["start_week"]
        end_week = course["end_week"]
        start_jie = course["start_jie"]
        end_jie = course["end_jie"]
        week = course["week"]
        if(start_week<=13<=end_week and week==3):
            mdict={
                'course_name': course_name,
                'teacher' : teacher,
                'address' : address,
                'start_jie' : start_jie,
                'end_jie' : end_jie,
                'week' : week,
                'start_week' : start_week,
                'end_week' : end_week
            }
            tables.append(mdict)

    sorted_tables = sorted(tables,key=lambda d:d['start_jie'])
    content = ''
    for table in sorted_tables:
        if(table['start_week']<=13<=table['end_week'] and table['week']==3):
            # 打印课程信息
            content+= table['course_name']+"\n"
            content+= table['teacher']+'\n'
            content+= table['address']+'\n'
            content+= str(table['start_jie'])+" "+str(table['end_jie'])+"节"
            content+= '\n\n'

    fina_res = json.dumps(content,ensure_ascii=False)
    
    return fina_res
