# Quotera

基于Vercel和Flask实现的api

可以随机从服务器获取一个句子和搜索诗句

## 使用

### 随机生成一句

请求地址：

```url
https://api.pwxiao.top/
```

参数说明：*https://api.pwxiao.top?catogory=*
```
’Anime':动画,
'Comic':漫画,
'Game':游戏,
'Literature':文学,
'Original':原创,
'Internet':来源网络,
'Other':其他,
'Video':影视,
'Poem':古诗文,
'NCM':网易云,
'Philosophy':哲学,
'Funny':搞笑
```
>数据库来自[一言数据库](https://github.com/hitokoto-osc/sentences-bundle)

返回值：
```
{
    "id": 1263,
    "uuid": "a58936ac-f3fb-4e5d-838e-a77a7219d1a4",
    "hitokoto": "渔舟唱晚，响穷彭蠡之滨；雁阵惊寒，声断衡阳之浦。",
    "type": "i",
    "from": "滕王阁序",
    "from_who": null,
    "creator": "毛毛毛布斯",
    "creator_uid": 562,
    "reviewer": 0,
    "commit_from": "web",
    "created_at": "1507184994",
    "length": 24
  }
```

### 搜索古诗

请求地址:

```url
https://api.pwxiao.top/search/
```

参数说明：*https://api.pwxiao.top/search/?s=query*
```
query为要搜索的内容
```







### 使用Vercel一键部署

&emsp;&emsp;点击下方按钮根据提示操作即可

&emsp;&emsp;[![Powered by Vercel](https://www.datocms-assets.com/31049/1618983297-powered-by-vercel.svg)](https://vercel.com/new/clone?repository-url=https://github.com/pwxiao/MyWords_API)




