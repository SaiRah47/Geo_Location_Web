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

# def login(request):
#     return render(request, "login.html")

def dashboard(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = auth_user.sign_in_with_email_and_password(email,password)
        except:
            messages.info(request, 'Invalid Credentials')
            return render(request, "dashboard.html")
        return render(request, "dashboard.html", {
            'user': user
        })
    return render(request, "dashboard.html")


def logout(request):
    auth.logout(request)
    return redirect("dashboard")

