from django.shortcuts import render



# Create your views here.
def food(request):
    return render(request, 'index.html')

def bank(request):
    return render(request, 'contact.html')



    


    

