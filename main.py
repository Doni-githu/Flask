import datetime

from flask import *

app = Flask(__name__)
app.secret_key = "password"

@app.route("/")
def home():
    return render_template('main.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/search")
def greet():
    q = request.args.get("q")
    if not q:
        return render_template('form.html')
    return redirect(f"http://google.com/search?q={q}")


@app.route('/time')
def time():
    time = datetime.datetime.now()
    return render_template('time.html', time=time)


@app.route("/numbers")
def numbers():
    nums = [1, 2, 1, 5]
    return render_template('numbers.html', nums=nums)


@app.route("/regist", methods=["GET", "POST"])
def regist():

    if "registered" in request.cookies:
        return render_template('success.html', obj=json.loads(request.cookies['obj']))

    if request.method == "GET":
        return render_template('register.html')

    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    if len(password) > 8:
        return render_template('error.html', because="Your password must not be more than 8")

    file = request.files['CV']
    file.save("uploads/bmw-i7-teaser.jpg")



    obj = [
        {"text": 'Your nikname', "info": username},
        {"text": 'Your email', "info": email},
        {"text": 'Your password', "info": password}
    ]

    res = make_response(
        render_template('success.html', obj=obj)
    )
    res.set_cookie("obj", json.dumps(obj))
    session['obj'] = obj[0]['info']
    res.set_cookie("registered", 'true')

    return res


if __name__ == '__main__':
    app.run(debug=True, port=4100)
