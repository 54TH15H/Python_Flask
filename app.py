import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from bot import search_image_in_telegram_groups

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['image']
        if uploaded_file:
            filename = secure_filename(uploaded_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(filepath)

            matches = search_image_in_telegram_groups(filepath)
            return render_template('index.html', matches=matches)

    return render_template('index.html', matches=None)

if __name__ == '__main__':
    app.run(debug=True)