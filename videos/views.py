from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from glob import glob
import pathlib
from .models import Movie
import re

def discover(request):
    existing = set(Movie.objects.values_list('path', flat=True))
    files = {f.name for f in pathlib.Path('../static/movies/').iterdir()}
    todo = sorted(files - existing)
    keywords = [' '.join(re.findall(r"[a-zA-Z0-9]+", s)) for s in todo]
    return render(request, 'videos/discover.html', {'files': zip(todo, keywords)})

def generate(request):
    r = render(request, 'videos/generate.html', {'movies': Movie.objects.order_by('name')})
    # The replacement here is because I'm lazy and this works for my shitty simple content :-P
    open('../static/index.html', 'w').write(r.content.decode('utf-8').replace('="/', '="'))
    return r
