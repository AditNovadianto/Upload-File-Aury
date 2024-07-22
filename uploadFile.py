from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretkey"
app.config["UPLOAD_FOLDER"] = "./files"

class uploadFileForm(FlaskForm):
    file = FileField('File')
    submit = SubmitField('Upload File')

@app.route("/", methods=['GET', 'POST'])
def home():
    return "Hello, this is home page!"

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    form = uploadFileForm()

    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"], secure_filename(file.filename)))
        return "File uploaded"
    
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)