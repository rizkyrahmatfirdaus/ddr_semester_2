product = {
    "Beras": 18000,
    "Gula": 12500,
    "Telur": 35000,
    "Susu": 19000,
}

def belanja():
    print ("selamat datang, selamat berbelanja")
    print ("berikut adalah daftar barang yang tersedia")
    for barang, harga in product.items():
        print(f"{barang}: Rp{harga} per kg")

    total_belanja = 0
    while True:
        barang_dipilih = input("masukkan nama barang yang ingin anda beli(atau 'selesai' untuk selesai)")
        if barang_dipilih.lower() == 'selesai' :
            break
        if barang_dipilih not in product:
            print("maaf, barang tersebut tidak tersedia")
            continue
        jumlah = float(input(f"berapa kg {barang_dipilih} yang anda inginkan?"))
        total_belanja += product[barang_dipilih] * jumlah
    print(f"total belanja anda adalah : Rp{total_belanja}")

belanja()


