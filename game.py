import random

def play():
    print("=== Selamat datang di Game Tebak Angka! ===")
    print("Pilih tingkat kesulitan:")
    print("1. Mudah (1-20)")
    print("2. Sedang (1-50)")
    print("3. Sulit (1-100)")

    while True:
        choice = input("Masukkan pilihan (1/2/3): ")
        if choice == "1":
            min_v, max_v, lives = 1, 20, 10
            break
        elif choice == "2":
            min_v, max_v, lives = 1, 50, 7
            break
        elif choice == "3":
            min_v, max_v, lives = 1, 100, 5
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

    secret = random.randint(min_v, max_v)
    attempts = 0

    print(f"\nTebak angka antara {min_v} sampai {max_v}. Kamu punya {lives} nyawa!")

    while lives > 0:
        try:
            guess = int(input("Masukkan tebakan: "))
        except ValueError:
            print("Input bukan angka, coba lagi.")
            continue

        attempts += 1

        if guess < secret:
            print("Terlalu kecil!")
            if secret - guess > (max_v - min_v) // 3:
                print("➡️ Kamu terlalu jauh dari jawabannya!")
        elif guess > secret:
            print("Terlalu besar!")
            if guess - secret > (max_v - min_v) // 3:
                print("⬅️ Kamu terlalu jauh dari jawabannya!")
        else:
            print(f"🎉 Benar! Angkanya {secret}. Kamu menebak dalam {attempts} percobaan.")
            score = (lives * 10) + (100 - attempts * 5)
            print(f"Skor kamu: {max(score, 0)}")
            break

        lives -= 1
        print(f"Nyawa tersisa: {lives}\n")

        if lives == 0:
            print(f"💀 Kamu kehabisan nyawa! Angka yang benar adalah {secret}.")

    again = input("Mau main lagi? (y/n): ").lower()
    if again == "y":
        print("\n" + "="*40 + "\n")
        play()
    else:
        print("Terima kasih sudah bermain! 👋")

if __name__ == "__main__":
    play()
