import os
import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== BrunoOS Web Translator ===")
    print("Zadej URL stránky, kterou chceš přeložit (např. https://example.com)")
    print("Zadej 'exit' pro ukončení.\n")

    translator = Translator()

    while True:
        url = input(">> URL: ").strip()
        if url.lower() in ["exit", "quit"]:
            print("Ukončuji překladač...")
            break

        try:
            # stáhnutí stránky
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # získání textu z HTML
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text(separator="\n", strip=True)

            print("\nPřekládám... chvíli strpení...\n")
            translation = translator.translate(text, src="auto", dest="cs")

            os.system("cls" if os.name == "nt" else "clear")
            print(f"=== Překlad stránky: {url} ===\n")
            print(translation.text[:3000])  # omezíme délku výstupu, aby se to vešlo do CMD
            print("\n(Překlad zkrácen – stránka je moc dlouhá)\n")

        except Exception as e:
            print("❌ Chyba při překladu nebo načtení stránky:", e)

        input("\nStiskni Enter pro pokračování...")

if __name__ == "__main__":
    main()
