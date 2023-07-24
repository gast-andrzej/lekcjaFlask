from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/matrix")
def func_matrix():
    return dict(zip(list(range(1,100)), list(__import__("string").ascii_uppercase)))

@app.route("/passwd")
def func_passwd():
    return ''.join(list(__import__("random").choice(list(__import__("string").punctuation)
                                                    + list(__import__("string").ascii_letters)
                                                    + list(__import__("string").digits)) for i in range(100)))

@app.route("/calc", methods = ["GET", "POST"])
def CALC():
    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        res = num1 + num2
        return f"Resoult {res}"
    return render_template("CALC.html")



if __name__ == "__main__":
    app.run()