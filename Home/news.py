# newsapp/news.py

import requests
from langdetect import detect

class News:
    def __init__(self, topic):
        self.topic = topic
        self.url = f"https://newsapi.org/v2/everything?q=law&apiKey=69ec163d3a8c4dcb934dcbbb79aa8ec2"
        self.fetch_news()

    def fetch_news(self):
        try:
            self.response = requests.get(self.url)
            self.response.raise_for_status()  # Raise HTTPError for bad responses
            if self.response.status_code == 200:
                self.articles = self.response.json().get('articles', [])
            else:
                print(f"Error occurred: {self.response.status_code}")
                print(self.response.json())  # Print detailed error response
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Request failed: {err}")

    def get_articles(self):
        articles = []
        for article in self.articles:
            source = article.get('source', {}).get('name', 'Unknown')
            author = article.get('author', 'Unknown')
            title = article.get('title', 'No title')
            description = article.get('description', 'No description')
            url = article.get('url', 'No URL')

            try:
                language = detect(description)
                title_language = detect(title)
                if language == "en" and title_language == "en":
                    articles.append({
                        'source': source,
                        'author': author,
                        'title': title,
                        'description': description,
                        'url': url
                    })
            except Exception as e:
                print(f"Error detecting language: {e}")
        return articles
