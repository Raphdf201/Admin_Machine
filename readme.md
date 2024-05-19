# App executer

This little python program runs an exe like if it haves admin rights on windows.
It only works if the app asks for admin at launch. If it asks multiple times or inside the app, it doesn'T work.

Instructions : 
1. Copy the entire name of your program (with the file extension) and paste it in my software
2. Click enter, a file named programme.bat should appear in the same directory that the app
3. Make sure that your .exe or .msi file if in the same directory as programme.bat ant execute the .bat
4. It should start as if you were an admin
5. This will only work if the app asks for admin at launch (if there is the admin icon on the app)

Example of input : SteamSetup.exe

I didn't try this software on .msi files si if it doesnt works, please report it in the issues in github and attach your msi

Credits : for the exe : pyinstaller</br>
For the code : ChatGPT
