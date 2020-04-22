from django.urls import path
# from byuier.news.api.views import (
#     article_list_create_api_view,
#     article_detail_api_view
# )
from byuier.news.api.views import (
    ArticleListCreateAPIView,
    ArticleDetailAPIView,
    JournalistListAPIView
)

urlpatterns = [
    path('articles/', ArticleListCreateAPIView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='article-detail'),
    path('journalists/', JournalistListAPIView.as_view(), name='journalist-list'),
    # path('articles/', article_list_create_api_view, name='article-list'),
    # path('articles/<int:pk>/', article_detail_api_view, name='article-detail')
]
