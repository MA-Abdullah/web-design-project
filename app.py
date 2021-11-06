from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Sr',
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
    return render_template('home.html',
    title=" HOME PAGE " ,
    myposts= posts)
     

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




@app.errorhandler(404)
def err_404(error):
   return render_template( '404.html' ), 404


@app.route("/jsondata")
def jsondata():
    return render_template('jsondata.html')



app.run(debug=True)
    