from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import IPOForm
from rest_framework import viewsets
from .models import IPO
from .serializers import IPOSerializer

class IPOViewSet(viewsets.ModelViewSet):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer

# def home(request):
#     return HttpResponse("<h1>IPO web application</h1>")

def register_ipo(request):
    if request.method == 'POST':
        form = IPOForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ipo_list')
    else:
        form = IPOForm()
    return render(request, 'ipo_register.html', {'form': form})

def ipo_list(request):
    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')

    ipos = IPO.objects.all().order_by('-id') 

    if query:
        ipos = ipos.filter(company_name__icontains=query)

    if status_filter:
        ipos = ipos.filter(status=status_filter)
        
    paginator = Paginator(ipos, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'ipo_list.html', {
        'page_obj': page_obj,
        'query': query,
        'status_filter': status_filter,
        'total_ipos': IPO.objects.count(),
    })

def delete_ipo(request, pk):
    ipo = get_object_or_404(IPO, pk=pk)
    if request.method == 'POST':
        ipo.delete()
        return redirect('ipo_list')
    return render(request, 'ipo_delete.html', {'ipo': ipo})

def update_ipo(request, pk):
    ipo = get_object_or_404(IPO, pk=pk)
    if request.method == 'POST':
        form = IPOForm(request.POST, request.FILES, instance=ipo)
        if form.is_valid():
            form.save()
            return redirect('ipo_list')
    else:
        form = IPOForm(instance=ipo)
    return render(request, 'ipo_register.html', {'form': form, 'is_update': True})

def ipo_detail(request, pk):
    ipo = get_object_or_404(IPO, pk=pk)
    return render(request, 'ipo_detail.html', {'ipo': ipo})