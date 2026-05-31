from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def old_home_page_view(request, *args, **kwargs):
    html_ = ''
    html_file_path = this_dir/'home.html'
    html_ = html_file_path.read_text()
    return HttpResponse(html_)

def home_page_view(request):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    context = {
        'page_visit_count': page_qs.count(),
        'total_visit_count': qs.count()
    }
    
    path = request.path
    PageVisit.objects.create(path = request.path)
    
    return render(request, 'home.html', context)



