from django.shortcuts import render
from math import ceil
from .models import Memes

# Create your views here.
from django.http import HttpResponse

def index(request):
    all_meme = []
    meme_cat = Memes.objects.values('meme_catagory')
    cats = {item['meme_catagory'] for item in meme_cat}
    for cat in cats:
        meme = Memes.objects.filter(meme_catagory=cat)
        n = len(meme)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        all_meme.append([meme, range(1, nSlides), nSlides])
    params = {'all_meme': all_meme}
    return render(request, 'home/index.html', params)