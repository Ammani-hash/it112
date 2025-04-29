from flask import Flask, request, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database backbone
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)

# Starting and filling up the databas
with app.app_context():
    db.create_all()
    if Item.query.count() == 0:
        db.session.add_all([
            Item(name = "Pacha Collective", category="Cafe", description="A cozy work area near Green Lake where you can get a lot of focused work done!"),
            Item(name = "North Seattle College Library", category="Library", description="Recently opened, this library is one of my favorite places to go to spend large chunks of time near the end of the quarter to study. Great wifi, and very quiet."),
            Item(name = "Jewel Box", category="Coffee Shop", description="If you are looking for a place that is open till late to get work don, this is th spot since most places close earlier.")
        ])
        db.session.commit()

# Sample fortunes (I kept everything from the last project)
fortunes = {
    'green': {
        '1': "You will major in Computer Science!",
        '2': "You will major in Biology.",
        '3': "You will major in Graphic Design",
    },
    'yellow': {
        '1': "You will be roommates with your best friend.",
        '2': "You will have a private room.",
        '3': "You will have a bunk bed.",
    },
    'red': {
        '1': "You are going to excel in all your classes",
        '2': "You will accomplish all your goals after college.",
        '3': "You’ll reconnect with an old friend.",
    },
}

# Route displays the form + item list
@app.route('/', methods=['GET', 'POST'])
def index():
    fortune_message = ""
    if request.method == 'POST':
        name = request.form['user']
        color = request.form['color']
        number = request.form['number']
        message = fortunes.get(color, {}).get(number, "Your future is mysterious...")
        fortune_message = f"<h2>Hello, {name}!</h2><p><strong>Your fortune:</strong> {message}</p>"

    items = Item.query.all()

    full_html = f'''
    <!doctype html>
    <html>
    <head><title>Fortune Teller</title></head>
    <body>
        <h1>Fortune Teller & Study Locations </h1>

        <form method="POST" action="/">
            <label>Name:</label><br>
            <input type="text" name="user"><br><br>

            <label>Choose a color:</label><br>
            <select name="color">
                <option>green</option>
                <option>yellow</option>
                <option>red</option>
            </select><br><br>

            <label>Choose a number:</label><br>
            <select name="number">
                <option>1</option>
                <option>2</option>
                <option>3</option>
            </select><br><br>

            <button type="submit">Submit</button>
        </form>

        {fortune_message}

        <hr>

        <h2>Quite Places to Work, Seattle</h2>
        <ul>
    '''
    for item in items:
        full_html += f"<li><a href='/items/{item.id}'>{item.name}</a></li>"
    full_html += "</ul>"

    return full_html

# Item detail route
@app.route('/items/<int:item_id>')
def item_detail(item_id):
    item = Item.query.get_or_404(item_id)
    return f"""
        <h1>{item.name}</h1>
        <p><strong>Category:</strong> {item.category}</p>
        <p><strong>Description:</strong> {item.description}</p>
        <a href="/">Back to main page</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
