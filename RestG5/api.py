from rest_framework import routers
from api.views import *
router = routers.DefaultRouter()
router.register(r'category', Category_view, basename='category')
router.register(r'brand', Brand_view, basename='brand')
router.register(r'unit', Unit_view, basename='unit')
router.register(r'product', Product_view, basename='product')
router.register(r'stock', Stock_view, basename='stock')
router.register(r'price', PriceHistory_view, basename='price')
router.register(r'supplier', Supplier_view, basename='supplier')
router.register(r'debit', Debit_view, basename='debit')
