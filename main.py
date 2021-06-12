from flask import Flask, render_template

app = Flask(__name__) # instantiate the class, __name__ is a special variable


@app.route("/") # decorator
def home():
    return render_template("home.html") # now we want to return a html template


@app.route("/about/") # decorator
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
