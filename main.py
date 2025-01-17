import feedparser
import sys

def fetch_news(search_terms):
    for search_term in search_terms:
        search_term = search_term.replace(" ", "+")
        gn_url = f"https://news.google.com/rss/search?q={search_term}&hl=en-US&gl=US&ceid=US:en"
        gn_feed = feedparser.parse(gn_url)

        if gn_feed.entries:
            for news_item in gn_feed.entries:
                news_title = news_item.title
                news_link = news_item.link
                publication_date = news_item.published
                news_source = news_item.source
                print(
                    f"Headline: {news_title}\nPublished: {publication_date}\nSource: {news_source}\nURL: {news_link}"
                )
                print(20 * "-")
        else:
            print(f"No news found for the term: {search_term}")

if __name__ == "__main__":
    search_terms = sys.argv[1:]
    if not search_terms:
        print("No search terms provided. Exiting.")
        sys.exit()
    fetch_news(search_terms)