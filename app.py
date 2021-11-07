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
        'date_posted': 'April 21, 2020'
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
    title=" there no page  " ,
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


from flask import request

@app.route('/handle_data', methods=['POST', 'GET'])
def handle_data():
    us = request.form['username']
    pw = request.form['password']
    # your code...
    return render_template(
        'home.html',
        posts=posts,
        message=f"{us} is registered {pw}",
        msg_class= "alert alert-success")



@app.route("/")
def hello():
    return request.args.get("page_number")

app.run(host="0.0.0.0", port=8080)



app.run(debug=True)
    