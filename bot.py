import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

URL = "https://trouverunlogement.lescrous.fr/tools/47/search?bounds=-0.6176931_47.5262993_-0.508546_47.4373546&locationName=Angers"

EMAIL_DESTINATION = "Laurent.bryana971@gmail.com"

def verifier_logement():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    texte = soup.get_text(" ", strip=True)

    if "Jean-Zay" in texte:
        return True
    
    return False


def envoyer_mail():
    message = MIMEText(
        "🚨 Un logement est peut-être disponible à la résidence Jean-Zay à Angers.\n\nVérifie rapidement le site du CROUS."
    )

    message["Subject"] = "🚨 Logement Jean-Zay disponible"
    message["From"] = EMAIL_DESTINATION
    message["To"] = EMAIL_DESTINATION

    # Configuration à compléter ensuite
    print("Alerte envoyée :", datetime.now())


if verifier_logement():
    envoyer_mail()
else:
    print("Aucun logement détecté :", datetime.now())
