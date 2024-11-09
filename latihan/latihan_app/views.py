from django.shortcuts import render
from django.http import HttpResponse
from latihan_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    kamus = {'insert_me': "Halo, saya Rifdah!"}
    date_kamus = {'access_record': webpages_list}
    
    # Gabungkan kedua kamus menjadi satu
    context = {**kamus, **date_kamus}
    
    return render(request, 'aplikasi/index.html', context=context)
