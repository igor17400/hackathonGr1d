from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('client/', views.ClientViewSet.as_view(), name='clients'),
    path('transaction/', views.TransactionViewSet.as_view(), name='transactions'),
    path('transaction/<int:id>', views.TransactionPerId.as_view(), name='transaction'),
    path('bank/', views.BankViewSet.as_view(), name='banks'),
    path('account/', views.AccountViewSet.as_view(), name='accounts'),
    path('operation/', views.AccountViewSet.as_view(), name='operations'),
    path('meuScore/', views.meuScore, name='getApi'),
]