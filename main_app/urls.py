from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'), #homepage/root
    path('about/', views.about, name='about'), # .about via import views.py
    path('dates/', views.date_index, name='date-index'),
    path('dates/<int:date_id>/', views.date_detail, name='date-detail'),
    path('dates/create/', views.DateCreate.as_view(), name='date-create'),
    path('dates/<int:pk>/update/', views.DateUpdate.as_view(), name='date-update'),
    path('dates/<int:pk>/delete/', views.DateDelete.as_view(), name='date-delete'),

    path('foods/create/', views.FoodCreate.as_view(), name='food-create'),
    path('foods/<int:pk>/', views.FoodDetail.as_view(), name='food-detail'),
    path('foods/', views.FoodList.as_view(), name='food-index'),

    path('foods/<int:pk>/update/', views.FoodUpdate.as_view(), name='food-update'),
    path('foods/<int:pk>/delete/', views.FoodDelete.as_view(), name='food-delete'),

    path('foods/<int:date_id>/associate-food/<int:food_id>/', views.associate_food, name='associate-food'), # via models.py food
    path('dates/<int:date_id>/remove-food/<int:food_id>/', views.remove_food, name='remove-food'),
    path('accounts/signup/', views.signup, name='signup'),


]

