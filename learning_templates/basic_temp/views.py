from django.shortcuts import render


# Create your views here.
def index(request):
    context_dict = {'text':'Hello World', 'number':100}
    return render(request, 'basic_temp/index.html', context=context_dict)


def other(request):
    return render(request, 'basic_temp/other.html')


def relative(request):
    return render(request, 'basic_temp/relative_url_templates.html')
