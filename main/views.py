from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Thread, Comment
from .forms import ThreadForm, CommentForm

def index(request):
    return render(request, 'index.html', {})

@login_required(login_url='redirect_to_login')
def profile(request):
    user = request.user
    threads = request.user.thread_set.all()
    return render(request, 'profile.html', {'user':user, 'threads':threads})

def threads(request):
    thread = Thread.objects.all()

    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            new_thread = form.save(commit=False)
            new_thread.author = request.user
            new_thread.save()
            messages.success(request, 'New thread has been created!')
        form = ThreadForm() 
    else:
        form = ThreadForm()
        
    return render(request, 'threads.html', {'form':form, 'threads':thread})

def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    comments = Comment.objects.filter(thread=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.thread = thread
            new_comment.save()
            messages.success(request, 'You added a new comment!')
        form = CommentForm() 
    else:
        form = CommentForm()

    return render(request, 'thread_detail.html', {'form':form, 'thread':thread, 'comments':comments})

@login_required(login_url='redirect_to_login')
def delete_thread(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    comments = Comment.objects.filter(thread=pk)

    if thread.author == request.user:
        thread.delete()
        messages.success(request, 'You have deleted the thread.')
        return redirect('threads')
    else:
        messages.warning(request, 'You don\'t have a right to delete this thread since you are not owner of this thread.')
        return redirect('thread_detail', pk=thread.pk)

@login_required(login_url='redirect_to_login')
def delete_comment(request, th_pk, cm_pk):
    thread = get_object_or_404(Thread, pk=th_pk)
    comment = get_object_or_404(Comment, pk=cm_pk)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'You have deleted the comment.')
        return redirect('thread_detail', pk=thread.pk)
    else:
        messages.warning(request, 'You don\'t have a right to delete this comment since this comment is not yours.')
        return redirect('thread_detail', pk=thread.pk)