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

@app.route('/meny')
def ukesmeny():
    weekly_menu = [
        {"dag": "Mandag", "rett": "Kyllingsalat", "pris": "49 kr", "bilde": "/static/images/IMG_9941.jpg"},
        {"dag": "Tirsdag", "rett": "Pasta Bolognese", "pris": "59 kr", "bilde": "/static/images/rask-pasta-bolognese-1200-720.gif"},
        {"dag": "Onsdag", "rett": "Vegetar wok", "pris": "45 kr", "bilde": "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?q=80&w=1200&auto=format&fit=crop"},
        {"dag": "Torsdag", "rett": "Fiskeboller i hvit saus", "pris": "65 kr", "bilde": "/static/images/hjemmelagde-fiskeboller.jpeg"},
        {"dag": "Fredag", "rett": "Taco buffet", "pris": "79 kr", "bilde": "/static/images/assets.brandplatform.generalmills.com---media-project-gmi-oldelpaso-oldelpaso-us-recipes-qtcu578og0gukdk_kb_rmg_gmi_hi_res_jpeg.jpeg%3F.jpeg"},
    ]
    return render_template("menu.html", weekly_menu=weekly_menu)

if __name__ == "__main__":
    app.run(debug=True)

