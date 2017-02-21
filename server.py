from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def greeting_generator():
    return render_template("index.html")


@app.route('/greeting')
def greeting():
    user = request.args.get("person")
    return render_template("greeting.html", name=user)


if __name__ == "__main__":
    app.run(debug=True)
