from django.shortcuts import render , redirect
from django.contrib.auth.models import User

from accounts.models import Profile


import random
import http.client
from django.conf import settings
from django.contrib.auth import authenticate, login


def send_otp(mobile, otp):
        conn = http.client.HTTPConnection("api.msg91.com")
        headers = { 'content-type': "application/json" }
        authkey = settings.AUTH_KEY
        url = "http://control.msg91.com/api/sendotp.php?otp="+otp+"&message="+"your otp is "+otp+"&mobile="+mobile+"&authkey="+authkey+"&country=91"
        conn.request("GET", url , headers=headers)
        res = conn.getresponse()
        data = res.read()
        print(data)
        return None

def register(request):
    if request.method == 'POST':
        email = request.data['email']
        name = request.data['name']
        mobile = request.data['mobile']

        check_user = User.objects.filter(user=user).first()
        check_profile = Profile.objects.filter(mobile=mobile).first()

        if check_user or check_profile:
            context = {'Message':'Mobile already exist', 'class':'danger'}
            return render (request, 'register.html', context)

        user = User(name=name, email = email)        
        user.save()
        otp = str(random.randint(1000, 9999))
        profile = Profile(user=user, mobile=mobile, otp = otp)
        profile.save()
        send_otp(mobile, otp)
        request.session['mobile']= mobile
        return redirect['otp']
    return render(request, 'register.html')


def otp (request):
        mobile = request.session['mobile']
        context = {mobile:mobile}
        return render (request, 'otp.html', context)

        