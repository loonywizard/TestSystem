from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'subject$', views.subject),

]