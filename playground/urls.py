from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compress', views.compress, name='compress'),
    path('decode', views.decode, name='decode'),
    path('compressrle', views.compressrle, name='compressrle'),
    path('decoderle', views.decoderle, name='decoderle')
]
