from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View

from filmyapp.models import Person, Category, Studio, Film
from filmyapp.forms import MovieForm, PersonForm, MovieFullForm, StudioFullForm, MovieModelForm, PersonModelForm, \
    StudioModelForm


class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')


class MoviesView(View):
    pass


class AddPersonView(View):
    def get(self, request):
        # person = Person.objects.all()
        # return render(request, 'add_person.html', {'person': person})
        form = PersonForm()
        return render(request, 'add_obj.html', {'form': form})

    def post(self, request):
        # first_name = request.POST.get('first_name', '')
        # last_name = request.POST.get('last_name', '')
        # Person.objects.create(first_name=first_name, last_name=last_name)
        # return redirect(reverse("person"))
        form = PersonForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            Person.objects.create(first_name=first_name, last_name=last_name)
            return redirect(reverse("persons"))
        return render(request, 'add_obj.html', {'form': form})


class AddCategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'add_category.html', {'categories': categories})

    def post(self, request):
        name = request.POST.get('name', '')
        Category.objects.create(name=name)
        return redirect(reverse("categories"))


class AddMovieView(View):
    def get(self, request):
        form = MovieForm()
        objects = Film.objects.all()
        return render(request, 'add_obj.html', {'form': form, 'objects': objects})

    def post(self, request):
        # title = request.POST.get('title', '')
        # year = request.POST.get('year', '')
        # category = request.POST.get('category', '')
        # directory = request.POST.get('directory', '')
        # Movie.objects.create(title=title, year=year, category=category, directory=directory)

        form = MovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            year = form.cleaned_data['year']
            Film.objects.create(title=title, year=year, directory=Person.objects.reverse()[0])
            return redirect(reverse("movie"))
        return render(request, 'add_obj.html', {'form': form})


class AddStudioView(View):
    def get(self, request, ):
        studios = Studio.objects.all()
        return render(request, 'add_studio.html', {'studios': studios})

    def post(self, request):
        name = request.POST.get('name', '')
        city = request.POST.get('city', '')
        Studio.objects.create(name=name, city=city)
        return redirect(reverse("studio"))


class ListMovieView(View):
    def get(self, request):
        movies = Film.objects.all()
        return render(request, "movie_list.html", {'movies': movies})


class ListPersonView(View):
    def get(self, request):
        persons = Person.objects.all()
        return render(request, "person_list.html", {'persons': persons})


class ListCategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, "categories_list.html", {'categories': categories})


class ListStudioView(View):
    def get(self, request):
        studios = Studio.objects.all()
        return render(request, "studio_list.html", {'studios': studios})


class AddMovieFullFormView(View):
    def get(self, request):
        form = MovieFullForm()
        return render(request, 'add_obj.html', {'form': form})

    def post(self, request):
        form = MovieFullForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            year = form.cleaned_data['year']
            directory = form.cleaned_data['directory']
            category = form.cleaned_data['category']
            movie = Film.objects.create(title=title, year=year, directory=directory)
            movie.category.set(category)
            return redirect((reverse('add_movie_form')))
        return render(request, 'add_obj.html', {'form': form})


class AddStudioFullFormView(View):
    def get(self, request):
        form = StudioFullForm()
        return render(request, 'add_obj.html', {'form': form})

    def post(self, request):
        form = StudioFullForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            Studio.objects.create(name=name, city=city)
            return redirect(reverse('studios'))
        return render(request, 'add_obj.html', {'form': form})


class AddMovieModelView(View):
    def get(self, request):
        form = MovieModelForm()
        return render(request, 'add_obj.html', {'form': form})

    def post(self, request):
        form = MovieModelForm()
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            form.save_m2m()
            return redirect(reverse('movies'))
        return render(request, 'add_obj.html', {'form': form})

class AddPersonModelView(View):
    def get(self, request):
        form = PersonModelForm()
        return render(request, 'add_obj.html', {'form':form})

    def post(self, request,):
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_person_model'))
        return render(request, 'add_obj.html', {'form':form})

class AddStudioModelView(View):
    def get(self, request):
        form = StudioModelForm()
        return render(request, 'add_obj.html', {'form':form})

    def post(self, request,):
        form = StudioModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_studio_model'))
        return render(request, 'add_obj.html', {'form':form})