## LeakPass-Hunter
LeakPass Hunter is a project aimed at detecting sensitive data, especially passwords, that developers unintentionally log in Android applications in real-time. It continuously monitors the log output generated while the application is running; dynamic analysis and reverse engineering techniques are used to identify critical information such as passwords.

*LeakPass Hunter, Android uygulamalarında geliştiricilerin istemeden logladığı hassas verileri, özellikle parolaları, gerçek zamanlı olarak tespit etmeye yönelik bir projedir. Uygulama çalışırken oluşan log çıktıları anlık olarak izlenir; parolalar gibi kritik bilgilerin tespiti için dinamik analiz ve tersine mühendislik teknikleri kullanılır.*

# Project Objectives / Proje Amaçları
— Detect sensitive data unintentionally logged in Android applications
*Android uygulamalarında istemeden loglanan hassas verileri tespit etmek*

— Perform real-time data monitoring from Logcat, console outputs, and system log APIs

*Logcat, konsol çıktıları ve sistem log API’lerinden gerçek zamanlı veri takibi yapmak*

— Capture in-app leaks instantly using dynamic instrumentation tools like Frida

*Frida gibi dinamik enstrümantasyon araçlarıyla uygulama içi sızıntıları anlık olarak yakalamak*

— Classify password-like expressions with a Python-based analysis module

*Python tabanlı analiz modülü ile parolaya benzeyen ifadeleri sınıflandırmak*

— Help developers improve the security of their applications

*Geliştiricilerin uygulama güvenliğini artırmalarına yardımcı olmak*

