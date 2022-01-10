from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os


# Create your views here.
def index(request):
    return render(request, 'index.html')

def download(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'resume.pdf'
    filepath = base_dir + '/Files/' + filename
    thefile = filepath
    filename =  os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'), chunk_size),
    content_type = mimetypes.guess_type(thefile[0]))
    response['content-Length'] = os.path.getsize(thefile)
    response['content-Disposition'] = "Attachment;filename=%s" % filename
    return response
