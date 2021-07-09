from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchlistResultPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
    last_page_strings = 'last'

class WatchlistLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 7

class WatchListCursorPagination(CursorPagination):
    page_size = 5
    # ordering = 'title'