from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from PIL import Image
from django.conf import settings
import uuid
from .forms import UploadFileForm
from .models import guessed_result
from django.utils import timezone
#from .dogpredict import *
from subprocess import check_output
import os

'''
from .extract_bottleneck_features import *
from keras.layers import Flatten, Dense
from keras.models import Sequential
from keras.preprocessing import image
from glob import glob
import numpy as np
import os

def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)
	
bottleneck_feature = extract_Resnet50(path_to_tensor('c:/temp/wtime/b.jpg'))
print('end extract')


dog_names = \
[
'Affenpinscher',
'Afghan_hound',
'Airedale_terrier',
'Akita',
'Alaskan_malamute',
'American_eskimo_dog',
'American_foxhound',
'American_staffordshire_terrier',
'American_water_spaniel',
'Anatolian_shepherd_dog',
'Australian_cattle_dog',
'Australian_shepherd',
'Australian_terrier',
'Basenji',
'Basset_hound',
'Beagle',
'Bearded_collie',
'Beauceron',
'Bedlington_terrier',
'Belgian_malinois',
'Belgian_sheepdog',
'Belgian_tervuren',
'Bernese_mountain_dog',
'Bichon_frise',
'Black_and_tan_coonhound',
'Black_russian_terrier',
'Bloodhound',
'Bluetick_coonhound',
'Border_collie',
'Border_terrier',
'Borzoi',
'Boston_terrier',
'Bouvier_des_flandres',
'Boxer',
'Boykin_spaniel',
'Briard',
'Brittany',
'Brussels_griffon',
'Bull_terrier',
'Bulldog',
'Bullmastiff',
'Cairn_terrier',
'Canaan_dog',
'Cane_corso',
'Cardigan_welsh_corgi',
'Cavalier_king_charles_spaniel',
'Chesapeake_bay_retriever',
'Chihuahua',
'Chinese_crested',
'Chinese_shar-pei',
'Chow_chow',
'Clumber_spaniel',
'Cocker_spaniel',
'Collie',
'Curly-coated_retriever',
'Dachshund',
'Dalmatian',
'Dandie_dinmont_terrier',
'Doberman_pinscher',
'Dogue_de_bordeaux',
'English_cocker_spaniel',
'English_setter',
'English_springer_spaniel',
'English_toy_spaniel',
'Entlebucher_mountain_dog',
'Field_spaniel',
'Finnish_spitz',
'Flat-coated_retriever',
'French_bulldog',
'German_pinscher',
'German_shepherd_dog',
'German_shorthaired_pointer',
'German_wirehaired_pointer',
'Giant_schnauzer',
'Glen_of_imaal_terrier',
'Golden_retriever',
'Gordon_setter',
'Great_dane',
'Great_pyrenees',
'Greater_swiss_mountain_dog',
'Greyhound',
'Havanese',
'Ibizan_hound',
'Icelandic_sheepdog',
'Irish_red_and_white_setter',
'Irish_setter',
'Irish_terrier',
'Irish_water_spaniel',
'Irish_wolfhound',
'Italian_greyhound',
'Japanese_chin',
'Keeshond',
'Kerry_blue_terrier',
'Komondor',
'Kuvasz',
'Labrador_retriever',
'Lakeland_terrier',
'Leonberger',
'Lhasa_apso',
'Lowchen',
'Maltese',
'Manchester_terrier',
'Mastiff',
'Miniature_schnauzer',
'Neapolitan_mastiff',
'Newfoundland',
'Norfolk_terrier',
'Norwegian_buhund',
'Norwegian_elkhound',
'Norwegian_lundehund',
'Norwich_terrier',
'Nova_scotia_duck_tolling_retriever',
'Old_english_sheepdog',
'Otterhound',
'Papillon',
'Parson_russell_terrier',
'Pekingese',
'Pembroke_welsh_corgi',
'Petit_basset_griffon_vendeen',
'Pharaoh_hound',
'Plott',
'Pointer',
'Pomeranian',
'Poodle',
'Portuguese_water_dog',
'Saint_bernard',
'Silky_terrier',
'Smooth_fox_terrier',
'Tibetan_mastiff',
'Welsh_springer_spaniel',
'Wirehaired_pointing_griffon',
'Xoloitzcuintli',
'Yorkshire_terrier'
]

app_path = os.path.dirname(os.path.abspath(__file__))

bottleneck_features = np.load(os.path.join(app_path, 'bottleneck_features/DogResnet50Data.npz'))
train_Resnet50 = bottleneck_features['train']

Resnet50_model = Sequential()
Resnet50_model.add(Dense(133, input_shape=train_Resnet50.shape[1:], activation='softmax'))
Resnet50_model.add(Flatten())
Resnet50_model.load_weights(os.path.join(app_path, 'saved_models/weights.best.Resnet50.hdf5'))

print('Hi')

def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)

def Resnet50_predict_breed(img_path):
    print(img_path)
    img_path = 'c:/temp/wtime/b.jpg'
    # extract bottleneck features
    bottleneck_feature = extract_Resnet50(path_to_tensor(img_path))
    print('end extract')
	#print(bottleneck_feature.shape)
    # obtain predicted vector
    predicted_vector = Resnet50_model.predict(bottleneck_feature)
    print('2')
	# return dog breed that is predicted by the model
    return dog_names[np.argmax(predicted_vector)]

'''

def index(request):
   return render(request, 't/home.html')

def test(request):
   return HttpResponse(request.POST['dog'])

'''
from keras.applications.resnet50 import preprocess_input
#b = ResNet50(weights='imagenet', include_top=False)
'''

from django.template.response import TemplateResponse

def upload_file(request):
    
    breed = ''
    fn = 'white.jpg'
    prob = ''
    app_path = os.path.dirname(os.path.abspath(__file__))

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #a = 1 / 0
            fn = uuid.uuid4().hex
            handle_uploaded_file(request.FILES['file'], fn)
           
            #render(request, 't/upload.html', {'form': form, 'fn': fn, 'breed': breed})
            #t = TemplateResponse(request, 't/upload.html', {})
            #t.resolve_context({'form': form, 'fn': fn, 'breed': breed})
            #t.render()
			
            res = check_output(["python", os.path.join(app_path, 'dogpredict.py'), os.path.join(settings.MEDIA_ROOT, fn)])
            res = res.decode('utf-8')
            breed, prob = res.split(' ')

            #return HttpResponseRedirect(reverse('dogs:success', kwargs={'file_name': fn, 'breed': breed}))
            #return render(request, 't/result.html', {'fn': fn, 'breed': breed})
            guessed_result(guess_date=timezone.now(), breed=breed, accurancy=prob[:-2], imagepath=fn).save()
            return render(request, 't/upload.html', {'form': form, 'fn': fn, 'breed': breed,
                                                     'prob': prob})
        else:
            b = 1/ 0
    else:
        form = UploadFileForm()
    return render(request, 't/upload.html', {'form': form, 'fn': fn, 'breed': breed, 
	                                         'prob': prob})
    #return TemplateResponse(request, 't/upload.html', {'form': form, 'fn': fn, 'breed': breed})

def success(request, file_name):
    return render(request, 't/result.html', {'fn': file_name})
    #return HttpResponse('Hello a file is upload!')

def handle_uploaded_file(f, file_name):
    #with open('dogs/tmp/' + file_name, 'wb+') as destination:
    with open(settings.MEDIA_ROOT + file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
			
def history(request):
   results = guessed_result.objects.all()
   return render(request, 't/history.html', {'results': results})
