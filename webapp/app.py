import numpy as np
import pickle

from flask import Flask
from flask import render_template

from flask_bootstrap import Bootstrap
from form import MyForm

app = Flask(__name__)

app.config.from_prefixed_env()
app.config['SECRET_KEY']
Bootstrap(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/form', methods=['GET', 'POST'])
def form():
	form = MyForm()
	if form.validate_on_submit():
		formData = form.data
		del formData['csrf_token']
		features = formData.values()
        
		features = list(map(float, features))
		# features = list(features.values())
		# features = list(map(float, features))
		print("Features", features)
		prediction = predictProgression(features)

		return render_template("result.html", prediction = prediction)
		# return redirect('/result')
	return render_template('form.html', form=form)


"""
Take a numpy array of size of age, bmi, and sex, and return predicted progression
"""
def predictProgression(features):
    num_features = 3
    to_predict = np.array(features).reshape(1, num_features)
    loaded_model = pickle.load(open('model.pkl', 'rb'))
    result = loaded_model.predict(to_predict)
    return result[0]
