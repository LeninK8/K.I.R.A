from logic_engine import responder

# Entrada principal
while True:
    entrada = input("Tú: ")
    if entrada.lower() in ["salir", "exit", "adiós"]:
        print("KIRA: Apagándome... Hasta la próxima, creador.")
        break
    respuesta = responder(entrada)
    print(f"KIRA: {respuesta}")
