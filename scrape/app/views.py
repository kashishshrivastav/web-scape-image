import os
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ValidationError
import requests
from bs4 import BeautifulSoup
from django.conf import settings
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    url = request.POST['url']
    name_of_image = request.POST['number']
    if name_of_image is None:
        return HttpResponse('number of image is required')
    try:
        name_of_image = int(name_of_image)
        if name_of_image <= 0:
            raise ValidationError('number of image must be a positive integer')
    except ValueError:
        return HttpResponse('number of image please enter a positive integer')
    image_urls = []
    response  = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    for img in soup.find_all('img'):
        image_urls.append(img['src'])

    for image_url in image_urls[:name_of_image]:
        image_data = requests.get(image_url).content
        file_name = os.path.basename(image_url)


        media_folder = settings.MEDIA_ROOT
        print(media_folder)
        with open(os.path.join(media_folder,file_name),'wb') as f:
            f.write(image_data)

        scrape_data = Scrapeimage(url=url,name_of_image=file_name)
        scrape_data.save()
    return render(request,'index.html',{'scrape_data':scrape_data})