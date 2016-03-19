from django.shortcuts import render


# Create your views here.
from owacontent.models import Content


def homepage(request, template):
    context = dict()
    featured_content = Content.objects.all().filter(featured_piece=True)[:5]
    if featured_content is not None and len(featured_content) > 0:
        context["featured_content"] = featured_content
        print "Featured content: ", featured_content
    content_list = Content.objects.all()[:5]
    context["home_content_list"] = content_list

    return render(request, template, context=context)


def content_list(request):
    return render(request, "content/article.html")


def content_detail(request, slug):
    return render(request, "content/detail.html")
