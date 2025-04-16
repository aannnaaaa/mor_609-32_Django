from django.http import HttpResponse
from django.shortcuts import render

from articles.models import Article


def homepage(request):
    data = { 'header': 'Find the newest articles here',
        'message': 'Stay updated with the latest trends and information.',
        'featured_articles': Article.objects.all().order_by('-date')[:3]}
    return render(request, 'homepage.html', context=data)

def about(request):
    header = "About Us"
    staff = ['Jhon Nichols', 'Jhon Rogers', 'Timothy Smith']
    director = {"name": "David Lee", "img": '/director.png'}
    address = ('20 W 34th St.', 'New York', 'NY 10001', 'USA')
    data = {"header": header, "staff": staff, "director": director, "address": address}
    return render(request, 'about.html', data)

