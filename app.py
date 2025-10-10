from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/about')
def om():
    return render_template("about.html")

@app.route('/base')
def hoved():
    return render_template("base.html")

@app.route('/contact')
def kontakt():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

