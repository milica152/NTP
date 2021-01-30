from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import CreateUserForm
from .models import Member


# Create your views here.

def index(request):
    all_members = Member.objects.all()
    return HttpResponse(render(request, 'application/index.html', {
        'all_members': all_members,
        'all_members_size': len(all_members),
    }))


class CreateUserFormView(View):
    form_class = CreateUserForm
    template_name = 'application/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']

            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
            else:
                return render(request, self.template_name, {'form': form})

            return redirect('index')
        else:
            return render(request, self.template_name, {'form': form})
