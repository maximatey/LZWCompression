from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
import playground.main_function
import playground.main_function_RLE
# Create your views here.

def index(request):
    return render(request, 'index.html')


def compress(request):
    try :
        inputtext = request.POST['compresstext']
        compressed_text = playground.main_function.LZWcompress(inputtext)
        return render(request, 'compress.html', {'outText' : compressed_text})
    except MultiValueDictKeyError:
        return render(request, 'index.html')
    

def decode(request):
    try :
        inputtext = request.POST['decodetext']
        decompressed_text = playground.main_function.LZWdecompress(inputtext)
        return render(request, 'decode.html', {'outText' : decompressed_text})
    except MultiValueDictKeyError:
        return render(request, 'index.html')
    
    
def compressrle(request):
    try :
        inputtext = request.POST['compresstextrle']
        compressed_text = playground.main_function_RLE.compress_rle(inputtext)
        return render(request, 'compressrle.html', {'outText' : compressed_text})
    except MultiValueDictKeyError:
        return render(request, 'index.html')
    

def decoderle(request):
    try :
        inputtext = request.POST['decodetextrle']
        decompressed_text = playground.main_function_RLE.decompress_rle(inputtext)
        return render(request, 'decoderle.html', {'outText' : decompressed_text})
    except MultiValueDictKeyError:
        return render(request, 'index.html')
