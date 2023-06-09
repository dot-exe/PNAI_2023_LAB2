from django.shortcuts import render
from .models import Autor, Gatunek, Ksiazka, InstancjaKsiazki
from django.views import generic
# Create your views here.


def index(request):
    num_ks = Ksiazka.objects.all().count()
    num_in = InstancjaKsiazki.objects.all().count()
    num_in_d = InstancjaKsiazki.objects.filter(status__exact='d').count()
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


class AutorListView(generic.ListView):
    model = Autor
    context_object_name = 'autor_list'
    queryset = Autor.objects.all()
    template_name = 'autor_list.html'


class KsiazkaListView(generic.ListView):
    model = Ksiazka
    context_object_name = 'moja_ksiazka_list'
    queryset = Ksiazka.objects.all()
    template_name = 'ksiazka_moja_list.html'
    paginate_by = 3


class KsiazkaSzczegolView(generic.DetailView):
    model = Ksiazka
    template_name = 'ksiazka_detail.html'
