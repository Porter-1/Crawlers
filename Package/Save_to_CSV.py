import pandas as pd

def save_to_csv(csv_name, titles, urls, authors, translators, publishers, publish_dates, prices, scores,
                star_peoples, one_evaluates):
    df = pd.DataFrame()  # 初始化一个DataFrame对象
    df['书名'] = titles
    df['豆瓣链接'] = urls
    df['作者'] = authors
    df['译者'] = translators
    df['出版社'] = publishers
    df['出版日期'] = publish_dates
    df['价格'] = prices
    df['评分'] = scores
    df['评分人数'] = star_peoples
    df['一句话评价'] = one_evaluates
    df.to_csv(csv_name, encoding='utf-8-sig')  # 添加 BOM 标记