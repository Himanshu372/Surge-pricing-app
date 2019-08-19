from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.views.decorators.csrf import ensure_csrf_cookie
import pandas as pd



class surgePricingList(viewsets.ModelViewSet):
    queryset = None

    @ensure_csrf_cookie
    def put(self, request, filename = 'data.xlsx' , format = None):
        '''

        :param request:
        :param filename:
        :param format:
        :return:
        '''
        file_obj = request.data['file']
        data = pd.read_excel(file_obj)
        print(data.head())



