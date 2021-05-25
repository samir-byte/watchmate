
from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchDetailsAV, StreamPlatformListAV, StreamPlatformDetailAV

urlpatterns = [
    path('', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailsAV.as_view(), name='movie-details'),
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('list/<int:pk>', WatchDetailsAV.as_view(), name='movie-details'),
    path('stream', StreamPlatformListAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),

]
