from django.shortcuts import render

# Create your views here.
def home(request):
    context_dic = {'text': 'Hello World!', 'number': 1000}
    return render(request,'app1/home.html', context_dic)

def other1(request):
    context_dic = {'text': 'Hello World!', 'number': 1000}
    return render(request, 'app1/other1.html', context_dic)

def other2(request):
    return render(request, 'app1/other2.html')

def relative(request):
    return render(request, 'app1/relative_url_templates.html')
