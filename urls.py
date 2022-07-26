
from .views import product_list, product_detail, ProductAPIView, ProductViewSet, ProductDetails, GenericAPIView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static 
from django.conf import settings


router = DefaultRouter()

router.register('product', ProductViewSet, basename= 'product')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('detail/<int:id>/', ProductDetails.as_view()),
    path('product/', ProductAPIView.as_view()),
    path('detail/<int:id>/', ProductDetails.as_view()),
    path('generic/product/<int:id>',GenericAPIView.as_view()),

]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # will help display the image 
