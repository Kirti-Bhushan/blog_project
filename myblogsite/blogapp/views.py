from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blogapp.models import blogPost,Comment
from blogapp.forms import BlogPostForm,CommentForm
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,)
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.

class AboutView(TemplateView):
    template_name='blogapp/about.html'

class PostListView(ListView):
    model= blogPost

    def get_queryset(self):
        return blogPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model=blogPost

class PostCreateView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='blogapp/blogpost_detail.html'
    form_class= BlogPostForm

    model= blogPost

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name='blogapp/blogpost_detail.html'
    form_class=BlogPostForm

    model=blogPost

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=blogPost
    success_url= reverse_lazy('blogpost_list')

class PostDraftListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='blogapp/blogpost_draft_list.html'
    model=blogPost

    def get_queryset(self):
        return blogPost.objects.filter(published_date__isnull=True).order_by('-create_date')

@login_required
def post_publish(request,pk):
    post=get_object_or_404(blogPost,pk=pk)
    post.publish()
    return redirect('blogpost_detail',pk=pk)


@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(blogPost,pk=pk)

    if request.method=='POST':
        form=CommentForm(request.POST)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('blogpost_detail',pk=post.pk)

    else:
        form=CommentForm()
    return render(request,'blogapp/comment_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('blogpost_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('blogpost_detail',pk=post_pk)
