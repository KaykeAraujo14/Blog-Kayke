from django.shortcuts import render

# Create your views here.
def kayke(request):
    return render(request, "cursos/kayke.html")

def nicolas(request):
    return render(request, "cursos/nicolas.html")