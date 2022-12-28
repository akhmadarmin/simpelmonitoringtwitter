# simpelmonitoringtwitter

Baca baca modul snscrape dan tweepy, terus pake pandas python buat monitoring twitter tanpa API dari twitter

contoh kasus ini saya pake buat jadiin dataframe sederhana berdasar siapa usernamenya, kapan twitnya juga link twitnya, dengan contoh  kata yang saya pakai adalah "asuransi" di seluruh belantara (halah) twitter pengen tau, apa aja sih twit orang2 tentang keyword "asuransi"



Nah ini gampang banget make snscrape ama tweepy juga pandas.



Pertama bikin keyword apa dulu yang mau dipake, lalu pake limit dan lanjut bikin perulangan, dan append ke list kosong trus pake pandas buat bikin kolom, lalu jadiin ke excel atw csv kalau mau langsung baca tinggal print(df) .



Di sini df adalah variabel dengan obyek pandas bwt read csv

gampang yak...

pertama install library yang dibutuhkan

pip install pandas
pip install tweepy
pip install snscrape
