from flask import *
app = Flask(__name__)

# @app.route('/')
# def log():
#     return render_template('login.html')

# @app.route('/login', methods=['POST'])
# def login():
#     uname = request.form['username']
#     passwrd = request.form['userpass']
#     if uname == "Jayden" and passwrd == "1234":
#         return "Welcome %s" % uname + request.method
#     else:
#         return "Error in logging in" + request.method


@app.route('/')
def shopping():
    return render_template('shoppinglist.html')


@app.route('/showitems', methods=['POST', 'GET'])
def showitems():
    if request.method == 'POST':
        result = request.form
        return render_template('showitems.html', result=result)
if __name__ == '__main__':
    app.run(debug=True)
    app.run()