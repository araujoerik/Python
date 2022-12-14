# Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
# El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.

morse = {
  "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", 
  "g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", "l": ".-..", 
  "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".__.", "q": "--.-",
  "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
  "x": "-..-", "y": "-.--", "z": "--..", 
}

texto_codificado = ""

palabra = input("Ingresa una palabra o texto a codificar: ")

for c in palabra:
  if c != " " and c.lower() in morse:
    texto_codificado += morse[c.lower()]
  else:
    texto_codificado += c

print("Texto codificado: {}".format(texto_codificado))