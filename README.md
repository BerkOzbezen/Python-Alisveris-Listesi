# 🛒 Python Alışveriş Listesi Yönetimi

Bu uygulama, temel Python fonksiyonları, listeler ve dosya işlemlerini (`os` modülü) kullanarak geliştirilmiş, konsol (terminal) tabanlı **kalıcı** bir alışveriş listesi yönetim programıdır.

---

## ✨ Temel Özellikler (Features)

Uygulama aşağıdaki işlemleri gerçekleştirir:

* **💾 Kalıcı Kayıt:** Uygulama kapatılırken listenin içeriğini otomatik olarak `alisveris_listem.txt` dosyasına kaydeder.
* **↩️ Kayıtlı Veri Yükleme:** Uygulama açıldığında, varsa kayıtlı listeyi dosyadan otomatik olarak yükler.
* **➕ Ekleme/Görüntüleme:** Ürünleri listeye ekleme ve **1'den başlayan numaralandırma** ile görüntüleme.
* **✏️ Öğeyi Düzenleme (Edit):** Mevcut bir ürünü **sıra numarasıyla** seçerek adını güvenli bir şekilde günceller.
* **❌ Güvenli Çıkarma (Delete):** Ürünleri **sıra numarasıyla** seçerek listeden siler ve aynı adlı ürün karmaşmasını önler.
* **🗑️ Temizleme:** Listenin tüm içeriğini tek komutla temizler.

---

## 🚀 Nasıl Başlatılır? (Getting Started)

Uygulamayı çalıştırmak için sadece Python 3'e ihtiyacınız var.

### 1. Kurulum ve Çalıştırma

1.  Projenin ana klasörüne terminalde gidin.
2.  Uygulamayı başlatmak için terminal/Komut İstemi penceresinde aşağıdaki komutu çalıştırın:
    ```bash
    python alisveris_uygulamasi.py
    ```

### 2. Kritik Not

* Program, otomatik olarak **`alisveris_listem.txt`** adında bir veri dosyası oluşturur.
* Listede yaptığınız değişikliklerin kalıcı olması için **mutlaka 6. Çıkış** seçeneğini kullanın.

---

## 💻 Kullanılan Teknolojiler

* **Dil:** Python 3.x
* **Modüller:** `os`
* **Veri Yapısı:** Python Listeleri (`list`)

---

## ⚖️ Lisans ve Telif Hakkı

Bu projenin kaynak kodu ve telif hakkı [Kendi Adınız] tarafından tutulmaktadır.

Projenin yasal kullanım, kopyalama ve dağıtım şartlarının tamamı, deponun kök dizininde bulunan **`LICENSE`** dosyasında belirtilmiştir.

---