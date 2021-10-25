from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/reservation")
def reservation():
    return render_template('templates/reservation.html')

@app.route("/")
def contactus():
    return render_template('templates/contactus.html')


@app.route("/")
def aboutus():
    return render_template('templates/aboutus.html')



@app.route("/")
def regestration():
    return render_template('templates/regestration.html')




@app.route("/")
def login():
    return render_template('templates/login.html')



    



if __name__ == '__main__':
    app.run(debug=True)
    