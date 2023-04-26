from django.shortcuts import render
from rest_framework import generics
from .serializers import CarDetailSerializer, CarListSerializer
from .models import Car
from .permissions import IsOwnerOnReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
import xlwt
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from tablib import Dataset

from .resources import CarResource
from .models import Car


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAdminUser,)

    def post(self, request):
        print(request.data)
        print(request.POST)
        return Response({1: 123})


class CarsDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOnReadOnly,)


def export_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        employee_resource = CarResource()
        dataset = employee_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response

    return render(request, 'export.html')
# Create your views here.
