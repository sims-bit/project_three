from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "my_site/index.html"




def post_detail(request, slug):
    """
    Display an individual :model:`my_site.Post`.

    **Context**

    ``post``
        An instance of :model:`my_site.Post`.

    **Template:**

    :template:`my_site/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "my_site/post_detail.html",
        {"post": post},
    )