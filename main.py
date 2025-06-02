from Package.Get_html import get_html
from Package.Parse_html import parse_html
from Package.Parse_html import  save_to_csv
from time import sleep
import os


def main():
    # 初始化数据存储列表
    all_books = []
    all_imgUrls = []

    # 爬取豆瓣图书Top250
    for i in range(10):
        url = 'https://book.douban.com/top250?start={}'.format(i * 25)
        print(f"正在爬取第{i + 1}页，URL: {url}")

        # 获取HTML内容
        html = get_html(url)

        # 解析HTML内容
        books, imgUrls = parse_html(html)

        # 将结果添加到总列表
        all_books.extend(books)
        all_imgUrls.extend(imgUrls)

        # 休眠1秒，避免请求过快
        sleep(1)

    # 打印爬取结果统计
    print(f"爬取完成，共获取{len(all_books)}本书籍信息")

    # 准备保存到CSV的数据
    titles = [book['书名'] for book in all_books]
    urls = [book['链接'] for book in all_books]
    authors = [book['作者'] for book in all_books]
    translators = [book['译者'] for book in all_books]
    publishers = [book['出版社'] for book in all_books]
    publish_dates = [book['出版日期'] for book in all_books]
    prices = [book['价格'] for book in all_books]
    scores = [book['评分'] for book in all_books]
    star_peoples = [book['评价人数'] for book in all_books]
    one_evaluates = [book['一句话评价'] for book in all_books]

    # 保存到CSV文件
    csv_name = 'douban_books_top250.csv'
    save_to_csv(csv_name, titles, urls, authors, translators, publishers,
                publish_dates, prices, scores, star_peoples, one_evaluates)

    print(f"数据已保存到 {os.path.abspath(csv_name)}")


if __name__ == '__main__':
    main()