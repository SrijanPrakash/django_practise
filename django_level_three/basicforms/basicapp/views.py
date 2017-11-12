from django.shortcuts import render
form . import forms

# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form = forms.Formname()
    return render(request,'basicapp/forms.html',{'forms':form})
