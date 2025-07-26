    palabra = input("INGRESA LA PALABRA ")

    palabra_limpia = palabra.lower()

    if palabra_limpia == palabra_limpia[::-1]:
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")

