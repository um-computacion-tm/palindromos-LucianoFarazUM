
#def palindrome(word):
 #return True
#def palindrome(word):
 #   return False


#def palindrome(word):
   # if len(word) <=1:
   #     return True
    #if word[0]== word[-1]:
     #   return palindrome (word[1:-1]) 
    #else:
     #   return False 



def palindrome(palabra):
    palabra = palabra.lower()  # Convertir la palabra a minúsculas
    palabra = ''.join(c for c in palabra if c.isalnum())  # Eliminar caracteres no alfanuméricos
    palabra_invertida = palabra[::-1]  # Invertir la palabra

    if palabra == palabra_invertida:
        return True
    else:
        return False
    




