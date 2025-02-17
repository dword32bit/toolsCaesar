import time
from rich.progress import track
from rich import print
from rich.console import Console
from ascii_magic import AsciiArt

console = Console()

def ascii_art():
    myArt = AsciiArt.from_image("caesar5.jpg")
    myArt.to_terminal(columns=50, monochrome=True)
    console.print("[Created by putr4]\n".rjust(50), style="bold red")

def menu():
    print(f"\n [[red]1[/red]] Encrypt Plain Text\n"
          " [[red]2[/red]] Decrypt Cipher Text\n"
          " [[red]3[/red]] Exit\n"
          "\n")


ascii_art()
menu()
while True:
    while True:
        try:
            choice = int((input(" Select one of the options > ")))
            if choice > 3 or choice <= 0:
                raise Exception
            break
        except ValueError:
            print(" [[red]![/red]] Valid Input !")
        except Exception:
            print(" [[red]![/red]] Choose In range 1-3")

    if choice == 1:
        plainText = str(input(" Encrypt > ")).upper()
        letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        for key in track(range(1, len(letter)), description=" [[red]+[/red]] Processing..."):
            encrypt = ''
            for symbol in plainText:
                if symbol in letter:
                    num = letter.find(symbol)
                    num += key

                    if num >= len(letter):
                        num -= len(letter)
            
                    encrypt += letter[num]
                else:
                    encrypt += symbol
            print(f" [[red]+[/red]] Key [{key}]: {encrypt}")
            time.sleep(0.2)
        print(" [[red]+[/red]] Finished !")
                  
    elif choice == 2:
        cipherText = str(input(" Decrypt > ")).upper()
        letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for key in track(range(1, len(letter)), description=" [[red]+[/red]] Processing..."):
            translated = ''
            for symbol in cipherText:
                if symbol in letter:
                    num = letter.find(symbol)
                    num -= key

                    if num < 0:
                        num += len(letter)

                    translated += letter[num]
                else:
                    translated += symbol
            print(f" [[red]+[/red]] Key [{key}]: {translated}")
            time.sleep(0.2)
        print(" [[red]+[/red]] Finished !")

    elif choice == 3:
        print(" [[red]+[/red]] Thanks For Using !!")
        break

    




    