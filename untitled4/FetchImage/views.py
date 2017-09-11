from django.http import HttpResponse
from FetchImage import FetchImages
from .models import ImageData
import cgi

def index(request):
    htmlString = ""
    listOfImages = FetchImages.downloadPage()
    for imageUrl in listOfImages:
        imageData = ImageData(url=imageUrl)
        imageData.save()
    fetchImages = ImageData.objects.all()
    for image in fetchImages:
        url = "/imageData/" + str(image.id)
        htmlString += '<a href="' + url +'/">' + image.url + '<br></a>'
    return HttpResponse(htmlString)

def detail(request, album_id):
    imageUrl = ImageData.objects.get(id=album_id)
    return HttpResponse("<img src = " + str(imageUrl) + "></img><br><pre>" + str(imageUrl.url) + "</pre>")
