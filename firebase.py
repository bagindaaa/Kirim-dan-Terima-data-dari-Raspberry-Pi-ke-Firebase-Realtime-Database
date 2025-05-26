import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("")
firebase_admin.initialize_app(cred, {'databaseURL': ''})

# Referensi ke lokasi data di Firebase Realtime Database
ref = db.reference('/sensor')

# Kirim data
ref.update({'status': "data",})