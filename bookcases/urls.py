from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.bookcase_list, name='bookcase_list'),
    url(r'^(?P<id>\d+)/$', views.bookcase_detail, name="bookcase_detail"),
    url(r'^bookshelves/(?P<id>\d+)/$', views.bookshelf_detail, name='bookshelf_detail'),
]