from flask import Flask, redirect, url_for, request,render_template
import pickle
import numpy as np
import sklearn
app = Flask(__name__)


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 14)
    loaded_model = pickle.load(open("heart_disease.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result


@app.route("/")
def index():
    return render_template("index.html");
@app.route('/result',  methods =["GET", "POST"])
def result():
    if request.method == "POST":

       age = request.form.get("age")
       # getting input with name = lname in HTML form
       cp = request.form.get("cp")
       trestbps = request.form.get("trestbps")
       chol= request.form.get("chol")
       fbs= request.form.get("fbs")
       Gender = request.form.get("Gender")
       Geography = request.form.get("Geography")
       restecg = request.form.get("restecg")
       thalach = request.form.get("thalach")
       exang = request.form.get("exang")
       oldpeak = request.form.get("oldpeak")
       slope = request.form.get("slope")
       Ca= request.form.get("Ca")
       thal = request.form.get("thal")
       l1=[age,cp,trestbps,chol,fbs,Gender,Geography,restecg,thalach,exang,oldpeak,slope,Ca,thal]
       answer = ValuePredictor(l1)
    return render_template("result.html",Age=answer)


if __name__ == '__main__':
   app.run(debug = True)
