from extract_bottleneck_features import *
from keras.layers import Flatten, Dense
from keras.models import Sequential
from keras.preprocessing import image
from glob import glob
import numpy as np
import os, sys

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

#app_path = '.'
app_path = os.path.dirname(os.path.abspath(__file__))

bottleneck_features = np.load(os.path.join(app_path, 'bottleneck_features/DogResnet50Data.npz'))
train_Resnet50 = bottleneck_features['train']

Resnet50_model = Sequential()
Resnet50_model.add(Dense(133, input_shape=train_Resnet50.shape[1:], activation='softmax'))
Resnet50_model.add(Flatten())
Resnet50_model.load_weights(os.path.join(app_path, 'saved_models/weights.best.Resnet50.hdf5'))

#print('Hi')
def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)

def Resnet50_predict_breed(img_path):
#    print(img_path)
#    img_path = 'c:/temp/wtime/b.jpg'
    # extract bottleneck features
    bottleneck_feature = extract_Resnet50(path_to_tensor(img_path))
#    print('end extract')
	#print(bottleneck_feature.shape)
    # obtain predicted vector
    predicted_vector = Resnet50_model.predict(bottleneck_feature)
    #print('2')
	# return dog breed that is predicted by the model
    i = np.argmax(predicted_vector)
    return (dog_names[i], str(predicted_vector[0][i] - predicted_vector[0][i] % 0.01))

#print(sys.argv[1])
#print(Resnet50_predict_breed(sys.argv[1]))
ret = Resnet50_predict_breed(sys.argv[1])
#ret = Resnet50_predict_breed('a')
print(' '.join(ret))
#'C:/Temp/wtime/dev/project1/project1/dogs/b.jpg'))
