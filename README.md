## LeakPass-Hunter
LeakPass Hunter is a project aimed at detecting sensitive data, especially passwords, that developers unintentionally log in Android applications in real-time. It continuously monitors the log output generated while the application is running; dynamic analysis and reverse engineering techniques are used to identify critical information such as passwords.

*LeakPass Hunter, Android uygulamalarında geliştiricilerin istemeden logladığı hassas verileri, özellikle parolaları, gerçek zamanlı olarak tespit etmeye yönelik bir projedir. Uygulama çalışırken oluşan log çıktıları anlık olarak izlenir; parolalar gibi kritik bilgilerin tespiti için dinamik analiz ve tersine mühendislik teknikleri kullanılır.*

# Project Objectives / Proje Amaçları
—Detect sensitive data unintentionally logged in Android applications

*Android uygulamalarında istemeden loglanan hassas verileri tespit etmek*

—Perform real-time data monitoring from Logcat, console outputs, and system log APIs

*Logcat, konsol çıktıları ve sistem log API’lerinden gerçek zamanlı veri takibi yapmak*

—Capture in-app leaks instantly using dynamic instrumentation tools like Frida

*Frida gibi dinamik enstrümantasyon araçlarıyla uygulama içi sızıntıları anlık olarak yakalamak*

—Classify password-like expressions with a Python-based analysis module

*Python tabanlı analiz modülü ile parolaya benzeyen ifadeleri sınıflandırmak*

—Help developers improve the security of their applications

*Geliştiricilerin uygulama güvenliğini artırmalarına yardımcı olmak*

# Features / Özellikler
—Dynamic Log Monitoring: Hooks into in-app Logcat, console outputs, and system APIs that handle sensitive data (e.g., android.util.Log.d, java.io.PrintStream.println) in real time using Frida.

*Dinamik Log Takibi: Frida kullanarak uygulama içindeki Logcat, konsol çıktıları ve hassas veriyi işleyen sistem API’lerine (örneğin android.util.Log.d, java.io.PrintStream.println) gerçek zamanlı olarak hook atar.*

—Intelligent Password Detection: Analyzes captured strings using RegEx and heuristic analysis to automatically identify password-like expressions.

*Akıllı Parola Tespiti: Yakalanan loglardaki string’leri RegEx ve sezgisel (heuristic) analiz kullanarak inceleyip, parolaya benzeyen ifadeleri otomatik olarak ayırır.*

—Detailed Reporting: Clearly reports the source, timestamp, and related log message for each detected leak.

*Detaylı Raporlama: Bulunan sızıntıların kaynağını, zamanını ve ilgili log mesajını açık ve anlaşılır şekilde raporlar.*

—Error-Focused Analysis: Helps developers identify real security issues by analyzing improper password handling in actual applications.

*Hata Odaklı İnceleme: Geliştiricilerin hatalı parola işleme durumlarını analiz ederek, gerçek uygulamalardaki güvenlik sorunlarının bulunmasını kolaylaştırır.*

# Team Members and Task Distribution / Ekip Üyeleri ve Görev Dağılımı

* 2320191087 Ebru Gündoğdu

* 2320191032 İrem Rabia Uzun 


# Roadmap / Yol Haritası
See the ROADMAP.md file to follow the journey.
 *Yolculuğu görmek için ROADMAP.md dosyasına göz atın.*

 | **Title / Başlık**                                                             | **Link**                                                                                    | **Description / Açıklama**                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Dynamic Analysis with Frida**<br>Frida ile Dinamik Analiz                    | [researchs/frida_dynamic_analysis](researchs/frida_dynamic_analysis)                          | In-depth analysis of Frida’s usage in mobile app security testing and in-app hooking mechanisms.<br>Frida'nın mobil uygulama güvenliği testlerindeki kullanımı ve uygulama içi hook mekanizmaları üzerine derinlemesine analiz. |
| **Sensitive Data Leakage Techniques**<br>Hassas Veri Sızıntı Teknikleri        | [researchs/data_leak_techniques](researchs/data_leak_techniques)                              | A study on logging errors and other common sensitive data leakage vectors.<br>Loglama hataları ve diğer yaygın hassas veri sızıntı vektörleri üzerine bir inceleme.                                                             |
| **RegEx and Heuristic Password Detection**<br>RegEx ve Heuristik Parola Tanıma | [researchs/regex_heuristic_password_detection](researchs/regex_heuristic_password_detection) | RegEx patterns and heuristic methods used to extract password-like strings from logs.<br>Parola benzeri string'leri loglardan ayıklamak için kullanılan RegEx desenleri ve heuristik yaklaşımlar.                               |

# Installation / Kurulum
To download and run the project on your computer, follow the steps below:  
*Projeyi bilgisayarınıza indirip çalıştırmak için aşağıdaki adımları izleyin*

**1. Clone the Repository / Depoyu Klonlayın**

```bash
git clone https://github.com/ebrugundogduu/LeakPass-Hunter.git
cd LeakPassHunter
```

**2. Set Up Virtual Environment / Sanal Ortam Kurulumu**
```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
```

**3. Install Dependencies / Bağımlılıkları Yükleyin**
```bash
pip install -r requirements.txt
```

# Usage / Kullanım
To run LeakPass Hunter on your project, follow the steps below:  *LeakPass Hunter'ı projeniz üzerinde çalıştırmak için aşağıdaki adımları izleyin*

**Steps/Adımlar**

1. Prepare Input Data; / *Giriş Verilerini Hazırlayın*

—LeakPass Hunter requires the target application to be installed on an Android device (real or emulator).

*LeakPass Hunter, hedef uygulamanın bir Android cihazda (gerçek veya emülatör) yüklü olmasını gerektirir*

—Ensure that the Frida Server is running on the device.

*Cihazda Frida Server'ın çalıştığından emin olun.*

2. Run the Script with Arguments: / *Betiği Argümanlarla Çalıştırın*

* --target_package [app_package_name]: Specifies the package name of the app to analyze (e.g., com.example.vulnerableapp). This argument is mandatory.

*target_package [uygulama_paket_adı]: Analiz edilecek uygulamanın paket adını belirtir (örn. com.example.vulnerableapp). Bu argüman zorunludur.*

* --output [file_name.txt]: Specifies the name of the output file where detected leaks will be saved (optional; if omitted, output is printed to the console).

*output [dosya_adı.txt]: Tespit edilen sızıntıların kaydedileceği çıktı dosyasının adını belirtir (isteğe bağlı, belirtilmezse konsola yazdırılır).*

* --duration [seconds]: Specifies how long the analysis will run (optional; default is unlimited).

*duration [saniye]: Analizin ne kadar süre çalışacağını belirtir (isteğe bağlı, varsayılan sınırsız).*

3. Check the Output: / *Çıktıyı Kontrol Edin*

—When the analysis is complete, detected passwords and related log information will be written to the specified output file (results.txt) or directly to the console.

*Analiz tamamlandığında, tespit edilen parolalar ve ilgili log bilgileri belirtilen çıktı dosyasına (results.txt) veya doğrudan konsola yazdırılacaktır.*

—Each leak record will contain detailed information about the context of the leak.

*Her sızıntı kaydı, sızıntının bağlamı hakkında detaylı bilgi içerecektir.*

# Acknowledgements / Teşekkürler

—Frida: For dynamic instrumentation capabilities.

—Python: For robust data analysis and scripting. 










