import re
import joblib
import numpy as np
from keras.utils import pad_sequences
from keras.preprocessing.text import tokenizer_from_json
from keras.models import load_model
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
# Load your models and other resources
# (Replace these with your actual model paths and imports)
# port_stem = PorterStemmer()
# tfidf_vect = joblib.load('tfidf_vectorizer.pkl')
# lsvc = joblib.load('linear_svc_model.pkl')
# lstm_model = load_model('lstm_model.h5')
# ensemble_model = load_model('ensemble_model.h5')

# with open('tokenizer.json', 'r', encoding='utf-8') as f:
#     tokenizer_config = f.read()
#     tokenizer = tokenizer_from_json(tokenizer_config)

# with open('maxlen.txt', 'r') as f:
#     maxlen = int(f.read())

# Function for stemming (You can use it when you uncomment the code above)
# def stemming(content):
#     con = re.sub('[^a-zA-Z]', ' ', content)
#     con = con.lower()
#     con = con.split()
#     con = [port_stem.stem(word) for word in con if not word in stopwords.words('english')]
#     con = ' '.join(con)
#     return con




















