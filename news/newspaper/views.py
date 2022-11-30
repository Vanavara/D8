from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment, Author
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .forms import PostForm, CommentForm


#def home(request):
 #   return render(request, 'home.html', {})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-details', args=[str(pk)]))

def DislikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.dislikes.add(request.user)
    return HttpResponseRedirect(reverse('article-details', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    #ordering = ['-id']
# ordering - сортировка. -id показывает, что последний пост находится на самом верху.
# Возможно измнить по дате

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article-details.html'

    #def get_context_data(self, *args, **kwargs):
     #   #cat_menu = Category.objects.all()
     #   context = super(ArticleDetailView, self).get_context_data()
     #   stuff = get_object_or_404(Post, id=self.kwargs['pk']
     #   total_likes = stuff.total_likes()
     #   #context['cat_menu'] = cat_menu
     #   context["total_likes"] = total_likes
     #   return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class AddAuthorView(CreateView):
    model = Author
    #form_class = PostForm
    template_name = 'add_author.html'
    fields = '__all__'

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
