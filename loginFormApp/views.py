from django.shortcuts import render
from . import forms


# Create your views here.
def loginFormView(request):
    form = forms.LoginForm()
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print("Form is valid!")
            print("Username: ", form.cleaned_data["username"])
            print("Password: ", form.cleaned_data["password"])
    return render(request, "loginFormApp/login_form.html", {"form": form})
