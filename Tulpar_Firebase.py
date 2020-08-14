import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Tulpar_Firebase():
    def __init__(self):
        self.connect_firebase()


    def connect_firebase(self):
        try:
            cred = credentials.Certificate("tulpar-219819-firebase-adminsdk-80jc8-230d931c25.json")
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://tulpar-219819.firebaseio.com/'
            })

            #self.update_data()

            print("Firebase was connected")
            #self.save_data()
        except:
            print("Firebase connection error")


    def save_english_data(self, english, turkish):
        ref = db.reference('/')

        ref.child('LIFE/ENGLISH').update({
            english: turkish
        })


    def update_data(self):
        """
        ref = db.reference('boxes')
        box_ref = ref.child('box001')
        box_ref.update({
            'color': 'blue'
        })
        """

        ref = db.reference('boxes')
        ref.update({
            'box001/color': 'white',
            'box002/color': 'blue'
        })