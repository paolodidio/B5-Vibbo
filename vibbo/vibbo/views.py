from django.shortcuts import render
from django.views.generic import DetailView, FormView
from django.db import models
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ChangeProfileView(FormView):
    template_name = 'vibbo/profile_change.html'
    form_class = ProfileForm

    def get_initial(self):
        return {
            'first_name': self.request.user.profile.first_name,
            'last_name': self.request.user.profile.last_name,

            'bio': self.request.user.profile.bio,

            'street': self.request.user.profile.street,
            'city': self.request.user.profile.city,
            'location_code': self.request.user.profile.location_code
        }

    def get_queryset(self):
        return Profile.objects.get(user=self.request.user)

    def form_valid(self, form):

        data = form.cleaned_data
        profile = self.get_queryset()

        profile.first_name = data['first_name']
        profile.last_name = data['last_name']

        profile.bio = data['bio']

        profile.street = data['street']
        profile.city = data['city']
        profile.location_code = data['location_code']

        profile.save()

        # return HttpResponse('ok')
        return HttpResponseRedirect(f"/vibbo/profile/{self.request.user.profile.pk}/")


class DisplayDetailView(DetailView):
    template_name = "vibbo/profile_page.html"
    model = Profile
