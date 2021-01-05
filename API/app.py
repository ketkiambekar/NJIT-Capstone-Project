import joblib
import util
#from flask import Flask, request, jsonify
from flask import Flask, render_template, jsonify,request

app = Flask(__name__)
app.config["DEBUG"]=True
model = joblib.load("EAFC_TC.joblib")
vectorizer = joblib.load("EAFC_vectorizer.joblib")

@app.route('/', methods=['POST'])
def index():
    return render_template('/index.html')

@app.route('/predict', methods=['GET'])
def predict():
    text =  request.form.get("msg")
    vectorizer =  util.Lemmatize(text)
    text_vectorized = util.vectorize(text, vectorizer)
    y_pred=model.predict(text_vectorized)

    if y_pred[0]==0:
        result = "Class 0: Newly Discovered"
    elif y_pred[0]==1:
        result = "Class 1: Venting/Sharing"
    elif y_pred[0]==2:
        result = "Class 2: Reaching out for help"
    elif y_pred[0]==3:
        result = "Class 3: Passing Away"
    elif y_pred[0]==4:
        result = "Class 4: Remission"

    return  "<h2>"+ result +"</h2>"
app.run()

