from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IPOViewSet,ipo_list,register_ipo

router = DefaultRouter()
router.register(r'ipos', IPOViewSet)

urlpatterns = [
    # path('home/',views.home,name="home"), 
    path('json/', include(router.urls)), 
    path('', ipo_list, name='ipo_list'),
    path('api/', include(router.urls)),     
    path('register/', register_ipo, name='ipo_register'),
    path('ipo/<int:pk>/delete/', views.delete_ipo, name='ipo_delete'), 
    path('ipo/<int:pk>/', views.ipo_detail, name='ipo_detail'),
    path('ipo/<int:pk>/edit/', views.update_ipo, name='ipo_edit'),
]
