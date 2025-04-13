# PurgeFile
explore a recursive folder, move copy and organise by A-Z

objectif du script

- creer un dossier purge s'il n'existe pas
- deplacer les fichier (j) (japan) (ja) (jp) (BR) vers le dossier purge
- si europe + usa (ou fr) existe ne garder que le fr/europe.
- organiser les fichier de 0,A -Z (0 pour tous ce qui n'est pas une lettres)
- si dans un dossier il existe avec zip et rom melangé, conserver les zip en cas de doublon
- ignore les fichier png
- parcourt le nombre de fichier total pour la barre de progression
- utilise colorama dans /config/color.py
- n'affiche que le total de reussite ou d'echec, les details seront dans les logs
- au deplacement, la structure des dossier est preserver dans purge
