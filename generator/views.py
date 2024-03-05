from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html',{'password':'fhgkhwrf'})#html document mein agar password ko call kiya toh 'fghkwrf' display hoga

def password(request):

    thepassword = ''
    
    characters = list('abcdefghijklmnopqrstuvwxyz')# these alphabets are stored as single characters in the characters list

    if request.GET.get('UpperCase'): # if you want uppercase then include them in the characters list
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('Numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('specialCharacters'):
        characters.extend(list('!@#$%^&*()'))

    # int(request.GET.get('length')) isliye kiya kyunki jo bhi aata wo string hoti aur humein integer chahiye tha
    length = int(request.GET.get('length',6)) #jo length likha hai, wo home.html mein as name diya tha when the select was made AGAR KUCH MENTION NAHI KIYA LENGTH MEIN TOH DEFAULT VALUE WILL BE 6
    for i in range(length):

        thepassword += random.choice(characters)

    return render(request,'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')