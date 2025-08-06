Funzionamento di base:
- Avviato lo script, verrà richiesto all'utente di compilare una o più regole, queste regole verranno usate per modificare tutti i file presenti nella cartella "input". Per ogni regola verrà richiesto all'utente di compilare il nome del tag che si vuole rimuovere (ad esempio "fieldPermissions" per i permission set in Salesforce) e un testo da cercare all'interno di questi tag (seguendo l'esempio di prima, qui potresti voler fornire il nome del campo). Se il testo viene trovato all'interno del tag, allora il tag verrà rimosso dal file.


Come usare lo script:
- Inserisci all'interno della cartella "input" i tuoi file, che non per forza devono avere estensione .xml, ma che devono poter essere letti come tali. (Ad esempio i file .permissionset in Salesforce)
- Installa le dipendenze con "pip install -r requirements.txt" (oppure manualmente)
- Avvia lo script con "python xml_cleaner.py"