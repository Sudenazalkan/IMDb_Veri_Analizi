import pandas as pd
import matplotlib.pyplot as plt
# Dosya yolunu belirtelim
file_path = "C:\\Users\\sudea\\OneDrive\\Belgeler\\VeriProjeleri\\moviedataset\\IMDb_Data_final.csv"

# CSV dosyasını okutalım.
df = pd.read_csv(file_path)

print(df.head()) # Baştan ilk beş satırını gösterir
print(df.tail()) # Sondan beş satırını gösterir
print(df.shape) # Boyut bilgisine ulaşmak için kullanırız
print(df.info()) # Değişkenlerin tipleri gibi detaylı bilgi almak için kullanırız

print(df.columns) # Değişkenlerin isimlerine erişiriz

print(df.index) # İndeks bilgisine erişiriz

print(df.describe()) # Özet istatistik verilerine erişelim

# Veri setinde eksiklik olup olmadığını kontrol edelim
print(df.isnull().values.any())

print(df.isnull().sum()) # Her bir değişkende kaç tane eksik değer olduğunu hesaplar

print(df["Category"].value_counts()) # Bir kategorik değişken içerisinde kaç tane sınıf olduğunu ve kaç tane olduğunu gösterir. Burada Category değişkenini ele aldık

print(df[0:15]) # Belirli bir aralıkta seçim işlemi. 0'dan 15'e kadar gider

# Duration sütununa bakalım
print(df["Duration"].head())
# Duration sütunundaki min kelimesini temizleyelim
df["Duration"] = df["Duration"].str.replace('min','')

print(df["Duration"].head())

# En popüler film türleri hangileri ?
category_counts = df["Category"].value_counts() # Türleri sayıyoruz
print(category_counts)

# Yıl bazında kaç film çekildiğine bakalım
film_yil = df['ReleaseYear'].value_counts().sort_index()
print(film_yil)

# Çizdirelim
plt.figure(figsize=(10,6))
film_yil.plot(kind='bar')
plt.title('Yıl bazında Film Sayısı')
plt.xlabel('Yıl')
plt.ylabel('Film Sayısı')
plt.grid(True)
plt.show()

# En iyi ve en kötü filmleri bulalım
en_iyi_filmler = df.sort_values(by='IMDb-Rating',ascending=False).head(3)
print("En iyi 3 film:")
print(en_iyi_filmler[['Title','IMDb-Rating']])

en_kötü_filmler = df.sort_values(by = 'IMDb-Rating').head(3)
print("En kötü 3 film:")
print(en_kötü_filmler[['Title','IMDb-Rating']])
















