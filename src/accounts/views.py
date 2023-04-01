from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import login, logout, get_user_model, authenticate
from django.views.generic import View, CreateView, TemplateView, DetailView, UpdateView

from .forms import LoginForm, SignUpForm, ProfileEditForm


class LoginView(TemplateView):
    template_name = 'registration/login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request=request, username=username, password=password)
        if not user:
            return redirect('login')
        login(request, user)
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('login')


class SignUpView(CreateView):
    template_name = 'registration/register.html'
    form_class = SignUpForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

        return self.render_to_response(context={
            'form': form
        })

    def get_success_url(self):
        return reverse('index')


# class ProfileDetailView(DetailView):
#     model = get_user_model()
#     template_name = 'accounts/user_detail.html'
#     context_object_name = 'user_obj'
#
#
# class ProfileEditView(UpdateView):
#     model = get_user_model()
#     form_class = ProfileEditForm
#     template_name = 'accounts/user_detail_edit.html'
#     context_object_name = 'user_obj'
#
#     def get_success_url(self):
#         return reverse('profile', kwargs={'pk': self.object.pk})
