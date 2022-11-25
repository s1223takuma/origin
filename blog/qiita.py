import requests

class QiitaArticle:
    def __init__(self, title, url):
        self.title = title
        self.url = url

class QiitaApiClient:

    def get_django_articles(self):
        # get リクエストを送る
        response = requests.get(
            "https://qiita.com/api/v2/tags/django/items",
            headers={"Authorization": "Bearer "},
        )
        if response.status_code != 200:
            raise RuntimeError("Qiitaの記事が取得できませんでした")


        qiita_articles = []
        json = response.json()
        for json_article in json:
            qiita_article = QiitaArticle(
                json_article["title"],
                json_article["url"],
            )
            qiita_articles.append(qiita_article) 
        return qiita_articles