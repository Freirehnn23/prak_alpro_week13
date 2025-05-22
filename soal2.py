data = ('FREIRE HANAN PUTRA', '71231046', 'TUBABA, LAMPUNG')

print("NIM     :", data[1])
print("NAMA    :", data[0])
print("ALAMAT  :", data[2])

nim_tuple = tuple(data[1])
print("\nNIM     :", nim_tuple)

nama_depan = tuple(data[0].split()[0])
print("NAMA DEPAN:", nama_depan[1:])

nama_terbalik = tuple(reversed(data[0].split()))
print("NAMA TERBALIK:", nama_terbalik)
