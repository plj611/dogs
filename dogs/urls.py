from django.urls import path

from . import views

app_name = 'dogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('t', views.test, name='test'),
    path('u', views.upload_file, name='upload'),
    path('h', views.history, name='history'),
    path('success/<str:file_name>', views.success, name='success'),
]
