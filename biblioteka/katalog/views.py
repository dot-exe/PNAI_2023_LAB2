from django.shortcuts import render

# Create your views here.

from .models import Autor, Gatunek, Ksiazka, InstacjaKsiazki


def index(request):
    num_ks = Ksiazka.objects.all().count()
    num_in = InstacjaKsiazki.objects.all().count()
    num_in_d = InstacjaKsiazki.objects.filter(status__exact='d').count()
    num_au = Autor.objects.count()

    return render(
        request,
        'index.html',
        context={
            'num_ks': num_ks,
            'num_in': num_in,
            'num_in_d': num_in_d,
            'num_au': num_au
        }
    )
