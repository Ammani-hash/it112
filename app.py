<<<<<<< HEAD
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Sample fortunes
fortunes = {
    'green': {
        '1': "You will major in Computer Science!",
        '2': "You will major in Biology.",
        '3': "You will major in Graphic Design",
    },
    'yellow': {
        '1': "You will be room mates with your best friend.",
        '2': "You will have a private room.",
        '3': "You will have a bunk bed.",
    },
    'red': {
        '1': "You are going to excell in all your classes",
        '2': "You will accomplish all your goals after college.",
        '3': "You’ll reconnect with an old friend.",
    },
    
}

form_html = '''
<!doctype html>
<html>
<head><title>Fortune Teller</title></head>
<body>
    <h1>Fortune Teller</h1>
    <form method="POST" action="/fortune">
        <label>Name:</label>

        <input type="text" name="user"><br><br>

        <label>Choose a color:</label>
        <select name="color">
            <!--changed colors to the colors of my country's flag (Ethiopia)-->
            <option>green</option>
            <option>yellow</option>
            <option>red</option>
        </select><br><br>

        <label>Choose a number:</label>
        <select name="number">
            <option>1</option>
            <option>2</option>
            <option>3</option>
        </select><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
'''

@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    if request.method == 'POST':
        name = request.form['user']
        color = request.form['color']
        number = request.form['number']
        message = fortunes.get(color, {}).get(number, "Your future is mysterious...")
        return f"<h1>Hello, {name}!</h1><p>Your fortune is: <strong>{message}</strong></p><a href='/fortune'>Try Again</a>"
    return render_template_string(form_html)
=======
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi, this my Flask App :)"

@app.route('/about')
def about():
    return "My name is Ammanuel. I am a filmmaker/editor and a application development major here at North Seattle College!"
>>>>>>> 55bfa69ea0d9769cdd63c686ce0634432c50e06f

if __name__ == '__main__':
    app.run(debug=True)
