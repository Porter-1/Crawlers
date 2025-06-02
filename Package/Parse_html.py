import requests
from lxml import etree
import pandas as pd
from Package.Save_to_CSV import save_to_csv

def parse_html(html_content):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }

    books = []
    imgUrls = []


    tree = etree.HTML(html_content)
    tables = tree.xpath('//table[@width="100%"]')
    for table in tables:
        # 获取书名
        title = table.xpath('.//div[@class="pl2"]/a/text()')[0].strip()
        # print(title)
        # 书链接
        url = table.xpath('.//div[@class="pl2"]/a/@href')[0].strip()
        # print(url)
        # 作者、译者、出版社、出版日期、价格
        info = table.xpath('.//p[@class="pl"]/text()')[0].strip()
        # print(info)

        # 拆分信息
        info_parts = [part.strip() for part in info.split('/')]

        # 判断作者信息是否包含国籍
        if '[' in info_parts[0]:
            # 提取国籍和作者
            country = info_parts[0].split(']')[0].strip('[')
            author = info_parts[0].split(']')[1].strip()
        else:
            country = ''
            author = info_parts[0]

        # 根据信息数量判断是否有译者，并处理可能的信息缺失情况
        if len(info_parts) >= 5:  # 有译者的情况
            translator = info_parts[1]
            publisher = info_parts[2]
            publish_date = info_parts[3]
            price = info_parts[4]
        elif len(info_parts) == 4:  # 无译者的情况
            translator = ''
            publisher = info_parts[1]
            publish_date = info_parts[2]
            price = info_parts[3]
        elif len(info_parts) == 3:  # 缺少价格的情况
            translator = ''
            publisher = info_parts[1]
            publish_date = info_parts[2]
            price = ''
        elif len(info_parts) == 2:  # 只有作者和出版社
            translator = ''
            publisher = info_parts[1]
            publish_date = ''
            price = ''
        else:  # 只有作者
            translator = ''
            publisher = ''
            publish_date = ''
            price = ''

        score = table.xpath('.//span[@class="rating_nums"]/text()')
        score = score[0] if score else ''

        # 获取评价人数
        people = table.xpath('.//span[@class="pl"]/text()')
        people = people[0] if people else ''

        # 获取一句话评价
        comment = table.xpath('.//span[@class="inq"]/text()')
        comment = comment[0] if comment else ''

        # 将书籍信息添加到列表
        book = {
            '书名': title,
            '链接': url,
            '国家': country,
            '作者': author,
            '译者': translator,
            '出版社': publisher,
            '出版日期': publish_date,
            '价格': price,
            '评分': score,
            '评价人数': people,
            '一句话评价': comment
        }
        books.append(book)

    return books, imgUrls
