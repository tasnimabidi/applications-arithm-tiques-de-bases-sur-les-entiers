import sys, collections, csv, json,os
from docx import Document
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QTextEdit

def lire_fichier_txt(chemin):
    with open(chemin, 'r', encoding='utf-8') as f:
        return f.readlines()

def ecrire_fichier_txt(chemin, contenu):
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write(contenu)

def lire_csv(chemin):
    with open(chemin, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def ecrire_csv(chemin, donnees, champs):
    with open(chemin, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=champs)
        writer.writeheader()
        writer.writerows(donnees)

def lire_json(chemin):
    with open(chemin, 'r', encoding='utf-8') as f:
        return json.load(f)

def ecrire_json(chemin, donnees):
    with open(chemin, 'w', encoding='utf-8') as f:
        json.dump(donnees, f, indent=4)

def lire_docx(chemin):
    doc = Document(chemin)
    return [p.text for p in doc.paragraphs]

def fichier_existe(chemin):
    return os.path.exists(chemin)



# 1. Lire et afficher un fichier
def lire_afficher():
    chemin, _ = QFileDialog.getOpenFileName(window, "Ouvrir fichier", "", "Tous les fichiers (*.txt *.csv *.json *.docx)")
    if chemin:
        if chemin.endswith(".txt"):
            contenu = "".join(lire_fichier_txt(chemin))
        elif chemin.endswith(".csv"):
            contenu = "\n".join(str(l) for l in lire_csv(chemin))
        elif chemin.endswith(".json"):
            contenu = json.dumps(lire_json(chemin), indent=4, ensure_ascii=False)
        elif chemin.endswith(".docx"):
            contenu = "\n".join(lire_docx(chemin))
        else:
            contenu = "Format non supporté"
        zone_texte.setText(contenu)

# 2. Statistiques fichier texte
def stats_txt():
    chemin, _ = QFileDialog.getOpenFileName(window, "Choisir fichier texte", "", "Fichiers texte (*.txt)")
    if chemin:
        contenu = lire_fichier_txt(chemin)
        nb_lignes = len(contenu)
        mots = " ".join(contenu).split()
        nb_mots = len(mots)
        nb_caracteres = len("".join(contenu))
        ligne_longue = max(contenu, key=len).strip()
        compteur = collections.Counter([m.lower() for m in mots]).most_common(5)
        stats = f"Lignes: {nb_lignes}\nMots: {nb_mots}\nCaractères: {nb_caracteres}\nLigne la plus longue: {ligne_longue}\nMots fréquents: {compteur}"
        zone_texte.setText(stats)

# 3a. TXT → JSON
def convertir_txt_json():
    chemin, _ = QFileDialog.getOpenFileName(window, "Choisir fichier TXT", "", "Fichiers texte (*.txt)")
    if chemin:
        lignes = lire_fichier_txt(chemin)
        data = {}
        for ligne in lignes:
            if ":" in ligne:
                cle, valeur = ligne.strip().split(":", 1)
                data[cle] = valeur
        ecrire_json("resultat.json", data)
        zone_texte.setText("Conversion TXT → JSON réussie (resultat.json)")

# 3b. CSV → JSON
def convertir_csv_json():
    chemin, _ = QFileDialog.getOpenFileName(window, "Choisir fichier CSV", "", "Fichiers CSV (*.csv)")
    if chemin:
        data = lire_csv(chemin)
        ecrire_json("resultat.json", data)
        zone_texte.setText("Conversion CSV → JSON réussie (resultat.json)")

# 3c. JSON → CSV
def convertir_json_csv():
    chemin, _ = QFileDialog.getOpenFileName(window, "Choisir fichier JSON", "", "Fichiers JSON (*.json)")
    if chemin:
        data = lire_json(chemin)
        champs = list(data[0].keys())
        ecrire_csv("resultat.csv", data, champs)
        zone_texte.setText("Conversion JSON → CSV réussie (resultat.csv)")

# 3d. DOCX → TXT
def convertir_docx_txt():
    chemin, _ = QFileDialog.getOpenFileName(window, "Choisir fichier DOCX", "", "Fichiers Word (*.docx)")
    if chemin:
        contenu = "\n".join(lire_docx(chemin))
        ecrire_fichier_txt("resultat.txt", contenu)
        zone_texte.setText("Conversion DOCX → TXT réussie (resultat.txt)")

# 4. Modifier CSV (ajout/suppression simple)
def modifier_csv():
    chemin, _ = QFileDialog.getOpenFileName(window, "Choisir fichier CSV", "", "Fichiers CSV (*.csv)")
    if chemin:
        data = lire_csv(chemin)
        # Exemple simple : on ajoute une ligne
        nouvelle_ligne = {"nom": "Test", "prenom": "Ajout", "age": "99", "ville": "TestVille"}
        data.append(nouvelle_ligne)
        champs = list(data[0].keys())
        ecrire_csv("resultat_modifie.csv", data, champs)
        zone_texte.setText("Modification CSV réussie (ajout d'une ligne → resultat_modifie.csv)")

# Interface
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("=== Application de Gestion de Fichiers ===")
window.setGeometry(100, 100, 600, 500)

layout = QVBoxLayout()
zone_texte = QTextEdit()

btn1 = QPushButton("1. Lire et afficher un fichier")
btn1.clicked.connect(lire_afficher)

btn2 = QPushButton("2. Afficher statistiques fichier texte")
btn2.clicked.connect(stats_txt)

btn3a = QPushButton("3a. Convertir TXT → JSON")
btn3a.clicked.connect(convertir_txt_json)

btn3b = QPushButton("3b. Convertir CSV → JSON")
btn3b.clicked.connect(convertir_csv_json)

btn3c = QPushButton("3c. Convertir JSON → CSV")
btn3c.clicked.connect(convertir_json_csv)

btn3d = QPushButton("3d. Convertir DOCX → TXT")
btn3d.clicked.connect(convertir_docx_txt)

btn4 = QPushButton("4. Modifier un fichier CSV")
btn4.clicked.connect(modifier_csv)

for b in [btn1, btn2, btn3a, btn3b, btn3c, btn3d, btn4, zone_texte]:
    layout.addWidget(b)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
