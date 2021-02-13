from django.urls import path, include
from rest_framework import routers
from . import views
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'portfolio', views.ListPortfolio)
router.register(r'houseplan', views.ListHousePlans)
router.register(r'service', views.ListServices)
router.register(r'newletter', views.ListNewsletterList)
router.register(r'applications', views.ListApplications)
router.register(r'blog', views.ListBlogs)

urlpatterns = [
    path('api/', include(router.urls)),
    path('index/', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services, name="services"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('house_plans/', views.house_plans, name="house_plans"),
    path('plans_upload/', views.plans_upload, name="plans_upload"),
    path('portfolio_upload/', views.portfolio_upload, name="portfolio_upload"),
    path('architecture/', views.architecture, name="architecture"),
    path('landscape/', views.landscape, name="landscape"),
    path('predesign/', views.predesign, name="predesign"),
    path('susdesign/', views.susdesign, name="susdesign"),
    path('blog/', views.blog, name="blog"),
    path('single_blog/', views.single_blog, name="single_blog")
]
