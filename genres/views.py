from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer



class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all() # qual a query set vai usar 
    serializer_class = GenreSerializer # e qual o serializers


class GenereRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer # e qual o serializers


