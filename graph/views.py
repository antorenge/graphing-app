"""
Graph views.
"""
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Default page to display graph."""

    def get(self, request, **kwargs):
        """Return a template view"""
        return render(request, 'index.html', context=None)
