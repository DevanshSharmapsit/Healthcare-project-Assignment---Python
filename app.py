from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', age_range=range(1, 101))

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        age = int(request.form['age'])
        file = request.files['file']
        if not file.filename:
            return "<h1>Error: No file selected!</h1>"
        return f'''
            <h1>Form Submitted Successfully!</h1>
            <p>Name: {name}</p>
            <p>Age: {age}</p>
            <p>File Uploaded: {file.filename}</p>
        '''
    except ValueError:
        return "<h1>Error: Invalid Age!</h1>"
    except Exception as e:
        return f"<h1>Error: {str(e)}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
