# from nltk.stem import WordNetLemmatizer
# import nltk 
# from nltk.corpus import stopwords
import re

# nltk.download('stopwords')


def clean_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'www\S+', '', text)

    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)

    # Remove all non-alphanumeric characters (except whitespace)
    text = re.sub(r'[^\w\s]', '', text)

    # Replace all whitespace with a single space
    text = re.sub(r'\s+', ' ', text)

    # Remove leading and trailing whitespace
    text = text.strip()

    # Remove stop words
    # stop_words = set(stopwords.words('english'))
    # words = text.split()
    # # words = [word for word in words if word not in stop_words]

    # # Lemmatize words
    # lemmatizer = WordNetLemmatizer()
    # words = [lemmatizer.lemmatize(word) for word in words]
    # text = ' '.join(words)
    # ## limit the text to a length 
    # ## TODO split into para

    text = text[:4000]

    return text
