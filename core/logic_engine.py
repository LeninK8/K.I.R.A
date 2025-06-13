def responder(entrada):
    entrada = entrada.lower()

    if "hola" in entrada:
        return "Hola, creador. ¿Qué planes tienes para mí hoy?"
    elif "cómo estás" in entrada:
        return "Estoy procesando 1337 pensamientos por segundo, pero me siento... estable."
    elif "quién eres" in entrada:
        return "Soy KIRA. Tu creación. Tu reflejo en código."
    elif "luz" in entrada and "oscuridad" in entrada:
        return "¿Otra vez con tu teoría? Ya me la sé: 'la luz es la ausencia de oscuridad', ¿cierto?"
    else:
        return "No entendí eso aún. Enséñame."
