import tweepy
import pandas as pd
import snscrape.modules.twitter as sntwitter

query = "Asuransi"
twit = []
limit = 200

for i in sntwitter.TwitterSearchScraper(query).get_items():
    if len(twit) == limit:
        break
    else:
        twit.append([i.date, i.user.username, i.content])
df = pd.DataFrame(twit, columns=['Date', 'User', 'tweet'])
df.to_csv('x.csv', index=False)
df = pd.read_csv('x.csv')
print(df)