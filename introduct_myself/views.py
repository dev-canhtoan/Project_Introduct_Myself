from django.shortcuts import render
from .models import IntroductMyself

def introduct_myself_view(request):
    data = IntroductMyself.objects.all()  # Lấy dữ liệu từ database
    return render(request, 'introduct_myself/introduct_myself.html', {'data': data})
