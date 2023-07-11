from django.shortcuts import render
from .models import Work
from .mailchimp_utils import subscribe_user_to_mailchimp

def index(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def services(request):
    return render(request, 'myapp/services.html')

def portfolio(request):
    return render(request, 'myapp/portfolio.html')

def works(request):
    works = Work.objects.all()
    return render(request, 'myapp/works.html', {'works': works})



def contact(request):
    return render(request, 'myapp/contact.html')
