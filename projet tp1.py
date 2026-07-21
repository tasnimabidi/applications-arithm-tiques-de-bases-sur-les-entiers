import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,QHBoxLayout
def calculer():
    A=champ_A.text()
    B=champ_B.text()
    if A=="":
        label_resultat.setText("Entrer A")
        label_resultat.setStyleSheet("color: red; font-weight: bold; font-size: 20px;")

    elif B=="":
        label_resultat.setText("Entrer B")
        label_resultat.setStyleSheet("color: red; font-weight: bold; font-size: 20px;")

    elif A.isdigit() == False and B.isdigit() == False:
        label_resultat.setText("A et B doivent  etre des entiers!")
        label_resultat.setStyleSheet("color: red; font-weight: bold; font-size: 20px;")
    elif A.isdigit() == False:
        label_resultat.setText("A doit etre un entier!")
        label_resultat.setStyleSheet("color: red; font-weight: bold; font-size: 20px;")
    elif B.isdigit() == False:
        label_resultat.setText("B doit etre un entier!")
        label_resultat.setStyleSheet("color: red; font-weight: bold; font-size: 20px;")

    elif int(B) == 0:
        label_resultat.setText("Erreur, division impossible par 0")
        label_resultat.setStyleSheet("color: red; font-weight: bold; font-size: 20px;")
    elif A.isdigit()==True and B.isdigit()==True:
            label_somme.setText(f"Somme (A + B) : {int(A) + int(B)}")
            label_difference.setText(f"Différence (A - B) : {int(A) - int(B)}")
            label_produit.setText(f"Produit (A × B) : {int(A) * int(B)}")
            label_division.setText(f"Division (A ÷ B) : {int(A) / int(B)}")
def effacer():
    champ_A.clear()
    champ_B.clear()
    label_somme.setText(f"Somme (A + B) :")
    label_difference.setText(f"Différence (A - B) :")
    label_produit.setText(f"Produit (A × B) :")
    label_division.setText(f"Division (A ÷ B) :")
    label_resultat.clear()
def quitter():
    fenetre.close()
app = QApplication(sys.argv)
fenetre = QWidget()
fenetre.setWindowTitle("calculatrice des entiers")  # Titre de la fenêtre
fenetre.resize(400, 200)
label_A = QLabel("Entier A:")  # Texte statique invitant l'utilisateur d'entrer le premier entier A
label_A.setStyleSheet("color: #000080; font-weight: bold; font-size: 20px;")
champ_A = QLineEdit()
label_B = QLabel("Entier B:")  # Texte statique invitant l'utilisateur d'entre le deuxième entier B
label_B.setStyleSheet("color: #000080; font-weight: bold; font-size: 20px;")
champ_B = QLineEdit()
bouton1= QPushButton("Calculer")     # Bouton qui permet d’afficher les résultats des calculs nécessaires
bouton1.setStyleSheet(" QPushButton {background-color: lightgreen;} QPushButton:hover {background-color: green;}")
bouton2= QPushButton("Effacer")      # Bouton qui permet de supprimer les valeurs saisies et les calculs précédents
bouton2.setStyleSheet("QPushButton {background-color: pink;} QPushButton:hover {background-color: purple;}")
bouton3= QPushButton("Quitter")       # Bouton qui permet de quitter l’application
bouton3.setStyleSheet("QPushButton {background-color: red;} QPushButton:hover {background-color: #6D071A;};")
label_somme=QLabel("Somme (A+B):")
label_somme.setStyleSheet("color: #000080; font-weight: bold; font-size: 16px;")
label_difference=QLabel("Difference (A-B):")
label_difference.setStyleSheet("color: #000080; font-weight: bold; font-size: 16px;")
label_produit=QLabel("Produit (A*b):")
label_produit.setStyleSheet("color: #000080; font-weight: bold; font-size: 16px;")
label_division=QLabel("Division (A÷B):")
label_division.setStyleSheet("color: #000080; font-weight: bold; font-size: 16px;")
label_resultat = QLabel("")
bouton1.clicked.connect(calculer)
bouton2.clicked.connect(effacer)
bouton3.clicked.connect(quitter)
#layout
# Layout pour Entier A
layout_A = QHBoxLayout()
layout_A.addWidget(label_A)
layout_A.addWidget(champ_A)

# Layout pour Entier B
layout_B = QHBoxLayout()
layout_B.addWidget(label_B)
layout_B.addWidget(champ_B)

layout = QVBoxLayout()
layout.addLayout(layout_A)   # ajoute la ligne A
layout.addLayout(layout_B)   # ajoute la ligne B

boutonlayout = QHBoxLayout()
boutonlayout.addWidget(bouton1)         # 5. Bouton d'action
boutonlayout.addWidget(bouton2)         # 6. Bouton d'action
boutonlayout.addWidget(bouton3)         # 7. Bouton d'action
#ajouter les boutons à la fenetre
layout.addLayout(boutonlayout)
layout.addWidget(label_somme)
layout.addWidget(label_difference)
layout.addWidget(label_produit)
layout.addWidget(label_division)
layout.addWidget(label_resultat)
# On applique le layout à la fenêtre
fenetre.setLayout(layout)
fenetre.setStyleSheet("background-color: #CDE7F0;")
# On rend la fenêtre visible
fenetre.show()
sys.exit(app.exec_())

