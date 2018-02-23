from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm


def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)#get_object_or_404当要获取的数据存在，就获取，不存在则返回404
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():#判定表单的数据类型是否正确
            comment = form.save(commit=False)#commit=false不存入数据库
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {'post':post,
                       'form':form,
                       'comment_list':comment_list
                        }
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)#redirect的作用是重定向