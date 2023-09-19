# views.py
from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm
from django.views import View



# def comment_view(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             text = form.cleaned_data['text']
#             parent_id = request.POST.get('parent_id')
#             parent_comment = None
#             if parent_id:
#                 parent_comment = Comment.objects.get(pk=parent_id)
#             Comment.objects.create(text=text, parent=parent_comment)
#             return redirect('comment_view')
#     else:
#         form = CommentForm()
#     comments = Comment.objects.filter(parent=None)
#     return render(request, 'comments.html', {'form': form, 'comments': comments})

class CommentView(View):
    def post(self,request):
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            parent_id = request.POST.get('parent_id')
            parent_comment = None
            if parent_id:
                parent_comment=Comment.objects.get(pk=parent_id)
            Comment.objects.create(text=text,parent=parent_comment)
            return redirect('comment_view')
        else:
            form = CommentForm()
            comments = Comment.objects.filter(parent=None)

            return render(request, 'comments.html', {'form': form, 'comments': comments})


    
    def get(self,request):

        form = CommentForm()
        comments = Comment.objects.filter(parent=None)

        return render(request, 'comments.html', {'form': form, 'comments': comments})

        


            