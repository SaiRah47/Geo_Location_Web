from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import pyrebase
import json
from django.core import serializers
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
    all_users = db.child("users").get()
    users = {}
    for user in all_users.each():
        if(not(user.val()['isAdmin'])):
            users[user.key()] = user.val()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = auth_user.sign_in_with_email_and_password(email,password)
            isAdmin=db.child("users").child(user['localId']).child('isAdmin').get()    
            print(users)  
            if(isAdmin.val()):
                request.session['user'] = user
                return redirect('report')
            else:
                messages.info(request, 'You are not an admin..')    
                return render(request, "dashboard.html")
        except:
            messages.info(request, 'Invalid Credentials')
            return render(request, "dashboard.html")    
    return render(request, "dashboard.html")


def logout(request):
    auth.logout(request)
    return redirect("dashboard")


def report(request): 
    map_pickers = []
    ml=list()
    json_map_list=[]
    map_str=''
    try:
        user = request.session['user']
        print(user)
        all_users = db.child("users").get()
        users = {}
        # map_pickers_data = {}
        for user in all_users.each():
            if(not(user.val()['isAdmin'])):
                users[user.key()] = user.val()
        # print(users)
        if request.method == 'POST':
            user_select = request.POST['userSelect']
            date_pick = request.POST['date']
            li=list(date_pick.split('-'))[::-1]
            date_final='-'.join(li)
           
            map_pickers=db.child('latlong').child(user_select).child(date_final).get().val()
            
            map_user_latlng_dict=dict(map_pickers)
            print("Map Pickers:",map_user_latlng_dict)
            
            for k,v in map_user_latlng_dict.items():              
                # ml.append([v['latitude'],v['longitude'],v['time']])
                # ml.append([v['latitude'],v['longitude']])
                map_str+=str(v['latitude'])+','+str(v['longitude'])+','+str(v['time'])+';'
            # json_map_list=serializers.serialize("json",ml)           
    except KeyError:
        print("exception caused")
        return redirect("dashboard")
    return render(request, "Report.html", { 'user' : user,  'users': users, "latlng" : map_str})
    # return render(request, "Report.html", { 'user' : user,  'users': users, 'latlng': map_pickers, })
 

def profiles(request):
    try:
        user = request.session['user']
        all_users = db.child("users").get()
        users = {}
        for user in all_users.each():
            users[user.key()] = user.val()
        return render(request, "Profiles.html", { 'users': users })
    except KeyError:
        messages.info(request, "Please Login Into Your Account...")
        return redirect("dashboard")


