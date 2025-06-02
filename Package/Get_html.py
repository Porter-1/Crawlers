import requests
def get_html(url):
    headers = \
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    # 异常处理
    try:
        html = requests.get(url, headers=headers)
        # 声明编码方式
        html.encoding = html.apparent_encoding
        # 判断
        if html.status_code == 200:
            print('成功获取源代码')
            # print(html.text)
    except Exception as e:
        print('获取源代码失败：%s' % e)
    # 返回html
    return html.text
