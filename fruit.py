import pandas as pd
import requests
from translate import terjemah
from get_random import generate_fruit

fruits = pd.read_csv('fruits.txt')
database = []
def get_dictionary_data(word):
    api_key = "413fd211-3e6b-4927-bc26-c0751a731ea4"
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

sum_word = len(fruits['fruit'].unique())
for i in range(sum_word): 
    word_to_lookup = generate_fruit()
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
            combine = {'kata': kata,'jenis' : jenis, 'kategori': "buah", 'pengucapan':pengucapan,'penjelasan':penjelasan,'pengucapan':pengucapan,'arti':arti, 'gambar':gambar}

            # print("Kata :", kata+"\nJenis :",jenis+"\nPengucapan :", pengucapan+"\nTerjemahan :",arti+"\nPenjelasan :",penjelasan+"\nGambar :", gambar)
            print(i)
            print("================================================================================================")
        else :
            kata = word_to_lookup
            jenis =  dictionary_data[0]['fl']
            if 'hwi' in dictionary_data[0] and 'prs' in dictionary_data[0]['hwi'] and dictionary_data[0]['hwi']['prs']:
                pengucapan = dictionary_data[0]['hwi']['prs'][0]['mw']
            else:
                pengucapan = dictionary_data[0]['hwi']['hw']
            arti = terjemah(kata)
            gambar = "Default.jpg"
            penjelasan = dictionary_data[0]['shortdef'][0]
            penjelasan = terjemah(penjelasan)
            combine = {'kata': kata,'jenis' : jenis, 'kategori': "buah", 'pengucapan':pengucapan,'penjelasan':penjelasan,'pengucapan':pengucapan,'arti':arti, 'gambar':gambar}
            
            # print("Kata :", kata+"\nJenis :",jenis+"\nPengucapan :", pengucapan+"\nTerjemahan :",arti+"\nPenjelasan :",penjelasan+"\nGambar :", gambar)
            print(i)
            print("================================================================================================")

    else:
        print("Failed to retrieve data.")
        print("================================================================================================")

    database.append(combine)

df = pd.DataFrame(database)
file_path = "fruit-bingbank.csv"
# Writing to CSV file
df.to_csv(file_path, index=False)

print(f"Data has been saved to {file_path}")
