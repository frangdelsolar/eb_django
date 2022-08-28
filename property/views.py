from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from apieasybroker import APIEasyBroker


class PropertyListView(View):
    api = APIEasyBroker()
    template_name = 'property/list.html'

    def get(self, request, *args, **kwargs):

        limit = 15
        page = request.GET.get('page')
        if page:
            page = int(page)
        else:
            page = 1

        context = self.api.get_properties_by_page(page, limit)
        context['pags'] = {
            'prev': page - 1,
            'curr': page,
            'next': page + 1
        }

        return render(request, self.template_name, context)


class PropertyDetailView(View):
    api = APIEasyBroker()
    template_name = 'property/detail.html'

    def get(self, request, *args, **kwargs):
        property_id = kwargs.get('id')
        context = self.api.get_property_by_id(property_id)
        return render(request, self.template_name, context)
