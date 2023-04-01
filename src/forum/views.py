from django.shortcuts import render, redirect, reverse
from django.views.generic import View, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin

from .models import Theme, Reply
from .forms import ThemeCreationForm, ReplyCreationForm


class ThemeListView(ListView):
    model = Theme
    template_name = 'forum/index.html'
    context_object_name = 'themes'
    ordering = ['-created_at']
    paginate_by = 10
    paginate_orphans = 1


class ThemeDetailView(DetailView):
    model = Theme
    template_name = 'forum/theme_detail.html'
    context_object_name = 'theme'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        replies = self.object.replies.all()

        paginator = Paginator(replies, 3)
        page = self.request.GET.get('page')

        context['replies'] = paginator.get_page(page)
        context['paginator'] = paginator
        context['page_obj'] = paginator.get_page(page)
        context['replies_form'] = ReplyCreationForm
        return context


class ThemeAddView(LoginRequiredMixin, CreateView):
    model = Theme
    form_class = ThemeCreationForm
    template_name = 'forum/theme_create.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            theme = form.save(commit=False)
            theme.author = user
            theme.save()
            return redirect('themes')

        return self.render_to_response(context={
            'form': form,
        })


class ThemeEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    permission_required = 'forum.change_theme'
    model = Theme
    template_name = 'forum/theme_update.html'
    form_class = ThemeCreationForm

    def test_func(self):
        theme_id = self.kwargs.get('pk')
        theme = Theme.objects.get(pk=theme_id)

        curr_user = self.request.user
        targ_user = theme.author
        return targ_user.username == curr_user.username

    def get_success_url(self):
        return reverse('theme_detail', kwargs={'pk': self.object.pk})


class ThemeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    permission_required = 'forum.delete_theme'
    model = Theme

    def test_func(self):
        theme_id = self.kwargs.get('pk')
        theme = Theme.objects.get(pk=theme_id)

        curr_user = self.request.user
        targ_user = theme.author
        return targ_user.username == curr_user.username

    def get_success_url(self):
        return reverse('themes')


class ReplyAddView(LoginRequiredMixin, CreateView):
    model = Reply
    form_class = ReplyCreationForm
    template_name = 'forum/theme_detail.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            theme_id = kwargs.get('pk')
            theme = Theme.objects.get(pk=theme_id)
            reply = form.save(commit=False)
            reply.user = user
            reply.theme = theme
            reply.save()
            return redirect('theme_detail', pk=theme_id)

        return self.render_to_response(context={
            'form': form,
        })
