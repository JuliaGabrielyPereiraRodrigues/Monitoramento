from django.shortcuts import render
from django.http import JsonResponse
from .models import File

def home(request):
    print("Página carregada!")  
    return render(request, 'home.html')

def get_files(request):
    print("Rota get_files acessada!")
    files = File.objects.all().values('name', 'path', 'updated_at')
    return JsonResponse(list(files), safe=False)