def calculate_scrap_percentage(defective_count, total_production):
    # İskarta yüzdesini hesaplamak için bir fonksiyon tanımlıyoruz
    scrap_percentage = (defective_count / total_production) * 100
    return scrap_percentage


def main():
    # Kullanıcıdan aylık toplam üretim miktarını alıyoruz
    total_production = int(input("Aylık toplam üretim miktarını girin: "))

    # Kullanıcıdan aylık ıskarta ürün miktarını alıyoruz
    defective_count = int(input("Aylık ıskarta ürün miktarını girin: "))

    # İskarta yüzdesini hesaplayıp ekrana yazdırıyoruz
    scrap_percentage = calculate_scrap_percentage(defective_count, total_production)
    print(f"Aylık ıskarta yüzdesi: {scrap_percentage:.2f}%")

    target_percentage = 5.0

    # İlk döngü: Aylık üretim raporu almak için
    for i in range(1, 5):  # Toplam 4 aylık rapor
        # Kullanıcıdan her ay için üretim miktarını alıyoruz
        prod = int(input(f"{i}. ay üretim miktarını girin: "))

        # Kullanıcıdan her ay için ıskarta ürün miktarını alıyoruz
        def_count = int(input(f"{i}. ay ıskarta ürün miktarını girin: "))

        # İskarta yüzdesini hesaplayıp ekrana yazdırıyoruz
        scrap_percentage = calculate_scrap_percentage(def_count, prod)
        print(f"{i}. ay ıskarta yüzdesi: {scrap_percentage:.2f}%")

        # İskarta yüzdesini hedefle karşılaştırıyoruz
        if scrap_percentage <= target_percentage:
            print(f"{i}. ay: Hedefe ulaşıldı")
        else:
            print(f"{i}. ay: Hedefe ulaşılamadı")
        print("x"*30)

    # İkinci döngü: Kullanıcıdan toplam üretim ve ıskarta miktarını almak için
    total_production = 0
    total_defective = 0
    while i <= 4:  # Toplam 4 ay
        # Kullanıcıdan toplam üretim miktarını alıyoruz
        total_production += int(input(f"{i}. ay toplam üretim miktarını girin: "))

        # Kullanıcıdan toplam ıskarta ürün miktarını alıyoruz
        total_defective += int(input(f"{i}. ay toplam ıskarta ürün miktarını girin: "))

        i += 1  # Döngü değişkenini artırıyoruz
    # Toplamda aylık ortalama ıskarta yüzdesini hesaplayalım
    average_scrap_percentage = calculate_scrap_percentage(total_defective, total_production)
    print(f"Toplamda aylık ortalama ıskarta yüzdesi: {average_scrap_percentage:.2f}%")

    # Ortalama ıskarta yüzdesini hedefle karşılaştırıyoruz
    if average_scrap_percentage <= target_percentage:
        print("Hedefe ulaşıldı: Ortalama ıskarta yüzdesi hedefin altında.")
    else:
        print("Hedefe ulaşılamadı: Ortalama ıskarta yüzdesi hedefin üstünde.")


if __name__ == "__main__":
    main()
