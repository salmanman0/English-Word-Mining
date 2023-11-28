import pandas as pd
import requests
from translate import terjemah
from get_random import generate_word
from get_random import not_random
words = pd.read_csv('unigram_freq.csv')
database = []
def get_dictionary_data(word):
    api_key = "YOUR API KEY"
    base_url = "https://dictionaryapi.com/api/v3/references/collegiate/json/"
    url = f"{base_url}{word}?key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad requests
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None

sum_word = len(words['word'].unique())
for i in range(20): 
    word_to_lookup = not_random(i+1000)
    print("kata random :",word_to_lookup)
    dictionary_data = get_dictionary_data(word_to_lookup)

    if dictionary_data is not None:
        if not dictionary_data or type(dictionary_data[0]) is str :
            kata = word_to_lookup
            jenis = "None"
            pengucapan = "None"
            arti = terjemah(kata)
            gambar = "Default.jpg"
            penjelasan = "None"
            combine = {'kata': kata,'jenis' : jenis, 'pengucapan':pengucapan,'penjelasan':penjelasan,'pengucapan':pengucapan,'arti':arti, 'gambar':gambar}

            # print("Kata :", kata+"\nJenis :",jenis+"\nPengucapan :", pengucapan+"\nTerjemahan :",arti+"\nPenjelasan :",penjelasan+"\nGambar :", gambar)
            print(i)
            print("================================================================================================")
        else :
            kata = word_to_lookup
            if 'fl' in dictionary_data[0] :
                jenis =  dictionary_data[0]['fl']
            else :
                jenis = dictionary_data[0]['cxs'][0]['cxtis'][0]['cxt']
            if 'hwi' in dictionary_data[0] and 'prs' in dictionary_data[0]['hwi'] and dictionary_data[0]['hwi']['prs']:
                pengucapan = dictionary_data[0]['hwi']['prs'][0]['mw']
            else:
                pengucapan = dictionary_data[0]['hwi']['hw']
            arti = terjemah(kata)
            gambar = "Default.jpg"
            if dictionary_data[0]['shortdef'] == [] :
                penjelasan = jenis
            else :
                penjelasan = dictionary_data[0]['shortdef'][0]
            penjelasan = terjemah(penjelasan)
            combine = {'kata': kata,'jenis' : jenis, 'pengucapan':pengucapan,'penjelasan':penjelasan,'pengucapan':pengucapan,'arti':arti, 'gambar':gambar}
            
            # print("Kata :", kata+"\nJenis :",jenis+"\nPengucapan :", pengucapan+"\nTerjemahan :",arti+"\nPenjelasan :",penjelasan+"\nGambar :", gambar)
            print(i)
            print("================================================================================================")

    else:
        print("Failed to retrieve data.")
        print("================================================================================================")

    database.append(combine)

df = pd.DataFrame(database)
file_path = "dictionary-bingbank3.csv"
# Writing to CSV file
df.to_csv(file_path, index=False)

print(f"Data has been saved to {file_path}")
