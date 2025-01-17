import feedparser

gn_url = "https://news.google.com/rss/search?q=taoist&hl=en-US&gl=US&ceid=US:en"

gn_feed = feedparser.parse(gn_url)

print(gn_feed)