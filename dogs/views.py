from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from PIL import Image
from django.conf import settings
import uuid
from .forms import UploadFileForm


# Create your views here.
#print("I am inside view: " + settings.MEDIA_ROOT)

def index(request):
   return render(request, 't/home.html')

def test(request):
   return HttpResponse(request.POST['dog'])

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #a = 1 / 0
            fn = uuid.uuid4().hex
            handle_uploaded_file(request.FILES['file'], fn)
            return HttpResponseRedirect(reverse('dogs:success', kwargs={'file_name': fn}))
        else:
            b = 1/ 0
    else:
        form = UploadFileForm()
    return render(request, 't/upload.html', {'form': form})

def success(request, file_name):
    return render(request, 't/result.html', {'fn': file_name})
    #return HttpResponse('Hello a file is upload!')

def handle_uploaded_file(f, file_name):
    #with open('dogs/tmp/' + file_name, 'wb+') as destination:
    with open(settings.MEDIA_ROOT + file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
