input_file = input("Enter a file name: ")

try:
    buka_file = open(input_file)
except:
    print("File tidak ditemukan.")
    quit()

hitung_jam = dict()
for line in buka_file:
    if line.startswith("From "):
        parts = line.split()
        waktu = parts[5]
        jam = waktu.split(':')[0]
        hitung_jam[jam] = hitung_jam.get(jam, 0) + 1

hasil = sorted(hitung_jam.items())
for jam, jumlah in hasil:
    print(jam, jumlah)
