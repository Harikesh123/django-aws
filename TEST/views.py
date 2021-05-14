from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    d = {"head":"abcd", "des":"asdadasdadasas"}
    return render(request,'index.html', d)

def about(request):
    return render(request,'it_about.html')

def blog(request):
    return render(request,'it_blog.html')

def blogdetail(request):
    return render(request,'it_blogdetail.html')

def bloggrid(request):
    return render(request,'it_bloggrid.html')

def career(request):
    return render(request,'it_career.html')

def cart(request):
    return render(request,'it_cart.html')

def checkout(request):
    return render(request,'it_checkout.html')

def computerrepair(request):
    return render(request,'it_computer_repair.html')

def contact(request):
    return render(request,'it_contact.html')

def contact2(request):
    return render(request,'it_contact_2.html')

def datarecovery(request):
    return render(request,'it_data_recovery.html')

def error(request):
    return render(request,'it_error.html')

def faq(request):
    return render(request,'it_faq.html')

def home(request):
    return render(request,'it_home.html')

def homedark(request):
    return render(request,'it_home_dark.html')

def mobileservice(request):
    return render(request,'it_mobile_service.html')

def networksolution(request):
    return render(request,'it_network_solution.html')

def news(request):
    return render(request,'it_news.html')

def price(request):
    return render(request,'it_price.html')

def privacypolicy(request):
    return render(request,'it_privacy_policy.html')

def service(request):
    return render(request,'it_service.html')

def servicedetail(request):
    return render(request,'it_service_detail.html')

def servicelist(request):
    return render(request,'it_service_list.html')

def shop(request):
    return render(request,'it_shop.html')

def shopdetail(request):
    return render(request,'it_shop_detail.html')

def techsupport(request):
    return render(request,'it_techn_support.html')

def termcondition(request):
    return render(request,'it_term_condition.html')

def appointment(request):
    return render(request,'it_make_appointment.html')

def register(request):
    return render(request,'register.html')