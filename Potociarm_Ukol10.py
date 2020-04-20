import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Word Counter - Michal Potočiar')
    parser.add_argument("nazev", help = "Napiste nazev souboru")
    parser.add_argument("--chars", help = "Vypsání znaků", action = "store_true")
    parser.add_argument("--words", help = "Vypsání slov", action = "store_true")
    parser.add_argument("--lines", help = "Vypsání řádků", action = "store_true")
    args = parser.parse_args()

    try:
    
        if args.chars and args.words and args.lines: #musí tu být, protože jinak při napsání všech třech "volitelných" by se zobrazil jiný výsledek
            file = open(args.nazev)
            text = file.read()
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text} \n\nPočet znaků v textu: [{znaky}] \nPočet slov v textu: [{slova}] \nPočet řádků v textu: [{radky}] \n")
            file.close()
        
        elif args.chars and args.words:
            file = open(args.nazev)
            text = file.read()
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text} \n\nPočet znaků v textu: [{znaky}] \nPočet slov v textu: [{slova}] \n")
            file.close()
            
        elif args.chars and args.lines:
            file = open(args.nazev)
            text = file.read()
            znaky = len(text)
            radky = len(text.split("\n"))
            print(f"\n{text} \n\nPočet znaků v textu: [{znaky}] \nPočet řádků v textu: [{radky}] \n")
            file.close()
        
        elif args.words and args.lines:
            file = open(args.nazev)
            text = file.read()
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text} \n\nPočet slov v textu: [{slova}] \nPočet řádků v textu: [{radky}] \n")
            file.close()
            
        elif args.chars:
            file = open(args.nazev)
            text = file.read()
            znaky = len(text)
            print(f"\n{text} \n\nPočet znaků v textu: [{znaky}]\n")
            file.close()
         
        elif args.words:
            file = open(args.nazev)
            text = file.read()
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\n\nPočet slov v textu: [{slova}] \n")
            file.close()
            
        elif args.lines:
            file = open(args.nazev)
            text = file.read()
            radky = len(text.split("\n"))
            print(f"\n{text}\n\nPočet řádků v textu: [{radky}] \n")
            file.close()
        
        else:
            file = open(args.nazev)
            text = file.read()
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text} \n\nPočet znaků v textu: [{znaky}] \nPočet slov v textu: [{slova}] \nPočet řádků v textu: [{radky}] \n")
            file.close()
            
    except PermissionError:
        print("Nemáte oprávnění k zadanému souboru")        
    except:
        print("Špatný název souboru nebo chybný soubor")  
     
if __name__ == "__main__":
    main()
