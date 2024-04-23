import logging

from bs4 import BeautifulSoup

from ._base import ArticleData
from ._base import CustomSitemapSpider

logger = logging.getLogger(__name__)


class News24Spider(CustomSitemapSpider):
    name = "news24_spider"
    
    def _get_article_data(self, soup: BeautifulSoup) -> ArticleData:
        headline = soup.find("h1", attrs={"class": "article__title"}).text.strip()
        category = None

        content_soup = soup.find("div", attrs={"class": "article__body NewsArticle"})
        content_elements = content_soup.find_all("p")
        content = self._clean_string(" ".join([elem.text for elem in content_elements]))
        
        return self.article_data(headline, content, category)