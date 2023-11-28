import requests
from bs4 import BeautifulSoup

# Baca URLnya dan ambil HTMLnya,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# Kamu akan memulai "scraping" dari data pada halaman ini
url = 'https://www.sederet.com/tutorial/nama-nama-makanan-dalam-bahasa-inggris/'

# Gunakan requests library untuk mendapatkan kode HTML dari link diatas
data = requests.get(url=url, headers=headers)

# library BeautifulSoup memudahkan kita dalam
# menguraikan kode HTML tersebut,
soup = BeautifulSoup(data.text, 'html.parser')

# Menggunakan select
# movies = soup.select_one('.content-body > p:nth-child(12) > em:nth-child(1)').text
# print(movies)
# movies = soup.select_one('.content-body > p:nth-child(12) > em:nth-child(3)
# Looping pada setiap filmnya
# figure.wp-block-table:nth-child(10) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1)
# figure.wp-block-table:nth-child(10) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1)
# figure.wp-block-table:nth-child(10) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1)
# div.article_content:nth-child(6) > ul:nth-child(10) > li:nth-child(1) > em:nth-child(1)
# div.article_content:nth-child(6) > ul:nth-child(10) > li:nth-child(2) > em:nth-child(1)

for i in range(30):
    # Pertama, mari kita ambil judul dari filmnya
    movies = soup.select_one(f'div.article_content:nth-child(6) > ul:nth-child(14) > li:nth-child({i+1}) > em:nth-child(1)').text
    print(movies)