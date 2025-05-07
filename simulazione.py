# Dizionario per memorizzare i libri
libreria = {}

# Funzione per aggiungere un libro
def aggiungi_libro():
    print("Inserisci un nuovo libro:")
    nome = input("Nome: ")
    autore = input("Autore: ")
    prezzo = input("Prezzo: ")
    libreria[nome] = (autore, prezzo)  # Usa il titolo come chiave e una tupla (autore, prezzo) come valore
    print(f"Libro '{nome}' aggiunto!")

# Funzione per modificare il prezzo di un libro esistente
def cambia_prezzo():
    libro_ricerca = input("Inserisci il nome del libro a cui vuoi cambiare il prezzo: ")
    if libro_ricerca in libreria:
        nuovo_prezzo = input("Inserisci il nuovo prezzo: ")
        autore, _ = libreria[libro_ricerca]  # Estrai autore e prezzo, ma non usiamo autore
        libreria[libro_ricerca] = (autore, nuovo_prezzo)  # Aggiorna solo il prezzo
        print(f"Il prezzo del libro '{libro_ricerca}' è stato cambiato in {nuovo_prezzo}.")
    else:
        print("Libro non trovato.")

# Funzione per visualizzare tutti i libri
def stampa_libri():
    if libreria:
        print("Tutti i libri nel catalogo:")
        for nome, (autore, prezzo) in libreria.items():  # Itera attraverso i libri nel dizionario
            print(f"Nome: {nome}, Autore: {autore}, Prezzo: {prezzo}")
    else:
        print("Non ci sono libri nel catalogo.")

# Funzione per eliminare un libro
def rimuovi_libro():
    nome_ricerca = input("Inserisci il nome del libro da rimuovere: ")
    if nome_ricerca in libreria:
        del libreria[nome_ricerca]  # Rimuovi il libro dal dizionario
        print(f"Libro '{nome_ricerca}' rimosso.")
    else:
        print("Libro non trovato.")

# Funzione per calcolare lo scontrino
def calcolo_scontrino():
    while True:
        try:
            libri = int(input("Quanti libri hai acquistato? "))
            if libri <= 0:
                print("Non hai acquistato libri.")
                continue
            prezzi = []
            for i in range(libri):
                prezzo = float(input(f"Inserisci il prezzo del libro {i+1}: "))
                prezzi.append(prezzo)
            return libri, prezzi
        except ValueError:
            print("Per favore, inserisci un numero valido.")

# Funzione per calcolare lo sconto fedeltà
def sconto_fedelta():
    sconto_fedelta = float(input("Inserisci gli anni di fedeltà del cliente: "))
    if 0 <= sconto_fedelta <= 1:
        print("Sconto: 0%")
    elif 2 <= sconto_fedelta <= 3:
        print("Sconto: 5%")
    elif 4 <= sconto_fedelta <= 5:
        print("Sconto: 10%")
    else:
        print("Sconto: 15%")

# Funzione per il menu principale
def menu():
    while True:
        print("\nMenu:")
        print("1. Aggiungere un libro")
        print("2. Modificare il prezzo di un libro")
        print("3. Visualizzare tutti i libri")
        print("4. Eliminare un libro")
        print("5. Calcolare lo scontrino")
        print("6. Calcolare sconto fedeltà")
        print("7. Uscire")
        
        scelta = input("Scegli un'opzione: ")
        
        if scelta == '1':
            aggiungi_libro()
        elif scelta == '2':
            cambia_prezzo()
        elif scelta == '3':
            stampa_libri()
        elif scelta == '4':
            rimuovi_libro()
        elif scelta == '5':
            numero_libri, prezzo_libri = calcolo_scontrino()
            print(f"Hai acquistato {numero_libri} libri.")
            for i, prezzo in enumerate(prezzo_libri, start=1):
                print(f"Prodotto {i}: {prezzo} euro")
        elif scelta == '6':
            sconto_fedelta()
        elif scelta == '7':
            print("Uscita dal programma.")
            break  # Esce dal ciclo e termina il programma
        else:
            print("Opzione non valida, per favore riprova.")

# Esegui il programma
menu()
