# Tulis ke file
with open("catatan.txt", "w") as f:
    f.write("Ini adalah catatan saya!\n")
    f.write("Baris kedua.")

# Baca dari file
with open("catatan.txt", "r") as f:
    isi = f.read()
    print(isi)