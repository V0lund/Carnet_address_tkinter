# Module
from tkinter import *
from tkinter import messagebox


# main window
canvas = Tk()
canvas.title("Carnet d'adresses")
canvas.iconbitmap("Pics/addressbook.ico")
canvas.geometry("710x150")


# Variable
nom = StringVar()
prenom = StringVar()
adress = StringVar()
telephone = StringVar()
donnes_aj = {"nom": "", "prenom": "", "adress": "", "telephone": ""}
list_nom_prenom = [""]


# Functions
def ajouter():
    """
    Methode pour le button "Ajouter".
    """
    nom = str(entry_nom.get()).capitalize()
    prenom = str(entry_prenom.get()).capitalize()
    adress = str(entry_adress.get())
    telephone = str(entry_telephone.get())
    donnes_aj.update({"nom": nom, "prenom": prenom, "adress": adress, "telephone": telephone})
    from sql_db import insert
    insert(donnes_aj)
    messagebox.showinfo("Carner d'adresses", "Nouveau contact ajouter!")
    list_nom_prenom.append(str(nom + ", " + prenom))
    entry_nom.delete(0, END)
    entry_prenom.delete(0, END)
    entry_adress.delete(0, END)
    entry_telephone.delete(0, END)


def append_to_ls_box():
    """
    Function pour ajouter au variable list_box toutes les donnees deja existent dans le db_carnet_address
    """
    from sql_db import select_all
    ls_temp = select_all()
    for i in ls_temp:
        list_nom_prenom.append(i[0] + ", " + i[1])
    list_box.delete(0, END)
    for x in list_nom_prenom:
        list_box.insert(END, x)


def select_val_lsbox(list_box):
    """
    Method to display all the recordings for a single entry in the list_box
    """
    entry_nom.delete(0, END)
    entry_prenom.delete(0, END)
    entry_adress.delete(0, END)
    entry_telephone.delete(0, END)

    value = list_box.curselection()
    index = value[0]
    full_name = list_box.get(index)
    full_name = full_name.partition(", ")
    l_name = str(full_name[0])
    f_name = str(full_name[2])

    from sql_db import select
    record = select(l_name, f_name)

    entry_nom.insert(0, l_name)
    entry_prenom.insert(0, f_name)
    entry_adress.insert(0, record[0])
    entry_telephone.insert(0, record[1])
    pass


def del_entry():
    value = list_box.curselection()
    index = value[0]
    full_name = list_box.get(index)
    full_name = full_name.partition(", ")
    l_name = str(full_name[0])
    f_name = str(full_name[2])
    from sql_db import delete
    delete(l_name, f_name)
    append_to_ls_box()
    messagebox.showinfo("Carnet d'adresses", "Contact supprimé!")


def update_entry(box_list):

    nom = str(entry_nom.get()).capitalize()
    prenom = str(entry_prenom.get()).capitalize()
    adress = str(entry_adress.get())
    telephone = str(entry_telephone.get())
    from sql_db import update_entry
    update_entry(nom, prenom, adress, telephone)
    messagebox.showinfo("Carner d'adresses", "Contact actualisé!")


# Frames
frame_left = Frame(canvas, width=64, height=118, bd=2)
frame_left.grid(row=0, column=0)
frame_right = Frame(canvas, width=224, height=118, bd=2)
frame_right.grid(row=0, column=2)
frame_bottom_righ = Frame(canvas, height=16, width=224, bd=4)
frame_bottom_righ.grid(row=1, column=2, sticky="SE")

# Labels
nom_label = Label(frame_right, text="Nom")
nom_label.grid(row=0, column=0, sticky="W")

prenom_label = Label(frame_right, text="Prenom")
prenom_label.grid(row=1, column=0, sticky="W")

adresse_label = Label(frame_right, text="Adress")
adresse_label.grid(row=2, column=0, sticky="W")

tel_label = Label(frame_right, text="Téléphone")
tel_label.grid(row=3, column=0, sticky="W")

# My list_box
list_box = Listbox(frame_left, selectmode=SINGLE, width=32, height=5, bd=2)
list_box.pack(side=LEFT)
append_to_ls_box()

# Entries
entry_nom = Entry(frame_right, width=64, bd=2)
entry_nom.grid(row=0, column=1, sticky="E")

entry_prenom = Entry(frame_right, width=64, bd=2)
entry_prenom.grid(row=1, column=1, sticky="E")

entry_adress = Entry(frame_right, width=64, bd=2)
entry_adress.grid(row=2, column=1, sticky="E")

entry_telephone = Entry(frame_right, width=64, bd=2)
entry_telephone.grid(row=3, column=1, sticky="E")

# Scrollbar
scroll_bar = Scrollbar(frame_left, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=Y)
# Link btw scrollbar and list_box
scroll_bar.config(command=list_box.yview)
list_box.config(yscrollcommand=scroll_bar.set)

# Buttons
display_button = Button(frame_bottom_righ, text="Afficher", command=lambda: select_val_lsbox(list_box))
display_button.grid(row=0, column=0, sticky="W")
add_button = Button(frame_bottom_righ, text="Ajouter", command=ajouter)
add_button.grid(row=0, column=1, sticky="W")

update_button = Button(frame_bottom_righ, text="Actualisé", command=lambda: update_entry(list_box))
update_button.grid(row=0, column=2, sticky="W")

del_button = Button(frame_bottom_righ, text="Supprimer", command=lambda: del_entry(list_box))
del_button.grid(row=0, column=3, sticky="W")

quit_button = Button(frame_bottom_righ, text="Quitter", command=exit)
quit_button.grid(row=0, column=4, sticky="W")

mainloop()

