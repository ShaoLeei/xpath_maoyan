#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Hamdi
import requests

from lxml import etree


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
page = 0
while page < 91:
    url = 'https://maoyan.com/board/4?offset=' + str(page)
    page += 10
    response = requests.get(url).text

    html = etree.HTML(response)


    titles = html.xpath('//p[@class="name"]//text()')
    movie_urls = html.xpath('//p[@class="name"]/a/@href')
    img_urls = html.xpath('//img[@class="board-img"]/@src')
    stars = html.xpath('//p[@class="star"]//text()')

    for title, movie_url, star in zip(titles, movie_urls, stars):
        movies_urls = 'https://maoyan.com' + movie_url
        print u'电影:' + title + u'\t电影地址:' + str(movies_urls) + '\t' + star


