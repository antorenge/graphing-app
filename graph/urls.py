"""
Graph urls config.
"""
from django.conf.urls import url
from .views import HomePageView

app_name = 'graph'

urlpatterns = [
    url(r'^$', HomePageView.as_view()),
]
