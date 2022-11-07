from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import login, logout
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Userinfo
import requests
import time


@login_required(redirect_field_name='logar')
def index(request, id):
    info = get_object_or_404(Userinfo, id=id)
    if request.method == 'POST':
        receiver = request.POST.get('score')
        print(receiver)
        saver = Userinfo.objects.update(usuario_id=1, score = receiver, ac = 0)
    return render(request, 'index.html', {'info': info})

def logar(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        check = auth.authenticate(request, username=usuario, password=senha)
        if check is not None:
            login(request,check)
            return redirect('index', id=request.user.id)
        else:
            messages.info(request, 'botou algo errado ai troxa')
            return render(request, )
    return render(request, 'login.html')

def deslogar(request):
    logout(request)
    return redirect('logar')