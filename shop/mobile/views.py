from django.shortcuts import render
from .models import Mobile
from django.views.generic import ListView , DetailView
# Create your views here.

# def home_page(request):
#     mobiles=Mobile.objects.all()
#     return render(request , 'home.html' , {'mobiles':mobiles})

class HomePage(ListView):
    model=Mobile
    template_name='home.html'
    context_object_name='mobiles'



# def mobile_detail(request , detail_id):
#     detail=Mobile.objects.get(id=detail_id)
#     return render(request , 'detail.html', {'detail':detail})

class MobileDetail(DetailView):
    model=Mobile
    template_name='detail.html'
    context_object_name='detail'