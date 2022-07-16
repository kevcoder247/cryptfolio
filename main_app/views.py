#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.views.generic.detail import ListView
from .models import Crypto
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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

@login_required
def crypto_index(request):
    cryptos = Crypto.objects.filter(user=request.user)
    return render(request, 'cryptos/index.html', {'cryptos' : cryptos})

@login_required
def crypto_detail(request, crypto_id):
    crypto = Crypto.objects.get(id=crypto_id)
    return render(request, 'cryptos/detail.html', {'crypto': crypto})


#CUD Class Bases Views
class CryptoCreate(LoginRequiredMixin, CreateView):
    model = Crypto 
    fields = ['name', 'price', 'qty',  'date']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class CryptoUpdate(LoginRequiredMixin, UpdateView):
    model = Crypto
    fields = ['price', 'qty']


class CryptoDelete(LoginRequiredMixin, DeleteView):
    model = Crypto
    success_url = '/crypto/'



def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)