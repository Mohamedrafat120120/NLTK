# محمد رافت محمد البهي- cs
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import pandas as pd


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

dataset = pd.read_csv(r"C:\Users\ghost\Desktop\archive_2\text.csv")


# Replace 'your_dataset.csv' with your actual dataset file
df = pd.read_csv(r"C:\Users\ghost\Desktop\archive_2\text.csv")


stemmer = PorterStemmer()


def tokenize_and_stem(text):
    words = word_tokenize(text)
    stemmed_words = [stemmer.stem(word) for word in words]
    return " ".join(stemmed_words)


df['tokenized_and_stemmed'] = df['text_column'].apply(tokenize_and_stem)


print(df[['text_column', 'tokenized_and_stemmed']])
