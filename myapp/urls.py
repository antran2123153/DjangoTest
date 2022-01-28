from django.urls import include, path
from rest_framework import routers
from myapp import views

router = routers.DefaultRouter()
router.register(r'account', views.AccountViewSet)
router.register(r'book', views.BookViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'cart', views.CartViewSet)
router.register(r'order', views.OrderViewSet)

urlpatterns = [
    path('login', views.Login.as_view(), name='login'),
    path('register', views.Register.as_view(), name='register'),
    path('', include(router.urls)),
]