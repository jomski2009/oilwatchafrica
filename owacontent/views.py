from django.shortcuts import render


# Create your views here.
def homepage(request, template):
    context = dict()
    return render(request, template, context=context)


def content_list(request):
    return render(request, "content/article.html")


def content_detail(request, slug):
    return render(request, "content/detail.html")
