from django.shortcuts import render
import requests
# Create your views here.
def homeView(request):
    return render(request, 'index.html')

def newsView(request):
    Str = request.path
    url =  "https://inshorts.deta.dev/news?category="
    if Str != "/all/" :
        url = url + Str[1:-1]
    Str = Str[1:-1] + " News"
    response = requests.get(url=url)
    indata = response.json()    
    return render(request, 'home.html', {'title' : Str, 'indata':indata})
