from django.shortcuts import render
from .serializer import *
from rest_framework.response import Response
from rest_framework import viewsets


class Category_view(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        data = self.queryset.get(id=kwargs['pk'])
        print(data)
        serializer = self.get_serializer(data)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class Brand_view(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class Unit_view(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class Product_view(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        data = self.get_object()
        print(partial)
        if data.price != float(request.data['price']):
            price_history = PriceHistory.objects.create(
                product=data,
                price=float(request.data['price'])
            )
        serializer = self.get_serializer(data, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class Stock_view(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class PriceHistory_view(viewsets.ModelViewSet):
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializer


class Supplier_view(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class Debit_view(viewsets.ModelViewSet):
    queryset = Debit.objects.all()
    serializer_class = DebitSerializer
