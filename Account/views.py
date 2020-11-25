from django.conf import settings
from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

# Create your views here.
def login_form(request):
    username = request.POST['user_name']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        if user.is_admin:
            # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
            return render(request, "Admin")
    else:
        # Return an 'invalid login' error message
        # return redirect('%s?next=%s' % ("/", request.path))
        return render(request, "home")