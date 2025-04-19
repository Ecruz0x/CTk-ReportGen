import customtkinter as ctk
import tkinter as tk
import csv
import re



main = ctk.CTk()
main.configure(fg_color="#23272D")
main.title("Géstionnaire des dépenses")
main.geometry("1000x500")
main._set_appearance_mode("light")
photo = main.iconbitmap("src/ofppt.ico")

label = ctk.CTkLabel(master=main, text="Géstionnaire des dépenses")
label.configure(width=404, height=67, text_color="#ffffff", font=("Arial", 32))
label.place(x=20, y=0)

options = ["Gagne", "Depense"]

def top_level_win(nom_win, text):
    top_win = ctk.CTkToplevel(main)
    top_win.title(nom_win)
    top_win.geometry("500x200")
    top_win.attributes("-topmost", True)
    top_win.iconbitmap("src/ofppt.ico")
    label_top = ctk.CTkLabel(master=top_win, text=text)
    label_top.configure(width=60, height=30, text_color="#ffffff", font=("Arial", 16))
    label_top.place(x=120, y=70)
    button_top = ctk.CTkButton(master=top_win, text="Ok", command=top_win.withdraw)
    button_top.configure(width=100, height=40, text_color="#fff", border_color="#000")
    button_top.place(x=380, y=150)


def add():
    nom = entry.get()
    prix = entry1.get()
    quantite = entry2.get()
    type = option_menu.get()
    try:
        float(prix)
        int(quantite)
    except ValueError:
        top_level_win("Erreur", "Erreur : Veuillez verifiez les entrée.")
        return
    if nom == "" or float(prix) <= 0.0 or int(quantite) <= 0 or prix == '' or type not in options:
        top_level_win("Erreur", "Erreur : Veuillez verifiez vos entrées.")
        return
    prix = float(prix) * int(quantite)
    prix = str(prix) + " DH"
    quantite = str(quantite) + " Piéces"
    with open("file.csv", "r", newline="") as f:
        rows = list(csv.reader(f))
        rows.append([nom,quantite,prix,type])
    with open('file.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)
    tree.insert("", "end", values=[nom,quantite,prix,type])


def remove():
    id = tree.focus()
    details = tree.item(id)
    item = details['values']
    with open("file.csv", "r", newline="") as f:
        rows = list(csv.reader(f))
    print(rows)
    print(item)
    rows.remove(item)
    tree.delete(id)
    with open('file.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)

def opencsv(csvfile):
    with open(csvfile, "r", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        tree.delete(*tree.get_children())

        tree["columns"] = header
        for col in header:
            tree.heading(col, text=col)
            tree.column(col, width=120)

        for row in reader:
            tree.insert("", "end", values=row)


tree = tk.ttk.Treeview(main, show="headings", selectmode=ctk.BROWSE)
tree.grid(padx=490, pady=105)
selections = tree.selection()
opencsv("file.csv")

button = ctk.CTkButton(master=main, text="Ajouter", command=add)
button.configure(fg_color="#029CFF", width=100, height=40, text_color="#fff", border_color="#000")
button.place(x=30, y=410)

button1 = ctk.CTkButton(master=main, text="Supprimer", command=remove)
button1.configure(fg_color="#C42828",width=120, height=42, text_color="#fff", border_color="#000",)
button1.place(x=850, y=420)

button2 = ctk.CTkButton(master=main, text="Générer le rapport")
button2.configure(fg_color="#398E3D", width=120, height=42, text_color="#fff", border_color="#000")
button2.place(x=850, y=20)

label = ctk.CTkLabel(master=main, text="Nom du produit")
label.configure(width=60, height=30, text_color="#ffffff", font=("Arial", 12))
label.place(x=32, y=105)

label1 = ctk.CTkLabel(master=main, text="Prix du produit")
label1.configure(width=60, height=30, text_color="#ffffff", font=("Arial", 12))
label1.place(x=32, y=175)

label2 = ctk.CTkLabel(master=main, text="Quantité du produit")
label2.configure(width=60, height=30, text_color="#ffffff", font=("Arial", 12))
label2.place(x=32, y=245)

entry = ctk.CTkEntry(master=main, placeholder_text="Ex: Ordinateur")
entry.configure(fg_color="#fff", width=320, height=30, text_color="#000", border_color="#000")
entry.place(x=30, y=130)

entry1 = ctk.CTkEntry(master=main, placeholder_text="Ex: 1500.25 (Prix en MAD)")
entry1.configure(fg_color="#fff", width=320, height=30, text_color="#000", border_color="#000")
entry1.place(x=30, y=200)

entry2 = ctk.CTkEntry(master=main, placeholder_text="Quantité du produit")
entry2.configure(fg_color="#fff", width=320, height=30, text_color="#000", border_color="#000")
entry2.place(x=30, y=270)

option_menu_options = options
option_menu_var = ctk.StringVar(value="Type d'entrée")
option_menu = ctk.CTkOptionMenu(main, variable=option_menu_var, values=option_menu_options)
option_menu.configure(fg_color="#E4E2E2", text_color="#000")
option_menu.place(x=30, y=335)

main.mainloop()
