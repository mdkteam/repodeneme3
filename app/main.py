def show_menu():
    print("=" * 50)
    print(" Codex Deneme Uygulaması ".center(50, "="))
    print("1) Not ekle")
    print("2) Notları listele")
    print("3) Çık")
    print("=" * 50)


def main():
    notes = []

    while True:
        show_menu()
        choice = input("Seçim: ").strip()

        if choice == "1":
            note = input("Not metni: ").strip()
            if note:
                notes.append(note)
                print("→ Not kaydedildi.\n")
            else:
                print("Boş not kaydedilmedi.\n")

        elif choice == "2":
            if not notes:
                print("Henüz hiç not yok.\n")
            else:
                print("\n--- Notlar ---")
                for i, n in enumerate(notes, start=1):
                    print(f"{i}. {n}")
                print()

        elif choice == "3":
            print("Çıkılıyor, görüşürüz 👋")
            break

        else:
            print("Geçersiz seçim, 1 / 2 / 3 gir.\n")


if __name__ == "__main__":
    main()
