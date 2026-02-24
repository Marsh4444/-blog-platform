from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Blog ,Comment
from .forms import CommentForm
from django.contrib import messages



# Create your views here.
def category_posts(request, pk):
    posts = Blog.objects.filter(category=pk, status='published').order_by('-updated_at')
    category = get_object_or_404(Category, pk=pk)

    context = {
        'posts': posts,
        'category': category,
    }

    return render(request, 'category_posts.html', context)


def single_blogs(request, blog_slug):
    single_post = get_object_or_404(Blog, slug=blog_slug, status='published')
    
    comments = single_post.comments.all().order_by("-created_at")

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.blog = single_post
                comment.save()
                messages.success(request, "Your comment has been posted.")
                return redirect("single_blogs", blog_slug=blog_slug)# return HttpResponseRedirect(request.path_info)
        else:
            messages.warning(request, "You must be logged in to comment.")
            return redirect("login")
    else:
        form = CommentForm()

    context = {
        "single_post": single_post,
        "comments": comments,
        "form": form,
    }

    return render(request, "single_blogs.html", context)

