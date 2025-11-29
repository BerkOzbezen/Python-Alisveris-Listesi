import os
SHOPPING_FILE = "alisveris_listem.txt"
shopping_list = []


def load_list():  #Dosyadan listeyi yükler ve başlatır
    if os.path.exists(SHOPPING_FILE):
        with open(SHOPPING_FILE , "r" , encoding="utf-8") as f:
             # Her satırı okuyup yeni satır karakterini (\n) kaldırarak listeye ekler
            loaded_items = [line.strip() for line in f]
            shopping_list.extend(loaded_items)
        print(f"[{SHOPPING_FILE}] dosyasindan {len(loaded_items)} urun yuklendi.")
    else:
        print("Mevcut alisveris dosyasi bulunamadi, bos liste ile basliyor.")


def save_list():    #Alisveris listesini dosyaya kaydeder
    with open(SHOPPING_FILE, "w" , encoding="utf-8") as f:
        for item in shopping_list:
            f.write(item + "\n")
        print(f"\n Alisveris listesi ({len(shopping_list)} urun) [{SHOPPING_FILE}] dosyasina kaydedildi")


def edit_item():
    if not shopping_list:
        print("Listeniz bos oldugu icin duzenleme yapilamaz")
        return
    
    # Listeyi numarayla göster
    print("\n---Duzenlenicek Urunu Seciniz---")
    for index , item in enumerate(shopping_list):
        print(f"{index + 1}. {item}")
    
    try:
        secilen_index = int(input("Duzenlemek istediginiz urunun sira numarasini giriniz : ")) -1
    # Kullanıcının girdiği numaranın geçerli olup olmadığının kontrol edildiği kısım
        if 0 <= secilen_index < len(shopping_list):
            eski_isim = shopping_list[secilen_index]
            yeni_isim = input(f"'{eski_isim}' icin yeni ismi giriniz : ")

            shopping_list[secilen_index] = yeni_isim
            print(f"'{eski_isim}' artik '{yeni_isim}' olarak guncellendi.")
        else:
            print("Gecersiz sira numarasi")
    
    except ValueError:
        print("Lutfen sadece sayi giriniz")
    

def show_menu():
    print("---Alisveris Listesi---")
    print("1.Alisveris listesini goster")
    print("2.Alisveris listesine urun ekle")
    print("3.Alisveris listesinden urun cikart")
    print("4.Alisveris listesini temizle")
    print("5.Alisveris listesindeki mevcut urunu duzenle")
    print("6.Cikis")

load_list()
while True:
    show_menu()
    secim =input("Secmek istedigniz islem numarasini giriniz : ")

    if secim == "1":
        print("\n---Alisveris Listesi---\n")
        if not shopping_list:
            print("Alisveris listeniz bos \n")
        else:
            for index, item in enumerate(shopping_list):
                print(f"{index + 1}. {item}")
            print("\n")
    
    elif secim == "2":
        item = input("Alisveris listesine eklemek istediginiz esyanin ismini giriniz : ")
        shopping_list.append(item)
        print(f"{item} listeye eklendi")

    elif secim == "3":
        if not shopping_list:
            print("Alisveris listeniz bos oldugu icin urun cikartilamaz.")
            continue
        print("\n--- Cikartilacak Urunu Secin ---")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
        try:
            secilen_sira = int(input("Cikartmak istediginiz urunun sira numarasini giriniz: "))
            index_to_delete = secilen_sira - 1
            if 0 <= index_to_delete < len(shopping_list):
                item_to_delete = shopping_list[index_to_delete]
                del shopping_list[index_to_delete] # İndekse göre silme
                print(f"'{item_to_delete}' listeden cikartildi.")
            else:
                print("Gecersiz sira numarasi.")
            
        except ValueError:
            print("Lutfen sadece sayi giriniz.")
        except IndexError:
            print("Hata: Gecersiz sira numarasi.")

    elif secim == "4":
        shopping_list.clear()
        print("Alisveris listesi temizlendi")

    elif secim == "5":
        edit_item()

    elif secim == "6":
        save_list()
        print("Programdan cikiliyor gorusuruz :)")
        break

    else:
        print("Gecersiz secim , Lutfen tekrar deneyiniz : ")
        