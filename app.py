import feedparser

gn_url = "https://news.google.com/rss/search?q=taoist&hl=en-US&gl=US&ceid=US:en"

gn_feed = feedparser.parse(gn_url)

# print(gn_feed)

# Iterate through each news entry in the feed
for entry in gn_feed.entries:
    news_title = entry.title
    news_link = entry.link
    publication_date = entry.published
    news_source = entry.source

    print([news_title, publication_date, news_source, news_link])