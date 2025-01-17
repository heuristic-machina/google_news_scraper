import feedparser
import sys
import pyshorteners

# Shortens a given url using tinyURL
def shorten_url(url):
     s = pyshorteners.Shortener()
     try:
          short_url = s.tinyurl.short(url)
          return short_url
     except Exception as e:
          print(f"Error shortening URL: {e}")
          return url

# Cleans a news title by removing the source name
def clean_title(title):
     return title.rsplit(' - ', 1)[0].strip()

def fetch_news(search_terms, max_articles):
        for search_term in search_terms:
            search_term = search_term.replace(" ", "+")
            gn_url = f"https://news.google.com/rss/search?q={search_term}&hl=en-US&gl=US&ceid=US:en"
            gn_feed = feedparser.parse(gn_url)

        if gn_feed.entries[:max_articles]:
            for news_item in gn_feed.entries[:max_articles]:
                news_title = clean_title(news_item.title)
                news_link = shorten_url(news_item.link)
                publication_date = news_item.published
                news_source = news_item.source.get("title")
                source_url = news_item.source.get("href")
                print(
                    f"Headline: {news_title}\nURL: {news_link}\nPublished: {publication_date}\nSource: {news_source} ({source_url})"
                )
                print(20 * "-")
            # print(f"No news found for the term: {search_term}")

if __name__ == "__main__":
    search_terms = sys.argv[1:-1]
    max_articles = int(sys.argv[-1])
    if not search_terms:
        print("No search terms provided. Exiting.")
        sys.exit()
    fetch_news(search_terms, max_articles)

# python main.py "meta llama 3.2" "chatgpt o1 model" 1