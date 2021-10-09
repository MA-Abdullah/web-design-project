print ('hello')


from logging import debug
from flask import Flask
app = Flask(__name__)

@app.route("/")
def Home ():
    x=1
    y=55
    return f"""<h1 style='coler:red' >Hello world!</h1> 
                <h1> {x+y} </h1>"""



app.run (debug=True)

print('good bey ')