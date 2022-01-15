alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#So if this number which is going toget its position  in the alphabet and
#add the shift amount to the position toget the new position. this is already at the  end of the alphabet. So I dublicated the alphabet after last letter.
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#create a function which is done using Def and it's called encrypt
#And this function is going to take two inputs. So inside the parentheses, I am going to put two parentheses.
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#Inside the encrypt function, shift each letter of the text forwards in the alphabet by the shift amount and print
#the encrypted text.



def encrypt(plain_text, shift_amount):
    cipher_text =''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position=position+shift_amount
        new_letter =alphabet[new_position]
        cipher_text+=new_letter
    print(f'The encoded text is{cipher_text}')

encrypt(plain_text=text, shift_amount=shift)

#Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
def decrypt(cipher_text, shift_amount):
    plain_text =''# takes empty text
    for letter in cipher_text:
        position =alphabet.index(letter)
        new_position =position-shift_amount
        plain_text+=alphabet[new_position]
    print(f'The decoded text is {plain_text}')




if direction =='encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction =='decode':
    decrypt(cipher_text=text, shift_amount=shift)





