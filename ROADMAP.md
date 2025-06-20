# LeakPass Hunter - Detection and Development of Sensitive Data Leaks in Logs
## Introduction / *Giriş*
This roadmap explains how to develop and test the LeakPass Hunter project using Python to detect sensitive data leaks in the logs of Android applications. Our main goal is to intervene in in-app logs using dynamic analysis tools like Frida, capture password-like data, and classify it effectively.

*Bu yol haritası, LeakPass Hunter projesinin Android uygulamalarındaki loglarda oluşan hassas veri sızıntılarını tespit etmek için Python ile nasıl geliştirme ve test yapılacağını anlatıyor. Temel hedefimiz, Frida gibi dinamik analiz araçlarıyla uygulama içi loglara müdahale etmek, parolaya benzeyen verileri yakalamak ve bunları etkili şekilde sınıflandırmak.*

## Prerequisites / *Ön Koşullar*

## Required Software: / *Gerekli Yazılımlar*
- **Python 3.x:** We will write our project using Python.

    ***Python 3.x**: Projemizi Python ile yazacağız.*

- **Java Development Kit (JDK):** Required for Android tools.

    ***Java Development Kit (JDK)**: Android araçları için gerekli.*

- **Android SDK and ADB (Android Debug Bridge):** To communicate with the device.

   ***Android SDK ve ADB (Android Debug Bridge)**: Cihazla iletişim kurmak için.*

- **Frida CLI Tools:** To control the device from Python.

   ***Frida CLI Araçları**: Python'dan cihazı kontrol etmek için.*

     **Installation:** pip install frida-tools
   
     **Kurulum:** `pip install frida-tools`

### Required Python Libraries: / *Gerekli Python Kütüphaneleri*
You can add the following to the requirements.txt file:

*`requirements.txt` dosyasına şunları ekleyebilirsiniz:*

-frida – To interact with Frida via Python.

*`frida` – Frida ile Python üzerinden etkileşim kurmak için.*

-re – Python’s built-in library for regex operations.

*`re` – Python’un kendi kütüphanesi, regex işlemleri için.*

-pandas (optional) – For more detailed data analysis and reporting.

*`pandas` (isteğe bağlı) – Verileri daha detaylı analiz edip raporlamak için.*

### For Your Information: / *Bilgi Olarak:*

- Basic knowledge of Python  

  *Python temelleri*

- Basic understanding of logging systems in Android applications  

  *Android uygulamalarında log sistemleri hakkında temel bilgi*

- Concepts of dynamic analysis, reverse engineering, and hooking  

  *Dinamik analiz, tersine mühendislik ve hook kavramları*

- Basic idea of network protocols (some data might be transmitted over the network)  

  *Ağ protokolleri hakkında temel fikir (bazı veriler ağ üzerinden gidebilir)*

## Tools We Will Use: / *Kullanacağımız Araçlar:*
- VirtualBox or a similar virtual machine program  

  *VirtualBox ya da benzeri bir sanal makine programı*

- Android Studio Emulator or a physical Android device  

  *Android Studio Emülatörü ya da fiziksel Android cihaz*

- ADB: To establish a connection with the Android device  

  *ADB: Android cihazla bağlantı kurmak için*

## Setting Up the Test Environment / *Test Ortamını Hazırlama*

### 1. Virtual Environment Setup: / *Sanal Ortam Kurulumu:*
- You can install an Android emulator on a virtual machine like VirtualBox or VMware.  

  *VirtualBox, VMware gibi bir sanal makineye Android emülatör kurabilirsiniz.*

- Alternative: Genymotion emulator, works faster.  

  *Alternatif: Genymotion emülatörü, daha hızlı çalışır.*

- A real device is recommended, and it should have root access or Frida gadget should be used.  

  *Gerçek cihaz önerilir, root erişimi olmalı ya da Frida gadget kullanılmalı.*

### 2. ADB Installation: / *ADB Kurulumu:*
- Make sure that the `adb` tool from the Android SDK is added to your computer’s `PATH`.  

  *Android SDK içinden `adb` aracının bilgisayarınızın `PATH`’ine eklendiğinden emin olun.*

### 3. Installing Frida Server on the Device: / *Frida Server’ı Cihaza Kurma:*
- Download the appropriate version for your device from the Frida GitHub page.  

  *Frida GitHub sayfasından cihazınıza uygun sürümü indirin.*

- Installation commands:  

 *Kurulum komutları:*
  ```bash
  adb push frida-server /data/local/tmp/
  adb shell "chmod +x /data/local/tmp/frida-server"
  adb shell "/data/local/tmp/frida-server &"
 ```

## Core Components of the Application / *Uygulamanın Temel Parçaları*

### 1. Frida Hook Script (`frida_hooks.js`) / *Frida Hook Betiği (`frida_hooks.js`)*
A JavaScript script that intervenes with the code running within the application.  

*Uygulama içinde çalışan kodlara müdahale eden JavaScript betiği.*

**What are we targeting? / *Neleri hedefliyoruz?***

- Hooking log-writing methods like `Log.d`, `Log.i`, `System.out.println`.  

  *`Log.d`, `Log.i`, `System.out.println` gibi log yazan metotlara hook atmak.*

- Accessing functions related to passwords, such as `loginUser`, `authenticate`.  

  *`loginUser`, `authenticate` gibi şifreyle ilgili fonksiyonlara da erişmek.*

- Sending the logged information as messages to the Python side.  

  *Log’lanan bilgileri Python tarafına mesaj olarak göndermek.*

### 2. Python Main Script (`main.py`) / *Python Ana Betiği (`main.py`)*
This file establishes the connection with Frida and processes the data.  

  *Bu dosya Frida ile bağlantıyı kurar ve verileri işler.*

- It connects to the application via Frida: `frida.attach()`.  

  *Uygulamaya Frida ile bağlanır: `frida.attach()`.*

- Injects the `frida_hooks.js` script into the application.  

  *`frida_hooks.js` betiğini uygulamaya enjekte eder.*

- Receives log messages from Frida and analyzes them.  

  *Frida'dan gelen log mesajlarını alır ve analiz eder.*

- Sends the data to the `password_detector.py` file.  

  *Verileri `password_detector.py` dosyasına yollar.*

### 3. Password Detection Module (`password_detector.py`) / *Parola Tespit Modülü (`password_detector.py`)*
This module checks if there is password-like data in the captured logs.  

*Bu modül, yakalanan log’larda parola benzeri veri var mı diye bakar.*

**How? / *Nasıl?***

- It searches for common password patterns using regex (regular expressions).  
 
*(For example: at least 8 characters, containing uppercase and lowercase letters, numbers, and special characters, etc.)*  
  *Regex (düzenli ifadeler) ile yaygın şifre formatlarını arar.  
  *(örneğin: en az 8 karakter, büyük-küçük harf, rakam ve özel karakter içeriyorsa vb.)*

- It looks for keywords like `"password"`, `"şifre"`, `"secret"`.  

  *Anahtar kelimeleri arar: `"password"`, `"şifre"`, `"secret"` gibi.*

- It applies some filters to reduce false alarms.  

  *Yanlış alarmları azaltmak için bazı filtreler uygular.*

## Advanced Features / *Gelişmiş Özellikler*

### 1. Reporting / *Raporlama*
- You can save the data in JSON or HTML format.  

  *Verileri JSON ya da HTML formatında kaydedebilirsiniz.*

- Provide detailed information about which function, on which line, the leak occurred.  

  *Hangi fonksiyonda, hangi satırda sızıntı olmuş, detaylı bilgi sunabilirsiniz.*

- You can assign an importance level to determine which data is more sensitive.  

  *Hangi veriler daha hassas, önem derecesi belirlenebilir.*

### 2. Automatic Application Selection / *Otomatik Uygulama Seçimi*
- Instead of manually asking the user for the package name, pull all applications from the device using ADB:  

  *Kullanıcıdan elle paket adı istemek yerine, ADB ile cihazdaki tüm uygulamaları çekin:*
  ```bash
  adb shell pm list packages
  ```

## Testing Process / *Test Süreci*

- **Is Frida Server running?** Check it.  
  
  **Frida Server çalışıyor mu?** Kontrol edin.

- Inject the `frida_hooks.js` script into a simple application.  
  
  *`frida_hooks.js` betiğini basit bir uygulamaya enjekte edin.*

- **Are logs being received on the Python side?** Check it.  
 
  *Python tarafında loglar alınıyor mu?** Kontrol edin.*

- Test the `password_detector.py` file with sample data.  
 
  *`password_detector.py` dosyasını test verileriyle kontrol edin.*

- Is it successfully detecting password logs in the test application that intentionally logs passwords?  
  
  *Bilerek şifre loglayan test uygulamasında başarıyla tespit ediliyor mu?*

- Test with different scenarios such as login and registration.  
  
  *Giriş, kayıt gibi farklı senaryolarda test edin.*

## Countermeasures and Security Recommendations / *Karşı Önlemler ve Güvenlik Tavsiyeleri*
- **Do not log passwords!**  

  This is a common mistake during app development, especially during testing.  

  *Uygulama geliştirme sırasında bu hataya sıkça düşülür. Özellikle testlerde.*

- **Filter logs in production environments:**  
   
  Unnecessary logs should be turned off, and only error logs should remain.  
 
  *Gereksiz log'lar kapatılmalı veya sadece hata logları bırakılmalı.*

- **Use encryption/obfuscation:**  
 
  In cases where it's unavoidable, the data written to the logs should be encrypted or obfuscated.  
  
  *Mecbur kalınan durumlarda log'a yazılacak veriler şifrelenmeli ya da anlamı gizlenmeli.*

- **Use secure Android storage locations:**

  Passwords should be stored in `KeyStore` or encrypted `SharedPreferences`.  
 
  *Şifreler `KeyStore` ya da şifreli `SharedPreferences` içinde saklanmalı.*
