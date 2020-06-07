from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
import pyrebase

firebaseConfig = {
    'apiKey' : "AIzaSyB0rtz2Q8ejgA63Yv0McdkDZWZ-_xyI8xs",
    'authDomain' : "geolocation-1b35f.firebaseapp.com",
    'databaseURL' : "https://geolocation-1b35f.firebaseio.com",
    'projectId' : "geolocation-1b35f",
    'storageBucket' : "geolocation-1b35f.appspot.com",
    'messagingSenderId' : "1020735781907",
    'appId' : "1:1020735781907:web:11ce2cf876fd271c6f53e6",
    'measurementId' : "G-XH3YMEGJYL"
}

#   firebase.initializeApp(firebaseConfig)
#   firebase.analytics()
firebase = pyrebase.initialize_app(firebaseConfig)
auth_user = firebase.auth()
db = firebase.database()
<<<<<<< HEAD

=======
>>>>>>> d59f936fbcce674d47233935e1360ba45658d6e0
# def login(request):
#     return render(request, "login.html")

def dashboard(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = auth_user.sign_in_with_email_and_password(email,password)
<<<<<<< HEAD
            print(auth_user.get_account_info(user['idToken']))
=======
            print('success')
            # print(user)
            isAdmin=db.child("users").child(user['localId']).child('isAdmin').get()
            print(isAdmin.val())
            
            if(isAdmin.val()):
                return render(request, "dashboard.html", {
                'user': user})
>>>>>>> d59f936fbcce674d47233935e1360ba45658d6e0
        except:
            messages.info(request, 'Invalid Credentials')
            return render(request, "dashboard.html")
    messages.info(request, 'You are not an admin..')    
    return render(request, "dashboard.html")


def logout(request):
    auth.logout(request)
    return redirect("dashboard")


