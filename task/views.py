from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .form import GenerateRandomUserForm
from .task import create_random_user_accounts


class UsersListView(ListView):
    template_name = 'task/user_list.html'
    model = User


class GenerateRandomUserView(FormView):
    template_name = 'task/generate_random_user.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')
