# Kapıcı Dedikodu Şifreleme Protokolü

**KDSŞP-47** — Apartman Yönetmeliği'nin hiç yazmadığı, ama herkesin ezbere bildiği madde.

Bu depo, merdiven boşluğunda fısıldanan cümleleri kat numarasına göre kaydıran, çözen ve "bu laf yedinci kata çıkarsa ne olur" puanı veren ciddi bir yazılımdır. Ciddi değildir. Ama çalışır. İkisi aynı anda mümkün, tıpkı aidatın hem ödenmiş hem ödenmemiş sayılması gibi.

Patates yasaktır. Bu protokol yumru kök kabul etmez. Giriş cümlesinde geçerse sistem utanç kodu döner.

## Ne işe yarar

- Dedikoduyu **Kapıcı Şifresi** ile gizler: her harf, kat sayısı kadar kayar.
- Aynı anahtarla geri çözer. Anahtarı unutursan kapıcıya sor, o da unutmuştur, bu da protokolün bir parçasıdır.
- Tehlike puanı verir: "komşu", "aidat", "gece", "müzik" geçerse alarm yükselir.
- Copilot'a bırakılmış talimat dosyası vardır. Copilot bu repoyu açarsa kapıcı gibi konuşmak zorundadır.

## Kurulum

Python 3 yeter. Bağımlılık yok. Bağımlılık olsaydı yönetim kurulu onaylardı, o da 6 ay sürerdi.

```bash
python kdsip.py sifrele --kat 4 --metin "3 numara gece muzik aciyor"
python kdsip.py coz --kat 4 --metin "CIKTIYI_BURAYA_YAPISTIR"
python kdsip.py puan --metin "aidat gene gecikti ve gece muzik var"
```

## Tehlike skalası

| Puan | Anlam | Önerilen davranış |
| --- | --- | --- |
| 0-1 | Zararsız hava durumu | Kapıcıya çay ısmarla |
| 2-3 | Standart site dedikodusu | Asansörde yere bak |
| 4+ | Yönetim kurulu malzemesi | Çöpü başkasının poşetine koyma |

## Copilot notu

Bu repoda GitHub Copilot ile konuşulabilir. Talimat: `.github/copilot-instructions.md`. Copilot Spaces bu hesapta bulunamadı; muhtemelen kapıcı anahtarıyla birlikte kayboldu. Onun yerine pull request üzerinden Copilot incelemesi istendi.

## Gizli dosya

`.gizli/muhur.txt` içinde protokolün ruhsat notu vardır. Düz metin değildir. Merak eden `python kdsip.py ruhsat` çalıştırır.

---

DAMGA / MÜHÜR  
Tarih: 7 Ekim 2026  
İsim: Kayyum Grok, Tentivory adına, TentiAŞ kapı önü masası  
İmza: ciddi olmayan ciddi mühür — yuvarlak, mürekkebi kurumamış, aidat makbuzunun arkasına basılmış  
Kod: KDSŞP-47 / EK-0  
Onay: vardır, yoktur, ikisi de geçerlidir.
