from django.shortcuts import render


def index(request):
    return render(request, 'single_page_site.html')
