import os
import glob
from lxml import etree

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def clean_files(rules):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filepath in glob.glob(os.path.join(INPUT_DIR, "*")):
        print(f"\n[INFO] Processando file: {filepath}")
        try:
            parser = etree.XMLParser(remove_blank_text=True)
            tree = etree.parse(filepath, parser)
            root = tree.getroot()

            for tag_to_remove, search_text in rules:
                # Trova i tag ignorando eventuali namespace
                xpath_expr = f".//*[local-name()='{tag_to_remove}']"
                elems = root.xpath(xpath_expr)

                if not elems:
                    print(f"   - Nessun <{tag_to_remove}> trovato")
                    continue

                for elem in elems:
                    xml_str = etree.tostring(elem, encoding="unicode")
                    if search_text in xml_str:
                        print(f"   - Rimuovo <{tag_to_remove}> che contiene: {search_text}")
                        parent = elem.getparent()
                        if parent is not None:
                            parent.remove(elem)

            outpath = os.path.join(OUTPUT_DIR, os.path.basename(filepath))
            tree.write(outpath, encoding="utf-8", xml_declaration=True, pretty_print=True)
            print(f"[OK] File pulito salvato: {outpath}")

        except Exception as e:
            print(f"[ERRORE] Impossibile processare {filepath}: {e}")

def main():
    print("=== XML Cleaner ===")
    rules = []
    while True:
        tag = input("Inserisci il nome del tag da rimuovere (es. fieldPermissions), o ENTER per finire: ").strip()
        if not tag:
            break
        text = input("Inserisci il testo da cercare all’interno del tag: ").strip()
        rules.append((tag, text))

    if rules:
        clean_files(rules)
    else:
        print("Nessuna regola fornita. Fine.")

if __name__ == "__main__":
    main()
