from django.urls import path
from short_url.views import ShortUrlView

urlpatterns = [
    path('all/', ShortUrlView.as_view({'get': 'list'})),
    path('', ShortUrlView.as_view({'post': 'create'})),
    path('show/<str:code>/', ShortUrlView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'update'})),
    path('<str:code>/', ShortUrlView.as_view({'get': 'go_short_url'})),
]
