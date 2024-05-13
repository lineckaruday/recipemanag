"""
URL configuration for recipemanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipe import views



app_name="recipe"

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', views.allrecipe, name="allrecipe"),                          # func based api view url

    path('detail/<int:pk>', views.recipedetails, name="recipedetails"),         # func based api view url
    #
    # path('bookdel/<int:pk>', views.bookdel, name="bookdel"),

    path('user_logout', views.user_logout.as_view()),

    path('allrev', views.allrev.as_view()),

    path('detailrev/<int:pk>', views.detailrev.as_view()),

    path('cuisinefilter', views.cuisinefilter.as_view()),

    path('mealfilter', views.mealfilter.as_view()),

    path('ingredientsfilter', views.ingredientsfilter.as_view()),

]
