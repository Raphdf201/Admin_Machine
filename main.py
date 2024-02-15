def creer_fichier_bat(app):
    contenu_bat = f'Set __COMPAT_LAYER=RunAsInvoker\nStart {app}'

    with open('programme.bat', 'w') as fichier:
        fichier.write(contenu_bat)


if __name__ == "__main__":
    mot_a_inserer = input("Entrez le nom du EXE ou MSI (avec l'extension) : ")
    creer_fichier_bat(mot_a_inserer)
    print("Le fichier bat a été créé avec succès.")
