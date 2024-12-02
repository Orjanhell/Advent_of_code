def er_stigende(nivåer):
    return all(nivåer[i] > nivåer[i-1] for i in range(1, len(nivåer)))

def er_synkende(nivåer):
    return all(nivåer[i] < nivåer[i-1] for i in range(1, len(nivåer)))

def er_sikker(nivåer):
    if len(nivåer) < 2:
        return False

    if not (er_stigende(nivåer) or er_synkende(nivåer)):
        return False

    for i in range(1, len(nivåer)):
        forskjell = abs(nivåer[i] - nivåer[i-1])
        if forskjell < 1 or forskjell > 3:
            return False

    return True

def er_sikker_med_dampener(nivåer):
    if er_sikker(nivåer):
        return True  # Rapporten er allerede sikker

    # Prøv å fjerne hver enkelt nivå og sjekk om det gjør rapporten sikker
    for i in range(len(nivåer)):
        modifisert_nivåer = nivåer[:i] + nivåer[i+1:]
        if er_sikker(modifisert_nivåer):
            return True  # Rapporten er sikker ved fjerning av nivå i
    return False  # Ingen enkelt nivå kan fjernes for å gjøre rapporten sikker

# Åpne og lese filen
with open('note.txt', 'r') as file:
    rapporter = file.readlines()

# Konvertere rapportene til lister med tall, hopp over tomme linjer
rapporter_lister = []

for rapport in rapporter:
    stripped_rapport = rapport.strip()
    if not stripped_rapport:
        continue  # Hopper over tomme linjer
    try:
        nivåer = list(map(int, stripped_rapport.split()))
        rapporter_lister.append(nivåer)
    except ValueError:
        print(f"Ugyldig rapport format: {rapport}")
        continue  # Hopper over ugyldige linjer

# Teller sikre rapporter med dampener
antall_sikre = 0

for nivåer in rapporter_lister:
    if er_sikker(nivåer) or er_sikker_med_dampener(nivåer):
        antall_sikre += 1
        print(f"Sikker rapport: {nivåer}")
    else:
        print(f"Usikker rapport: {nivåer}")

# Skriv ut resultatet
print(f"Totalt antall sikre rapporter: {antall_sikre}")
