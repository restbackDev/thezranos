from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login #auto log-ins the user; no need to retype the username and password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Date, Food
from .forms import DateForm



class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )


def about(request):
    contact_details = 'you can reach support at support@thezranos.com'
    return render(request, 'about.html', {
        'contact' : contact_details
    })

@login_required
def date_index(request):
    dates = Date.objects.filter(user=request.user)
    return render(request, 'dates/index.html', {'dates': dates})

@login_required
def date_detail(request, date_id):
    date = Date.objects.get(id=date_id)
    foods_date_doesnt_have = Food.objects.exclude(id__in = date.foods.all().values_list('id'))
    date_form = DateForm()


    return render(request, 'dates/detail.html', {
        'date': date,
        'date_form': date_form,
        'foods' : foods_date_doesnt_have
    })

@login_required
def associate_food(request, date_id, food_id):
    # Note that you can pass a food's id instead of the whole object
    Date.objects.get(id=date_id).foods.add(food_id)
    return redirect('date-detail', date_id=date_id)

@login_required
def remove_food(request, date_id, food_id):
    # Note that you can pass a food's id instead of the whole object
    Date.objects.get(id=date_id).foods.remove(food_id)
    return redirect('date-detail', date_id=date_id)


class DateCreate(LoginRequiredMixin, CreateView):
    model = Date
    fields = ['day', 'weight', 'water_intake']
    date_form = DateForm()
    # success_url = '/dates' # replace for get_absolute_url via models.py
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class DateUpdate(LoginRequiredMixin, UpdateView):
    model = Date
    # Let's disallow the renaming of a date by excluding the name field!
    fields = ['day', 'weight', 'water_intake']

class DateDelete(LoginRequiredMixin, DeleteView):
    model = Date
    success_url = '/dates/'

class FoodCreate(LoginRequiredMixin, CreateView):
    model = Food
    fields = '__all__'

class FoodList(ListView):
    model = Food

class FoodDetail(DetailView):
    model = Food

class FoodUpdate(LoginRequiredMixin, UpdateView):
    model = Food
    fields = ['name', 'grams', 'calories']

class FoodDelete(LoginRequiredMixin, DeleteView):
    model = Food
    success_url = '/foods/'
