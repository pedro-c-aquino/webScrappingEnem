from pathlib import Path

import scrapy
from scrapy.http import Response

anos = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
        2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
lista_urls = []

for ano in anos:
    url = f"https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enem/provas-e-gabaritos/{ano}"
    lista_urls.append(url)


class Spider(scrapy.Spider):
    name = "provas"


    def start_requests(self):
        urls = lista_urls
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        href_list = response.css('a::attr(href)').getall()
        for href in href_list:
            if 'amarel' in href.lower() or 'cd10' in href.lower():
                print(href)


