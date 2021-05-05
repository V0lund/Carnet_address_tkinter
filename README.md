# Carnet_address_tkinter
projet avece tkinter et sqlite3
Concevez un logiciel de gestion de carnet d’adresses avec une interface graphique (tkinter) et un support de base de
données (sqlite).
L’interface est composée d’une Listbox (à gauche), de différents Labels et Entry (à droite) et de 4 boutons :
• Le bouton Nouveau efface les champs et prépare une nouvelle entrée dans la db ;
• Le bouton Enregistrer enregistre ou met à jour l’entrée sélectionnée et ajoute éventuellement une entrée dans
la liste ;
• Le bouton Supprimer supprime une entrée dans la liste et dans la base de données ;
• Le bouton Quitter quitte l’application.
Au démarrage de l’application, elle chargera les entrées dans la Listbox. Si on sélectionne un élément de la Listbox, les
champs seront remplis.
Voici quelques conseils pour la réalisation du projet :
• Créez un nouveau projet vide et utilisez git pour suivre votre projet ;
• Divisez votre projet en deux fichiers : un fichier avec l’interface graphique et un avec les fonctions sqlite.
Essayez de garder les fonctionnalités séparées.
• Séparez votre interface graphique en plusieurs zones : la zone de définitions des fonctions, la zone de création
des widgets, la zone de configuration des widgets, et la zone de placement des widgets. Vous y gagnerez en
lisibilité.
• Je vous conseille de conserver un dictionnaire en mémoire avec les différentes entrées (du style id:user).
• Ne passez pas par un namedtuple. Utilisez un dictionnaire pour stocker les champs de chaque entrée. Ce sera
plus facile à manipuler...
• La base de données ne contient qu’une seule table
