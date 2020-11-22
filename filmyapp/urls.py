"""filmy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from filmyapp import  views

urlpatterns = [
 path("", views.IndexView.as_view(), name = 'index' ),
 path("add_person/", views.AddPersonView.as_view(), name = 'person'),
 path("add_movie/",views.AddMovieView.as_view(), name = 'movie'),
 path("add_category/", views.AddCategoryView.as_view(), name = 'category'),
 path("add_studio/", views.AddStudioView.as_view(), name='studio'),
 path("movie_list/", views.ListMovieView.as_view(), name= 'movies'),
path("persons_list/", views.ListPersonView.as_view(), name= 'persons'),
path("categories_list/", views.ListCategoriesView.as_view(), name= 'categories'),
path("studios_list/", views.ListStudioView.as_view(), name= 'studios'),
path("add_movie_form/", views.AddMovieFullFormView.as_view(), name= 'add_movie_form'),
path("add_studio_form/", views.AddStudioFullFormView.as_view(), name= 'add_studio_form'),
path("add_movie_model/", views.AddMovieModelView.as_view(), name= 'add_movie_model'),
path("add_person_model/", views.AddPersonModelView.as_view(), name= 'add_person_model'),
path("add_studio_model/", views.AddStudioModelView.as_view(), name= 'add_studio_model'),
 path("add_person_generic/", views.AddPersonGenericView.as_view(), name= 'add_person_generic'),
 path("add_studio_generic/", views.AddStudioGenericView.as_view(), name='add_studio_generic'),
 path("edit_movie/<int:pk>/", views.MovieUpdateView.as_view(), name='edit_movie'),
 path("edit_person/<int:pk>/", views.PersonUpdateView.as_view(), name='edit_person'),
path("editGenericMovie/<int:pk>/", views.MovieGenericUpdateView.as_view(), name='edit_movie_generic'),
]
