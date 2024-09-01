#install streamlit libary
#install hazmat cryptogaphy
#run it by: python -m streamlit run pythonApp.py
#FROM CMD IN THE FILE AS THIS FILE ^^^


import hashlib
import math

import streamlit as st
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

#------------------------------------------------
# Made By Oleg Kovalchuk (2106398)
# Stuck? Use: o.kovalchuk@rgu.ac.uk to get help
#------------------------------------------------

## GENERATES KEYS ##
def generate_key_pair():
    #This method is using RSA algorithm to create a key.
    private_key = rsa.generate_private_key(public_exponent=65537,
                                        key_size=2048,
                                        backend = default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def generate_keys_and_write_in_file():
    private_key, public_key = generate_key_pair()
    
    #PRIVATE KEY#
    unencrypted_pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    #open a folder Keys, either create a file named private.pem OR overwrite exiting one.
    with open("Keys/private.pem", 'wb') as pem_out:
        pem_out.write(unencrypted_pem_private_key)
        
    #- - - - - - - - - - -
    
    #PUBLIC KEY#
    pem_public_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    #open a folder Keys, either create a file named public.pem OR overwrite exiting one.
    with open("Keys/public.pem", 'wb') as pem_out:
        pem_out.write(pem_public_key)

def gettingFile(file_name, reason):
    a = file_name.name
    #opens a file "file_name.name" that is in the same place as this document.
    if reason== "bit":
        #reads the file as byte format. Used when you are opening encrypted file.
        f = open(a, "rb")
    else:
        #reads the file as string format. Used when you are opening unencrypted file.
        f= open(a, "r")
    f = f.read()
    return f



def get_private_key(location):
    #opens a file in "Keys/(safecare OR clients)/private.pem" directory
    with open("Keys/"+location+"private.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

def get_public_key(location):
    #opens a file in "Keys/(safecare OR clients)/public.pem" directory
    with open("Keys/"+location+"public.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key

##if the file is too big, find a way to encryting it by dividing it int smallrt sections

def firstTimeSignatureSAFECARE(public_key,message):
    #This function is used by safeCare to sign a file with SAFECARE's public
    signature = hashlib.sha256(message.encode("ASCII"))
    
    newMessage = message.encode("ASCII")+(signature.hexdigest()).encode("ASCII")
    #if the file is more than 256 bytes, encode it part by part
    fullMessage = b''
    value = 190
    if len(newMessage)/value >1:
        for i in range(math.floor(len(message)/value)+1):
            #the temp message will be used by encryption algorithm to be encrypted.
            message = newMessage[i*value:value+(i*value)]
            
            encrypted_message = public_key.encrypt(
                message,
                padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
            )
            fullMessage=fullMessage+encrypted_message

    else:
    #use safecare public key here, uses sha256
        message = newMessage
        encrypted_message = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
        )
        fullMessage = encrypted_message
    return fullMessage

def regularSignatureSAFECARE(public_key,message):
    
    #take the message alone WITHOUT the signature.
    actualMessage = message[0:len(message)-64]
    signature = hashlib.sha256(actualMessage.encode("ASCII"))
    message = message[0:len(message)-64]
    
    #join the created signature and the message.
    actualMessage = message.encode("ASCII")+(signature.hexdigest()).encode("ASCII")
    message = actualMessage
    
    fullMessage = b''
    value = 190
    if len(actualMessage)/value >1:
        for i in range(math.floor(len(message)/value)+1):
            #the temp message will be used by encryption algorithm to be encrypted.
            message = actualMessage[i*value:value+(i*value)]
            
            encrypted_message = public_key.encrypt(
                message,
                padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
            )
            fullMessage=fullMessage+encrypted_message

    else:
        #use safecare public key here to encrypt the message with the signature, using sha265.
        encrypted_message = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
        )
        fullMessage = encrypted_message
    return fullMessage

def INTENSIONAL_BREAL(public_key,message):
    #This function is used by safeCare to sign a file with SAFECARE's public
    signature = hashlib.sha256(message.encode("ASCII"))
    
    newMessage = message.encode("ASCII")+b"SafeCare"+(signature.hexdigest()).encode("ASCII")
    #if the file is more than 256 bytes, encode it part by part
    fullMessage = b''
    value = 190
    if len(newMessage)/value >1:
        for i in range(math.floor(len(message)/value)+1):
            #the temp message will be used by encryption algorithm to be encrypted.
            message = newMessage[i*value:value+(i*value)]
            
            encrypted_message = public_key.encrypt(
                message,
                padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
            )
            fullMessage=fullMessage+encrypted_message

    else:
    #use safecare public key here, uses sha256
        message = newMessage
        encrypted_message = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
        )
        fullMessage = encrypted_message
    return fullMessage

def decrypt_message(private_key, message):
    
    tempMessage = message
    fullMessage = b''
    if len(message)/256>1:
        for i in range(math.floor(len(message)/256)):
            message = tempMessage[i*256:256+(i*256)]
            
            decrypted_message = private_key.decrypt(
            message,
                padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
            )
            fullMessage=fullMessage+decrypted_message
    else:
    #decrypts the file usng private key.
        decrypted_message = private_key.decrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
        )
        fullMessage = decrypted_message
    
    #takes decrypted file and mathes hashes
    originalMessage = fullMessage.decode("ASCII")
    

    #hashValue will be what we will be using to re-create a hash.
    hashValue = originalMessage[0:len(originalMessage)-64]
    hashValue = hashlib.sha256(hashValue.encode("ASCII"))
    hashValue = (hashValue.hexdigest()).encode("ASCII")
    
    if fullMessage[len(fullMessage)-64:len(fullMessage)]==hashValue:
        st.header("The signature is Valid.")
        return fullMessage
    else:
        st.header("The signature is Invalid.")
        return fullMessage


def main():
    st.title("Digital Signature Application")
tab1, tab2, tab3 = st.tabs(["Keys", "SafeCare", "Patients"])

with tab1:
    st.title("Key creation tab.")
    #Pressing the button below will create keys in the folder: Keys
    if st.button("Generate keys"):
        generate_keys_and_write_in_file()

with tab2:
    st.title("SafeCare area")
    uploaded_file = st.file_uploader("Choose a file", key=1, type=["txt"])

    #Sign the file for the first time
    if st.button("First Signature"):
        u_f = gettingFile(uploaded_file,"any")
        data = firstTimeSignatureSAFECARE(get_public_key("SafeCare//"), u_f)
        st.download_button("Download First Signature",
                            data,
                            file_name=uploaded_file.name,
                            type="primary")

    #Signs a message using SAFECARE key, which can be used ONLY by SafeCare, NOT the clients.
    if st.button("Sign for SafeCare"):
        u_f = gettingFile(uploaded_file,"any")
        data = regularSignatureSAFECARE(get_public_key("SafeCare//"), u_f)
        st.download_button("Download Sign for SafeCare",
                            data,
                            file_name=uploaded_file.name,
                            type="primary")

    #Signs a message using Patient key, this message can ONLY be seen by the patien.
    if st.button("Sign for Client"):
        u_f = gettingFile(uploaded_file,"any")
        data = regularSignatureSAFECARE(get_public_key("Clients//"), u_f)
        st.download_button("Download Sign for Client",
                            data,
                            file_name=uploaded_file.name,
                            type="primary")

    #Decrypts using SAFECARE key. Clients or safecare will send their file, and you will use this button to decrypt it.
    if st.button("SafeCare's Decryption"):
        u_f = gettingFile(uploaded_file,"bit")
        data = decrypt_message(get_private_key("SafeCare//"),u_f)
        if data != False:
            st.download_button("Download SafeCare's Decryption",
                                data,
                                file_name=uploaded_file.name,
                                type="primary")


with tab3:
    st.title("Clients area")
    uploaded_file = st.file_uploader("Choose a file", key=2, type=["txt"])
    #Decrypts using Clients key
    if st.button("Client Decrypption"):
        u_f = gettingFile(uploaded_file,"bit")
        data = decrypt_message(get_private_key("Clients//"),u_f)
        if data != False:
            st.download_button("Download Client Decrypption",
                                data,
                                file_name=uploaded_file.name,
                                type="primary")
            
            
    #Sign a message using SAFECARE public key
    if st.button("Sign to SafeCare"):
        u_f = gettingFile(uploaded_file,"any")
        data = regularSignatureSAFECARE(get_public_key("SafeCare//"), u_f)
        st.download_button("Download Sign to SafeCare",
                            data,
                            file_name=uploaded_file.name,
                            type="primary")

    if st.button("INTENTIAL BREAK"):
        u_f = gettingFile(uploaded_file,"any")
        data = INTENSIONAL_BREAL(get_public_key("SafeCare//"), u_f)
        st.download_button("WIIL BE REMOVED IN ACTUAL APP.",
                            data,
                            file_name="Broken.txt",
                            type="primary")
        
        

#------------------------------------------------
## MAIN FILE - APP ##
#------------------------------------------------





if __name__ == "__main__":
    main()