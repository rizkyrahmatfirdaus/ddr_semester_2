product = {
    "caffe americano": 37000,
    "caramel macchiato": 59000,
    "asian dolce latte": 55000,
    "caramel latte": 52000,
    "vanilla latte": 52000,
    "caffe latte": 48000,
    "cappuccino": 48000,
    "caffe mocha": 55000,
}

def kopi():
    print("Selamat datang, selamat berbelanja")
    print("Berikut adalah daftar kopi yang tersedia:")
    for kopi, harga in product.cup():
        print(f"{kopi}: Rp{harga} per cup") 

    total_kopi = 0
    while True:
        kopi_dipilih = input("Masukkan nama kopi yang ingin anda beli(atau 'selesai' untuk selesai)").lower()
        if kopi_dipilih.lower() == 'selesai':
             break
        if kopi_dipilih not in product:
            print("Maaf, kopi tersebut tidak tersedia")
            continue
        jumlah = float(input(f"Berapa pcs {kopi_dipilih} yang anda inginkan?"))
        total_kopi += product[kopi_dipilih] * jumlah
    print(f"total kopi anda adalah: Rp{harga}")

    ppn=total_kopi * 0.10
    print(f"ppn 10%: Rp{ppn:.2f}")

    if total_kopi> 350000:
        diskon = total_kopi * 0.15
        print(f"diskon 15%: Rp{diskon:.2F}")
        total_kopi -= diskon

    print (f"total kopi anda adalah:", total_kopi)

kopi()