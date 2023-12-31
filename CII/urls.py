from django.urls import path, include

from rest_framework.routers import DefaultRouter
from CII import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet)
router.register('VesselOwnerMaster', views.VesselOwnerMasterViewSet)
router.register('ContactTypeMaster',views.ContactTypeMasterViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))

]
