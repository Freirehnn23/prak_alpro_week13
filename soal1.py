def cek(tA):
    acuan = tA[0]

    for elemen in tA:
        if elemen != acuan:
            return False
    return True

tA = (90, 90, 90, 91)
print(cek(tA))
