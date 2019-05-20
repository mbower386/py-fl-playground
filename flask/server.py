from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def play():
    return render_template("index.html", times=3)

if __name__ == "__main__":
    app.run(debug=True)
