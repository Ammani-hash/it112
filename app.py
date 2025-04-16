from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi, this my Flask App :)"

@app.route('/about')
def about():
    return "My name is Ammanuel. I am a filmmaker/editor and a application development major here at North Seattle College!"

if __name__ == '__main__':
    app.run(debug=True)
