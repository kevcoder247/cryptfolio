from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
#from django.views.generic.detail import ListView
from .models import Crypto

# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, 'about.html')
'''
#Seed Data
class Crypto:
    def __init__(self, name, price, rank):
        self.name = name
        self.price = price
        self.rank = rank

cryptos =[
    Crypto('Bitcoin', '$20,000', 1),
    Crypto('Ethereum', '$1,000', 2),
    Crypto('Tether', '$1.00', 3),
    Crypto('USD', '$1.00', 4),
    Crypto('BNB', '$200.00', 5),
    Crypto('Xrp', '$0.30', 6),
    Crypto('Cardano', '$0.40', 7),
    Crypto('Dogecoin', '$0.05', 8),
    Crypto('Polkadot', '$7.00', 9),
    Crypto('Shiba Inu', '$0.000010', 10),
    ]
'''
def crypto_index(request):
    cryptos = Crypto.objects.all()
    return render(request, 'cryptos/index.html', {'cryptos' : cryptos})

def crypto_detail(request, crypto_id):
    crypto = Crypto.objects.get(id=crypto_id)
    return render(request, 'cryptos/detail.html', {'crypto': crypto})


#CUD Class Bases Views
class CryptoCreate(CreateView):
    model = Crypto 
    fields = '__all__'