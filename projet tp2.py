import sys
import math
from collections import Counter
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

def subdiviser():
    phrase = text_edit.toPlainText().lower()
    #phrase = phrase.replace("'", " ")

    stopwords = [
        "alors","au","aucun","aucune","aujourd’hui","aussi","autre","autres","avant","avec","avoir","bon","car","ce","cela",
        "celle","celles","celui","cependant","ces","cet","cette","ceux","chaque","chez","ci","comme","comment","d","da",
        "dans","de","depuis","des","devrait","devraient","doit","donc","du","dedans","dehors","elle","elles","en","encore",
        "enfin","entre","es","est","et","être","eu","eux","fait","faites","fois","font","hors","ici","il","ils","j","je",
        "jusqu","la","là","le","les","leur","leurs","lui","ma","maintenant","mais","me","même","mes","moi","mon","mot","ni",
        "nos","notre","nous","on","ont","ou","où","par","parce","parmi","pas","peu","peut","peuvent","plus","plusieurs",
        "plutôt","pour","pourquoi","qu","quand","que","quel","quelle","quelles","quels","qui","sa","sans","se","sera",
        "seront","ses","seulement","si","sien","sienne","siennes","siens","sous","soyez","sont","sur","ta","te","tel",
        "telle","telles","tels","tes","toi","ton","tous","tout","toute","toutes","très","trop","tu","un","une","uns",
        "unes","vers","via","vieux","vos","votre","vous","vu","y"
    ]

    exceptions = [
        "d'accord","d'antan","d'habitude","d'ailleurs",
        "d'aventure","d'emblée","d'autant","aujourd'hui"
    ]

    ponctuations = ",.;:?!"

    for p in ponctuations:
        phrase = phrase.replace(p, " ")

    mots_temp = phrase.split()
    mots = []
    for mot in mots_temp:
        if "'" in mot and mot not in exceptions:
            mot= mot.replace("'", " ")
            parties = mot.split()
            mots.extend(parties) #[p for p in parties if p != ""]
        else:
            mots.append(mot)

    mots_filtres = [mot for mot in mots if mot not in stopwords]

    return mots_filtres


def afficher_subdivision():
    mots_filtres = subdiviser()
    label.setText(f"Après subdivision : {mots_filtres}")


def nb_mots():
    mots_filtres = subdiviser()
    nb = len(mots_filtres)
    labelnb.setText(
        f"Nombre des mots après subdivision et suppression des stopwords : {nb}"
    )


def calcul_tfidf():

    texte = text_edit.toPlainText()

    if not texte:
        resultat_tfidf.setText("Aucun mot à analyser.")
        return

    # séparation des documents avec ###
    documents = texte.split("###")

    N = len(documents)

    texte_affichage = "Mot\tTF-IDF\n"
    texte_affichage += "-" * 30 + "\n"

    for doc in documents:

        mots = doc.split()

        if not mots:
            continue

        total_mots = len(mots)
        compteur = Counter(mots)

        for mot, count in compteur.items():

            # TF
            tf = count / total_mots

            # calcul nd (nombre de documents contenant le mot)
            nd = 0
            for d in documents:
                if mot in d.split():
                    nd += 1

            # IDF
            idf = math.log((1 + N) / (1 + nd)) + 1

            score = tf * idf

            texte_affichage += f"{mot}\t{round(score,5)}\n"

        texte_affichage += "\n"

    resultat_tfidf.setText(texte_affichage)
def quitter():
    fen.close()
def effacer():
    text_edit.clear()
    label.setText(f"Après subdivision :")
    labelnb.setText(f"Nombre des mots :")
    resultat_tfidf.clear()

# ================= INTERFACE =================

app = QApplication(sys.argv)

fen = QWidget()
fen.setWindowTitle("Compteur de mots avec TF-IDF")
fen.resize(900, 700)

layout = QVBoxLayout(fen)

text_edit = QTextEdit()
text_edit.setPlaceholderText("Saisissez (ou collez) votre texte ici...,écrit### pour passer à un nouveau document")
text_edit.setStyleSheet("color: #000080; font-weight: bold; font-size: 20px;")
text_edit.setFont(QFont("Segoe UI", 11))
text_edit.setMinimumHeight(300)
layout.addWidget(text_edit)

ligne_boutons = QHBoxLayout()

bouton_sub = QPushButton("Subdiviser")
bouton_sub.setStyleSheet(" QPushButton {background-color: lightgreen;} QPushButton:hover {background-color: green;}")
bouton_nb = QPushButton("Nombre des mots")
bouton_nb.setStyleSheet(" QPushButton {background-color: lightblue;} QPushButton:hover {background-color: green;}")
bouton_tfidf = QPushButton("TF-IDF")
bouton_tfidf.setStyleSheet(" QPushButton {background-color:yellow;} QPushButton:hover {background-color: green;}")
bouton_efface= QPushButton("effacer")
bouton_efface.setStyleSheet(" QPushButton {background-color: purple;} QPushButton:hover {background-color: green;}")
bouton_quit= QPushButton("Quitter")
bouton_quit.setStyleSheet(" QPushButton {background-color: red;} QPushButton:hover {background-color: green;}")
for bouton in [bouton_sub, bouton_nb, bouton_tfidf, bouton_efface, bouton_quit]:
    bouton.setFont(QFont("Segoe UI", 11, QFont.Bold))
    bouton.setCursor(Qt.PointingHandCursor)
    ligne_boutons.addWidget(bouton)
layout.addLayout(ligne_boutons)

label = QLabel(f"Après subdivision :")
label.setStyleSheet("color: deeppink; font-weight: bold; font-size: 20px;")
label.setFont(QFont("Segoe UI", 11))
layout.addWidget(label)

labelnb = QLabel(f"Nombre des mots :")
labelnb.setStyleSheet("color: deeppink; font-weight: bold; font-size: 20px;")
labelnb.setFont(QFont("Segoe UI", 11))
layout.addWidget(labelnb)

resultat_tfidf = QTextEdit()
resultat_tfidf.setReadOnly(True)
resultat_tfidf.setMinimumHeight(200)
resultat_tfidf.setStyleSheet("color: blue; font-weight: bold; font-size: 20px;")
layout.addWidget(resultat_tfidf)

# Connexions
bouton_sub.clicked.connect(afficher_subdivision)
bouton_nb.clicked.connect(nb_mots)
bouton_tfidf.clicked.connect(calcul_tfidf)
bouton_quit.clicked.connect(quitter)
bouton_efface.clicked.connect(effacer)
# On applique le layout à la fenêtre
fen.setLayout(layout)
fen.setStyleSheet("background-color: pink")
fen.show()
sys.exit(app.exec_())