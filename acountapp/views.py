from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from acountapp.decorators import account_ownership_required
from acountapp.forms import AccountCreationForm
from acountapp.models import HelloWorld

@login_required(login_url=reverse_lazy('acountapp:login'))
def hello_world(request):
    if request.user.is_authenticated:

        if request.method == 'POST':

            temp = request.POST.get('hello_world_input')

            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            return HttpResponseRedirect(reverse('acountapp:hello_world'))

        else:
            hello_world_list = HelloWorld.objects.all()
            return render(request, 'acountapp/hello_world.html',
                        context={'hello_world_list': hello_world_list})

    else:
        return HttpResponseRedirect(reverse('acountapp:login'))


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('acountapp:hello_world')
    template_name = 'acountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'acountapp/detail.html'

has_ownership = [login_required, account_ownership_required]

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('acountapp:hello_world')
    template_name = 'acountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('acountapp:hello_world')
    template_name = 'acountapp/delete.html'

