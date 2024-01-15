import time

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso.",
            "LOL": "Una respuesta común a algo gracioso.",
            "ROASTED": "Cortar a alguien mientras están quejándose o discutiendo sobre algo.",
            "KAREN": "Una mujer que se enfada por cualquier razón y siempre cree que tiene razón.",
            "KEVIN": "Un hombre que se enfada por cualquier razón y siempre creee que tiene razón.",
            "GIGA CHAD": "Un hombre muy saludable, musculoso y guapo."
            }
            
print("¡Hola!")
time.sleep(1)
print("Con esta aplicación puedes traducir palabras que no sepas que sean del 2024.")
time.sleep(2)

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("¡No tengo esa palabra registrada!")
