from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from genres.views import GenreCreateListView, GenereRetriveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>',GenereRetriveUpdateDestroyView.as_view(), name='genre-detail-view'),

    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
]
