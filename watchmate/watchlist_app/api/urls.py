
from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (WatchListAV, WatchDetailsAV,
                                     StreamPlatformListAV, StreamPlatformDetailAV,
                                      ReviewList, ReviewDetail, ReviewCreate)

urlpatterns = [
    path('', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailsAV.as_view(), name='movie-details'),
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('list/<int:pk>', WatchDetailsAV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
]
