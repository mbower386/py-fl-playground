from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play/')
def play():
    color = "white"
    times = "3"

    return render_template("index.html", times=int(times), box_color=color)


@app.route('/play/<times>/')
def times(times):
    color = "white"

    return render_template("index.html", times=int(times), box_color=color)


@app.route('/play/<times>/<color>')
def color(times, color):
    if (color is None):
        color = "white"

    return render_template("index.html", times=int(times), box_color=color)


if __name__ == "__main__":
    app.run(debug=True)
