from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)






# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get the input data from the request
#         data = request.json
#         text_data = data['text']

#         # Preprocess the new text data
#         text_data = stemming(text_data)
#         text_data_tfidf = tfidf_vect.transform([text_data])

#         # Predict using LinearSVC
#         lsvc_pred = lsvc.predict(text_data_tfidf)

#         # Tokenize and pad the input data for LSTM model
#         text_data_seq = tokenizer.texts_to_sequences([text_data])
#         # text_data_pad = pad_sequences(text_data_seq, padding='post', maxlen=maxlen)

#         # Predict using LSTM model
#         # lstm_pred = lstm_model.predict(text_data_pad)

#         # Convert predictions to the correct data type (float32)
#         lsvc_pred = lsvc_pred.astype('float32')
#         lstm_pred = lstm_pred.astype('float32')

#         # Reshape and stack the predictions horizontally
#         ensemble_input = np.hstack([lsvc_pred.reshape(-1, 1), lstm_pred.reshape(-1, 1)])

#         # Predict using Ensemble model
#         ensemble_pred = ensemble_model.predict(ensemble_input)

#         # Determine the result based on your threshold
#         result = {"prediction": "fake" if ensemble_pred[0][0] >= 0.5 else "real"}
        
#         return jsonify(result)

#     except Exception as e:
#         return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)







# app = Flask(__name__)


# if __name__ == '__main__':
#     app.run(debug=True)

