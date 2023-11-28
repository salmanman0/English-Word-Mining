from googletrans import Translator

def terjemah(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='id')
    return translation.text

# Contoh penggunaan
# english_text = "Hello, how are you?"
# indonesian_translation = terjemah(english_text)
