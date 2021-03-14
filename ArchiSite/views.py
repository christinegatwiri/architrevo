from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import generics, views, viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import PortfolioForm
from ArchiSite.models import *
from ArchiSite.serializers import *
from ArchiSite.forms import *
from django.conf import settings


# Create your views here.

def index(request):
    kikuyu_port_list = Portfolio.objects.filter(title='Kikuyu')
    likoni_port_list = Portfolio.objects.filter(title="Likoni")
    kithoka_port_list = Portfolio.objects.filter(title="Kithoka")
    
    return render(request, 'archisite/index.html',{'kikuyu_portfolio': kikuyu_port_list,
                                                        'likoni_port': likoni_port_list,
                                                        'nbar':'home',
                                                        'kithoka_port': kithoka_port_list,
                                                         'media_url':settings.MEDIA_URL})
def about(request):
    return render(request, 'archisite/about.html',{'nbar':'about'})

def contact(request):
    return render(request, 'archisite/contact.html',{'nbar':'contact'})

def services(request):
    return render(request, 'archisite/services.html',{'nbar':'services'})

def architecture(request):
    return render(request, 'archisite/architecture.html')

def landscape(request):
    return render(request, 'archisite/landscape_arch.html')

def predesign(request):
    return render(request, 'archisite/pre_design.html')

def susdesign(request):
    return render(request, 'archisite/sus_design.html')

def single_blog(request):
    return render(request, 'archisite/blog-single.html')

def blog(request):
    blog_list = Blog.objects.all()
    return render(request, 'archisite/blog.html',{'blog': blog_list,'nbar':'blog', 'media_url':settings.MEDIA_URL})

def portfolio(request):
    port_list = Portfolio.objects.all()
    return render(request, 'archisite/portfolio.html',{'portfolio': port_list,'nbar':'portfolio', 'media_url':settings.MEDIA_URL})

def portfolio_upload(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST,request.FILES)
        if form.is_valid():
            plans = form.save(commit=False)
            plans.save()
            return redirect('portfolio')
    else:
        form = PortfolioForm()
    return render(request,'archisite/upload_portfolio.html',{'form': form})

class ListPortfolio(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class ListServices(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

class ListNewsletterList(viewsets.ModelViewSet):
    queryset = NewsletterList.objects.all()
    serializer_class = NewsletterListSerializer

class ListApplications(viewsets.ModelViewSet):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer

class ListBlogs(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer



    