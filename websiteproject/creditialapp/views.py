from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def demo(request):
    if request.method == 'POST':
         username = request.POST['username']
         first_name = request.POST['first_name']
         last_name = request.POST['last_name']
         email = request.POST['email']
         password = request.POST['password']
         cpassword = request.POST['cpassword']
         if password==cpassword:
             if User.objects.filter(username=username).exists():
                 messages.info(request, "Username Taken")
                 return redirect('register')
             elif User.objects.filter(email=email).exists():
                 messages.info(request, "Email Already Taken")
                 return redirect('register')
         else :
                user = User.objects.create_user(username=username, password=password, email=email,
                                                 first_name=first_name, last_name=last_name)
                user.save();
    else:
        messages.info(request,'password not matching')
        return  redirect('register')





    return render(request,'index.html')




