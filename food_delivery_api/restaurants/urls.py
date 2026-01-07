from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, MenuItemViewSet
from django.urls import path
from .views import (
    RestaurantListCreateView,
    RestaurantDetailView,
    MenuItemListCreateView,
    MenuItemDetailView
)

router = DefaultRouter()
router.register("restaurants", RestaurantViewSet)
router.register("menu-items", MenuItemViewSet)

urlpatterns = router.urls

urlpatterns = [
    # Restaurants
    path('restaurants/', RestaurantListCreateView.as_view()),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view()),

    # Menu Items
    path('restaurants/<int:restaurant_id>/menu/', MenuItemListCreateView.as_view()),
    path('menu-items/<int:pk>/', MenuItemDetailView.as_view()),
]
