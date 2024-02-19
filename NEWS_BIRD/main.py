from typing import List, Tuple

from bs4 import BeautifulSoup
from urllib.request import urlopen

class MediaCrawler:
    def __init__(self):
        self.root_url = "https://media.naver.com/press/"
        self.media_list: List[Media] = []

    def init_media(self):
        root_html = urlopen(self.root_url)
        bs = BeautifulSoup(root_html, "html.parser")
        a_list = bs.find(class_="press_list_only").find_all("a")
        media_url_list = [i["href"] for i in a_list]

        # Create Media List
        for url in media_url_list:
            html = urlopen(url)
            bs = BeautifulSoup(html, "html.parser")
            title = bs.find(class_="press_hd_name").text.strip()
            headline_info = bs.find_all(class_="press_news_item")
            self.media_list.append(Media(title,url,headline_info))

    def run(self) -> None:
        # not run
        self.init_media()


    def test(self):
        for media in self.media_list:
            media.media_content_print()
            print("-------------------")

class Media:
    def __init__(self, name, url, headline_info):
        self.title = name
        self.url = url
        self.headline_list: List[Tuple] = list(map(self.headline_parser, headline_info))
        self.media_content_list: List[MediaContent] = list(map(self.create_media_content, self.headline_list))


    @staticmethod
    def headline_parser(headline_info) -> Tuple:
        news_link = headline_info.find("a")["href"]
        news_title = headline_info.text.strip("\n")

        return news_title, news_link

    @staticmethod
    def create_media_content(headline):
        return MediaContent(headline)

    def media_content_print(self):
        for i in self.media_content_list:
            i.print_info()


class MediaContent:
    def __init__(self, headline_tuple):
        self.__title = headline_tuple[0]
        self.__href = headline_tuple[1]

    def print_info(self):
        print(f"{self.title}: {self.href}")

    @property
    def title(self):
        return self.__title

    @property
    def href(self):
        return self.__href

m2 = MediaCrawler()
m2.run()
m2.test()
