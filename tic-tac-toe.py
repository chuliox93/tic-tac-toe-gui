import tkinter as tk
from tkinter import messagebox

# 1. Spielbrett erstellen
def erstelle_brett():
    brett = []
    for i in range(3):
        zeile = [" ", " ", " "]
        brett.append(zeile)
    return brett

# 2. Zug machen
def mache_zug(brett, spieler, zeile, spalte, button):
    if brett[zeile][spalte] == " ":
        brett[zeile][spalte] = spieler
        button.config(text=spieler)
        return True
    return False

# 3. Gewinn Überprüfen
def pruefe_gewonnen(brett, spieler):
    for zeile in range(3):
        if brett[zeile][0] == brett[zeile][1] == brett[zeile][2] == spieler:
            return True
    for spalte in range(3):
        if brett[0][spalte] == brett[1][spalte] == brett[2][spalte] == spieler:
            return True

    if (brett[0][0] == brett[1][1] == brett[2][2] == spieler) or \
       (brett[0][2] == brett[1][1] == brett[2][0] == spieler):
        return True
    return False

# 4. Prüfe ob unentschieden
def pruefe_unentschieden(brett):
    for zeile in brett:
        if " " in zeile:
            return False
    return True

# 5. Klick-Ereignis für ein Feld
def feld_geklickt(zeile, spalte, button):
    global aktueller_spieler
    if mache_zug(brett, aktueller_spieler, zeile, spalte, button):
        if pruefe_gewonnen(brett, aktueller_spieler):
            messagebox.showinfo("Spiel beendet", f"Spieler {aktueller_spieler} hat gewonnen!")
            fenster.quit()
        elif pruefe_unentschieden(brett):
            messagebox.showinfo("Spiel beendet", "Unentschieden!")
            fenster.quit()
        else:
            aktueller_spieler = "O" if aktueller_spieler == "X" else "X"

# 6. GUI erstellen
def spiele_tic_tac_toe():
    global fenster, brett, aktueller_spieler
    fenster = tk.Tk()
    fenster.title("Tic-Tac-Toe")

    brett = erstelle_brett()
    aktueller_spieler = "X"

    # Spielfeld mit Buttons erstellen
    for zeile in range(3):
        for spalte in range(3):
            button = tk.Button(fenster, text=" ", width=10, height=3, font=('Arial', 20))
            button.config(command=lambda z=zeile, s=spalte, b=button: feld_geklickt(z, s, b))
            button.grid(row=zeile, column=spalte)

    fenster.mainloop()

# Spiel starten
spiele_tic_tac_toe()
