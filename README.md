# KIRIM/TERIMA DATA DARI RAPSBERRY PI KE FIREBASE REALTIME DATABASE

## Instal Library
Instal library **Firebase-Admin** dengan cara ketik command berikut pada terminnal.
```python
pip install firebase-admin
```
[cek tautan berikut](https://pypi.org/project/firebase-admin/)

## Import Library
```python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
```
## Autentikasi dan Inialisasi
```python
cred = credentials.Certificate(" (masukan directory file JSON) ")
```
credentials untuk autentikasi dengan Firebase menggunakan file service account yang berbentuk file JSON.
Untuk mendapatkan file JSON ini adalaah sebagai berikut.

- go to console
- open **project**
- buka **Realtime Database**
- buka **Project setting**
- buka **Service accounts**
- pada Service accounts ada tab **Firebase Admin SDK**. lalu klik **Generate new private key**
- file yang terunduh adalah file JSON untuk credentials

![SS](https://imgur.com/a/cFJwyEM)

lalu untuk menginialisasi realtime database yang digunakan, masukan tautan realtime database yang digunakan.
```python
firebase_admin.initialize_app(cred, {'databaseURL': ' (masukan url) '})
```
## Referensi Data
```python
ref = db.reference('/')
```
fungsi ini berguna untuk memeberikan referesni kemana data dikirim/diambil. sesuaikan path dimana data akan disimpan. Contohnya seperti `sensor/status` maka data akan disimpan pada `status` yang berada didalam directory `sensor`.
```
senor/
└── status: 'data'
```
Atau hanya menuliskan `sensor/` dan penyimpanan data berikut nya dapat dilakukan pada syntax berikut nya.
## Kirim/Terima Data
Untuk mengirim data atau memperbarui data dari raspi ke Firebase, dapat menggunakan fungsi `update`. sedangkan untuk menerima data dari Firebase ke raspi menggunakan `get`. contoh:
```python
ref.update({'status': "terdeteksi",})
```
Maka pada Firebase Realtime Database akan terlihat sebagai berikut.
```
senor/
└── status: "terdeteksi"
```
