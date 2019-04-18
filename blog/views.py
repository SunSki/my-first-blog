from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts':posts}) #postsをrender先に渡す

def post_detail(request, pk):
    # Postモデルのpkが一致するものを取得
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})


def post_new(request):
    if request.method == "POST":
        # POSTされた時request.POSTにデータが追加されている
        form = PostForm(request.POST)

        if form.is_valid():
            # commit=False: データベースに保存する前のモデルオブジェクトを返す
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form':form})


###### views for tool ########
from .generate_text import generate_text
from .get_image_url import get_image_url

def txtGen(request):
    img_url = get_image_url()
    text_list = generate_text()
    return render(request, 'blog/text_generate.html', {'text_list':text_list, 'img_url':img_url})

def txtGen_raw(request):
    return render(request, 'blog/text_generate_raw.html')
