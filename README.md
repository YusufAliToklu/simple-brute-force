# simple-brute-force
Bu uygulamada basi simple brute force uygular şifreleri 64 karakterli 110 faklı karakteri kullanark bütün kombinasyonları dener. Bu karakterler kod içinde değiştirilebilir RAR dosyası için yapılmıştır. her basamak için 110 karkter dener.
Bu kod, karakterler listesindeki her bir karakterin her bir pozisyonda tekrarlanmasıyla oluşturulabilecek tüm kombinasyonları deneyecek. Burada maksimum şifre uzunluğu 64 olarak belirlenmiş, bu nedenle toplam deneme sayısı:

(110 karakter) ^ 64 = 1.856938e+115

yani yaklaşık olarak 1.8 * 10 ^ 115 olacaktır. Ancak bu, "hedefli şifre"nin tüm kombinasyonlarını deneyerek bulunabileceği anlamına gelmez. Ayrıca, pyautogui kütüphanesi kullanıldığından, şifre denemeleri sırasında bilgisayarın tepkisiz kalması muhtemeldir ve bu da programın çalışmasını etkileyebilir.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

This code will try all possible combinations that can be created by repeating each character in the characters list at each position. The maximum password length is set to 64, so the total number of attempts will be:

(110 characters) ^ 64 = 1.856938e+115

which is approximately 1.8 * 10 ^ 115. However, this does not mean that the "target password" can be found by trying all combinations. Also, since the pyautogui library is used, the computer may become unresponsive during password attempts, which can affect the program's performance.
