
from PIL import Image
import os

lenn = 0
def encode_image(img, msg):
   
    length = len(msg)
    global lenn
    lenn = length
    
    encoded = img.copy()
    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
           
            if index < length:
                c = msg[index]
                asc = ord(c)
            else:
                asc = r
            encoded.putpixel((col, row), (asc, g , b))
            index += 1
    return encoded
def decode_image(img):
    
    global lenn
    length = lenn
    width, height = img.size
    msg = ""
    index = 0
    for row in range(height):
        for col in range(width):
            try:
                r, g, b = img.getpixel((col, row))
            except ValueError:
                r, g, b, a = img.getpixel((col, row))		
            
            if index < length:
                msg += chr(r)
            index += 1

    return msg

def caesar_encryption(n, plaintext):
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

def caesar_decryption(n, ciphertext):
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    decode = open("decode.txt","w")
    decode.write(result)
    decode.close()


key = 'abcdefghijklmnopqrstuvwxyz'
original_image_file = "Art.png"
img = Image.open(original_image_file)
print img
en_image = "enc_" + original_image_file

encrypt = open("encrypt.txt","r")
plaintext = encrypt.read()

secret_msg = caesar_encryption(5,plaintext)
"""
print 'press 1 for Caesar cipher\npress 2 for Playfair'
option = input("")"""
#if option==1:
 #   print 'Caesar Cipher'
  #  secret_msg = caesar_encryption(5,plaintext)
#elif option==2:
 #   print 'Playfair'
  #  secret_msg = playfair.play_encrypt(plaintext)


img_encoded = encode_image(img, secret_msg)



if img_encoded:
    img_encoded.save(en_image)
    print("{} saved!".format(en_image))
    os.startfile(en_image)
    img2 = Image.open(en_image)
    hidden_text = decode_image(img2)
    print("Hidden text:\n{}".format(hidden_text))
    caesar_decryption(5,hidden_text)
    """if option==1:
        caesar_decryption(5,hidden_text)
    else:
        playfair.play_decrypt(hidden_text)"""
