# Cryptography-for-academic-purposes

> [!Note]
> This project was done as a part of a university module **Computer Security and Cryptography CM3104** in the 2023-24 academic year. It will be posted as archive material to showcase my skills.

### Background
This project aims to allow its users to encrypt and decrypt text files in __.txt__ format. For this project, Python language was used in addition to streamlit and cryptography libraries. Streamlit was used to display Python in a web application and cryptography.hazmat package was used to asymmetrically encrypt and decrypt files. Despite working on Windows and Linux machines, for this project, I will only be discussing how to set it up on Windows 10 as Linux has different syntax e.g. **dir** and **ls** to view the files in the current directory on the respective operating system.

### Setup
In order to set the program to work, you would need a few things:
* Machine with Windows and access to the console
* Internet access to install the libraries and python

1) Download: [python here](https://www.python.org/downloads/)
2) Open the console, or use: [the guide here](https://www.lifewire.com/how-to-open-command-prompt-2618089#:~:text=Select%20the%20Start%20menu%20the,Prompt%20will%20open%20within%20Terminal)
3) pip install streamlit 
4) pip install cryptography
5) Clone this repository using: [the guide here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
6) Open this repository and select a file path, press on it and replace **all** of it with **cmd** and press enter
7) in the command prompt type in **python -m streamlit run pythonApp.py** or **streamlit run pythonApp.py**

> [!Important]
> If you get (**Error: Invalid value: File does not exist: pythonApp.py**) - You are in the wrong directory. <br>
> If you get (**'streamlit' is not recognized as an internal or external command,
operable program or batch file.**) - Your machine doesn't recognise streamlit, and you need to use the first option.<br>
> If you get (**You can now view your Streamlit app in your browser...**) - Congratulations, you have launched the code successfully. **do not close the console!**

### How does it work?
After you manage to install and launch the code you will be met with this window below, you can switch between tabs: Keys, SafeCare, and Patients. In the scenario below,  you are going to be following my lead. 

<img src="https://github.com/OlegKov33/Cryptography-for-academic-purposes/blob/main/media/landing_page.jpg">

Here you can generate keys by pressing the **Generate Keys** button. In the folder "Keys" you will find 2 new files with names **public.pem** and **private.pem**, I put those files in "SafeCare" folder and encrypted the files.

> [!WARNING]
> If you generate the new keys, replace the current keys in the SafeCare folder and try to decrypt the files you will get: (**ValueError: Decryption failed**) message.

In the SafeCare tab, you will see the following window:

<img src="https://github.com/OlegKov33/Cryptography-for-academic-purposes/blob/main/media/SafeCare_page.jpg">

* First signature - Use that option if the file hasn't been encrypted before, as this option __adds a digital signature__.
* Sign for SafeCare - Uses __unencrypted file__ with __digital signature__ and __Safecare's public key__  to re-create a new signature and encrypt everything.
* Sign for Client - Uses the **client's public key** and **unencrypted file** to encrypt that file that __has a digital signature__,  by re-creating a new signature and encrypting everything.
* SafeCare Decryption - Uses __encrypted__ file as well as __SafeCare private key__.

In the Clients tab, you will see the following window:

<img src="https://github.com/OlegKov33/Cryptography-for-academic-purposes/blob/main/media/Clients_page.jpg">

* Client Decryption - Uses __client's private key__ to unencrypt a file.
* Sign for SafeCare - Uses __SafeCare's public key__ to encrypt a file.
* INTENTIONAL BREAK - It is an option that adds "SafeCare" to the file and uses SafeCare's public key to encrypt a file.
<br><br>
Here are some screenshots of the program in action. The first two screenshots will show you the encryption of the "Original_File_Unencrypted.txt", and the last two will show you the verification of the files:<br>

__First two:__
<img src="https://github.com/OlegKov33/Cryptography-for-academic-purposes/blob/main/media/Encryption_Of_Original_File.jpg">

<img src="https://github.com/OlegKov33/Cryptography-for-academic-purposes/blob/main/media/Break_Of_Original_File.jpg">

__Last two:__
<img src="https://github.com/OlegKov33/Cryptography-for-academic-purposes/blob/main/media/Verifying_The_Original_File.jpg">

<img src="https://github.com/OlegKov33/Cryptography-for-academic-purposes/blob/main/media/Verifying_The_Bronek_File.jpg">

### Notes
The program can process a file with limited size, according to StackOverflow(1739913) the maximum capacity of a string is 2^63-1 bytes. There is a chance that the program may fail to encrypt/decrypt a file however, it happened once and I am unsure as to what happened as the text in the file was pasted from the discord app. If you try and encrypt a file that doesn't have a signature, what will end up happening is: 

1) The program will throw an error
2) The program will replace the last 64 characters with a digital signature.

The version of Python that was used to construct it was: Python 3.10.10 <br>
The version of Streamlit that was used was: 24.0 <br>
The version of Cryptography that was used was: 24.0
