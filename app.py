from flask import Flask, render_template  # Flask rammeverk og hjelpefunksjon for å rendre HTML-maler

app = Flask(__name__)  # Oppretter Flask-applikasjonen

@app.route("/")  # Hjemmeside
def index():
    # Viser forsiden (arver oppsett fra base.html)
    return render_template("index.html")

@app.route('/about')  # Faste varer
def om():
    # Statisk side med faste varer og priser
    omen = [
        { "produkt": "Brødskive med ost", "pris": "25 kr", "bilde": "/static/images/ost.webp", "beskrivelse": "Fersk brødskive med ost"},
        { "produkt": "Brødskive med skinke", "pris": "25 kr", "bilde": "/static/images/skinke.jpg", "beskrivelse": "Fersk brødskive med skinke"},
        { "produkt": "Fruktbeger", "pris": "20 kr", "bilde": "/static/images/fruktbeger.jpg", "beskrivelse": "Blandet frukt i et beger"},
        { "produkt": "Kaffe", "pris": "15 kr", "bilde": "/static/images/kaffe.webp", "beskrivelse": "Fersk brygget kaffe"},
        { "produkt": "Juice", "pris": "20 kr", "bilde": "/static/images/juice.webp", "beskrivelse": "Fruktjuice i forskjellige smaker"},
    ]
    return render_template("about.html", omen=omen)

@app.route('/base')  # Base-layout (brukes som mal av andre sider)
def hoved():
    return render_template("base.html")

@app.route('/contact')  # Kontaktinformasjon
def kontakt():
    # Viser kontaktinfo og adresse
    return render_template("contact.html")

@app.route('/meny')  # Ukens meny
def ukesmeny():
    # Data som sendes inn i Jinja2-malen menu.html
    weekly_menu = [
        {"dag": "Mandag", "rett": "Kyllingsalat", "pris": "49 kr", "bilde": "/static/images/kylling.jpg", "beskrivelse": "Frisk salat med kyllingkjøtt og grønnsaker"},
        {"dag": "Tirsdag", "rett": "Pasta Bolognese", "pris": "59 kr", "bilde": "/static/images/pasta.gif", "beskrivelse": "Klassisk italiensk pasta med kjøttsaus"},
        {"dag": "Onsdag", "rett": "Vegetar wok", "pris": "45 kr", "bilde": "/static/images/wok.avif", "beskrivelse": "Woket grønnsaker med asiatisk smak"},
        {"dag": "Torsdag", "rett": "Fiskeboller i hvit saus", "pris": "65 kr", "bilde": "/static/images/fiskeboller.jpeg", "beskrivelse": "Tradisjonelle norske fiskeboller"},
        {"dag": "Fredag", "rett": "Taco buffet", "pris": "79 kr", "bilde": "/static/images/taco.jpeg", "beskrivelse": "Mexicansk inspirert taco med diverse pålegg"},
    ]
    return render_template("menu.html", weekly_menu=weekly_menu)

if __name__ == "__main__":  # Starter utviklingsserver
    app.run(debug=True)

