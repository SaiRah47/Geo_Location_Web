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
# def login(request):
#     return render(request, "login.html")

def dashboard(request):
    context = {}
    users = []
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = auth_user.sign_in_with_email_and_password(email,password)
            # print('success')
            # print(user)
            isAdmin=db.child("users").child(user['localId']).child('isAdmin').get()
            # print('Admin:',isAdmin.val())
            if(isAdmin.val()):
                print("coming in")
                # users.append(user["idToken"])
                # users.append(user["email"])
                # users.append()
                context['user'] = user
                return render(request, "Dashboard.html", context)

        except:
            print("comming into except")
            messages.info(request, 'Invalid Credentials')
            return render(request, "Dashboard.html")
    messages.info(request, 'You are not an admin..')    
    return render(request, "Dashboard.html")


def logout(request):
    auth.logout(request)
    return redirect("dashboard")


