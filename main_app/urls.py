from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cakes/', views.cakes_index, name='index'),
    # path('cakes/<int:cake_id>', views.cakes_detail, name='detail'),
    path('cakes/<int:pk>', views.CakeDetail.as_view(), name='detail'),
    path('cakes/create', views.CakeCreate.as_view(), name='cakes_create'),
    path('cakes/<int:pk>/update', views.CakeUpdate.as_view(), name='cakes_update'),
    path('cakes/<int:pk>/delete', views.CakeDelete.as_view(), name='cakes_delete'),

    # Recipe
    # path('recipes/', views.RecipeList.as_view(), name='recipe_index'),
    # path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    # path('cakes/<int:cake_id>/add_recipe', views.RecipeCreate.as_view(), name='add_recipe'),
    path('cakes/<int:pk>/add_recipe', views.add_recipe, name='add_recipe'),
    path('recipes/<int:pk>/update', views.RecipeUpdate.as_view(), name='recipes_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),

    # Authentication Paths
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
]