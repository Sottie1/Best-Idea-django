from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static



app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('works/', views.works, name='works'),
    path('contact/', views.contact, name='contact'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

