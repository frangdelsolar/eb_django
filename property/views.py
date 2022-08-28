from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import requests
from apieasybroker import APIEasyBroker


class PropertyListView(View):
    api = APIEasyBroker()
    page = 1
    limit = 15
    template_name = 'property/list.html'

    def get(self, request, *args, **kwargs):

        if 'page' in request.GET:
            self.page = int(request.GET.get('page'))

        context = self.api.get_properties_by_page(self.page, self.limit)

        # get correct pages.
        context['pags'] = {
            'prev': self.page - 1,
            'curr': self.page,
            'next': self.page + 1
        }

        return render(request, self.template_name, context)


class PropertyDetailView(View):
    api = APIEasyBroker()

    template_name = 'property/detail.html'

    def get(self, request, *args, **kwargs):
        property_id = kwargs.get('id')
        context = self.api.get_property_by_id(property_id)
        print(context)
        return render(request, self.template_name, context)
