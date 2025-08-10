from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from model import predict

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB max size

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_and_predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error="No file part in the request")
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error="No file selected")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            results = predict(filepath)
            return render_template('result.html', results=results, filename=filename)
        else:
            return render_template('index.html', error="File type not allowed. Please upload an image.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
