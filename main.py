import subprocess

subprocess.run(['runas', '/user:Administrator', 'votrescript.exe'])

def create_bat(app):
    content_bat = f'Set __COMPAT_LAYER=RunAsInvoker\nStart {app}'

    with open('RunAsAdmin.bat', 'w') as fichier:
        fichier.write(content_bat)


if __name__ == "__main__":
    print("This program will launch an .exe file as admin")
    print("See instructions (readme.md) for more details")
    print("Exeample : SteamSetup.exe")
    fileName = input("File name (with extension) : ")
    create_bat(fileName)
