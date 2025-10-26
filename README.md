# Kantine Web App

En enkel Flask-basert webapplikasjon for en kantine som viser ukens meny og faste varer.

## Funksjonalitet

- **Hjemmeside** - Velkomstside med åpningstider
- **Ukesmeny** - Viser dagens retter for hver ukedag med bilder og priser
- **Faste varer** - Viser produkter som er tilgjengelige hver dag
- **Kontakt** - Kontaktinformasjon

## Teknisk oversikt

- **Backend**: Flask (Python)
- **Frontend**: HTML/CSS med Jinja2 templating
- **Styling**: Custom CSS med blåt og hvit design

## Prosjektstruktur

```
Kantine oppgave/
├── app.py                 # Flask applikasjon
├── templates/             # HTML maler
│   ├── base.html         # Grunnleggende oppsett
│   ├── index.html        # Hjemmeside
│   ├── menu.html         # Ukesmeny
│   ├── about.html        # Faste varer
│   └── contact.html      # Kontakt
├── static/               # Statiske filer
│   ├── css/
│   │   └── style.css     # Styling
│   ├── js/
│   │   └── script.js     # JavaScript
│   └── images/           # Bilder for retter og produkter
└── README.md
```


### Ukesmeny
- Viser 5 retter (Mandag-Fredag)
- Hver rett har et bilde, navn og pris

### Faste varer
- Produkter som er tilgjengelige hver dag
- Inkluderer brødskiver (ost, skinke), fruktbeger, kaffe og juice
- Samme oppset på faste varer som på ukesmenyen

### Design
- Jeg har gått for en clean og rent design med blå og hvit fargetema
- Kort-basert oppset for produkter og retter

## Utvikling

- Alt kjører i debug-modus, så hvis du skriver i koden vil nettsiden automatisk oppdateres når du lagrer filene

## Kilder

- Chat gpt til å generere tekst til nettsiden og hjelp hvis jeg ikke har forstått hva som er galt. Og jeg har fått den til å lage prosjekkt strukturen i README.md fordi jeg ikke viste hvordan jeg lagde de forsjellige strekene.
- Notionen til kjartan til CSS
