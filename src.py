import snscrape.modules.twitter as sntwitter
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
from afinn import Afinn
import re

def score_sentiment(score):
    if score >= 0.7:
        return 1, 'Baik'
    elif score >= 0.3:
        return 0, 'Lumayan'
    elif score >= -0.3:
        return -1, 'Buruk'
    else:
        return -2, 'Sangat buruk'

keyword = input("Masukkan keyword: ")
tanggal_awal = input("Masukkan tanggal awal (dd-mm-yyyy): ")
tanggal_akhir = input("Masukkan tanggal akhir (dd-mm-yyyy): ")
nama_negara = input("Masukkan nama negara: ")
limit = int(input("Masukkan limit tweet: "))

tanggal_awal = pd.to_datetime(tanggal_awal, format='%d-%m-%Y').strftime('%Y-%m-%d')
tanggal_akhir = pd.to_datetime(tanggal_akhir, format='%d-%m-%Y').strftime('%Y-%m-%d')

country_codes = pd.read_csv('https://raw.githubusercontent.com/datasets/country-codes/master/data/country-codes.csv')
country_codes = country_codes[country_codes['CLDR display name'] == nama_negara]
if country_codes.empty:
    print(f"Tidak dapat menemukan kode negara untuk {nama_negara}")
    exit()
country_code = country_codes.iloc[0]['ISO3166-1-Alpha-2']

af = Afinn()

tweets_list = []
limit = int(input("Masukkan limit jumlah tweet: "))
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{keyword} near:"{nama_negara}" within:500mi since:{tanggal_awal} until:{tanggal_akhir}').get_items()):
    if i >= limit: 
        break
    text = tweet.rawContent
    text = re.sub(r'http\S+', '', text) # hapus url
    text = re.sub(r'#\S+', '', text) # hapus hashtag
    text = re.sub(r'@\S+', '', text) # hapus mention
    text = re.sub(r'[^\w\s]', '', text) # hapus tanda baca
    
    sentiment_score_af = af.score(text)
    sentiment_category_af = score_sentiment(sentiment_score_af)
    
    tweets_list.append([tweet.date, tweet.id, text, word_tokenize(text), sentiment_score_af, sentiment_category_af[0], tweet.user.username])
    
tweets_df = pd.DataFrame(tweets_list, columns=['date', 'id', 'text', 'tokenized_text', 'sentiment_afinn', 'sentiment_score', 'user'])

# Menampilkan informasi tambahan
print(f"Rata-rata score sentiment: {tweets_df['sentiment_afinn'].mean():.2f}")
print(f"Tanggal dengan tweet terbanyak: {tweets_df['date'].value_counts().index[0].strftime('%Y-%m-%d')}")
