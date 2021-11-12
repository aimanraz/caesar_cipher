# import the logo
from art import logo
print(logo)
# list of alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text,shift_amount,cipher_direction):
  
  end_text ="" # the result cipher or decipher text
  if direction == "decode": #  direction will altenating shift foward or reverse
      shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char) # stored alphabet index position 
      new_position = position + shift_amount # foward or reversed alphabet
      end_text += alphabet[new_position] # turn index position into alphabet 
    else: # triggered when the characted not an alphabet
      end_text += char # still stored the non-alphabet character
  print(f"The {cipher_direction}d text is: {end_text}") # print type of direction and encode or decoded text

should_continue = True 
while should_continue: # program loop
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26 # used to avoid bug if the user input shift value more than 26
  caesar(start_text=text,shift_amount=shift,cipher_direction=direction)

  result = input("\nType 'yes' if you want to go again. Else type 'no'\n").lower()
  if result == 'no': 
    should_continue = False
    print("Your welcome")

