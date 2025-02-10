import os
import time

def create_bat(app):
    content_bat = f'set __COMPAT_LAYER=RunAsInvoker \nstart {app}'


    with open('RunAsAdmin.bat', 'w') as file:
        file.write(content_bat)



if __name__ == "__main__":
    print (os.getlogin())

    print("This program will launch an .exe file as admin")
    print("See instructions (readme.md) for more details")
    print("Example : SteamSetup.exe")
    fileName = input("File name (with extension) : ")
    create_bat(fileName)

    os.system("C:\\Users\\" + os.getlogin() + "\\Admin_Machine\\RunAsAdmin.bat")
    time.sleep(10)
    os.remove("C:\\Users\\" + os.getlogin() + "\\Admin_Machine\\RunAsAdmin.bat")