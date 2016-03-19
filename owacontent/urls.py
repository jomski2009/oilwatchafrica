from django.conf.urls import url

from owacontent.views import content_list, content_detail

urlpatterns = [
    url("^list/$", content_list, name="content_list"),
    url("^(?P<slug>[\d\w\-_]+)/$", content_detail, name="content_detail")
]