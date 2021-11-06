from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

from json import dumps

@app.route("/json_posts")
def json_posts():
    return dumps(posts)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title="HOME PAGE ")
     

@app.route("/reservation")
def reservation():
    return render_template('reservation.html')

@app.route("/contactus")
def contactus():
    return render_template('contactus.html')


@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')



@app.route("/regestration")
def regestration():
    return render_template('regestration.html')




@app.route("/login")
def login():
    return render_template('login.html')





app.run(debug=True)
    