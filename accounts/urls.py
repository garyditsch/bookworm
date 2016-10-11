from django.conf.urls import url
from .forms import LoginForm

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login', 
        {'authentication_form': LoginForm},
        name='login'),
    
    url(r'^logout/$', 
        'django.contrib.auth.views.logout', 
        {'template_name': 'accounts/logout.html'},
        name='logout'),
]