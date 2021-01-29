from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
        else:
            print('password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')
















