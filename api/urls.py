from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewsets,CartViewsets,CategoryViewsets,OrderViewsets,OrderItemViewsets

router = DefaultRouter()
router.register('product',ProductViewsets)
router.register('category',CategoryViewsets)
router.register('cart',CartViewsets)
router.register('order',OrderViewsets)
router.register('orderitem',OrderItemViewsets)

urlpatterns = [
    path('',include(router.urls))
]