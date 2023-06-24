from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
import playground.main_function
# Create your views here.

def index(request):
    return render(request, 'index.html')


def compress(request):
    try :
        inputtext = request.POST['compresstext']
    except MultiValueDictKeyError:
        inputtext =''
    compressed_text = playground.main_function.LZWcompress(inputtext)
    return render(request, 'compress.html', {'outText' : compressed_text})

def decode(request):
    try :
        inputtext = request.POST['decodetext']
    except MultiValueDictKeyError:
        inputtext =''
    decompressed_text = playground.main_function.LZWdecompress(inputtext)
    return render(request, 'decode.html', {'outText' : decompressed_text})
