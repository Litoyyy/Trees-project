from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from core import models, mixins
from django.views import generic


@method_decorator(cache_page(60 * 15), name='dispatch')
class ArticleDetailView(generic.DetailView):
    model = models.Article
    template_name = "pages/article_detail.html"
    slug_url_kwarg = "article_slug"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)