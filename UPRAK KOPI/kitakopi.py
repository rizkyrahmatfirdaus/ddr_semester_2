product = {
    "caffe americano": 37000,
    "caramel machiato": 59000,
    "asian dolce latte": 55000,
    "caramel latte": 52000,
    "vanilla latte": 52000,
    "caffe latte": 48000,
    "cappuccino": 48000,
    "caffe mocha": 55000,
}

def belanja():
    print("Selamat datang, selamat berbelanja")
    print("Berikut adalah daftar barang yang tersedia:")
    for barang, harga in product.items():
        print(f"{barang}: Rp{harga} per cup")
    total_belanja = 0
    while True:
        barang_dipilih = input("Masukan barang yang ingin anda beli(atau 'selesai' untuk selesai)")
        if barang_dipilih.lower() == 'selesai' :
            break
        if barang_dipilih not in product:
            ("Maaf, barang tersebut tidak tersedia")
            continue
        jumlah = float(input(f"Berapa cup{barang_dipilih} yang anda inginkan?"))
        total_belanja += product[barang_dipilih] * jumlah
    print(f"total belanja anda adalah: Rp{total_belanja}")
    
    if total_belanja > 350000:
       Diskon = total_belanja * 0.15
       print("Diskon anda kali ini adalah",Diskon)
       total_belanja -= Diskon

    pajak = total_belanja * 0.1
    print("pajak dari pesanan anda kali ini adalah Rp", pajak)
    print("total yang harus dibayar adalah",total_belanja+pajak,"terima kasih telah berbelanja di toko kami")
    

belanja()