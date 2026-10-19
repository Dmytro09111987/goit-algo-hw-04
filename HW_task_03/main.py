import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def show_directory(path, level=0):
    indent = "  " * level

    for item in sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower())):
        if item.is_dir():
            print(f"{indent} {Fore.BLUE}{Style.BRIGHT}{item.name}")
            show_directory(item, level + 1)
        else:
            print(f"{indent} {Fore.GREEN}{item.name}")

def main():
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Попередження: Шлях не вказано. Скануємо поточну директорію.\n")
        target_path = Path(".")
    else:
        target_path = Path(sys.argv[1])

    if not target_path.exists() or not target_path.is_dir():
        print(f"{Fore.RED}Помилка: Вказаний шлях не існує або не є директорією!")
        return

    print(f" {Fore.CYAN}{Style.BRIGHT}{target_path.resolve().name}")

    show_directory(target_path)

if __name__ == "__main__":
    main()