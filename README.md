# Guess-Game-
Game ini adalah permainan tebak-tebakan angka di terminal. Komputer memilih angka acak, tugas pemain cuma menebak sampai tepat. Versi ini tetap sederhana namun dilengkapi beberapa fitur kecil yang bikin permainan lebih enak dan nggak bikin frustrasi.

Cara main singkat

Jalankan skrip di terminal (python nama_file.py).

Pilih tingkat kesulitan: Mudah (1–20), Sedang (1–50), atau Sulit (1–100).

Tebak angkanya satu per satu lewat input di terminal.

Program akan memberi tahu apakah tebakanmu terlalu kecil, terlalu besar, atau benar.

Ada batas nyawa sesuai tingkat kesulitan; kalau habis, permainan selesai dan angka sebenarnya ditunjukkan.

PENJELASAN FITUR
1. Pilihan Tingkat Kesulitan

Di awal kamu diminta pilih level: Mudah, Sedang, atau Sulit.
Setiap level menentukan rentang angka dan jumlah nyawa (kesempatan) yang kamu punya. Jadi kalau mau santai, pilih Mudah; kalau mau deg-degan, pilih Sulit.

Mudah: angka 1–20, banyak kesempatan.

Sedang: angka 1–50, kesempatan moderat.

Sulit: angka 1–100, kesempatan lebih sedikit.

Intinya: pilih sesuai mood, mau latihan logika atau mau tantangan.

2. Umpan Balik Langsung (Terlalu Kecil / Terlalu Besar)

Setiap tebakan langsung dikomentari: “Terlalu kecil” atau “Terlalu besar”.
Kalimat ini membantu kamu tahu arah selanjutnya tanpa dibocorin jawabannya. Sederhana tapi efektif.

3. Petunjuk “Terlalu Jauh”

Kalau tebakanmu jauh dari angka rahasia (misal jaraknya cukup besar terhadap rentang), program akan memberi komentar tambahan seperti “Kamu terlalu jauh dari jawabannya!”.
Ini berguna supaya kamu nggak terus menebak di angka yang jelas-jelas jauh, sehingga proses tebak-tebakan terasa lebih cepat dan enggak buang waktu.

4. Sistem Nyawa (Lives)

Setiap level punya jumlah nyawa berbeda. Setiap tebakan yang salah mengurangi satu nyawa. Kalau nyawa habis, permainan berakhir dan angka rahasia ditunjukkan.
Fitur ini menambah unsur strategi: jangan asal nebak, pikir sedikit sebelum tekan enter.

5. Tampilan Hasil dan Skor Sederhana

Saat berhasil menebak, program menampilkan:

Berapa percobaan yang dipakai,

Skor sederhana yang dihitung dari sisa nyawa dan banyaknya percobaan.

Skor ini bukan leaderboard rumit cuma indikator seberapa “bagus” permainanmu di satu sesi.

6. Opsi Main Lagi

Setelah permainan usai (menang atau kalah), program menanyakan apakah mau main lagi. Kalau iya, permainan otomatis dimulai ulang dari level pemilihan. Praktis buat coba strategi baru tanpa harus jalankan skrip ulang.

Kenapa fitur ini berguna?

Biar permainan tetap ringan tapi tetep punya rasa tantangan.

Pemain dapat umpan balik yang cukup untuk memperbaiki tebakan tanpa diberi jawaban langsung.

CONTOH SINGKAT TAMPILAN DI TERMINAL

=== Selamat datang di Game Tebak Angka! ===
Pilih tingkat kesulitan:
1. Mudah (1-20)
2. Sedang (1-50)
3. Sulit (1-100)
Masukkan pilihan (1/2/3): 2

Tebak angka antara 1 sampai 50. Kamu punya 7 nyawa!
Masukkan tebakan: 25
Terlalu kecil!
Nyawa tersisa: 6

Masukkan tebakan: 40
Terlalu besar!
➡️ Kamu terlalu jauh dari jawabannya!
Nyawa tersisa: 5

... (lanjut sampai menang/kehabisan nyawa)


Cocok buat pemula yang mau latihan logika ataupun buat hiburan singkat di terminal.
