from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from .models import Cake, Recipe
from .forms import NewUserForm, RecipeForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView, LoginView, LogoutView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator

# Create your views here.

# Cake CRUD operations

class CakeDetail(DetailView):
    model = Cake
    def get_context_data(self, **kwargs):
        # Defines the context as the CakeDetail view being accessed
        context = super(CakeDetail, self).get_context_data(**kwargs)
        # Fetches the currently-accessed page of paginated objects
        page = self.request.GET.get('page')
        # Initializes the paginator, sets the paginated objects to a list of Recipes attributed to the currently-accessed Cake, 
        # orders the filtered list by the date of creation, and asserts 3 Recipes per page
        paginator = Paginator(Recipe.objects.filter(cake=self.get_object()).order_by('created_date'), 3)
        # declares that any use of "page_obj" in the relevant template is equated to the current page of Recipes
        context['page_obj'] = paginator.get_page(page)
        # declares that any use of 'form' in the relevant template is equated to the RecipeForm CBV
        context['form'] = RecipeForm
        return context


class CakeCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Cake
    fields = ['name', 'flavours', 'description', 'imageurl']
    success_message = "Cake successfully created."
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class CakeUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cake
    fields = ['name', 'flavours', 'description', 'imageurl']
    success_message = "Cake successfully updated."
    
class CakeDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Cake
    success_message = "Cake successfully deleted."
    success_url = '/cakes/'


# Home/Landing page

def home(request):
    return render(request, 'home.html')

def cakes_index(request):
    # cakes = all established Cake objects in the DB
    cakes = Cake.objects.all()
    # initializes the paginator and asserts that there must be 3 cakes to a page
    paginator = Paginator(cakes, 4)
    # defines the page number of the currently accessed page of cakes
    page_number = request.GET.get('page')
    # defines the contents of the currently accessed page of cakes
    page_obj = paginator.get_page(page_number)
    # renders the cakes index and passes the page_obj variable to any use of 'page_obj' in the template
    return render(request, 'cakes/index.html', {'page_obj': page_obj})

# def cakes_detail(request, pk):
#     cake = Cake.objects.get(id=pk)
#     recipe_form = RecipeForm
#     return render(request, "cakes/detail.html", {'cake': cake, 'recipe_form': recipe_form})

#adding RECIPE CRUD OPERATIONS - RecipeUpdate view, Richard 28/6/22
class RecipeUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Recipe
    fields = ['title', 'description', 'ingredients', 'instructions', 'imageurl']
    success_message = "Recipe Successfully Updated."
    


#Richard uncommented this class 28/6/22
# class RecipeCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     model = Recipe
#     fields = ['title', 'description', 'ingredients', 'instructions', 'imageurl']
#     success_message = "Recipe successfully created."
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         form.instance.cake = self.request.cake_id
#         return super().form_valid(form)

"""@login_required
def add_feeding(request, cat_id):
    # where req.body in express represented the posted form data, django uses request.POST
    form = FeedingForm(request.POST)
    print(form)
    if form.is_valid():
        # Collect the data, but do not commit it to the DB
        new_feeding = form.save(commit=False)
        # sets the cat_id value of cat_id passed from the form(?)
        new_feeding.cat_id = cat_id
        # save to db
        new_feeding.save()
        return redirect('detail', cat_id = cat_id)"""

@login_required
def add_recipe(request, pk):
    form = RecipeForm(request.POST)
    print(form)
    if form.is_valid():
        new_recipe = form.save(commit = False)
        new_recipe.cake_id = pk
        form.instance.created_by = request.user
        new_recipe.save()
        messages.success(request, f"Recipe successfully added.")
        return redirect('detail', pk = pk)

class RecipeDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Recipe
    success_message = "Recipe successfully deleted."
    #success_url = reverse_lazy('detail', kwargs = {'pk': model.cake_id})
    def get_success_url(self):
        return reverse('detail', kwargs={'pk' : self.object.cake_id})
    

# Authentication Views

# Signup View - using new custom form in forms.py called NewUserForm to allow for email input on signup
def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You successfully signed up and are now logged in.')
            return redirect('/')
        else:
            messages.error(request, "Invalid sign up - try again.")
    
    form = NewUserForm()
    return render(request, 'registration/signup.html', {'form': form})


# Password Change - specifying success url redirect, otherwise will default to a URL with the name 'password_change_done' which will need a new view & template specified.
class PasswordChange(SuccessMessageMixin, PasswordChangeView):
    success_message = "Password changed successfully."
    success_url = '/'

class LoginView(SuccessMessageMixin, LoginView):
    def form_valid(self, form):
            messages.success(self.request, f"You have successfully logged in!")
            return super().form_valid(form)

class LogoutView(LoginRequiredMixin, SuccessMessageMixin, LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You have successfully logged out.")
        return super().dispatch(request, *args, **kwargs)


